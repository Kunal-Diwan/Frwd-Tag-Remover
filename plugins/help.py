import logging
from bot import DevelopedBots
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

logging.basicConfig(level=logging.INFO)

# =====================================================================

class Messages():
      HELP_MSG = [
        ".",

        "**Features 🧰**\n\n◆ <b>Works Only in channel</b> \n\n◆ Fastest Automatic Forward Remover \n\n◆ Forward a message/file/Text/media to the channel \n\n◆ Automatically Deletes The Forward Tag and Resends the Message",
        
        "**Setup**\n\n<b>👉 First of all add me to your channel as admin with all permission .\n\n<b><u>⚠️ Note ⚠️</u> - Only Channel Creator can set me and i will leave the channel if i am not an admin in the channel. </b>",
        
        "**Excellent**\n\n<u>All Setup Done</u> \n\n<i>Now, I will remove any type of forwarded post from that channel will and send it again without forward tag .</i>",
        
        "**Report a Problem**\n\nIf something <b>unexpected</b> happens, you can report it to us. (You can also suggest features.)\n\n<b>Steps</b>\n1) Try whatever you did again. If it shows the same unexpected thing, move to step 2 \n2) Visit @DevelopedBotz and define your problem <b>completely</b>, i.e, what you expected and what happened instead.If you don't get a reply, tag an admin."
      ]

# =====================================================================

@Client.on_message(filters.private & filters.incoming & filters.command(['help']))
def _help(client, message):
    client.send_message(chat_id = message.chat.id,
        text = HELP_MSG[1],
        parse_mode="markdown",
        disable_notification = True,
        reply_markup = InlineKeyboardMarkup(map(1)),
        reply_to_message_id = message.message_id
    )

help_callback_filter = filters.create(lambda _, __, query: query.data.startswith('help+'))

@Client.on_callback_query(help_callback_filter)
def help_answer(client, callback_query):
    chat_id = callback_query.from_user.id
    message_id = callback_query.message.message_id
    msg = int(callback_query.data.split('+')[1])
    client.edit_message_text(chat_id=chat_id,    message_id=message_id,
        text=HELP_MSG[msg],    reply_markup=InlineKeyboardMarkup(map(msg))
    )


def map(pos):
    if(pos==1):
        button = [
            [InlineKeyboardButton(text = '➡️', callback_data = "help+2")]
        ]
    elif(pos==len(HELP_MSG)-1):
        url = "https://t.me/kunaldiwan"
        button = [
            [InlineKeyboardButton(text = 'Support Chat 🔉', url="https://t.me/DevelopedBotz")],
            [InlineKeyboardButton(text = 'Developer 👨‍💻', url=url)],
            [InlineKeyboardButton(text = 'Return ↩️', callback_data = f"help+{pos-1}")]
        ]
    else:
        button = [
            [
                InlineKeyboardButton(text = 'Back 🔙', callback_data = f"help+{pos-1}"),
                InlineKeyboardButton(text = 'Continue ➡️', callback_data = f"help+{pos+1}")
            ],
        ]
    return button
