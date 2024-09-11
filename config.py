import os
import logging
from logging.handlers import RotatingFileHandler




BOT_TOKEN = os.environ.get("BOT_TOKEN", "7441112276:AAHQiEMr3ZP0SiLpbaMcAcUNhuAJiqWovNc")
API_ID = int(os.environ.get("API_ID", "26132893"))
API_HASH = os.environ.get("API_HASH", "5f8cc9ef2e106d963607432c1a21bbc8")


OWNER_ID = int(os.environ.get("OWNER_ID", "847244116"))
DB_URL = os.environ.get("DB_URL", "mongodb+srv://AU:o3LDfsISb1ukWNJX@cluster0.1wvzx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "actressuniverse-files-bot")


CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002198571183"))
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001119766850"))


FILE_AUTO_DELETE = int(os.getenv("FILE_AUTO_DELETE", "86400")) # auto delete in seconds


PORT = os.environ.get("PORT", "8585")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))



try:
    ADMINS=[847244116]
    for x in (os.environ.get("ADMINS", "847244116").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")









CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

DISABLE_CHANNEL_BUTTON = True if os.environ.get('DISABLE_CHANNEL_BUTTON', "True") == "True" else False

BOT_STATS_TEXT = "<b>BOT UPTIME :</b>\n{uptime}"







USER_REPLY_TEXT = "❌Don't Send Me Messages Directly I'm Only File Share Bot !"

START_MSG = os.environ.get("START_MESSAGE", "Hello {mention}\n\nI'm a Files Share Bot of @actressuniverseofficial.")

FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {mention}\n\n<b>You Need To Join In My Channel! To Use Me\n\nKindly Join @actressuniverseofficial</b>")





ADMINS.append(OWNER_ID)
ADMINS.append(847244116)

LOG_FILE_NAME = "actressuniverse-files-bot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   






