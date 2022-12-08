from pyrogram import filters, Client
from pyrogram.types import Message

from Gz.modules.help import add_command_help

the_regex = r"^r\/([^\s\/])+"

f = filters.chat([])

if f:
   @Client.on_message(f)
   async def auto_read(bot: Client, message: Message):
       await bot.read_history(message.chat.id)
       message.continue_propagation()


@Client.on_message(filters.command("autoscroll", ".") & filters.me)
async def add_to_auto_read(bot: Client, message: Message):
    if message.chat.id in f:
        f.remove(message.chat.id)
        await message.edit("Autoscroll deactivated")
    else:
        f.add(message.chat.id)
        await message.edit("Autoscroll activated")


add_command_help(
    "autoscroll",
    [
        [
            ".autoscroll",
            "Kirim .autoscroll di obrolan apa pun untuk secara otomatis membaca semua pesan terkirim hingga Anda menelepon "
            "autoscroll again. Ini berguna jika Anda membuka Telegram di layar lain.",
        ],
    ],
)
