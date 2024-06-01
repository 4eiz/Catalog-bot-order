from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

from keyboards.client import Menu_callback, cancel, admin
from data import users
from config import bot, ADMIN



class Admin(StatesGroup):
    new_message = State()
    new_photo = State()


router = Router()


@router.message(Command("admin"))
async def admin_menu(message: Message, state: FSMContext):
    user_id = message.from_user.id
    
    if user_id == ADMIN:
        message_id = message.message_id

        await bot.delete_message(user_id, message_id)

        kb = admin()
        count = await users.get_user_count()
        text = f'<b>Админ меню\nЮзеров: <code>{count}</code></b>'

        await message.answer(text=text, reply_markup=kb)


@router.callback_query(Menu_callback.filter(F.menu == 'news'))
async def new_mes(call: CallbackQuery, callback_data: Menu_callback, state: FSMContext):
    user_id = call.from_user.id
    if user_id == ADMIN:
        await state.set_state(Admin.new_message)

        message_id = call.message.message_id
        await bot.delete_message(user_id, message_id)

        kb = cancel()
        text = '<b>Введите сообщение рассылки:</b>'
        await call.message.answer(text=text, reply_markup=kb)
    else:
        return


@router.message(Admin.new_message, F.text)
async def result(message: Message, state: FSMContext):
    await state.update_data(new_mes=message.text)
    await state.set_state(Admin.new_photo)
    
    kb = cancel()
    text = '<b>Отправьте фото для рассылки или напишите что угодно:</b>'
    await message.answer(text=text, reply_markup=kb)


@router.message(Admin.new_photo, F.photo)
async def result_with_photo(message: Message, state: FSMContext):
    state_data = await state.get_data()
    new_mes = state_data.get("new_mes")
    new_photo = message.photo[-1].file_id
    
    user_table = await users.get_all_ids_from_db()
    text1 = '<b>Рассылка успешно запущена!</b>'
    await message.answer(text=text1)
    for user in user_table:
        try:
            await bot.send_photo(user, new_photo, caption=new_mes)
        except Exception as e:
            print(e)
    
    text2 = '<b>Рассылка успешно завершена!</b>'
    await message.answer(text=text1)


    await state.clear()


@router.message(Admin.new_photo, F.text)
async def result_without_photo(message: Message, state: FSMContext):
    new_mes = message.text
    
    user_table = await users.get_all_ids_from_db()
    for user in user_table:
        try:
            await bot.send_message(user, new_mes)
        except Exception as e:
            print(e)
    
    text1 = '<b>Рассылка успешно запущена!</b>'
    await message.answer(text=text1)
    kb = admin()
    text2 = 'Админ меню'
    await message.answer(text=text2, reply_markup=kb)

    await state.clear()
