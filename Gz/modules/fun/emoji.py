import asyncio
from collections import deque
from random import randint

from pyrogram import filters, Client
from pyrogram.types import Message


from Gz.modules.help import add_command_help

emojis = {
    "moon": list("🌗🌘🌑🌒🌓🌔🌕🌖"),
    "clock": list("🕙🕘🕗🕖🕕🕔🕓🕒🕑🕐🕛"),
    "thunder": list("☀️🌤️⛅🌥️☁️🌩️🌧️⛈️⚡🌩️🌧️🌦️🌥️⛅🌤️☀️"),
    "earth": list("🌏🌍🌎🌎🌍🌏🌍🌎"),
    "heart": list("❤️🧡💛💚💙💜🖤"),
}
emoji_commands = [x for x in emojis]


@Client.on_message(filters.command(emoji_commands, ".") & filters.me)
async def emoji_cycle(bot: Client, message: Message):
    deq = deque(emojis[message.command[0]])
    try:
        for _ in range(randint(16, 32)):
            await asyncio.sleep(0.3)
            await message.edit("".join(deq), parse_mode=None)
            deq.rotate(1)
    except Exception:
        await message.delete()


special_emojis_dict = {
    "target": {"emoji": "🎯", "help": "Emoji target khusus"},
    "dice": {"emoji": "🎲", "help": "Emoji dadu khusus"},
    "bb": {"emoji": "🏀", "help": "Emoji khusus bola basket"},
    "soccer": {"emoji": "⚽️", "help": "Emoji sepak bola spesial"},
}
special_emoji_commands = [x for x in special_emojis_dict]


@Client.on_message(filters.command(special_emoji_commands, ".") & filters.me)
async def special_emojis(bot: Client, message: Message):
    emoji = special_emojis_dict[message.command[0]]
    await message.delete()
    await bot.send_dice(message.chat.id, emoji["emoji"])


# Command help section
special_emoji_help = [
    [".moon", "Putar semua fase emoji bulan."],
    [".clock", "Siklus semua fase emoji jam."],
    [".thunder", "Siklus guntur."],
    [".heart", "Siklus emoji hati."],
    [".earth `or` .globe", "Membuat dunia berputar."],
]

for x in special_emojis_dict:
    special_emoji_help.append([f".{x}", special_emojis_dict[x]["help"]])

add_command_help("emoji", special_emoji_help)
