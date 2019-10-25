#SMT112 983159806:AAFhwLriaQxPv8KQPhyQ_kkMQmLcT0Ajp7w

import logging
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler)

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

LAPTOP, PHONE, LIGHT, AIRCON, FAN, BUS, CAR, MRT, ENDING = range(9)

user_choice_dict = {}
def start(update, context):
    user = update.message.from_user
    user_choice_dict[user.first_name] = {
        "laptop" : 0, 
        "phone" : 0,
        "light" : 0,
        "aircon": 0,
        "fan": 0,
        "bus": 0,
        "car": 0,
        "mrt": 0
        
    }
    reply_keyboard = [['< 1h', '1h', '2h', '3h', '4h','5h', '6h','7h','> 7h']]
    update.message.reply_text(
        "Hi! I am a ChatBot created to calculate your daily CO2 emissions, let's begin!")
    update.message.reply_text(
        "I will be starting my calculations with your ELECTRONIC DEVICES...")
    update.message.reply_text(
        'So tell me! how long did you charge your laptop today?',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return LAPTOP

def change_laptop(text):
    laptop_list = ["< 1h", "1h", "2h", "3h", "4h","5h", '6h','7h','> 7h']
    ans_num = laptop_list.index(text)
    return (ans_num)

def laptop(update, context):
    reply_keyboard = [["< 1h", "1h", "2h", "3h", "4h","5h", '6h','7h','> 7h']]
    user = update.message.from_user
    logger.info("Laptop of %s: %s", user.first_name, update.message.text)  
    user_choice_num = change_laptop(update.message.text)
    user_choice_dict[user.first_name]["laptop"] = user_choice_num
    logger.info("user laptop # %s", user_choice_num)
    update.message.reply_text(
        'Ahh... what about your phone?',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return PHONE

def change_phone(text):
    phone_list = ["< 1h", "1h", "2h", "3h", "4h","5h", '6h','7h','> 7h']
    ans_num = phone_list.index(text)
    return (ans_num)

def phone(update, context):
    reply_keyboard = [["< 1h", "1h", "2h", "3h", "4h","5h", '6h','7h','> 7h']]
    user = update.message.from_user
    logger.info("Phone of %s: %s", user.first_name, update.message.text)
    user_choice_num = change_phone(update.message.text)
    user_choice_dict[user.first_name]["phone"] = user_choice_num
    logger.info("user phone # %s", user_choice_num)
    update.message.reply_text(
        'OK got it!' 
    )
    update.message.reply_text(
        'How many hours of artificial lighting did you use today?',
        reply_markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)) 
    return LIGHT

def change_light(text):
    light_list = ["< 1h", "1h", "2h", "3h", "4h","5h", '6h','7h','> 7h']
    ans_num = light_list.index(text)
    return (ans_num)


def light(update, context):
    reply_keyboard = [["< 1h", "1h", "2h", "3h", "4h","5h", '6h','7h','> 7h']]
    user = update.message.from_user
    logger.info("Light of %s: %s", user.first_name, update.message.text)
    user_choice_num = change_light(update.message.text)
    user_choice_dict[user.first_name]["light"] = user_choice_num
    logger.info("user light # %s", user_choice_num)
    update.message.reply_text(
        "Ah... it's warm here in Singapore,how many hours of aircon were you under today?", 
        reply_markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return AIRCON

def change_aircon(text):
    aircon_list = ["< 1h", "1h", "2h", "3h", "4h","5h", '6h','7h','> 7h']
    ans_num = aircon_list.index(text)
    return (ans_num)


def aircon(update, context):
    reply_keyboard = [["< 1h", "1h", "2h", "3h", "4h","5h", '6h','7h','> 7h']]
    user = update.message.from_user
    logger.info("Aircon of %s: %s", user.first_name, update.message.text)
    user_choice_num = change_aircon(update.message.text)
    user_choice_dict[user.first_name]["aircon"] = user_choice_num
    logger.info("user aircon # %s", user_choice_num)
    update.message.reply_text(
        'Alright alright, how long were you under a running fan today?', 
        reply_markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return FAN 

def change_fan(text):
    fan_list = ["< 1h", "1h", "2h", "3h", "4h","5h", '6h','7h','> 7h']
    ans_num = fan_list.index(text)
    return (ans_num)


def fan(update, context):
    reply_keyboard = [["0.5h", "1h", "1.5h", "2h", "2.5h","3h", '3.5h','4h','> 4h']]
    user = update.message.from_user
    logger.info("Fan of %s: %s", user.first_name, update.message.text)
    user_choice_num = change_fan(update.message.text)
    user_choice_dict[user.first_name]["fan"] = user_choice_num
    logger.info("user fan # %s", user_choice_num)
    update.message.reply_text(
        'Moving on to TRANSPORT MEANS...'
    )
    update.message.reply_text(
        'How long were you on the bus today!', 
        reply_markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return BUS

def change_bus(text):
    bus_list = ["0.5h", "1h", "1.5h", "2h", "2.5h","3h", '3.5h','4h','> 4h']
    ans_num = bus_list.index(text)
    return ((ans_num+1)*0.5)


def bus(update, context):
    reply_keyboard = [["0.5h", "1h", "1.5h", "2h", "2.5h","3h", '3.5h','4h','> 4h']]
    user = update.message.from_user
    logger.info("Bus of %s: %s", user.first_name, update.message.text)
    user_choice_num = change_bus(update.message.text)
    user_choice_dict[user.first_name]["bus"] = user_choice_num
    logger.info("user bus # %s", user_choice_num)
    update.message.reply_text(
        'OK! Now tell me how long did u stay on a car today?', 
        reply_markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return CAR 

def change_car(text):
    car_list = ["0.5h", "1h", "1.5h", "2h", "2.5h","3h", '3.5h','4h','> 4h']
    ans_num = car_list.index(text)
    return ((ans_num+1)*0.5)


def car(update, context):
    reply_keyboard = [["0.5h", "1h", "1.5h", "2h", "2.5h","3h", '3.5h','4h','> 4h']]
    user = update.message.from_user
    logger.info("Car of %s: %s", user.first_name, update.message.text)
    user_choice_num = change_car(update.message.text)
    user_choice_dict[user.first_name]["car"] = user_choice_num
    logger.info("user car # %s", user_choice_num)
    update.message.reply_text(
        'How about MRT? How long did you ride on MRT?', 
        reply_markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return MRT 

def change_mrt(text):
    mrt_list = ["0.5h", "1h", "1.5h", "2h", "2.5h","3h", '3.5h','4h','> 4h']
    ans_num = mrt_list.index(text)
    return ((ans_num+1)*0.5)


def mrt(update, context):
    reply_keyboard = [["Now let's see your score!!"]]
    user = update.message.from_user
    logger.info("MRT of %s: %s", user.first_name, update.message.text)
    user_choice_num = change_mrt(update.message.text)
    user_choice_dict[user.first_name]["mrt"] = user_choice_num
    logger.info("user mrt # %s", user_choice_num)
    update.message.reply_text(
        'Great!', 
        reply_markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return ENDING 

def calculate_sum(user_dict):
    sum = 0
    for index, data in user_dict.items():
        if index == "laptop":
            sum += int(data) * 60
        if index == "phone":
            sum += int(data) * 10
        if index == "light":
            sum += int(data) * 100
        if index == "aircon":
            sum += int(data) * 200
        if index == "fan":
            sum += int(data) * 100 
        if index == "bus":
            sum += int(data) * 30
        if index == "car":
            sum += int(data) * 50
        if index == "mrt":
            sum += int(data) * 40
    return sum

def sendImg(update):
    user = update.message.from_user
    imgUrl = "https://media.giphy.com/media/UReWNqLOku35dpKIDb/giphy.gif"
    sendPhoto(user, imgUrl, caption = NULL, disable_notification = FALSE, reply_to_message_id = NULL, reply_markup = NULL, parse_mode = NULL)

def ending(update, context):
    user = update.message.from_user
    cal_sum = calculate_sum(user_choice_dict[user.first_name])
    update.message.reply_text('Thank you! Your estimated CO2 emission amount is: ' + str(cal_sum))
    logger.info("user sum %s", str(cal_sum))
    sendImg(update)
    return ConversationHandler.END

#######################################
def cancel(update, context):
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    update.message.reply_text('Bye! I hope we can talk again some day.',
                              reply_markup=ReplyKeyboardRemove())

    return ConversationHandler.END


def error(update, context): 
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    updater = Updater("983159806:AAFhwLriaQxPv8KQPhyQ_kkMQmLcT0Ajp7w", use_context=True)
    dp = updater.dispatcher
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],

        states={
            LAPTOP: [MessageHandler(Filters.regex('^(< 1h|1h|2h|3h|4h|5h|6h|7h|> 7h)$'), laptop)],

            PHONE: [MessageHandler(Filters.regex('^(< 1h|1h|2h|3h|4h|5h|6h|7h|> 7h)$'), phone)],

            LIGHT: [MessageHandler(Filters.regex('^(< 1h|1h|2h|3h|4h|5h|6h|7h|> 7h)$'), light)],

            AIRCON: [MessageHandler(Filters.regex('^(< 1h|1h|2h|3h|4h|5h|6h|7h|> 7h)$'), aircon)],

            FAN: [MessageHandler(Filters.regex('^(< 1h|1h|2h|3h|4h|5h|6h|7h|> 7h)$'), fan)],

            BUS: [MessageHandler(Filters.regex('^(0.5h|1h|1.5h|2h|2.5h|3h|3.5h|4h|> 4h)$'), bus)],

            CAR: [MessageHandler(Filters.regex('^(0.5h|1h|1.5h|2h|2.5h|3h|3.5h|4h|> 4h)$'), car)],

            MRT: [MessageHandler(Filters.regex('^(0.5h|1h|1.5h|2h|2.5h|3h|3.5h|4h|> 4h)$'), mrt)],

            ENDING: [MessageHandler(Filters.regex("^(Now let's see your score!!)$"), ending)]
        },

        fallbacks=[CommandHandler('cancel', cancel)]
    )

    dp.add_handler(conv_handler)

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()