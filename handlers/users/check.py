from typing import final
from loader import dp, bot
from data.config import CHANNELS
from utils.misc import subscription
from aiogram import types
from keyboards.default.lang import menu
from keyboards.inline.obuna import check_button
from states.tarjima import Translate

@dp.callback_query_handler(text="check_subs")
async def checker(call: types.CallbackQuery):
    await call.answer("Obuna tekshirildi")
    final_status = True
    result = str()
    for channel in CHANNELS:
        status = await subscription.check(user_id=call.from_user.id,
                                          channel=channel)
        channel = await bot.get_chat(channel)
        if status:
            final_status *= status
            result += f"✅ <b>{channel.title}</b> kanaliga obuna bolsangiz!\n\n"

        else:
            final_status *= False
            invite_link = await channel.export_invite_link()
            result += (f"❌ <a href= '{invite_link}'><b>{channel.title}</b></a> kanaliga obuna bo'lmagansiz.\n\n")

    if final_status:
        await call.message.delete()
        msg = f"Salom xush kelibsiz\n🧍 <b>{call.from_user.full_name}</b>!\nTarjima turini tanlang! ⬇️"
        await call.message.answer(msg, reply_markup=menu)
        await Translate.lang.set()
    else:
        await call.message.delete()
        await call.message.answer(result, disable_web_page_preview=True, reply_markup=check_button)
