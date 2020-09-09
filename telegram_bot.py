from telegram.ext import Updater, CommandHandler

updater = Updater(token='1327123695:AAHMOrU3khDWTdQrD_pSbvP4aC1FlWrfOC4', use_context=True)
dispatcher = updater.dispatcher

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Стильный, модный, молодежный парсер на питоне")

def show(update, context):
    f=open('rasp.txt')
    context.bot.send_message(chat_id=update.effective_chat.id, text=f.read())

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

show_handler = CommandHandler('show', show)
dispatcher.add_handler(show_handler)

updater.start_polling()
updater.idle()