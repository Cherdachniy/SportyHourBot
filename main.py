import random
import sched
import time

import telebot

bot = telebot.TeleBot('1768619317:AAHyDzzg9OE19_htVeV7fbyMrBls5HgE_k8')
startKeyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=1)
startKeyboard.row('Каждый час')
continueKeyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=1)
continueKeyboard.row('Продолжим')
s = sched.scheduler(time.time, time.sleep)

trainings = {
    0: 'отжимайся 💪',
    1: 'приседай 🦵',
    2: 'пресс качай 🙆‍♂️'
}


def random_training(obj):
    return random.choice(obj)


def send_message(chat_id):
    bot.send_message(chat_id, f'Давай, {random_training(trainings)}', reply_markup=continueKeyboard)


def run_task(fn, **kwargs):
    s.enter(3600, 1, fn, kwargs=kwargs)
    s.run()


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Погнали!', reply_markup=startKeyboard)


@bot.message_handler(content_types=['text'])
def send_text(message):
    print(message)
    if message.text.lower() in ['каждый час', 'продолжим']:
        bot.send_message(message.chat.id, 'Увидимся через час 😑')
        run_task(send_message, chat_id=message.chat.id)


bot.polling()
