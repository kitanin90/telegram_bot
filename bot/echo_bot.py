#! /usr/bin/env python
# -*- coding: utf-8 -*-

import telebot, time
from telebot import apihelper, types

# Configure
TOKEN = '959039109:AAE0sPZPtj_bfbgs3zUhYhP78UKivIXo19w'
PROXY = 'socks5://162.243.32.120:33727'

apihelper.proxy = {'https': PROXY}
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Привет, как тебя зовут?')


@bot.message_handler(commands=['reg'])
def reg(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_18_21 = types.KeyboardButton(text="18-21")
    button_22_25 = types.KeyboardButton(text="22-25")
    button_25_30 = types.KeyboardButton(text="25-30")
    button_30 = types.KeyboardButton(text="30+")
    keyboard.add(button_18_21, button_22_25, button_25_30, button_30)
    bot.send_message(message.chat.id, 'Сколько тебе лет?', reply_markup=keyboard)


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message.message.text)


while True:
    try:
        print('Запущен')
        bot.polling(none_stop=True)
    except Exception:
        print('Что-то не работает')
