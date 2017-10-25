"""
Main module.

Contains the main function that starts the bot.
"""

from telegram.ext import Updater, MessageHandler, Filters
from handlers import echo
from utils import error
from settings import TELEGRAM_TOKEN

def main():
    """
    Main function.

    Running the bot occurs here.
    """
    updater = Updater(TELEGRAM_TOKEN)

    updater.dispatcher.add_handler(MessageHandler(Filters.text, echo))
    updater.dispatcher.add_error_handler(error)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
