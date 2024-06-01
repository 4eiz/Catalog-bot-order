from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, FSInputFile

from keyboards.client import Menu_callback, service
from config import bot

router = Router()


@router.callback_query(Menu_callback.filter(F.menu == 'updating'))
async def updating(call: CallbackQuery, callback_data: Menu_callback):
    text = '''
Обновление
описание и бла бла бла бла
'''

    chat_id = call.from_user.id
    message_id = call.message.message_id
    await bot.delete_message(chat_id, message_id)

    photo = FSInputFile('app/photos/updating.jpeg')
    kb = service()
    await call.message.answer_photo(caption=text, reply_markup=kb, photo=photo)