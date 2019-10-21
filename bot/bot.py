#! /usr/bin/env python
# -*- coding: utf-8 -*-

import telebot, time
import requests
from telebot import apihelper, types


# Configure
TOKEN = '959039109:AAE0sPZPtj_bfbgs3zUhYhP78UKivIXo19w'
# PROXY = 'socks5://162.243.32.120:33727'

# apihelper.proxy = {'https': PROXY}
bot = telebot.TeleBot(TOKEN)

text_messages = {
    'start':
        u'Приветствую тебя, {name}!\n'
        u'Я помогу тебе добавить или удалить твою заметку.\n\n'
        u'Для работы нужно узнать твое имя и возраст\n'
        u'И все! Можешь пользоваться ботом',
}


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.from_user.id, text_messages['start'].format(name=message.from_user.first_name))
    r = requests.get('http://localhost:8000/TG_user')
    print(r.text)


@bot.message_handler(commands=['allnote'])
def allnote(message):
    allnotedb = requests.get('http://localhost:8000/Note')
    bot.send_message(message.from_user.id, allnotedb)
    print(allnotedb)


@bot.message_handler(commands=['reg'])
def reg(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_18_21 = types.KeyboardButton(text="18-21")
    button_22_25 = types.KeyboardButton(text="22-25")
    button_25_30 = types.KeyboardButton(text="25-30")
    button_30 = types.KeyboardButton(text="30+")
    keyboard.add(button_18_21, button_22_25, button_25_30, button_30)
    bot.send_message(message.chat.id, 'Сколько тебе лет?', reply_markup=keyboard)


# @bot.message_handler(func=lambda m: True)
# def echo_all(message):
#     bot.reply_to(message.message.text)


while True:
    try:
        print('Запущен')
        bot.polling(none_stop=True)
    except Exception:
        print('Что-то не работает')
