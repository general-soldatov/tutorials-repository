# LAB 6 "РАЗРАБОТКА TELEGRAM-БОТА НА PYTHON"

## Target
овладеть	навыками	разработки	Telegram-бота	на Python с использованием API Telegram.

## Theory
Telegram – это бесплатный мессенджер для обмена сообщениями, изображениями и документами различных форматов (XLS, PDF, DOCX и др.).  
API (Application Programming Interface) – программный интерфейс, позволяющий одной программе взаимодействовать с другой с помощью набора методов и инструментов.  
Telegram API – программный интерфейс, через который Telegram интегрируется с внешними сервисами.  
Telegram Bot API – программный интерфейс, используемый для создания ботов в Telegram.  
 
## Practics
Для создания телеграм-бота воспользуйтесь сервисом BotFather.
BotFather – это официальный бот в Telegram, предназначенный для регистрации и управления пользовательскими ботами.  
* Ниже перечислим шаги по созданию бота.  
* Откройте	приложение	Telegram	и	введите	в	строке	поиска @BotFather. Убедитесь, что у бота есть синяя галочка.  
* Начните взаимодействие с ботом, отправив команду /start  
* Введите команду /newbot для создания нового бота.  
* Укажите уникальное имя бота (оно будет отображаться в верхней строке чата).  
* Укажите юзернейм бота (он должен быть на английском языке, содержать только буквы и цифры и заканчиваться на bot) по шаблону Familiya01052025_bot, где Familiya – фамилия обучающегося на англий- ском языке, 01052025 – дата создания бота в формате ДДММГГГ (день, месяц, год).  
* BotFather отправит вам токен – уникальный ключ, который потребуется для управления ботом. Сохраните токен в файле token.txt. Загрузите этот файл в своем Google Диске.  
* Введите команду /mybots, выберите бота и перейдите в Edit Bot / Edit Description. Укажите описание бота (оно будет отображаться пользователям при открытии чата).

В новом блокноте создайте текстовую ячейку и впишите следующий текст: «Лабораторная работа студента группы … Фамилия Имя», указав свой номер группы, фамилию и имя. Установите последнюю версию библиотеки python-telegram-bot:
```py
!pip install python-telegram-bot --upgrade
```
Установка необходимых библиотек:
```py
import nltk
import re
import nest_asyncio
import random
from google.colab import drive
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
```
Подключение Google Диска, загрузка токена и json-файла. Код, расположенный ниже, написанный через пустую строку, следует размещать в разных ячейках. Вместо переменной Smirnov укажите переменную с вашей фамилией. 
```py
import json 

# загружаем JSON с вопросами и ответами 
try:
    with open(file_path_gis, 'r', encoding='utf-8') as smirnovGeo:
        testGeo = json.load(smirnovGeo)
except (FileNotFoundError, json.JSONDecodeError) as e:
    print('JSON loading error', e)

# проверяем наличие ключевого раздела в JSON 
EXPO_KEY = 'Интерэкспо ГЕО-Сибирь'
if EXPO_KEY not in testGeo:
    print(f"WARNING: Key '{EXPO_KEY}' no found.")
    testGeo[EXPO_KEY] = {}
    
# подключаем Google Диск для загрузки токена
drive.mount('/content/drive')

# задаем путь к файлу с токеном бота 
TOKEN_PATH = '/content/drive/MyDrive/TOKEN.txt'
try:
    with open(TOKEN_PATH, 'r') as token_file:
        TOKEN = token_file.read().strip()
        if not TOKEN:
            raise ValueError('Token is not found')
except (FileNotFoundError, ValueError) as e:
    print('Token loading error', e)
    TOKEN = None
```
Создадим объект приложения Telegram-бота: проверим, задан ли токен, и либо создадим объект Telegram-бота, либо остановим выполнение, если токен отсутствует.
```py
if TOKEN:
    app = Application.builder().token(TOKEN).build()
else:
    print('Bot can`t working without TOKEN')
    exit()
```
Формирование обучающих данных (X, y) для модели на основе словаря.
```py
# формируем обучающие данные для модели
X, y = [], []
for name, data in testGeo[EXPO_KEY].items():
    for example in data.get('Вопрос', []):
        X.append(example)
        y.append(name)
```
Обработка текста и обучение модели для определения намерения пользователя.
```py
# загрузка модуля punkt 
nltk.download('punkt')

# проверяем, есть ли данные для обучения
if not X or not y:
    print('WARNING: there is no data for training the model')

# векторизация текста
vectorizer = TfidfVectorizer()
XX = vectorizer.fit_transform(X) if X else None

# обучение модели, если есть данные
model = RandomForestClassifier()
if XX is not None and y:
    model.fit(XX, y)

# функция нормализации текста
def normalize(text):
    return re.sub(r'[^\w\s]', '', text.lower())

# функция оценки схожести строк
def get_rank(text1, text2):
    text1, text2 = normalize(text1), normalize(text2)
    if not text1 or not text2:
        return 100
    return (nltk.edit_distance(text1, text2) / 
                      (len(text1) + len(text2) / 2)) * 100

# определение намерения пользователя
def get_intent(text, best_rank = 50):
    result = None
    for name, data in testGeo[EXPO_KEY].items():
        for question in data.get('Вопрос', []):
            rank = get_rank(text, question)
            if rank < best_rank:
                best_rank, result = rank, name
    
    return result
```
Реализация функции ответа бота на основе правил и машинного обучения.
```py
# Функция ответа бота
def answer(text, min_confidence=0.3, fall_text='Извините, я не понимаю ваш вопрос.'):
    answer_bot = lambda key: testGeo[EXPO_KEY][key].get('Ответ', ["Ответ не найден"])
    intent = get_intent(text)
    if intent in testGeo[EXPO_KEY]:
        return random.choice(answer_bot(intent))
    
    if XX is not None:
        test = vectorizer.transform([text])
        probabilities = model.predict_proba(test)
        predicted_intent = model.predict(test)[0]
        confidence = max(probabilities[0])
        print(f'ML-model predicted: {predicted_intent} with confidence {confidence:.2f}')
        if confidence < min_confidence:
            return fall_text
        if predicted_intent in testGeo[EXPO_KEY]:
            return random.choice(answer_bot(predicted_intent))
    
    return fall_text
```
Обработка команд и сообщений для Telegram-бота.
```py
# обработчик команды /start
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("""Привет!
    Я бот, отвечающий на вопросы о научном конгрессе Интерэкспо ГЕО-Сибирь. 
    Задайте мне вопрос!""")

# обработчик текстовых сообщений
async def send_message(update: Update, context: CallbackContext):
    user_text = update.message.text
    response = answer(user_text)
    await update.message.reply_text(response)

# добавляем обработчики сообщений 
app.add_handler(CommandHandler('start', start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, send_message))
```
Запуск бота. 
```py
# запуск бота
import asyncio

nest_asyncio.apply()

async def main():
    await app.run_polling()

# Проверяем, работает ли код в среде, поддерживающей event loop 
if __name__ == '__main__':
    try:
        asyncio.run(main())
    except RuntimeError:
        print('Async event loop is driven')
```
Откройте Telegram-бот и задайте в чате вопросы о научном конгрессе «Интерэкс-по ГЕО-Сибирь».
Сохраните блокнот через меню «Файл / Сохранить».
Переименуйте файл на Google Диске, используя шаблон «Итоговый проект по созданию телеграм-бота студента группы … Фамилия Имя», указав свой номер группы, фамилию и имя.
