from pyrogram import Client, enums, filters
from pyrogram.types import Message

from Gz import SUDO_USER
from Gz.modules.help import add_command_help

@Client.on_message(
    filters.command(["join"], ".") & (filters.me | filters.user(SUDO_USER))
)
async def join(client: Client, message: Message):
    tex = message.command[1] if len(message.command) > 1 else message.chat.id
    g = await message.reply_text("`Processing...`")
    try:
        await client.join_chat(tex)
        await g.edit(f"**Berhasil Bergabung dengan Obrolan ID** `{tex}`")
    except Exception as ex:
        await g.edit(f"**ERROR:** \n\n{str(ex)}")


@Client.on_message(
    filters.command(["leave"], ".") & (filters.me | filters.user(SUDO_USER))
)
async def leave(client: Client, message: Message):
    xd = message.command[1] if len(message.command) > 1 else message.chat.id
    xv = await message.reply_text("`Processing...`")
    try:
        await xv.edit_text(f"{client.me.first_name} telah meninggalkan grup ini, bye!!")
        await client.leave_chat(xd)
    except Exception as ex:
        await xv.edit_text(f"**ERROR:** \n\n{str(ex)}")


@Client.on_message(
    filters.command(["leaveallgc"], ".") & (filters.me | filters.user(SUDO_USER))
)
async def kickmeall(client: Client, message: Message):
    tex = await message.reply_text("`Cuti Global dari obrolan grup...`")
    er = 0
    done = 0
    async for dialog in client.get_dialogs():
        if dialog.chat.type in (enums.ChatType.GROUP, enums.ChatType.SUPERGROUP):
            chat = dialog.chat.id
            try:
                done += 1
                await client.leave_chat(chat)
            except BaseException:
                er += 1
    await tex.edit(
        f"**Berhasil pergi {done} Groups, Gagal Untuk pergi {er} Groups**"
    )


@Client.on_message(filters.command(["leaveallch"], ".") & filters.me)
async def kickmeallch(client: Client, message: Message):
    ok = await message.reply_text("`Cuti Global dari obrolan grup...`")
    er = 0
    done = 0
    async for dialog in client.get_dialogs():
        if dialog.chat.type in (enums.ChatType.CHANNEL):
            chat = dialog.chat.id
            try:
                done += 1
                await client.leave_chat(chat)
            except BaseException:
                er += 1
    await ok.edit(
        f"**Berhasil pergi {done} Channel, gagal untuk pergi {er} Channel**"
    )


add_command_help(
    "joinleave",
    [
        [
            "kickme",
            "To leave!!.",
        ],
        ["leaveallgc", "to leave all groups where you joined."],
        ["leaveallch", "to leaveall channel where you joined."],
        ["join [Username]", "give an specific username to join."],
        ["leave [Username]", "give an specific username to leave."],
    ],
)
