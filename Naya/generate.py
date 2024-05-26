import asyncio
from telethon import TelegramClient
from pyrogram.types import Message
from pyrogram import Client, filters
from asyncio.exceptions import TimeoutError
from telethon.sessions import StringSession
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from telethon.errors import rpcerrorlist
from pyrogram.errors import UserBannedInChannel
import telethon
import pyrogram
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from pyrogram.errors import (
    ApiIdInvalid,
    PhoneNumberInvalid,
    PhoneCodeInvalid,
    PhoneCodeExpired,
    SessionPasswordNeeded,
    PasswordHashInvalid
)
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.errors import (
    ApiIdInvalidError,
    PhoneNumberInvalidError,
    PhoneCodeInvalidError,
    PhoneCodeExpiredError,
    SessionPasswordNeededError,
    PasswordHashInvalidError
)
from config import *
from data import Data


ask_ques = "<b>Silakan Pilih Ya Anjeng Lu Mo Buat Apa\n\nSesuaikan Ya Anjeng, Pyrogram V2 atau Telethon</b>"
buttons_ques = [
    [
        InlineKeyboardButton("Pyrogram V2", callback_data="pyrogram"),
        InlineKeyboardButton("Telethon", callback_data="telethon"),
    ],

]

admin_kynan = [
    [
      InlineKeyboardButton(text="👮‍♂ Owner", user_id=f"5779185981"),
    ],
  ]

@Client.on_message(filters.private & ~filters.forwarded & filters.command('generate'))
async def main(_, msg):
    await msg.reply(ask_ques, reply_markup=InlineKeyboardMarkup(buttons_ques))


async def generate_session(bot: Client, msg: Message, telethon=False, is_bot: bool = False):
    if telethon:
        ty = "Telethon"
    else:
        ty = "Pyrogram V2"
    if is_bot:
        ty += " Bot"
    user_id = msg.chat.id
    api_id = API_ID
    api_hash = API_HASH
    await asyncio.sleep(1.0)
    if not is_bot:
        t = "**Woy Bangsat Kirim Nomer Akun Telegram Lu.** \n**Contoh** : `+6214045` **Jing Jadi Laper Gua**"
    else:
        t = "**Woy Bangsat Kirim Nomer Akun Telegram Lu.** \n**Contoh** : `+6214045` **Jing Jadi Laper Gua**"
    phone_number_msg = await bot.ask(user_id, t, filters=filters.text)
    if await cancelled(phone_number_msg):
        return
    phone_number = phone_number_msg.text
    if not is_bot:
        await msg.reply("**Bentar Jink Ngirim OTP Ke Akun Lu...**")
    else:
        await msg.reply("**Bentar Jink Ngirim OTP Ke Akun Lu...**")
    if telethon and is_bot:
        client = TelegramClient(StringSession(), api_id=api_id, api_hash=api_hash)
    elif telethon:
        client = TelegramClient(StringSession(), api_id=api_id, api_hash=api_hash)
    elif is_bot:
        client = Client(name="bot_{user_id}", api_id=api_id, api_hash=api_hash, bot_token=phone_number, in_memory=True)
    else:
        client = Client(name="user_{user_id}", api_id=api_id, api_hash=api_hash, in_memory=True)
    await client.connect()
    try:
        code = None
        if not is_bot:
            if telethon:
                code = await client.send_code_request(phone_number)
            else:
                code = await client.send_code(phone_number)
    except (PhoneNumberInvalid, PhoneNumberInvalidError):
        await msg.reply('**Nomer Akun Telegram Lu Ga Terdaftar Jink.**\n**Yang Bener Dikit Blog, Dari Ulang.**', reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return
    try:
        phone_code_msg = None
        if not is_bot:
            phone_code_msg = await bot.ask(user_id, "**Eh Bangsat periksa OTP Di Akun Telegram Lu, Buru cepet kirim OTP ke sini.** \n **Cara Masukin OTP kek gini** `1 2 3 4 5`\n**Jangan Salah Ya Nyet.**", filters=filters.text, timeout=600)
            if await cancelled(phone_code_msg):
                return
    except TimeoutError:
        await msg.reply('**Ngaret Lu Anjeng Lama...**', reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return
    if not is_bot:
        phone_code = phone_code_msg.text.replace(" ", "")
        try:
            if telethon:
                await client.sign_in(phone_number, phone_code, password=None)
            else:
                await client.sign_in(phone_number, code.phone_code_hash, phone_code)
        except (PhoneCodeInvalid, PhoneCodeInvalidError):
            await msg.reply('**Kode Nya Salah Monyet, Mata Lu Buta Apa Gimana.**', reply_markup=InlineKeyboardMarkup(Data.generate_button))
            return
        except (PhoneCodeExpired, PhoneCodeExpiredError):
            await msg.reply('**Goblok, Dibilang Pake Spasi Tiap Kode.**', reply_markup=InlineKeyboardMarkup(Data.generate_button))
            return
        except (SessionPasswordNeeded, SessionPasswordNeededError):
            try:
                two_step_msg = await bot.ask(user_id, '**Masukin Password Akun Lu Jing.**', filters=filters.text, timeout=300)
            except TimeoutError:
                await msg.reply('**Anjeng, Demen Banget Ngaret Jadi Manusia**', reply_markup=InlineKeyboardMarkup(Data.generate_button))
                return
            try:
                salah = await msg.reply("**Udah Jadi Nih Jing, Bentar**")
                password = two_step_msg.text
                if telethon:
                    await client.sign_in(password=password)
                else:
                    await client.check_password(password=password)
                if await cancelled(salah):
                    return
            except (PasswordHashInvalid, PasswordHashInvalidError):
                await two_step_msg.reply('**Lu Pikun Apa Gimana Si Nyet, Password Sendiri Salah.**', quote=True, reply_markup=InlineKeyboardMarkup(Data.generate_button))
                return
    else:
        if telethon:
            await client.start(bot_token=phone_number)
        else:
            await client.sign_in_bot(phone_number)
    if telethon:
        string_session = client.session.save()
    else:
        string_session = await client.export_session_string()
    text = f"**{ty.upper()} NIH JING.** \n\n`{string_session}` \n\n**Minimal Bilang Makasih Ke** @mhmdwldnnnn **Atau Ke** @musik_supportdan **Karna Akun Lu Kaga Deak**"
    try:
        try:
            if telethon:
                await client(JoinChannelRequest(f"https://t.me/Disney_storeDan"))
                await client(JoinChannelRequest(f"https://t.me/logsmusicbot"))
                await client(JoinChannelRequest(f"https://t.me/Great0623"))
                await client(JoinChannelRequest(f"{JOIN4}"))
            else:
                await client.join_chat(f"https://t.me/musik_supportdan")
                await client.join_chat(f"https://t.me/suportdanuserbot")
                await client.join_chat(f"{JOIN3}")
                await client.join_chat(f"{JOIN4}")
        except (rpcerrorlist.ChannelPrivateError, UserBannedInChannel):
            await msg.reply(f"**Jiah akun lu dibanned.\nCoba sono ngadu ke salah 1 admin biar dibuka ban nya.**", quote=True, reply_markup=InlineKeyboardMarkup(admin_mhmdwldnnnn))
            return
        if not is_bot:
            await client.send_message("me", text)
        else:
            await bot.send_message(msg.chat.id, text)
    except KeyError:
        pass
    await client.disconnect()
    await asyncio.sleep(1.0)
    await bot.send_message(msg.chat.id, " {} **Dah Jadi Ya Bangsat.** \n\n**Cek Pesan Tersimpan Lu Yang Banyak Bokep Nya!**".format("Telethon" if telethon else "Pyrogram"))


async def cancelled(msg):
    if "/cancel" in msg.text:
        await msg.reply("Goblok Ga jelas !", quote=True, reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return True
    elif "/restart" in msg.text:
        await msg.reply("Ngapain Jink !", quote=True, reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return True
    elif msg.text.startswith("/"):  # Bot Commands
        await msg.reply("Cancelled the generation process!", quote=True)
        return True
    else:
        return False
