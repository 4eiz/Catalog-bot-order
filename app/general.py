from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram import Router, F
from aiogram.types import CallbackQuery, FSInputFile
from aiogram.fsm.context import FSMContext

from keyboards.client import Menu_callback, menu_subscribe, menu
from data import users

from config import bot, CHANNEL_ID

router = Router()




@router.message(CommandStart())
async def start(message: Message, state: FSMContext):
    try:
        await state.clear()
    except:
        pass

    user_id = message.from_user.id

    sub = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=user_id)

    if sub.status != 'left':
        await users.new_user(user_id=user_id)

        text = 'Добро пожаловать!\nЧто вас интересует?'
        kb = menu()
        photo = FSInputFile('app/photos/menu.jpeg')

        await message.answer_photo(caption=text, reply_markup=kb, photo=photo)

    else:
        text = 'Подпишитесь на канал'
        kb = menu_subscribe()
        await message.answer(text=text, reply_markup=kb)





@router.callback_query(Menu_callback.filter(F.menu == 'menu'))
async def start(call: CallbackQuery, callback_data: Menu_callback, state: FSMContext):
    try:
        await state.clear()
    except:
        pass

    user_id = call.from_user.id

    sub = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=user_id)


    message_id = call.message.message_id
    await bot.delete_message(user_id, message_id)


    if sub.status != 'left':
        await users.new_user(user_id=user_id)

        text = 'Добро пожаловать!\nЧто вас интересует?'
        kb = menu()
        photo = FSInputFile('app/photos/menu.jpeg')

        await call.message.answer_photo(caption=text, reply_markup=kb, photo=photo)

    else:
        text = 'Подпишитесь на канал'
        kb = menu_subscribe()
        await call.message.answer(text=text, reply_markup=kb)