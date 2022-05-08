import logging
import os
import pickle

from telegram import Update
from telegram.ext import Application, CallbackContext, CommandHandler

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)


# auxiliary functions
def attendance(users_dict) -> str:
    with open(filename, "wb") as input:
      pickle.dump(users_dict, input)
    attendance = ""
    in_list = []
    stay_in_list = []
    off_list = []
    leave_list = []
    rso_list = []
    mc_list = []
    ao_list = []
    others_list = []
    for key, v in users_dict.items():
        value = v[:3]
        v3 = v[3:]
        if len(v3) != 0:
            v3 = ' ('+v3+')'
        if value == "in_":
            in_list.append(key+v3)
        if value == "sta":
            stay_in_list.append(key+v3)
        if value == "off":
            off_list.append(key+v3)
        if value == "lea":
            leave_list.append(key+v3)
        if value == "rso":
            rso_list.append(key+v3)
        if value == "mc_":
            mc_list.append(key+v3)
        if value == "ao_":
            ao_list.append(key+v3)
        if value == "oth":
            others_list.append(key+v3)

    attendance += "IN \n"
    attendance += pretty_print(in_list)
    attendance += "\nSTAY IN \n"
    attendance += pretty_print(stay_in_list)
    attendance += "\nOFF \n"
    attendance += pretty_print(off_list)
    attendance += "\nLEAVE \n"
    attendance += pretty_print(leave_list)
    attendance += "\nRSO \n"
    attendance += pretty_print(rso_list)
    attendance += "\nMC \n"
    attendance += pretty_print(mc_list)
    attendance += "\nAO \n"
    attendance += pretty_print(ao_list)
    attendance += "\nOTHERS \n"
    attendance += pretty_print(others_list)
    attendance += "\nNumber of IN: " + str(len(in_list)) + " STAY IN: " + str(len(stay_in_list)) + " OFF: " + str(len(in_list)) + " LEAVE: " + str(len(leave_list)) + " RSO: " + str(len(rso_list)) + " MC: " + str(len(mc_list)) + " AO: " + str(len(ao_list)) + " OTHERS: " + str(len(others_list))
    return attendance

def pretty_print(list) -> str:
    output = ""
    for i in range(len(list)):
        output += str(i+1) + ". "+ str(list[i]) + "\n"
    return output

'''def save():
    with open(filename, "wb") as input:
      pickle.dump(users_dict, input)

def load():
    with open(filename, "rb") as output:
        users_dict = pickle.load(output)'''
        


()
# users_dict = {}
filename = 'users_dict_persistance.pkl'

async def start_command(update: Update, context: CallbackContext.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Attendance-bot started')

async def help_command(update: Update, context: CallbackContext.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Type in command related to your status')
    
async def clear_command(update: Update, context: CallbackContext.DEFAULT_TYPE) -> None:
    with open(filename, "rb") as output:
        users_dict = pickle.load(output)
    users_dict.clear()
    await update.message.reply_text(attendance(users_dict))

async def in_command(update: Update, context: CallbackContext.DEFAULT_TYPE) -> None:
    with open(filename, "rb") as output:
        users_dict = pickle.load(output)
    users_dict[update.message.from_user.first_name] = "in_"+str(' '.join(context.args))
    await update.message.reply_text(attendance(users_dict))

async def stay_in_command(update: Update, context: CallbackContext.DEFAULT_TYPE) -> None:
    with open(filename, "rb") as output:
        users_dict = pickle.load(output)
    users_dict[update.message.from_user.first_name] = "sta"+str(' '.join(context.args))
    await update.message.reply_text(attendance(users_dict))

async def off_command(update: Update, context: CallbackContext.DEFAULT_TYPE) -> None:
    with open(filename, "rb") as output:
        users_dict = pickle.load(output)
    users_dict[update.message.from_user.first_name] = "off"+str(' '.join(context.args))
    await update.message.reply_text(attendance(users_dict))

async def leave_command(update: Update, context: CallbackContext.DEFAULT_TYPE) -> None:
    with open(filename, "rb") as output:
        users_dict = pickle.load(output)
    users_dict[update.message.from_user.first_name] = "lea"+str(' '.join(context.args))
    await update.message.reply_text(attendance(users_dict))

async def rso_command(update: Update, context: CallbackContext.DEFAULT_TYPE) -> None:
    with open(filename, "rb") as output:
        users_dict = pickle.load(output)
    users_dict[update.message.from_user.first_name] = "rso"+str(' '.join(context.args))
    await update.message.reply_text(attendance(users_dict))

async def mc_command(update: Update, context: CallbackContext.DEFAULT_TYPE) -> None:
    with open(filename, "rb") as output:
        users_dict = pickle.load(output)
    users_dict[update.message.from_user.first_name] = "mc_"+str(' '.join(context.args))
    await update.message.reply_text(attendance(users_dict))

async def ao_command(update: Update, context: CallbackContext.DEFAULT_TYPE) -> None:
    with open(filename, "rb") as output:
        users_dict = pickle.load(output)
    users_dict[update.message.from_user.first_name] = "ao_"+str(' '.join(context.args))
    await update.message.reply_text(attendance(users_dict))

async def others_command(update: Update, context: CallbackContext.DEFAULT_TYPE) -> None:
    with open(filename, "rb") as output:
        users_dict = pickle.load(output)
    users_dict[update.message.from_user.first_name] = "oth"+str(' '.join(context.args))
    await update.message.reply_text(attendance(users_dict))

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

def init():
    users_dict = {}
    with open(filename, "wb") as input:
      pickle.dump(users_dict, input)

if __name__ == '__main__':
    main()

