import logging
from config import Messages as tr
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

logging.basicConfig(level=logging.INFO)

@Client.on_message(filters.private & filters.incoming & filters.command(['help']))
def _help(client, message):
    await client.send_message(chat_id = message.chat.id,d,
        text = tr.HELP_MSG[1],
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
        text=tr.HELP_MSG[msg],    reply_markup=InlineKeyboardMarkup(map(msg))
    )


def map(pos):
    if(pos==1):
        button = [
            [InlineKeyboardButton(text = '➡️', callback_data = "help+2")]
        ]
    elif(pos==len(tr.HELP_MSG)-1):
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
