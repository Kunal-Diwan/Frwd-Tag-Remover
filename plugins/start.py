#(©) Kunal-Diwan

import os
import asyncio
from pyrogram import Client, filters, __version__
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram.errors import FloodWait, UserIsBlocked, InputUserDeactivated

from bot import DevelopedBots
from config import ADMINS, FORCE_MSG, START_MSG, OWNER_ID
from functions.helper_func import subscribed, encode, decode, get_messages
from database.sql import add_user, query_msg, full_userbase


#=====================================================================================##

WAIT_MSG = """"<b>Processing ...</b>"""

REPLY_ERROR = """<code>Use this command as a replay to any telegram message with out any spaces.</code>"""

#=====================================================================================##


@DevelopedBots.on_message(filters.command('start') & filters.private & subscribed)
async def start_command(client: Client, message: Message):
    id = message.from_user.id
    user_name = '@' + message.from_user.username if message.from_user.username else None
    try:
        await add_user(id, user_name)
    except:
        pass
    text = message.text
    if len(text)>7:
        try:
            base64_string = text.split(" ", 1)[1]
        except:
            return
        string = await decode(base64_string)
        argument = string.split("-")
        if len(argument) == 3:
            try:
                start = int(int(argument[1]) / abs(client.db_channel.id))
                end = int(int(argument[2]) / abs(client.db_channel.id))
            except:
                return
            if start <= end:
                ids = range(start,end+1)
            else:
                ids = []
                i = start
                while True:
                    ids.append(i)
                    i -= 1
                    if i < end:
                        break
        elif len(argument) == 2:
            try:
                ids = [int(int(argument[1]) / abs(client.db_channel.id))]
            except:
                return
        temp_msg = await message.reply("Please wait...")
        try:
            messages = await get_messages(client, ids)
        except:
            await message.reply_text("Something went wrong..!")
            return
        await temp_msg.delete()

    else:
        reply_markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("⚙️ Help ⚙️", callback_data = "help"),
                    InlineKeyboardButton("🔎 About 🔎", callback_data = "about")
                ],
                [
                    InlineKeyboardButton("📢 Channel 📢", url = "https://t.me/DevelopedBots"),
                    InlineKeyboardButton("💬 Support 💬", url = "https://t.me/DevelopedBotz")
                
                ],
                [
                    InlineKeyboardButton("👨‍💻 Developer 👨‍💻", url = "t.me/Kunaldiwan")

                ]
            ]
        )
        await message.reply_text(
            text = START_MSG.format(
                first = message.from_user.first_name,
                last = message.from_user.last_name,
                username = None if not message.from_user.username else '@' + message.from_user.username,
                mention = message.from_user.mention,
                id = message.from_user.id
            ),
            reply_markup = reply_markup,
            disable_web_page_preview = True,
            quote = True
        )
        return

@DevelopedBots.on_message(filters.command('start') & filters.private)
async def not_joined(client: Client, message: Message):
    buttons = [
        [
            InlineKeyboardButton(
                "Join Channel",
                url = client.invitelink)
        ]
    ]
    try:
        buttons.append(
            [
                InlineKeyboardButton(
                    text = 'Try Again',
                    url = f"https://t.me/{client.username}?start={message.command[1]}"
                )
            ]
        )
    except IndexError:
        pass

    await message.reply(
        text = FORCE_MSG.format(
                first = message.from_user.first_name,
                last = message.from_user.last_name,
                username = None if not message.from_user.username else '@' + message.from_user.username,
                mention = message.from_user.mention,
                id = message.from_user.id
            ),
        reply_markup = InlineKeyboardMarkup(buttons),
        quote = True,
        disable_web_page_preview = True
    )

@DevelopedBots.on_message(filters.command('users') & filters.private & filters.user(ADMINS))
async def get_users(client: DevelopedBots, message: Message):
    msg = await client.send_message(chat_id=message.chat.id, text=WAIT_MSG)
    users = await full_userbase()
    await msg.edit(f"{len(users)} users are using this bot")

@DevelopedBots.on_callback_query()
async def cb_handler(client: DevelopedBots, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ Creator : <a href='tg://user?id={OWNER_ID}'>This Person</a>\n○ Language : <code>Python3</code>\n○ Library : <a href='https://docs.pyrogram.org/'>Pyrogram asyncio {__version__}</a>\n○ Source Code : <a href='https://github.com/Kunal-Diwan/Frwd-Tag-Remover'>Click here</a>\n○ Channel : @DevelopedBots\n○ Support Group : @DevelopedBotz</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass

@Client.on_callback_query(filters.regex(r"^(help)$"))
async def callback_data(bot, update: CallbackQuery):

    query_data = update.data

    if query_data == "help":
        buttons = [[
            InlineKeyboardButton('❓ About❓', callback_data='about'),
            InlineKeyboardButton('🔐 Close 🔐', callback_data='close')
        ]]
    
        reply_markup = InlineKeyboardMarkup(buttons)
        
        await update.message.edit_text(
            "<b>◆ Works Only in channel</b>\n◆ Fastest Automatic Forward Remover\n◆ Add me to Your channel with all Admin Rights\nForward a message/file/Text/media to the channel\n◆ Automatically Deletes The Forward Tag and Resends the Message",
            reply_markup=reply_markup,
            parse_mode="html",
            disable_web_page_preview=True
        )
