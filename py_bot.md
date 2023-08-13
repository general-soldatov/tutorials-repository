# Создание телеграм-бота на Python
## Установка библиотеки
Для установки библиотеки pyTelegramBotAPI необходимо в терминале ввести следующую команду  
`$ pip install pyTelegramBotAPI`
API постоянно находится в разработке, поэтому делаем запросы  
`pip install pytelegrambotapi --upgrade`  
Более подробно библиотека описана в [ресурсе](https://github.com/eternnoir/pyTelegramBotAPI)
## Получаем токен
В телеграме обращаемся к "отцу" всех ботов [@BotFather](https://core.telegram.org/bots#botfather)


```python
import telebot
from telebot import types

bot = telebot.TeleBot('token')

@bot.message_handler(comand = ['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(relize_keybard=True)
    btn1 = types.KeyboardButton("Поздороваться")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "Привет! Я твой бот-помощник!", reply_markup=markup)
```
Вот такой код
