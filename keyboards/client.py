from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters.callback_data import CallbackData
from aiogram import types
from config import CHANNEL_URL, SUPPORT_URL, SUPPORT_BOT

class Menu_callback(CallbackData, prefix="menu"):
    menu: str



# Клавиатура с обязательной подпиской
def menu_subscribe():
    kb = [
        [
            types.InlineKeyboardButton(text='КАНАЛ', url=CHANNEL_URL),
        ],
        [
            types.InlineKeyboardButton(text='Проверить подписку', callback_data=Menu_callback(menu="menu").pack()),
        ]
    ]
    return types.InlineKeyboardMarkup(inline_keyboard=kb)


# Клавиатура главного меню
def menu():
    kb = [
        [
            types.InlineKeyboardButton(text='Список товаров', callback_data=Menu_callback(menu="goods").pack()),
        ],
        [
            types.InlineKeyboardButton(text='Наши услуги', callback_data=Menu_callback(menu="services").pack()),
        ],
        [
            types.InlineKeyboardButton(text='Бот обратной связи', url=SUPPORT_BOT),
        ]
    ]
    return types.InlineKeyboardMarkup(inline_keyboard=kb)


# Клавиатура с товарами
def goods():
    kb = [
        [
            types.InlineKeyboardButton(text='Мышка', callback_data=Menu_callback(menu="mouse").pack()),
        ],
        [
            types.InlineKeyboardButton(text='Клавиатура', callback_data=Menu_callback(menu="keyboard").pack()),
        ],
        [
            types.InlineKeyboardButton(text='Монитор', callback_data=Menu_callback(menu="monitor").pack()),
        ],
        [
            types.InlineKeyboardButton(text='Назад', callback_data=Menu_callback(menu="menu").pack()),
        ],
    ]
    return types.InlineKeyboardMarkup(inline_keyboard=kb)


# Клавиатура с услугами
def services():
    kb = [
        [
            types.InlineKeyboardButton(text='Ремонт ПК', callback_data=Menu_callback(menu="repair").pack()),
        ],
        [
            types.InlineKeyboardButton(text='Установка программ', callback_data=Menu_callback(menu="installing").pack()),
        ],
        [
            types.InlineKeyboardButton(text='Чистка ПК', callback_data=Menu_callback(menu="cleaning").pack()),
        ],
        [
            types.InlineKeyboardButton(text='Обновление драйверов', callback_data=Menu_callback(menu="updating").pack()),
        ],
        [
            types.InlineKeyboardButton(text='Назад', callback_data=Menu_callback(menu="menu").pack()),
        ],
    ]
    return types.InlineKeyboardMarkup(inline_keyboard=kb)


def item():
    kb = [
        [
            types.InlineKeyboardButton(text='Связаться с нами', url=SUPPORT_URL),
        ],
        [
            types.InlineKeyboardButton(text='Назад', callback_data=Menu_callback(menu="goods").pack()),
        ],
    ]
    return types.InlineKeyboardMarkup(inline_keyboard=kb)


def service():
    kb = [
        [
            types.InlineKeyboardButton(text='Связаться с нами', url=SUPPORT_URL),
        ],
        [
            types.InlineKeyboardButton(text='Назад', callback_data=Menu_callback(menu="services").pack()),
        ],
    ]
    return types.InlineKeyboardMarkup(inline_keyboard=kb)


def cancel():
    kb = [
        [
            types.InlineKeyboardButton(text='Назад', callback_data=Menu_callback(menu="menu").pack()),
        ],
    ]
    return types.InlineKeyboardMarkup(inline_keyboard=kb)


# Админка
def admin():
    # 
    kb = [
        [
            types.InlineKeyboardButton(text='Рассылка', callback_data=Menu_callback(menu="news").pack()),
        ],
        [
            types.InlineKeyboardButton(text='Назад', callback_data=Menu_callback(menu="menu").pack()),
        ],
    ]
    return types.InlineKeyboardMarkup(inline_keyboard=kb)