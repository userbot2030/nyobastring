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
      
    babi = await get_served_users()

    total_users = len(babi)
    sent_count = 0
    for x in babi:
        try:
            await bot.send_message(x, text)
            sent_count += 1
        except Exception as e:
            await message.reply(f"Error saat mengirim pesan ke {x}: {e}")

    return await message.reply_text(
        f"<b>Pesan siaran berhasil dikirim kepada {sent_count} babi dari {total_users} babi.</b>"
    )