from loader import dp, bot, db
from aiogram import types
from states.tarjima import Translate
from aiogram.dispatcher import FSMContext

@dp.message_handler(state=Translate.lang)
async def which_lang(message: types.Message, state: FSMContext):
    lang = message.text
    await state.update_data(
        {'lang': lang},
    )
    await message.answer(f"Tarjima qiluvchi matnni kiriting")
    await Translate.next()
