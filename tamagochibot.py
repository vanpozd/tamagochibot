import telebot
import tamconf
import json
import os
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
def beast_data_correcter(lvl, name):
    beast_data = {
        'name': name,
        'lvl': lvl
    }
    return beast_data
def beast_DB_data_change(file_path, key, data_dict):
    if not os.path.isfile(file_path):
        with open(file_path, 'w') as new_file:
            json.dump({}, new_file)

    try:
        with open(file_path, 'r') as file:
            data = json.load(file)  # Завантажуємо дані з JSON-файлу

        if key in data and isinstance(data[key], dict):
            data[key].update(data_dict)
        else:
            data[key] = data_dict  # Створюємо словник і додаємо значення

        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)  # Зберігаємо оновлені дані назад у файл

        print(f"Data was successfully add with key: {key} in file: '{file_path}'.")

    except json.JSONDecodeError:
        print(f"[ERROR]Incorrect data record in file: '{file_path}'.")
def beast_creation(message,beast_count):
    beast_key = int(str(message.chat.id) + str(beast_count))
    beast_lvl = 1
    beast_name = message.text
    beast_collected_info = beast_data_correcter(beast_lvl,beast_name)
    beast_DB_data_change(tamconf.main_data_file,beast_key,beast_collected_info)

def create_main_markup():
    main_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    feed_button = types.KeyboardButton("Покорми меня")
    main_markup.add(feed_button)
    return main_markup
def create_beast_markup():
    beast_creation_markup = types.InlineKeyboardMarkup()
    first_beast = types.InlineKeyboardButton("Add first beast", callback_data="beast_1")
    beast_creation_markup.add(first_beast)
    return beast_creation_markup

bot = telebot.TeleBot(tamconf.main_bot_token)

@bot.message_handler(commands=['start'])
def welocme(message):
    echo_all(message)
    main_markup = create_main_markup()
    bot.send_message(message.chat.id,"main menu",reply_markup = main_markup)
    beast_markup = create_beast_markup()
    bot.send_message(message.chat.id,"test_beast_create",reply_markup=beast_markup)

@bot.message_handler(func=lambda message: True)
def message_taker(message):
    echo_all(message)
    if message.chat.type == 'private':
        if message.text == "Покорми меня":
            feed_beast(message)

@bot.callback_query_handler(func=lambda call: call.data.startswith('beast_'))
def beast_counter(call):
    beast_count = int(call.data.split('_')[1])
    bot.send_message(call.message.chat.id,"Введите имя типочка")
    bot.register_next_step_handler(call.message, beast_creation, beast_count)

def main():
    bot.polling()

if __name__ == '__main__':
    main()