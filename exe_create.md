# Создание файла exe из PyCharm
Открываем терминал в среде разработки посредством комбинации ``Alt+F12``, затем в нём запускаем установку pyinstaller  
`` pip install pyinstaller ``
Преобразуем скрипт в исполняемый файл - `` pyinstaller your_script.py``  
Опционально: создаём один файл - ``pyinstaller --onefile your_script.py``  
Опционально: скрываем дополнительно консоль - ``pyinstaller --onefile --noconsole your_script.py`` 

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
