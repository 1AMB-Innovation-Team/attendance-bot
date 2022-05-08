import logging
import pickle
import os

from telegram import Update
from telegram.ext import Application, CallbackContext, CommandHandler

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

users_dict = {}
filename = 'users_dict_persistance'

async def start_command(update: Update, context: CallbackContext.DEFAULT_TYPE) -> None:
    load()
    await update.message.reply_text('Attendance-bot started')

async def help_command(update: Update, context: CallbackContext.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Type in command related to your status')
    
async def clear_command(update: Update, context: CallbackContext.DEFAULT_TYPE) -> None:
    users_dict.clear()
    await update.message.reply_text(attendance())

async def in_command(update: Update, context: CallbackContext.DEFAULT_TYPE) -> None:
    users_dict[update.message.from_user] = "in"
    await update.message.reply_text(attendance())

async def stay_in_command(update: Update, context: CallbackContext.DEFAULT_TYPE) -> None:
    users_dict[update.message.from_user] = "stay in"
    await update.message.reply_text(attendance())

async def off_command(update: Update, context: CallbackContext.DEFAULT_TYPE) -> None:
    users_dict[update.message.from_user] = "off"
    await update.message.reply_text(attendance())

async def leave_command(update: Update, context: CallbackContext.DEFAULT_TYPE) -> None:
    users_dict[update.message.from_userser] = "leave"
    await update.message.reply_text(attendance())

async def rso_command(update: Update, context: CallbackContext.DEFAULT_TYPE) -> None:
    users_dict[update.message.from_user] = "rso"
    await update.message.reply_text(attendance())

async def mc_command(update: Update, context: CallbackContext.DEFAULT_TYPE) -> None:
    users_dict[update.message.from_user] = "mc"
    await update.message.reply_text(attendance())

async def ao_command(update: Update, context: CallbackContext.DEFAULT_TYPE) -> None:
    update.message.from_users_dict[update.message.from_user] = "ao"
    await update.message.reply_text(attendance())

async def others_command(update: Update, context: CallbackContext.DEFAULT_TYPE) -> None:
    users_dict[update.message.from_user] = "others"
    await update.message.reply_text(attendance())

def main() -> None:
    """Start the bot."""
    application = Application.builder().token(os.environ["ATT_BOT_TOKEN"]).build()

    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("clear", clear_command))
    application.add_handler(CommandHandler("in", in_command))
    application.add_handler(CommandHandler("stay_in", stay_in_command))
    application.add_handler(CommandHandler("off", off_command))
    application.add_handler(CommandHandler("leave", leave_command))
    application.add_handler(CommandHandler("rso", rso_command))
    application.add_handler(CommandHandler("mc", mc_command))
    application.add_handler(CommandHandler("ao", ao_command))
    application.add_handler(CommandHandler("others", others_command))

    application.run_polling()

if __name__ == '__main__':
    main()

# auxiliary functions
def attendance() -> str:
    save()
    attendance = ""
    in_list = []
    stay_in_list = []
    off_list = []
    leave_list = []
    rso_list = []
    mc_list = []
    ao_list = []
    others_list = []
    for key, value in users_dict.items():
        if value == "in":
            in_list.append(key)
        if value == "stay_in":
            stay_in_list.append(key)
        if value == "off":
            off_list.append(key)
        if value == "leave":
            leave_list.append(key)
        if value == "rso":
            rso_list.append(key)
        if value == "mc":
            mc_list.append(key)
        if value == "ao":
            ao_list.append(key)
        if value == "others":
            others_list.append(key)
    
    attendance += "IN /n"
    attendance += pretty_print(in_list.sort())
    attendance += "STAY IN /n"
    attendance += pretty_print(stay_in_list.sort())
    attendance += "OFF /n"
    attendance += pretty_print(off_list.sort())
    attendance += "LEAVE /n"
    attendance += pretty_print(leave_list.sort())
    attendance += "RSO /n"
    attendance += pretty_print(rso_list.sort())
    attendance += "MC /n"
    attendance += pretty_print(mc_list.sort())
    attendance += "AO /n"
    attendance += pretty_print(ao_list.sort())
    attendance += "OTHERS /n"
    attendance += pretty_print(others_list.sort())
    attendance += "Number of IN: " + len(in_list) + " STAY IN: " + len(stay_in_list) + " OFF: " + len(in_list) + " LEAVE: " + len(leave_list) + " RSO: " + len(rso_list) + " MC: " + len(mc_list) + " AO: " + len(ao_list) + " OTHERS: " + len(others_list)
    return attendance

def pretty_print(list) -> str:
    output = ""
    for i in range(len(list)):
        output += i + ". "+ list[i] + "/n"
    return output

def save():
    with open("state.txt", "wb") as input:
      pickle.dump(users_dict, input)

def load():
    with open("state.txt", "rb") as output:
        users_dict = pickle.load(output)
