from pyrogram import Client
from pyrogram.types import Message
from config import Styles
import time

async def execute(client: Client, message: Message):
    start_time = time.time()
    processing_time = round((time.time() - start_time) * 1000, 2)
    
    response = Styles.bot_response(
        f"🏓 **PONG!**\n"
        f"⚡ Скорость ответа: `{processing_time}мс`\n"
        f"🔮 ID чата: `{message.chat.id}`"
    )
    
    await message.reply(response, disable_web_page_preview=True)
