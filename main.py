import os
import telegram
import random

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext
from telegram import Bot,Update
from telegram.ext import CommandHandler,Dispatcher

class salad(object):
    """docstring for salad."""
    def __init__(self):
        super(salad, self).__init__()
        self.base = ['tomatos', 'basil']
        self.dressing = ['olive oil', 'balsamic vinegar']
        self.extra = ['mozzarella']

    def mix(self):
        return f'{random.choice(self.base)}, {random.choice(self.dressing)}, {random.choice(self.extra)}'


def start(update,context):
  context.bot.send_message(chat_id=update.effective_chat.id,text=salad().mix())


def telegram_bot(request):
    bot = telegram.Bot(token=os.environ["TELEGRAM_TOKEN"])
    dispatcher = Dispatcher(bot,None,workers=0)
    dispatcher.add_handler(CommandHandler('start',start))
    if request.method == "POST":
        update = Update.de_json(request.get_json(force=True), bot)
        if update.message.text=="\start":
            dispatcher.process_update(update)
        else:
            chat_id = update.message.chat.id
            # Reply with the same message
            bot.sendMessage(chat_id=chat_id, text=update.message.text)
    return "okay"
