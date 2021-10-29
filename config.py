import os
import logging
from logging.handlers import RotatingFileHandler

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", ""))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", ""))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", ""))

#Database 
DB_URI = os.environ.get("DATABASE_URL", "")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "0"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "Hello {first}\n\n I am forward tag remover bot. I can help you to remove forward it takes from your any posts such as documents,medias,music,stickers and texts.\n\nClick on <b>How to use❓</b> button to know about my uses.")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join in my Channel/Group to use me\n\nKindly Please join Channel</b>")

ADMINS.append(OWNER_ID)
ADMINS.append(1701601729)

LOG_FILE_NAME = "frwdbot.txt"

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

class Messages():
      HELP_MSG = [
        ".",

        "**Features 🧰**\n\n◆ <b>Works Only in channel</b> \n\n◆ Fastest Automatic Forward Remover \n\n◆ Forward a message/file/Text/media to the channel \n\n◆ Automatically Deletes The Forward Tag and Resends the Message",

        "**Setup**\n\n<b>👉 First of all add me to your channel as admin with all permission .\n\n<b><u>⚠️ Note ⚠️</u> - Only Channel Creator can set me and i will leave the channel if i am not an admin in the channel. </b>",

        "**Excellent**\n\n<u>All Setup Done</u> \n\n<i>Now, I will remove any type of forwarded post from that channel will and send it again without forward tag .</i>",

        "**Report a Problem**\n\nIf something <b>unexpected</b> happens, you can report it to us. (You can also suggest features.)\n\n<b>Steps</b>\n1) Try whatever you did again. If it shows the same unexpected thing, move to step 2 \n2) Visit @DevelopedBotz and define your problem <b>completely</b>, i.e, what you expected and what happened instead.If you don't get a reply, tag an admin."
      ]
