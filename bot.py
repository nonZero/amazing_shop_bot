import logging

from telegram import Update
from telegram.ext import CommandHandler, CallbackContext, Updater

import bot_settings

WELCOME = "🛒 Please enter some items to add to the list." \
          "Enter /list to show all items or /help to get more help."
logging.basicConfig(
    format='[%(levelname)s %(asctime)s %(module)s:%(lineno)d] %(message)s',
    level=logging.INFO)

logger = logging.getLogger(__name__)

updater = Updater(token=bot_settings.BOT_TOKEN, use_context=True)
dispatcher = updater.dispatcher


def start(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    logger.info(f"> Start chat #{chat_id}")
    context.bot.send_message(chat_id=chat_id, text=WELCOME)


# def respond(update: Update, context: CallbackContext):
#     chat_id = update.effective_chat.id
#     text = update.message.text
#     logger.info(f"= Got on chat #{chat_id}: {text!r}")
#     response = text.replace("7", "💣")[::-1]
#     context.bot.send_message(chat_id=update.message.chat_id, text=response)


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

# echo_handler = MessageHandler(Filters.text, respond)
# dispatcher.add_handler(echo_handler)

logger.info("* Start polling...")
updater.start_polling()  # Starts polling in a background thread.
updater.idle()  # Wait until Ctrl+C is pressed
logger.info("* Bye!")
