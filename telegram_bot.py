from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from dir import getdir

updater = Updater(token='TOKEN', use_context=True)
dispatcher = updater.dispatcher

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Стильный, модный, молодежный парсер на питоне")

def help(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Для получения расписания введите номер и букву класса, а также дату.\nПример комманды: 10Б 14.09")

def get(update, context):
    input=update.message.text.split(" ")
    directory=getdir()
    clas=input[0][-1].capitalize()
    date=input[1]
    title='rasp'+clas+'_'+date+'.txt'
    for n in directory:
        if n==title:
            update.message.reply_text(open('./texts/{}'.format(title)).read())

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
help_handler = CommandHandler('help', help)
dispatcher.add_handler(help_handler)

dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, get))

updater.start_polling()
updater.idle()