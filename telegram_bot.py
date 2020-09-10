from telegram.ext import Updater, CommandHandler

updater = Updater(token='1327123695:AAHMOrU3khDWTdQrD_pSbvP4aC1FlWrfOC4', use_context=True)
dispatcher = updater.dispatcher

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Стильный, модный, молодежный парсер на питоне")

def showb(update, context):
    f=open('raspb.txt')
    context.bot.send_message(chat_id=update.effective_chat.id, text=f.read())

def showv(update, context):
    f=open('raspbv.txt')
    context.bot.send_message(chat_id=update.effective_chat.id, text=f.read())

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

showb_handler = CommandHandler('showb', showb)
dispatcher.add_handler(showb_handler)

showv_handler = CommandHandler('showv', showv)
dispatcher.add_handler(showv_handler)

updater.start_polling()
updater.idle()