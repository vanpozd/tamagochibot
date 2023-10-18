import telebot
import tamconf
import datetime

bot = telebot.TeleBot(tamconf.main_bot_token)

@bot.message_handler(commands=['start'])
def welocme(message):
    echo_all(message)

@bot.message_handler(commands=['newbeast'])
def create_new_beast(message):
    print("pisun")  
    #request to bd


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    chat_id = message.chat.id
    message_date = datetime.datetime.fromtimestamp(message.date)
    print(f'Новое сообщение от {message.chat.username}({message.chat.id})({message_date}): {message.text}')
    bot.send_message(1256707116, f"-{message.chat.username}({message.chat.id})\n-({message_date})\n-{message.text}")
    bot.send_message(617493696, f"Новое сообщение от {message.chat.username}({message.chat.id})({message_date}): {message.text}")

def main():
    bot.polling()

if __name__ == '__main__':
    main()
