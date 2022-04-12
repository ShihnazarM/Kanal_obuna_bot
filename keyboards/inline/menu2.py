from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

ozgar = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🔄 O'zgartirish", callback_data="change")],
        [InlineKeyboardButton(text="🎵 Audio tinglash", callback_data="speach")]
    ]
)