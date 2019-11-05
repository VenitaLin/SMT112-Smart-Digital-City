#SMT112 983159806:AAFhwLriaQxPv8KQPhyQ_kkMQmLcT0Ajp7w

import logging
from telegram import ParseMode
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler)

import random
# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

LAPTOP, PHONE, LIGHT, AIRCON, FAN, BUS, CAR, MRT, FLIGHT, ENDING = range(10)

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
        "mrt": 0,
        "flight": 0
        
    }
    reply_keyboard = [['< 1h', '1h', '2h', '3h', '4h','5h', '6h','7h','> 7h']]
    update.message.reply_text(
        "Hi! I am a ChatBot created to calculate *your daily CO2 emissions*, let's begin!", parse_mode=ParseMode.MARKDOWN)
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
        'How many hours of artificial lighting were you under today?',
        reply_markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)) 
    return LIGHT

def change_light(text):
    light_list = ["< 1h", "1h", "2h", "3h", "4h","5h", '6h','7h','> 7h']
    ans_num = light_list.index(text)
    return (ans_num)


def light(update, context):
    reply_keyboard = [["< 1h", "2h", "4h", "6h", "8h","10h", '12h','14h','> 14h']]
    user = update.message.from_user
    logger.info("Light of %s: %s", user.first_name, update.message.text)
    user_choice_num = change_light(update.message.text)
    user_choice_dict[user.first_name]["light"] = user_choice_num
    logger.info("user light # %s", user_choice_num)
    update.message.reply_text(
        "Ah... it's warm here in Singapore,how many hours of aircon were you in today?", 
        reply_markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return AIRCON

def change_aircon(text):
    aircon_list = ["< 1h", "2h", "4h", "6h", "8h","10h", '12h','14h','> 14h']
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
    reply_keyboard = [["0h","0.5h", "1h", "1.5h", "2h", "2.5h","3h", '3.5h','> 3.5h']]
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
    bus_list = ["0h","0.5h", "1h", "1.5h", "2h", "2.5h","3h", '3.5h','> 3.5h']
    ans_num = bus_list.index(text)
    return (ans_num*0.5)


def bus(update, context):
    reply_keyboard = [["0h","0.5h", "1h", "1.5h", "2h", "2.5h","3h", '3.5h','> 3.5h']]
    user = update.message.from_user
    logger.info("Bus of %s: %s", user.first_name, update.message.text)
    user_choice_num = change_bus(update.message.text)
    user_choice_dict[user.first_name]["bus"] = user_choice_num
    logger.info("user bus # %s", user_choice_num)
    update.message.reply_text(
        'OK! Now tell me how long did you stay on a car today?', 
        reply_markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return CAR 

def change_car(text):
    car_list = ["0h","0.5h", "1h", "1.5h", "2h", "2.5h","3h", '3.5h','> 3.5h']
    ans_num = car_list.index(text)
    return (ans_num*0.5)


def car(update, context):
    reply_keyboard = [["0h","0.5h", "1h", "1.5h", "2h", "2.5h","3h", '3.5h','> 3.5h']]
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
    mrt_list = ["0h","0.5h", "1h", "1.5h", "2h", "2.5h","3h", '3.5h','> 3.5h']
    ans_num = mrt_list.index(text)
    return (ans_num*0.5)


def mrt(update, context):
    reply_keyboard = [["0h","2h","4h", "6h", "8h", "10h", "12h","14h","> 14h"]]
    user = update.message.from_user
    logger.info("MRT of %s: %s", user.first_name, update.message.text)
    user_choice_num = change_mrt(update.message.text)
    user_choice_dict[user.first_name]["mrt"] = user_choice_num
    logger.info("user mrt # %s", user_choice_num)
    update.message.reply_text(
        'Great! How many hours were you on the airplane? ', 
        reply_markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return FLIGHT 

def change_flight(text):
    flight_list = ["0h","2h","4h", "6h", "8h", "10h", "12h", "14h","> 14h"]
    ans_num = flight_list.index(text)
    return (ans_num*2)


def flight(update, context):
    reply_keyboard = [["Now let's see your score!!"]]
    user = update.message.from_user
    logger.info("Flight of %s: %s", user.first_name, update.message.text)
    user_choice_num = change_flight(update.message.text)
    user_choice_dict[user.first_name]["flight"] = user_choice_num
    logger.info("user flight # %s", user_choice_num)
    update.message.reply_text(
        'Great!', 
        reply_markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True,resize_keyboard=True))
    return ENDING 

def calculate_sum(user_dict):
    sum = 0
    for index, data in user_dict.items():
        if index == "laptop":
            sum += int(data) * 0.022415
        if index == "phone":
            sum += int(data) * 0.000775
        if index == "light":
            sum += int(data) * 0.01698 
        if index == "aircon":
            sum += int(data) * 0.1425594
        if index == "fan":
            sum += int(data) * 0.01981 
        if index == "bus":
            sum += int(data) * 0.76 
        if index == "car":
            sum += int(data) * 2.805
        if index == "mrt":
            sum += int(data) * 0.585
        if index == "flight":
            sum += int(data) * 90
    return sum

def sendImg(update,cal_sum):
    user = update.message.from_user
    posList = ["https://media.giphy.com/media/UReWNqLOku35dpKIDb/giphy.gif",'https://media.giphy.com/media/iesygExkPilc0oeNZr/giphy.gif','https://media.giphy.com/media/XcMSqKXh4MDZ6Xg7TS/giphy.gif','https://media.giphy.com/media/l1KVcrdl7rJpFnY2s/giphy.gif','https://media.giphy.com/media/3o6UB7MOoxIfHet9PG/giphy.gif','https://media3.giphy.com/media/nWXvQqyGRJJtu/giphy.gif','https://cdn.dribbble.com/users/176039/screenshots/6944109/toogethr-wevoke-threetrees-01.gif','https://i.pinimg.com/originals/86/07/f3/8607f380ccf87e428cefcddd55ad4b7d.gif','https://i.pinimg.com/originals/b0/15/6f/b0156fdd707ab88d2a6ca71e758b16ab.gif','']
    negList = ['https://media.giphy.com/media/3oFzm9D3ofutq98QIU/giphy.gif','https://media.giphy.com/media/l3vRebbaRnNFVfvnW/giphy.gif','https://media.giphy.com/media/12XaepjzBlBUOY/giphy.gif','https://media.giphy.com/media/239S4COH5KHT2/giphy.gif','https://media.giphy.com/media/UBBRU1wwOwapG/giphy.gif','https://media.giphy.com/media/2jMDwajdZGUoy1dht2/giphy.gif','https://media.giphy.com/media/ZgSEzHSQbijCmhbS6F/giphy.gif','https://media.giphy.com/media/2tOrrbWzUfa8UoH1RO/giphy.gif','https://media.giphy.com/media/jpQJQxqANC450flu4i/giphy.gif','https://media.giphy.com/media/26gsm43ayV5GS5KDu/giphy.gif','https://media.giphy.com/media/pOgEzg2a8BOBEXZA7a/giphy.gif','https://media0.giphy.com/media/8clNSa9G7PRSp59Dx3/giphy.gif','https://media0.giphy.com/media/AS8jJdsFrs8c7YcyGC/source.gif']
    negWebs = ['https://www.nationalgeographic.com/news/2012/1/120106-harp-seals-global-warming-sea-ice-science-environment/','https://inhabitat.com/photo-of-frail-polar-bear-illuminates-the-tragedy-unfolding-in-the-arctic/','http://content.time.com/time/health/article/0,8599,2095114,00.html','https://www.nationalgeographic.com/environment/2019/09/ipcc-report-climate-change-affecting-ocean-ice/','https://phys.org/news/2016-03-drought-recovery-rocky-mountain-forests.html','https://phys.org/news/2011-07-climate-change-induced-wildfires-yellowstone-forests.html','https://www.weadapt.org/knowledge-base/forests-and-climate-change/future-impacts-of-climate-change-on-forests','https://www.nationalgeographic.com/news/2018/02/polar-bears-starve-melting-sea-ice-global-warming-study-beaufort-sea-environment/']
    posWebs = ['https://sciencing.com/the-importance-of-reducing-a-carbon-footprint-5229039.html','https://www.americanpowerandgas.com/10-ways-can-reduce-carbon-footprint-house/','https://www.conservation.org/carbon-offsets/?','https://www.saveonenergy.com/learning-center/energy-saving-tips/how-does-saving-energy-help-the-environment/','https://www.co2nsensus.com/how-can-i-save-the-planet','https://www.youtube.com/watch?time_continue=2&v=9pPsso2acew','https://www.theguardian.com/environment/2017/jan/19/how-to-reduce-carbon-footprint','https://www.carbonfootprint.com/carbonoffsetprojects.html','https://www.straitstimes.com/world/united-states/sixty-six-countries-vow-carbon-neutrality-by-2050-un']
    ranNum = 0
    if(cal_sum > 5):
        ranNum = random.randint(0,len(negList)-1)
        update.message.reply_text("Oh no, your carbon footprint for today is *above average*...To find out how you can reduce it, check out this link:" + negWebs[random.randint(0,len(negWebs)-1)], parse_mode=ParseMode.MARKDOWN)
        imgUrl = negList[ranNum]
    else:
        ranNum = random.randint(0,len(posList)-1)
        update.message.reply_text("*Well done!* Your carbon footprint today is within the average benchmark. Keep it up!" + posWebs[random.randint(0,len(posWebs)-1)], parse_mode=ParseMode.MARKDOWN)
        imgUrl = posList[ranNum]
    user.send_document(imgUrl)

def ending(update, context):
    reply_keyboard = [["/start"]]
    user = update.message.from_user
    cal_sum = calculate_sum(user_choice_dict[user.first_name])
    update.message.reply_text(
        'Thank you! The average carbon footprint per day is approximately *5kg*. And your carbon footprint today is *' 
        + str(round(cal_sum)) + 'kg.*'
        , parse_mode=ParseMode.MARKDOWN
        ,reply_markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True,resize_keyboard=True))
    
    sendImg(update,cal_sum)
    logger.info("user sum %s", str(round(cal_sum,2)))
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
    # 1065787092:AAExGWnI-t3sirfBAtks_Hvb-6SeuhLBuw0
    # 733697750:AAECi30XQowgOibpPA0ZTHFOAu4UYYPRpA4
    updater = Updater("733697750:AAECi30XQowgOibpPA0ZTHFOAu4UYYPRpA4", use_context=True)
    dp = updater.dispatcher
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],

        states={
            LAPTOP: [MessageHandler(Filters.regex('^(< 1h|1h|2h|3h|4h|5h|6h|7h|> 7h)$'), laptop)],

            PHONE: [MessageHandler(Filters.regex('^(< 1h|1h|2h|3h|4h|5h|6h|7h|> 7h)$'), phone)],

            LIGHT: [MessageHandler(Filters.regex('^(< 1h|1h|2h|3h|4h|5h|6h|7h|> 7h)$'), light)],

            AIRCON: [MessageHandler(Filters.regex('^(< 1h|2h|4h|6h|8h|10h|12h|14h|> 14h)$'), aircon)],

            FAN: [MessageHandler(Filters.regex('^(< 1h|1h|2h|3h|4h|5h|6h|7h|> 7h)$'), fan)],

            BUS: [MessageHandler(Filters.regex('^(0h|0.5h|1h|1.5h|2h|2.5h|3h|3.5h|> 3.5h)$'), bus)],

            CAR: [MessageHandler(Filters.regex('^(0h|0.5h|1h|1.5h|2h|2.5h|3h|3.5h|> 3.5h)$'), car)],

            MRT: [MessageHandler(Filters.regex('^(0h|0.5h|1h|1.5h|2h|2.5h|3h|3.5h|> 3.5h)$'), mrt)],

            FLIGHT: [MessageHandler(Filters.regex('^(0h|2h|4h|6h|8h|10h|12h|14h|> 14h)$'), flight)],

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