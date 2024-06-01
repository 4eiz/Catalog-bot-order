from aiogram import Router, F
from aiogram.types import CallbackQuery, FSInputFile

from keyboards.client import Menu_callback, services
from config import bot

router = Router()



@router.callback_query(Menu_callback.filter(F.menu == 'services'))
async def services_menu(call: CallbackQuery, callback_data: Menu_callback):
    text = f'''
Вы в списке наших услуг,
Что вас интересует?
'''
    
    kb = services()
    photo = FSInputFile('app/photos/menu.jpeg')

    chat_id = call.from_user.id
    message_id = call.message.message_id
    await bot.delete_message(chat_id, message_id)
    await call.message.answer_photo(caption=text, reply_markup=kb, photo=photo)