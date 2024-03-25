from Token import TOKEN
from telebot import *
from ps import *
from dc import *
import time
import threading

bot = telebot.TeleBot(TOKEN, parse_mode=None)


def main_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Анализ помещения")
    markup.add(btn1)
    return markup

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message: types.Message):
    global users
    markup = main_menu(message)
    users.add(message.chat.id)
    bot.send_message(message.chat.id, "Здравствуйте, я буду следить за состоянием воздуха в помещении", reply_markup=markup)


@bot.message_handler(func=lambda m: True)
def recvive(message):
    msg = ""

    if message.text == "Все датчики":
        values = get_values()
        for i in values.keys():
            msg += f"{dc_mapa[i]}: {values[i]} \n"
    elif message.text == "Мяу?":
        msg = "Мяяяу?"
       
    bot.reply_to(message, msg)

def poller():
    while(True):
        msg = ""
        values = get_values()

        if(float(values["temp"]) > 100):
            msg += "Темпереатура превышает норму\n"
        elif(float(values["hum"]) > 80):
            msg += "Влажность превышает норму\n"
        elif(float(values["lpg"] > 200)):
            msg += "Метан превышает норму\n"
        elif(float(values["co"] > 1000)):
            msg += "Угарный газ превышает норму\n"
        elif(float(values["propane"] > 50)):
            msg += "Пропан превышает норму\n"

        if(msg != ""):
            for i in users:
                bot.send_message(i, msg)
        time.sleep(5)
    


if __name__ == '__main__':
    users = set()
    t1 = threading.Thread(target=bot.infinity_polling)
    t2 = threading.Thread(target=poller)
    t1.start()
    t2.start()
    t1.join()
    t2.join()