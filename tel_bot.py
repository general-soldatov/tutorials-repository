from telegram import Update        # пакет называется python-telegram-bot, но Python-
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes  # модуль почему-то просто telegram ¯\_(ツ)_/¯

import logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Здравствуйте.")

updater = ApplicationBuilder().token('6195922408:AAFCID4v6-a6gKccR6Xj5jt6Vz4IKf3S6qE').build()  # тут токен, который выдал вам Ботский Отец!

start_handler = CommandHandler('start', start)  # этот обработчик реагирует
                                                # только на команду /start

updater.add_handler(start_handler)   # регистрируем в госреестре обработчиков
updater.run_polling()  # поехали!