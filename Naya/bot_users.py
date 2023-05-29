from pyrogram.types import Message
from pyrogram import Client, filters
from .basic import GUA
from .database.user import add_served_user, get_served_users


@Client.on_message(filters.private & ~filters.service, group=1)
async def users_sql(_, msg: Message):
    await add_served_user(msg.from_user.id)


@Client.on_message(filters.user(GUA) & filters.command("stats"))
async def _stats(_, msg: Message):
    users = len(await get_served_users())
    await msg.reply_text(f"» Kumpulan babi babi liar :\n\nTotal ada {users} babi ")


@Client.on_message(filters.command("bacot"))
async def bacot(bot: Client, message):
    if len(message.command) > 1:
        text = " ".join(message.command[1:])
    elif message.reply_to_message is not None:
        text = message.reply_to_message.text
    else:
        await message.reply(
            "<code>Silakan sertakan pesan atau balas pesan yang ingin disiarkan.</code>"
        )
        return
      
    if message.from_user.id not in GUA:
        await message.reply_text(
            "<b>Lu siapa Monyeddd.</b>"
        )
        return
      
    kntl = 0
    mmk = []
    babi = await get_served_users()
    for x in babi:
            mmk.append(int(x["user_id"]))
    for i in mmk:
        try:
            await bot.send_message(i, text)
            kntl += 1
        except Exception as e:
            await message.reply(f"Error saat mengirim pesan ke {x} babi, Karena: {e}")
    return await message.reply(f"Berhasil memotong {kntl} babi, dari {mmk} babi.")