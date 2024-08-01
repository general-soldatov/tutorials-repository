# Создание телеграм-бота на Python
## Установка библиотеки
Для установки библиотеки pyTelegramBotAPI необходимо в терминале ввести следующую команду  
`$ pip install pyTelegramBotAPI`
API постоянно находится в разработке, поэтому делаем запросы  
`pip install pytelegrambotapi --upgrade`  
Более подробно библиотека описана в [ресурсе](https://github.com/eternnoir/pyTelegramBotAPI)
## Получаем токен
В телеграме обращаемся к "отцу" всех ботов [@BotFather](https://core.telegram.org/bots#botfather)
Командой `/newbot` запрашиваем разрешение на создание бота, затем пишем название бота, его никнейм (должен содержать слово bot), после чего получаем токен, который вставляем далее в наш скрипт на Python.  
## Каркас бота
Создаём файл скрипта питона. Импортируем библиотеку и в экземпляре класса `TeleBot`, который инкапсулирует все вызовы API в один класс, укажите полученный у "бати ботов" токен.
```python
import telebot

bot = telebot.TeleBot('token')
```
После такого объявления нам необходимо зарегистрировать обработчики сообщений, которые определяют фильтры, через которые проходят все сообщения. После вызова обработчика указывается функция, обрабатывающая сообщение. Она может называться по любому, но должен быть только один параметр `message`. Определим обработчик команд `/start` и `/help`.  
```python
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")
```
Функция `bot.reply_to(message, "Ответ на сообщение")` реализует ответ на сообщение, захваченное обработчиком `@bot.message_handler(commands=['start', 'help'])`.  
Для захвата обработчиком сообщения, содержащего текст, в параметрах обработчика нужно указать `content_types=["text"]`. Тип сообщения может быть следующим `text, audio, document, photo, sticker, video, video_note, voice, location, contact, new_chat_members, left_chat_member, new_chat_title, new_chat_photo, delete_chat_photo, group_chat_created, supergroup_chat_created, channel_chat_created, migrate_to_chat_id, migrate_from_chat_id, pinned_message, web_app_data`.  
Для создания эхо-бота, необходимо включить такую функцию:
```python
@bot.message_handler(content_types=["text"])
def echo_all(message):
	bot.send_message(message.chat.id, message.text)
```
Здесь уже мы видим функцию `send_message`, которая не отвечает, а просто отправляет сообщение. В параметрах функции мы видим аргумент `message.chat.id`, которая обрабатывает сообщение от конкретного пользователя. Аргумент `message.text` переводит сообщение в строку `string`. 
В конце кода обязательно нужно указываеть функцию, которая постоянно обращается к серверу телеграм
```python
bot.infinity_polling()
```
В конце получаем код каркаса телеграм-бота, который отвечает на команды `run` и `help` и пересылает сообщения пользователя (эхо-бот): 
```python
import telebot

bot = telebot.TeleBot("YOUR_BOT_TOKEN")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.infinity_polling()
```
# Добавление кнопок
Вначале мы импортируем `types` из библиотеки
```python
from telebot import types
```
Для того, чтобы добавить Reply кнопки, которые можем видеть вместо клавиатуры, присвоим переменной метод `.ReplyKeyboardMarkup(resize_keyboard=True)`:
```python
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
```
Затем пропишем сами кнопки, возможно использование смайлов.
```python
app1 = types.KeyboardButton("🔑 Вариант")
app2 = types.KeyboardButton("📈 Топ")
app3 = types.KeyboardButton("📒 Методички")
app4 = types.KeyboardButton("📖 Учебник")
app5 = types.KeyboardButton("📆 Расписание преподавателя")
markup.add(app3, app4, app1, app2, app5)
bot.send_message(message.chat.id, "Приятно познакомиться! Теперь ты можешь пользоваться кнопками на телеграм-клавиатуре.", reply_markup=markup)
```
В этой части кода мы прописываем название кнопок, добавляем их с помощью метода `.add()`, после чего присылаем сообщение, где прописываем параметр `reply_markup=markup`.  
Для того, чтобы удалить клавиатуру, можно воспользоваться объекта `ReplyKeyboardRemove()`.
```python
bot.send_message(message.chat.id, 'Удаление ⚙️', reply_markup=types.ReplyKeyboardRemove())
```
Для добавления Inline кнопок вместе с рабочей ссылкой, пропишем такую процедуру:
```python
markup_inl = types.InlineKeyboardMarkup()
button1 = types.InlineKeyboardButton("Актуальные варианты", 					 
   			url='https://drive.google.com/file/d/17FIeGJSOMbaHVG1sxeFEaxKIovgdftIJ/view?usp=sharing')
markup_inl.add(button1)
bot.send_message(message.chat.id, 'Свой вариант можно найти в файле', reply_markup=markup_inl)
```
Здесь из класса `types` мы вызываем объект `InlineKeyboardMarkup()`, и добавляем кнопки методом `.add()`. В параметрах отправки сообщения `reply_markup` присваиваем `reply_markup=markup_inl`. Более подробно создание кнопок описано по [ссылке](https://habr.com/ru/sandbox/163347/).
# Функция обработки сообщений
Для обработки сообщений, содержащих текст, вызовем обработчик: `@bot.message_handler(content_types = ["text"])`.  
Фильтрация текста осуществляется с помощью конструкции `if() - elif() - else()`. В случае если полученный текст совпадает с условием, выполняется процедура. В случае несовпадения текста с предложенными конструкциями, то выводим в `else` сообщение об ошибке. 
```python
@bot.message_handler(content_types = ["text"]) #обработчик текстовых сообщений пользователя
def echo(message): #функция ответа на сообщения
    string = message.text
    markup_inl = types.InlineKeyboardMarkup()
    if string == "🔑 Вариант":
        button1 = types.InlineKeyboardButton("Актуальные варианты", url='https://drive.google.com/file/d/17FIeGJSOMbaHVG1sxeFEaxKIovgdftIJ/view?usp=sharing')
        markup_inl.add(button1)
        bot.send_message(message.chat.id, 'Свой вариант можно найти в файле', reply_markup=markup_inl)

    elif string == "📈 Топ":
        button1 = types.InlineKeyboardButton("Рейтинг студентов", url='https://drive.google.com/file/d/17H105tExHL_ZZjmNGhy5yhqfOBsexuvv/view?usp=sharing')
        markup_inl.add(button1)
        bot.send_message(message.chat.id, 'Рейтинг студентов в файле по ссылке:', reply_markup=markup_inl)

    elif string == "📒 Методички":
        button1 = types.InlineKeyboardButton("Статика", url='https://drive.google.com/file/d/172EuTxLjZlYR0GYi03wdbzu70kae4RdC/view?usp=sharing')
        button2 = types.InlineKeyboardButton("Кинематика", url='https://drive.google.com/file/d/1i23gh8Kcsu-R5OkyHfdbp7SFUW2c73kx/view?usp=sharing')
        button3 = types.InlineKeyboardButton("Динамика", url='https://drive.google.com/file/d/1wrluEFNR18gYT1wFe-oLsmar9pxSB8ZH/view?usp=sharing')
        markup_inl.add(button1, button2, button3)
        bot.send_message(message.chat.id, 'Ссылки на методические указания:', reply_markup=markup_inl)

    elif string == "📖 Учебник":
        button1 = types.InlineKeyboardButton("Учебник", url='https://drive.google.com/file/d/17OhsVDAaPVkdBEMbjl3wR0Scj7WjeMYo/view?usp=drive_link')
        markup_inl.add(button1)
        bot.send_message(message.chat.id, 'Ссылка на учебник: "Краткий курс теоретической механики"', reply_markup=markup_inl)

    elif string == "📆 Расписание преподавателя":
        button1 = types.InlineKeyboardButton("Расписание", url='https://drive.google.com/file/d/17JUNCEKttgoa4HwPY63l0RB3CGJITdyU/view?usp=sharing')
        markup_inl.add(button1)
        bot.send_message(message.chat.id, 'Расписание преподователя можете найти по ссылке ниже', reply_markup=markup_inl)

    elif string == "📞 Контакты преподавателя":
        button1 = types.InlineKeyboardButton("Telegram", url='https://t.me/general_soldatov')
        button2 = types.InlineKeyboardButton("ВК", url='https://vk.com/general_soldatov')
        markup_inl.add(button1, button2)
        bot.send_message(message.chat.id, 'Расписание преподователя можете найти по ссылке ниже', reply_markup=markup_inl)

    else:
        bot.send_message(message.chat.id, 'Пока что я вас не понимаю... 🤷‍♂')
```

# Работа с базой данных и рассылка сообщений
Для того, чтобы вести статистику по пользователям, которые используют чат-бот, необходимо подключение базы данных SQL. PythonAnywhere поддерживает возможность создание облачной базы данных и её управление через консоль. После регистрации базы на сервере, мы прописываем процедуру инициализации базы:
```python
from mysql.connector import connect

with connect(
        host="GeneralSoldatov.mysql.pythonanywhere-services.com",
        user='GeneralSoldatov',
        password='pass',
        database='ter_mex_sql',
    ) as connection:
        print(connection)
```
Здесь указываем хост, на котором находится БД, имя пользователя, пароль и саму БД. Управление БД можно осуществлять через консоль на языке SQL, что очень удобно для работы с любого устройства.  
Вначале через консоль мы создаём таблицу, назовём её `teldata` с помощью функции:
```SQL
CREATE TABLE teldata(
    ->         id INT AUTO_INCREMENT PRIMARY KEY,
    ->         user_id INT NOT NULL,
    ->         active INT DEFAULT 0);
```
В полученной таблице есть три столбца: `id`, `user_id`, `active`. Теперь мы можем добавлять значения в таблицу. Для этого пропишем функцию добавления строки:
```python
def user_sql(user_id):
    with connect(
        host="GeneralSoldatov.mysql.pythonanywhere-services.com",
        user='GeneralSoldatov',
        password='pass',
        database='GeneralSoldatov$ter_mex_sql',
    ) as connection:
        print(connection)

        show_db_query = "INSERT INTO teldata (user_id, active) VALUES (%s, %s)"
        data_tg = [(user_id, 1)]
        with connection.cursor() as cursor:
            cursor.executemany(show_db_query, data_tg)
            connection.commit()
            print("id append")
```
Представленная функция добавляет строку в таблицу с номером id. Поэтому логичнее выполнить её при обработке команды `start`.
```python
@bot.message_handler(commands=['start'])
def send_welcome(message): #функция на команды
	bot.reply_to(message, "Что Вам угодно?")
	user_sql(message.from_user.id)
```
Реализовать переборку массива `user_id` можно посредством описания процедуры:
```python
def user_select(text):
    with connect(
        host="GeneralSoldatov.mysql.pythonanywhere-services.com",
        user='GeneralSoldatov',
        password='pass',
        database='GeneralSoldatov$ter_mex_sql',
    ) as connection:
        print(connection)

        show_select = "SELECT user_id FROM teldata"
        with connection.cursor() as cursor:
            cursor.execute(show_select)
            for result in cursor.fetchall():
                bot.send_message(result[0], text)
```
Для того, чтобы сделать рассылку копии сообщения, можем прописать в цикле такую процедуру:
```python
bot.copy_message(chat_id = result, from_chat_id=message.chat.id, message_id=message.message_id)
```
Затем мы пропишем в обработчике сообщений команду `/sendall`, которая будет делать рассылку сообщений по пользователям через аккаунт админа.
```python
@bot.message_handler(commands=['sendall'])
def sendall(message):
    if message.from_user.id == "номер id":
        text = message.text[9:]
        user_select(text)
```
В случае рассылки копии сообщения, команду `/sendall` указывать не стоит в сообщении, поэтому построим простую цепочку ответов:
```python
@bot.message_handler(commands=['sendall'])  #команда рассылки сообщения пользователям
def sendall(message):
    if message.from_user.id == 980314213:
        msg = bot.send_message(message.chat.id, "Напиши сообщение для рассылки!")
        bot.register_next_step_handler(msg, mailling)


def mailling(message):
    user_select(message)
```

В результате аккаунты, подписанные на бота, будут получать сообщения от админа. Полезно почитать ресурс в [дзене](https://dzen.ru/a/Yd7T967Tu0a8Kgq9)  
# Полезные ссылки
* Работа с базами данных SQL описана в [статье](https://proglib.io/p/python-i-mysql-prakticheskoe-vvedenie-2021-01-06)
* [Всё, о чём должен знать разработчик Телеграм-ботов](https://habr.com/ru/articles/543676/)
* [О библиотеке PyTelegramBotAPI и использовании SQL](https://habr.com/ru/articles/347106/)
* [Подключаем Sqlite3 к Telegram боту](https://habr.com/ru/articles/552788/)
* [О построении цепочки ответов и ответы на разные типы контента](https://habr.com/ru/articles/350648/)
* [Добавление кнопок](https://surik00.gitbooks.io/aiogram-lessons/content/chapter5.html)
# Построение бота не в библиотеке PyTelegramBotAPI
* [Пишем диалоговые Telegram-боты на Питоне](https://habr.com/ru/articles/316666/)
* [Инструкция: Как создавать ботов в Telegram](https://habr.com/ru/articles/262247/)
* [Расширения на Ваш первый бот](https://github.com/python-telegram-bot/python-telegram-bot/wiki/Extensions---Your-first-Bot)
* [Использование фреймворка Aiogram 3.0](https://mastergroosha.github.io/aiogram-3-guide/)
