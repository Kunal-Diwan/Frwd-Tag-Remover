from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(filters.command('help'))
async def _manage(_, msg):
    help = '*Works Only in channel* \n\n'
    help += "Fastest Automatic Forward Remover\n\n"
    help += 'Add me to Your channel with all Admin Rights \n'
    help += 'Forward a message/file/Text/media to the channel'
    help += 'Automatically Deletes The Forward Tag and Resends the Message'
    help += "If you don't get a reply, tag an admin."
    await msg.reply(
        help,
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton('◀️ Back', callback_data='start')]
        ]),
        quote=True
    )
