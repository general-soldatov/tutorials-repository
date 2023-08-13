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
