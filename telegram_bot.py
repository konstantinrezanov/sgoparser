from telegram.ext import Updater, CommandHandler

updater = Updater(token='YOUR_TOKEN', use_context=True)
dispatcher = updater.dispatcher

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Стильный, модный, молодежный парсер на питоне")

def showa(update, context):
    f=open('raspa.txt')
    context.bot.send_message(chat_id=update.effective_chat.id, text=f.read())

def showb(update, context):
    f=open('raspb.txt')
    context.bot.send_message(chat_id=update.effective_chat.id, text=f.read())

def showv(update, context):
    f=open('raspv.txt')
    context.bot.send_message(chat_id=update.effective_chat.id, text=f.read())

def showg(update, context):
    f=open('raspg.txt')
    context.bot.send_message(chat_id=update.effective_chat.id, text=f.read())

def showd(update, context):
    f=open('raspd.txt')
    context.bot.send_message(chat_id=update.effective_chat.id, text=f.read())

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

showa_handler = CommandHandler('showa', showa)
dispatcher.add_handler(showa_handler)

showb_handler = CommandHandler('showb', showb)
dispatcher.add_handler(showb_handler)

showv_handler = CommandHandler('showv', showv)
dispatcher.add_handler(showv_handler)

showg_handler = CommandHandler('showg', showg)
dispatcher.add_handler(showg_handler)

showd_handler = CommandHandler('showd', showd)
dispatcher.add_handler(showd_handler)

updater.start_polling()
updater.idle()
