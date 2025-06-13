class Config:
    PREFIXES = ['.', '!', '/', '\\']
    CMD_FOLDER = "cub_cmd"

class Styles:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    @staticmethod
    def input_prompt(text):
        return f"{Styles.BLUE}╰─>{Styles.ENDC} {Styles.BOLD}{text}{Styles.END}"

    @staticmethod
    def success(text):
        return f"{Styles.GREEN}✓{Styles.ENDC} {text}"

    @staticmethod
    def error(text):
        return f"{Styles.RED}✗{Styles.ENDC} {text}"

    @staticmethod
    def bot_response(text):
        return f"{Styles.CYAN}🤖 {text}{Styles.ENDC}"
