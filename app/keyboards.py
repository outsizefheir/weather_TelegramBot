from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Прогноз', callback_data='forecast')]
])
