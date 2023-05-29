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
