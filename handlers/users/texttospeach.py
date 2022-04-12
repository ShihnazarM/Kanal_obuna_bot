from loader import dp
from gtts import gTTS
from aiogram import types
from states.tarjima import Translate
from aiogram.dispatcher import FSMContext
from keyboards.default.lang import menu
import os

@dp.callback_query_handler(state=Translate.audio, text="speach")
async def send_audio(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    await call.message.edit_reply_markup()
    lang = data.get("lang")
    text = data.get('text')

    if lang == '🇺🇿 Uzb - 🇬🇧 Eng':
        tts = gTTS(text, lang='en')
        tts.save(f'audio{call.message.from_user.id}.mp3')
        await call.message.answer_audio(audio=open(f'audio{call.message.from_user.id}.mp3', 'rb'), reply_markup=menu)
        if os.path.exists(f'audio{call.message.from_user.id}.mp3'):
            os.remove(f'audio{call.message.from_user.id}.mp3')
        await Translate.lang.set()

    elif lang == '🇬🇧 Eng - 🇺🇿 Uzb': 
        tts = gTTS(text, lang='tr')
        tts.save(f'audio{call.message.from_user.id}.mp3')
        await call.message.answer_audio(audio=open(f'audio{call.message.from_user.id}.mp3', 'rb'), reply_markup=menu)
        if os.path.exists(f'audio{call.message.from_user.id}.mp3'):
            os.remove(f'audio{call.message.from_user.id}.mp3')
        await Translate.lang.set()

    elif lang == '🇺🇿 Uzb - 🇷🇺 Rus':
        tts = gTTS(text, lang='ru')
        tts.save(f'audio{call.message.from_user.id}.mp3')
        await call.message.answer_audio(audio=open(f'audio{call.message.from_user.id}.mp3', 'rb'), reply_markup=menu)
        if os.path.exists(f'audio{call.message.from_user.id}.mp3'):
            os.remove(f'audio{call.message.from_user.id}.mp3')
        await Translate.lang.set()

    elif lang == '🇷🇺 Rus - 🇺🇿 Uzb':
        tts = gTTS(text, lang='tr')
        tts.save(f'audio{call.message.from_user.id}.mp3')
        await call.message.answer_audio(audio=open(f'audio{call.message.from_user.id}.mp3', 'rb'), reply_markup=menu)
        if os.path.exists(f'audio{call.message.from_user.id}.mp3'):
            os.remove(f'audio{call.message.from_user.id}.mp3')
        await Translate.lang.set()
