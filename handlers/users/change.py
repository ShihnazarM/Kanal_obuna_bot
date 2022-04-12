from loader import dp
from aiogram import types
from states.tarjima import Translate
from aiogram.dispatcher import FSMContext
from keyboards.default.lang import menu


@dp.callback_query_handler(text="change", state=Translate.audio)
async def change_lang(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer("Tilni o'zgartirmoqchimisiz?", reply_markup=menu)
    await call.message.edit_reply_markup()
    await Translate.lang.set()