import os
import sys
import time
import importlib.util
from pyrogram import Client, filters
from pyrogram.types import Message
from config import Config, Styles

def load_commands():
    commands = {}
    for filename in os.listdir(Config.CMD_FOLDER):
        if filename.endswith(".py") and filename != "__init__.py":
            module_name = filename[:-3]
            module_path = os.path.join(Config.CMD_FOLDER, filename)
            
            spec = importlib.util.spec_from_file_location(module_name, module_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            
            if hasattr(module, 'execute'):
                commands[module_name] = module.execute
    return commands

def first_time_setup():
    print(f"{Styles.HEADER}╔{'═' * 50}╗")
    print(f"║{'Telegram Bot First-Time Setup':^50}║")
    print(f"╚{'═' * 50}╝{Styles.ENDC}")
    
    api_id = input(Styles.input_prompt("Введите API ID: "))
    api_hash = input(Styles.input_prompt("Введите API HASH: "))
    
    # Проверка ввода
    if not api_id.isdigit() or len(api_hash) != 32:
        print(Styles.error("Ошибка: Неверный формат API данных"))
        print(Styles.error("Проверьте введенные значения и попробуйте снова"))
        sys.exit(1)
    
    return int(api_id), api_hash

async def start_bot():
    print(f"{Styles.HEADER}╔{'═' * 50}╗")
    print(f"║{'Запуск Telegram Bot':^50}║")
    print(f"╚{'═' * 50}╝{Styles.ENDC}")
    
    # Проверяем наличие сессии
    if not os.path.exists("my_bot.session"):
        api_id, api_hash = first_time_setup()
    else:
        api_id = None
        api_hash = None
    
    app = Client(
        "my_bot",
        api_id=api_id,
        api_hash=api_hash,
        in_memory=True
    )
    
    commands = load_commands()
    print(Styles.success(f"Загружено команд: {len(commands)}"))
    
    @app.on_message(filters.text & (filters.private | filters.group))
    async def handle_commands(client: Client, message: Message):
        prefix = next((p for p in Config.PREFIXES if message.text.startswith(p)), None)
        if not prefix: return
        
        cmd_text = message.text[len(prefix):].strip().split()
        if not cmd_text: return
        
        cmd_name = cmd_text[0].lower()
        if cmd_name in commands:
            start_time = time.time()
            await commands[cmd_name](client, message)
            response_time = round((time.time() - start_time) * 1000, 2)
            print(Styles.success(f"Ответил на {cmd_name} за {response_time}мс"))
    
    return app

if __name__ == "__main__":
    import asyncio
    
    try:
        loop = asyncio.get_event_loop()
        bot = loop.run_until_complete(start_bot())
        
        print(f"\n{Styles.GREEN}✅ Бот успешно запущен!{Styles.ENDC}")
        print(f"{Styles.YELLOW}🛑 Для остановки нажмите Ctrl+C{Styles.ENDC}\n")
        bot.run()
    except KeyboardInterrupt:
        print(f"\n{Styles.RED}🛑 Бот остановлен пользователем{Styles.ENDC}")
    except Exception as e:
        print(Styles.error(f"Критическая ошибка: {str(e)}"))
        print(Styles.error("Попробуйте удалить файл my_bot.session и перезапустить бота"))
