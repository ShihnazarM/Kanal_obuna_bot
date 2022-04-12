import sqlite3

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from data.config import ADMINS
from loader import dp, db, bot

from keyboards.default.lang import menu
from states.tarjima import Translate

from data.config import CHANNELS
from keyboards.inline.obuna import check_button



@dp.message_handler(CommandStart(), state="*")
async def bot_start(message: types.Message):
    name = message.from_user.full_name
    # Foydalanuvchini bazaga qo'shamiz
    try:
        db.add_user(id=message.from_user.id,name=name)
        # await message.answer(f"Xush kelibsiz! {name}", reply_markup=menu)
        channels_format = str()
        for channel in CHANNELS:
            chat = await bot.get_chat(channel)
            invite_link = await chat.export_invite_link()
            # logging.info(invite_link)
            channels_format += f"➡️ <a href='{invite_link}'><b>{chat.title}<b></a>\n"

        await message.answer(f"Quyudagi kanalga obuna boling: \n\n"f"{channels_format}",reply_markup=check_button,disable_web_page_preview=True)
        # await Translate.lang.set()
        # Adminga xabar beramiz
        count = db.count_users()[0]
        msg = f"{message.from_user.full_name} bazaga qo'shildi.\nBazada {count} ta foydalanuvchi bor."
        await bot.send_message(chat_id=ADMINS[0], text=msg)

    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS[0], text=f"{name} bazaga oldin qo'shilgan")
        # await message.answer(f"Xush kelibsiz! {name}", reply_markup=menu)
        # await Translate.lang.set()
        channels_format = str()
        for channel in CHANNELS:
            chat = await bot.get_chat(channel)
            invite_link = await chat.export_invite_link()
            # logging.info(invite_link)
            channels_format += f"➡️ <a href='{invite_link}'><b>{chat.title}</b></a>\n"

        await message.answer(f"Quyudagi kanalga obuna boling: \n\n"f"{channels_format}",reply_markup=check_button,disable_web_page_preview=True)


