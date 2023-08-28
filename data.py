from pyrogram.types import InlineKeyboardButton
from config import *


class Data:
    generate_single_button = [InlineKeyboardButton(" Mulai Ambil String ", callback_data="generate")]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text=" Kembali ", callback_data="home")]
    ]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [InlineKeyboardButton("Owner", user_id=OWNER_ID)],
        [
            InlineKeyboardButton("Bantuan", callback_data="help"),
            InlineKeyboardButton("Tentang Saya", callback_data="about")
        ],
        [InlineKeyboardButton("Support", url=f"https://t.me/{SUPPORT}")],
    ]

    START = """
**Woy Anjeng** {}

**Selamat Datang Di** {}

**Ini Adalah Bot String Session Anti Deak Ya Bangsat

Buat Lu ID 5 atau ID 6 yang Baru Maen Telegram**
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
**Tentang Saya** 

**Buat Lu Yang Baru Maen Tele Ya Anjeng..**

Cuma Modal Copas Ya Anjeng, Gua Bukan ProDev Ya Bangsat

Maintainer : @kenapanan**
    """
