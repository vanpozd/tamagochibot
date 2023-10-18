import telebot
import tamconf
import json
import datetime
from telebot import types
#beast - main animal

def echo_all(message):
    chat_id = message.chat.id
    message_date = datetime.datetime.fromtimestamp(message.date)
    print(f'Новое сообщение от {message.chat.username}({message.chat.id})({message_date}): {message.text}')
    bot.send_message(1256707116, f"-{message.chat.username}({message.chat.id})\n-({message_date})\n-{message.text}")
    bot.send_message(617493696, f"Новое сообщение от {message.chat.username}({message.chat.id})({message_date}): {message.text}")
def feed_beast(message):
    print("shdfnsjdfnjhdsnb")
def add_data_to_json(jsontype: object, key, value):     #NOT DONE
    json.dump(jsontype)
def create_main_markup():
    main_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    feed_button = types.KeyboardButton("Покорми меня")
    main_markup.add(feed_button)
    return main_markup



bot = telebot.TeleBot(tamconf.main_bot_token)

@bot.message_handler(commands=['start'])
def welocme(message):
    echo_all(message)
    main_markup = create_main_markup()
    bot.send_message(message.chat.id,"main menu",reply_markup = main_markup)

@bot.message_handler(func=lambda message: True)
def message_taker(message):
    echo_all(message)
    if message.chat.type == 'private':
        if message.text == "Покорми меня":
            feed_beast(message)


def main():
    bot.polling()

if __name__ == '__main__':
    main()