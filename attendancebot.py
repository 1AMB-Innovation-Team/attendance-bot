import logging

from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Attendance-bot started')

def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Help is coming soon')

def main() -> None:
    """Start the bot."""
    updater = Updater("TOKEN")

    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()