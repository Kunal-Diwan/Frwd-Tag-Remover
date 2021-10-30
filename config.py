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

        "**Force Subscribe**\n```𝐅𝐨𝐫𝐜𝐞 𝐠𝐫𝐨𝐮𝐩 𝐦𝐞𝐦𝐛𝐞𝐫𝐬 𝐭𝐨 𝐣𝐨𝐢𝐧 𝐚 𝐬𝐩𝐞𝐜𝐢𝐟𝐢𝐜 𝐜𝐡𝐚𝐧𝐧𝐞𝐥 𝐛𝐞𝐟𝐨𝐫𝐞 𝐬𝐞𝐧𝐝𝐢𝐧𝐠 𝐦𝐞𝐬𝐬𝐚𝐠𝐞𝐬 𝐢𝐧 𝐭𝐡𝐞 𝐠𝐫𝐨𝐮𝐩.\n𝐈 𝐰𝐢𝐥𝐥 𝐦𝐮𝐭𝐞 𝐦𝐞𝐦𝐛𝐞𝐫𝐬 𝐢𝐟 𝐭𝐡𝐞𝐲 𝐧𝐨𝐭 𝐣𝐨𝐢𝐧𝐞𝐝 𝐲𝐨𝐮𝐫 𝐜𝐡𝐚𝐧𝐧𝐞𝐥 𝐚𝐧𝐝 𝐭𝐞𝐥𝐥 𝐭𝐡𝐞𝐦 𝐭𝐨 𝐣𝐨𝐢𝐧 𝐭𝐡𝐞 𝐜𝐡𝐚𝐧𝐧𝐞𝐥 𝐚𝐧𝐝 𝐮𝐧𝐦𝐮𝐭𝐞 𝐭𝐡𝐞𝐦𝐬𝐞𝐥𝐟 𝐛𝐲 𝐩𝐫𝐞𝐬𝐬𝐢𝐧𝐠 𝐚 𝐛𝐮𝐭𝐭𝐨𝐧.```",
        
        "**Setup**\n```𝐅𝐢𝐫𝐬𝐭 𝐨𝐟 𝐚𝐥𝐥 𝐚𝐝𝐝 𝐦𝐞 𝐢𝐧 𝐭𝐡𝐞 𝐠𝐫𝐨𝐮𝐩 𝐚𝐬 𝐚𝐝𝐦𝐢𝐧 𝐰𝐢𝐭𝐡 𝐛𝐚𝐧 𝐮𝐬𝐞𝐫𝐬 𝐩𝐞𝐫𝐦𝐢𝐬𝐬𝐢𝐨𝐧 𝐚𝐧𝐝 𝐢𝐧 𝐭𝐡𝐞 𝐜𝐡𝐚𝐧𝐧𝐞𝐥 𝐚𝐬 𝐚𝐝𝐦𝐢𝐧.\n𝐍𝐨𝐭𝐞 ⚠️ : 𝐎𝐧𝐥𝐲 𝐜𝐫𝐞𝐚𝐭𝐨𝐫 𝐨𝐟 𝐭𝐡𝐞 𝐠𝐫𝐨𝐮𝐩 𝐜𝐚𝐧 𝐬𝐞𝐭𝐮𝐩 𝐦𝐞 𝐚𝐧𝐝 𝐢 𝐰𝐢𝐥𝐥 𝐥𝐞𝐚𝐯𝐞 𝐭𝐡𝐞 𝐜𝐡𝐚𝐭 𝐢𝐟 𝐢 𝐚𝐦 𝐧𝐨𝐭 𝐚𝐧 𝐚𝐝𝐦𝐢𝐧 𝐢𝐧 𝐭𝐡𝐞 𝐜𝐡𝐚𝐭.```",
        
        "**Commmands**\n```/ForceSubscribe``` - To get the current settings.\n```/ForceSubscribe no/off/disable``` - To turn of ForceSubscribe.\n```/ForceSubscribe {channel username}``` - To turn on and setup the channel.\n```/ForceSubscribe clear``` - To unmute all members who muted by me.\n\nNote: **/FSub is an alias of /ForceSubscribe**",
        
        "**𝐑𝐞𝐩𝐨𝐫𝐭 𝐁𝐮𝐠𝐬 🔽**"
      ]
