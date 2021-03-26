import config
# import exchange
import telebot
# import datetime
import pytz
# import json
# import traceback


P_TIMEZONE = pytz.timezone(config.TIMEZONE)
TIMEZONE_COMMON_NAME = config.TIMEZONE_COMMON_NAME

bot = telebot.TeleBot(config.TOKEN)



@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(
        message.chat.id,
        'Привет! Я могу показывать курсы валют!\n' +
        'Чтобы запросить список валют - нажми /exchange.\n' +
        'Чтобы запросить помощь - нажми /help.'
  )


# @bot.message_handler(commands=['help'])
# def help_command(message):
#     keyboard = telebot.types.InlineKeyboardMarkup()
#     keyboard.add(
#         telebot.types.InlineKeyboardButton(
#             'Message the developer', url='telegram.me/balashovia'
#   )
#     )
#     bot.send_message(
#         message.chat.id,
#         '1) Чтобы увидеть список доступных валют, нажмите /exchange.\n' +
#         '2) Нажмите на интересующую Вас валюту.\n' +
#         '3) Вы получите информацию по продаже и покупке выбранной валюты по курсу ЦБ.\n' +
#         '4) Нажмите “Update”, чтобы обновить текущую информацию по курсу.\n' +
#         '5) Поддержка Бота всегда на связи. Напишите telegram.me/balashovia по любым вопросам и предложениям',
#         reply_markup=keyboard
#     )
#
#
# @bot.message_handler(commands=['exchange'])
# def exchange_command(message):
#     keyboard = telebot.types.InlineKeyboardMarkup(row_width=4)
#     for val in exchange.load_exchange()['Valute']:
#         btn = telebot.types.InlineKeyboardButton(f'{val}', callback_data=f'btn-{val}')
#         keyboard.add(btn)
#     bot.send_message(
#         message.chat.id,
#         'Выберите валюту:',
#         reply_markup=keyboard
#     )

bot.polling(none_stop=True)