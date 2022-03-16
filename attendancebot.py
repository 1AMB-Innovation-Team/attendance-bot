from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Attendance-bot started')

def main() -> None:
    """Start the bot."""
    updater = Updater("TOKEN")

    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()