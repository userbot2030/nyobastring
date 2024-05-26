from config import MUST_JOIN
from pyrogram import Client, filters
from pyrogram.types import *
from pyrogram.errors import *

@Client.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(bot: Client, msg: Message):
    #if UserBannedInChannel:
      
    try:
        try:
            await bot.get_chat_member(MUST_JOIN, msg.from_user.id)
        except UserBannedInChannel:
            return await bot.send_message(msg.chat.id, "**Mᴀᴀғ, Aɴᴅᴀ ᴛɪᴅᴀᴋ ᴅᴀᴘᴀᴛ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ ʙᴏᴛ ɪɴɪ ᴋᴀʀᴇɴᴀ ᴀɴᴅᴀ ᴅɪ ʙᴀɴɴᴇᴅ ᴅᴀʀɪ ᴍᴜsɪᴄ Sᴜᴘᴘᴏʀᴛ**\n**sɪʟᴀᴋᴀɴ ᴄᴏɴᴛᴀᴄᴛ @ ᴀɢᴀʀ ᴅɪʙᴜᴋᴀ ʙʟᴏᴋɪʀ ᴀɴᴅᴀ.**"
            )
            try:
                chat_info = await bot.get_chat(MUST_JOIN)
                link = chat_info.invite_link
                await msg.reply(
                    f"sɪ ᴀɴᴊᴇɴɢ, ᴍᴀsᴜᴋ sɪɴɪ ᴅᴜʟᴜ ʟᴜ ʙᴀɴɢsᴀᴛ !",
                    disable_web_page_preview=True,
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton("sɪɴɪ ɴʏᴇᴛ ᴍᴀsᴜᴋ, ᴊᴀɴɢᴀɴ ʟᴜᴘᴀ sᴀʟᴀᴍ", url=f"")]
                    ])
                )
                await msg.stop_propagation()
            except UserBannedInChannel:
                await bot.send_message(
                msg.chat.id,
                "**Mᴀᴀғ, Aɴᴅᴀ ᴛɪᴅᴀᴋ ᴅᴀᴘᴀᴛ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ ʙᴏᴛ ɪɴɪ ᴋᴀʀᴇɴᴀ ᴀɴᴅᴀ ᴅɪ ʙᴀɴɴᴇᴅ ᴅᴀʀɪ ᴍᴜsɪᴄ Sᴜᴘᴘᴏʀᴛ**\n**sɪʟᴀᴋᴀɴ ᴄᴏɴᴛᴀᴄᴛ @mhmdwldnnnn ᴀɢᴀʀ ᴅɪʙᴜᴋᴀ ʙʟᴏᴋɪʀ ᴀɴᴅᴀ.**"
            )
    except ChatAdminRequired:
        print(f"I'm not admin in the MUST_JOIN chat : {MUST_JOIN} !")
