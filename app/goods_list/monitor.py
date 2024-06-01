from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, FSInputFile

from keyboards.client import Menu_callback, item
from config import bot

router = Router()


@router.callback_query(Menu_callback.filter(F.menu == 'monitor'))
async def monitor(call: CallbackQuery, callback_data: Menu_callback):
    text = '''
Монитор
описание и бла бла бла бла
'''

    chat_id = call.from_user.id
    message_id = call.message.message_id
    await bot.delete_message(chat_id, message_id)

    photo = FSInputFile('app/photos/monitor.jpeg')
    kb = item()
    await call.message.answer_photo(caption=text, reply_markup=kb, photo=photo)