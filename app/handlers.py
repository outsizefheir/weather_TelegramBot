from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
import app.keyboards as kb

from Forecast import get_forecast


router = Router()

start_message = '''
Тестовое задание.
Telegram-бот, который возвращает прогноз погоды.
'''

@router.message(CommandStart()) 
async def cmd_start(message: Message): 
	await message.answer(start_message, reply_markup=kb.main)
 
@router.callback_query(F.data == 'forecast') 
async def catolog(callback: CallbackQuery): 
	await callback.answer('Ah shit')
	await callback.message.answer('Ведите город для получения информации о текущей погоде')

@router.message()
async def cmd_forecast(message: Message):
    city = message.text.strip()
    data = get_forecast(city)
    
    if data:
        response_message = (
            f'Погода в городе {data['city']}:\n'
            f'Температура: {data['temp']}°C\n'
            f'Давление: {data['pressure']}\n'
            f'Влажность: {data['humidity']}%\n'
            f'Скорость ветра: {data['wind_speed']}\n'
            f'Описание: {data['description']}'
        )
    else:
        response_message = 'Упс, попробуйте еще раз.'

    await message.answer(response_message)

    