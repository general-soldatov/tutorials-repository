import telebot
from telebot import types

bot = telebot.TeleBot('6195922408:AAFCID4v6-a6gKccR6Xj5jt6Vz4IKf3S6qE')


@bot.message_handler(comand=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(relize_keybard=True)
    btn1 = types.KeyboardButton("Поздороваться")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "Привет! Я твой бот-помощник!", reply_markup=markup)


@bot.message_handler(comands=['text'])
def get_text_messages(massage):
    if message.text == 'Поздороваться':
        markup = types.ReplyKeyboardMarkup(relize_keyboard=True)
        btn1 = types.KeyboardButton('Расскажи о себе')
        btn2 = types.KeyboardButton('Написать определение')
        btn3 = types.KeyboardButton('Узнать вариант')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, 'Задайте интересующий вопрос', reply_markup=markup)


    elif message.text == 'Расскажи о себе':
        bot.send_message(message.from_user.id,
                         'Я пришёл издалека, чтобы научить тебя хорошему.\n \nЯ вышивать люблю и на машинке тоже... А создал меня ' + '[он](https://vk.com/general_soldatov)',
                         parse_mode='Markdown')


bot.polling(none_stop=True, interval=0)
