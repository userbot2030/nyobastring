from pyrogram.types import InlineKeyboardButton
from config import *


class Data:
    generate_single_button = [InlineKeyboardButton(" ᴍᴜʟᴀɪ ᴀᴍʙɪʟ sᴛʀɪɴɢ ", callback_data="generate")]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text=" ᴋᴇᴍʙᴀʟɪ ", callback_data="home")]
    ]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [InlineKeyboardButton("ᴏᴡɴᴇʀ", user_id=f"5779185981")],
        [
            InlineKeyboardButton("ʙᴀɴᴛᴜᴀɴ", callback_data="help"),
            InlineKeyboardButton("ᴛᴇɴᴛᴀɴɢ sᴀʏᴀ", callback_data="about")
        ],
        [InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/musik_supportdan")],
    ]

    START = """
**ᴡᴏʏ ᴀɴᴊᴇɴɢ** {}

**sᴇʟᴀᴍᴀᴛ ᴅᴀᴛᴀɴɢ ᴅɪ** {}

**ɪɴɪ ᴀᴅᴀʟᴀʜ ʙᴏᴛ sᴛʀɪɴɢ sᴇssɪᴏɴ ᴀɴᴛɪ ᴅᴇᴀᴋ ʏᴀ ʙᴀɴɢsᴀᴛ

ɪɴɪ ᴀᴅᴀʟᴀʜ ʙᴏᴛ sᴛʀɪɴɢ sᴇssɪᴏɴ ᴀɴᴛɪ ᴅᴇᴀᴋ ʏᴀ ʙᴀɴɢsᴀᴛ**
    """

    HELP = """
**List Bantuan**

/about - Cek Nyet
/help - Cek Nyet
/start - Cek Nyet
/generate - Cek Nyet
/cancel - Cek Nyet
/restart - Cek Nyet
"""

    ABOUT = """
**ᴛᴇɴᴛᴀɴɢ sᴀʏᴀ** 

**ʙᴜᴀᴛ ʟᴜ ʏᴀɴɢ ʙᴀʀᴜ ᴍᴀᴇɴ ᴛᴇʟᴇ ʏᴀ ᴀɴᴊᴇɴɢ..**

ᴄᴜᴍᴀ ᴍᴏᴅᴀʟ ᴄᴏᴘᴀs ʏᴀ ᴀɴᴊᴇɴɢ, ɢᴜᴀ ʙᴜᴋᴀɴ ᴘʀᴏᴅᴇᴠ ʏᴀ ʙᴀɴɢsᴀᴛ

ᴍᴀɪɴᴛᴀɪɴᴇʀ : @mhmdwldnnnn**
    """
