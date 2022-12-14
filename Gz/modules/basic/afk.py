import asyncio
from datetime import datetime

import humanize
from pyrogram import filters, Client
from pyrogram.types import Message

from Gz.helper.PyroHelpers import GetChatID, ReplyCheck
from Gz.modules.help import add_command_help

AFK = False
AFK_REASON = ""
AFK_TIME = ""
USERS = {}
GROUPS = {}


def subtract_time(start, end):
    subtracted = humanize.naturaltime(start - end)
    return str(subtracted)


@Client.on_message(
    ((filters.group & filters.mentioned) | filters.private) & ~filters.me & ~filters.service, group=3
)
async def collect_afk_messages(bot: Client, message: Message):
    if AFK:
        last_seen = subtract_time(datetime.now(), AFK_TIME)
        is_group = True if message.chat.type in ["supergroup", "group"] else False
        CHAT_TYPE = GROUPS if is_group else USERS

        if GetChatID(message) not in CHAT_TYPE:
            text = (
                f"`Beep boop. This is an automated message.\n"
                f"Saya tidak tersedia saat ini.\n"
                f"Terakhir terlihat: {last_seen}\n"
                f"Alasan: ```{AFK_REASON.upper()}```\n"
                f"Sampai jumpa setelah aku selesai melakukan apapun yang aku lakukan.`"
            )
            await bot.send_message(
                chat_id=GetChatID(message),
                text=text,
                reply_to_message_id=ReplyCheck(message),
            )
            CHAT_TYPE[GetChatID(message)] = 1
            return
        elif GetChatID(message) in CHAT_TYPE:
            if CHAT_TYPE[GetChatID(message)] == 50:
                text = (
                    f"`Ini adalah pesan otomatis\n"
                    f"Terakhir terlihat: {last_seen}\n"
                    f"Ini adalah ke-10 kalinya saya memberi tahu Anda bahwa saya AFK sekarang..\n"
                    f"Aku akan menemuimu saat aku sampai padamu.\n"
                    f"Tidak ada lagi pesan otomatis untuk Anda`"
                )
                await bot.send_message(
                    chat_id=GetChatID(message),
                    text=text,
                    reply_to_message_id=ReplyCheck(message),
                )
            elif CHAT_TYPE[GetChatID(message)] > 50:
                return
            elif CHAT_TYPE[GetChatID(message)] % 5 == 0:
                text = (
                    f"`Hei aku masih belum kembali.\n"
                    f"Terakhir terlihat: {last_seen}\n"
                    f"Masih sibuk: ```{AFK_REASON.upper()}```\n"
                    f"Coba ping nanti.`"
                )
                await bot.send_message(
                    chat_id=GetChatID(message),
                    text=text,
                    reply_to_message_id=ReplyCheck(message),
                )

        CHAT_TYPE[GetChatID(message)] += 1


@Client.on_message(filters.command("afk", ".") & filters.me, group=3)
async def afk_set(bot: Client, message: Message):
    global AFK_REASON, AFK, AFK_TIME

    cmd = message.command
    afk_text = ""

    if len(cmd) > 1:
        afk_text = " ".join(cmd[1:])

    if isinstance(afk_text, str):
        AFK_REASON = afk_text

    AFK = True
    AFK_TIME = datetime.now()

    await message.delete()


@Client.on_message(filters.command("afk", "!") & filters.me, group=3)
async def afk_unset(bot: Client, message: Message):
    global AFK, AFK_TIME, AFK_REASON, USERS, GROUPS

    if AFK:
        last_seen = subtract_time(datetime.now(), AFK_TIME).replace("ago", "").strip()
        await message.edit(
            f"`Saat kau pergi (for {last_seen}), Anda diterima {sum(USERS.values()) + sum(GROUPS.values())} "
            f"pesan dari {len(USERS) + len(GROUPS)} chats`"
        )
        AFK = False
        AFK_TIME = ""
        AFK_REASON = ""
        USERS = {}
        GROUPS = {}
        await asyncio.sleep(5)

    await message.delete()

if AFK:
   @Client.on_message(filters.me, group=3)
   async def auto_afk_unset(bot: Client, message: Message):
       global AFK, AFK_TIME, AFK_REASON, USERS, GROUPS

       if AFK:
           last_seen = subtract_time(datetime.now(), AFK_TIME).replace("ago", "").strip()
           reply = await message.reply(
               f"`Saat kau pergi (for {last_seen}), Anda diterima {sum(USERS.values()) + sum(GROUPS.values())} "
               f"messages from {len(USERS) + len(GROUPS)} chats`"
           )
           AFK = False
           AFK_TIME = ""
           AFK_REASON = ""
           USERS = {}
           GROUPS = {}
           await asyncio.sleep(5)
           await reply.delete()


add_command_help(
    "afk",
    [
        [".afk", "Mengaktifkan mode AFK dengan alasan apa pun setelahnya .afk\nUsage: ```.afk <reason>```"],
        ["!afk", "Nonaktifkan mode AFK."],
    ],
)
