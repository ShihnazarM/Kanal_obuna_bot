from loader import dp
from aiogram import types
from states.tarjima import Translate
from aiogram.dispatcher import FSMContext
from keyboards.inline.menu2 import ozgar
from googletrans import Translator


@dp.message_handler(state=Translate.trans)
async def do_translate(message: types.Message, state: FSMContext):
    text = message.text
    await state.update_data(
        {'text': text}
    )
    data = await state.get_data()
    lang = data.get("lang")
    tarjimon = Translator()
    if lang == 'πΊπΏ Uzb - π¬π§ Eng':
        tarjima = tarjimon.translate(text, dest="en")
        await message.answer(tarjima.text, reply_markup=ozgar)
        await state.update_data(
        {'text': tarjima.text}
    )

    elif lang == 'π¬π§ Eng - πΊπΏ Uzb': 
        tarjima = tarjimon.translate(text, dest="uz")
        await message.answer(tarjima.text, reply_markup=ozgar)
        await state.update_data(
        {'text': tarjima.text}
    )

    elif lang == 'πΊπΏ Uzb - π·πΊ Rus':
        tarjima = tarjimon.translate(text, dest="ru")
        await message.answer(tarjima.text, reply_markup=ozgar)
        await state.update_data(
        {'text': tarjima.text}
    )

    elif lang == 'π·πΊ Rus - πΊπΏ Uzb':
        tarjima = tarjimon.translate(text, dest="uz")
        await message.answer(tarjima.text, reply_markup=ozgar)
        await state.update_data(
        {'text': tarjima.text}
    )
    await Translate.audio.set()
