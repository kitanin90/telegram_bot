#! /usr/bin/env python
# -*- coding: utf-8 -*-

import telebot, time

from telebot import apihelper

#Configure
TOKEN = '959039109:AAE0sPZPtj_bfbgs3zUhYhP78UKivIXo19w'
PROXY = 'socks5://162.243.32.120:33727'

apihelper.proxy = {'https': PROXY}
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, 'Привет, как дела?')


@bot.message_handler(func=lambda m:True)
def echo_all(message):
	bot.reply_to(message.message.text)


while True:
	try:
		bot.polling(none_stop=True)
	except Exception:
		print('Что-то не работает')
