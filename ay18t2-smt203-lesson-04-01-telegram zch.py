########################################################################
# ay18t2-smt203-lesson-04-01-telegram
# references: 
# 	http://docs.python-requests.org/en/v0.6.1/api/#requests.models.Response
# 	https://core.telegram.org/bots/api
#   https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
# objectives:
#   in this exercise, you will learn how to use the Telegram API to
#   - CRUD text messages (send, read, update, delete msg)
#   - send stickers, photos and files via Telegram 
########################################################################

import requests
import json
import datetime 

########################################################################
# global variables 
########################################################################

my_token = '792397772:AAF5JOH6LaVs4wjPwoGDwH33rKGpNKzVzPs' # put your secret Telegram token here 
url_base = 'https://api.telegram.org/bot{}/'.format(my_token)

########################################################################
# The telegram API supports GET and POST HTTP methods. 
# https://core.telegram.org/bots/api#available-methods 
# The HTTP URLs for each method looks like this: 
# https://api.telegram.org/bot{token}/{method_name}.
# The following defines the URLs for each method that we will use.
########################################################################

# if you are not sure how each of these look like, you can print them
url_getMe = '{}getme'.format(url_base)
url_getUpdates = '{}getupdates'.format(url_base)
url_sendMsg = '{}sendMessage'.format(url_base)
url_editMsgText = '{}editMessageText'.format(url_base)
url_delMsg = '{}deleteMessage'.format(url_base)

url_sendPhoto = '{}sendPhoto'.format(url_base)
url_sendDoc = '{}sendDocument'.format(url_base)
url_sendSticker = '{}sendSticker'.format(url_base)

# here, we define common functions that we can use
def print_pretty_json(json_object):
    print(json.dumps(json_object, indent=2, sort_keys=True))
    return 

########################################################################
# *Qn 4.1.1
# Write a function that returns the id and username of your bot.
# See https://core.telegram.org/bots/api#getme for more details 
# You should get the same results if you visit 
# https://api.telegram.org/bot{token}/getMe on your web browser 
########################################################################

def get_bot_details():
    username = None 
    bot_id = None 

    # write your code here

    r = requests.get(url = url_getMe)
    username = r.json()["result"]["username"]
    bot_id = r.json()['result']['id']
    # your code should end above this line 
    
    print('username: {}, bot_id: {}'.format(username, bot_id))
    return username, bot_id 

get_bot_details()

########################################################################
# *Qn 4.1.2
# Write a function that returns the list of (username, chat_id) of users 
# who have interacted with your bot in the last 24 hrs.
# See https://core.telegram.org/bots/api#getupdates for more details 
# Note that incoming updates are not kept longer than 24 hrs
########################################################################

r = requests.get(url = url_getUpdates)
def get_user_list(): 
    user_list = []

    # write your code here

#     for i in r.json()['result']:
#         if i['message']['chat']['id'] not in user_list:
#             user_list.append(i['message']['chat']['id'])
#             user_list.append(i['message']['chat']['username'])

#     # your code should end above this line 
#     for user in user_list:
#         print('username: {}, chat_id: {}'.format(user[0], user[1]))
#     return user_list

# get_user_list() 

########################################################################
# **Qn 4.1.3
# Write a function that sends a Welcome message to the last user  
# who has interacted with your bot 
# See https://core.telegram.org/bots/api#sendmessage for more details 
# bonus: include the date/time in your welcome msg 
########################################################################

def send_welcome_msg():

    # write your code here
    params = {'chat_id':'412385892','text':'welcomeeee!!!'}
    r = requests.post(url_sendMsg,params)
    # params = {'chat_id':'412385892','photo':'https://pbs.twimg.com/profile_images/698243097365340162/OpF_q4vq_400x400.jpg'}
    # r = requests.post(url_sendPhoto,params)
    # your code should end above this line 
    return r.json()
        
# send_welcome_msg()

########################################################################
# *Qn 4.1.4
# Write a function that edits the last message that was sent by the bot
# See https://core.telegram.org/bots/api#updating-messages for more details
# You may use send_welcome_msg and edit the last msg   
########################################################################

def edit_msg(previous_response, new_msg):
    
    # write your code here
    params = {'chat_id':'412385892','message_id':'4','text':'Another new welcomeeee!!!'}
    r = requests.post(url_editMsgText,params)

    # your code should end above this line 
    return r.json()

r = send_welcome_msg()
edit_msg(r, 'this msg was edited')

########################################################################
# *Qn 4.1.5
# Write a function that deletes the last message that was sent by the bot
# See https://core.telegram.org/bots/api#deletemessage for more details
# Note that a message can only be deleted if it was sent < 48 hrs ago 
########################################################################

def delete_msg(previous_response):

    # write your code here
    
    # your code should end above this line
    return r.json()

# r = send_welcome_msg()
# delete_msg(r)

########################################################################
# *Qn 4.1.6
# Write a function that sends a photo (via a URL) to the last user  
# who has interacted with your bot 
# See https://core.telegram.org/bots/api#sendphoto for more details 
########################################################################

def send_photo(previous_response, photo_url, caption):

    # write your code here
    
    # your code should end above this line
    return r.json()

# r = send_welcome_msg()
# send_photo(r, 'https://static.boredpanda.com/blog/wp-content/uploads/2015/09/Instagrams-most-famous-cat-Nala16__605.jpg', 'Nala')

########################################################################
# *Qn 4.1.7
# Write a function that sends a file to the last user  
# who has interacted with your bot 
# See https://core.telegram.org/bots/api#senddocument for more details 
########################################################################

def send_file(previous_response, filename, caption):

    # write your code here
    
    # your code should end above this line
    return r.json()

# r = send_welcome_msg()
# send_file(r, 'req.txt', 'req file')

########################################################################
# **Qn 4.1.8
# Write a function that sends a sticker to the last user  
# who has interacted with your bot 
# See https://core.telegram.org/bots/api#sendsticker for more details 
# To get the sticker ID, you can send a sticker to your bot
# and retrieve details of the sticker ID in the last msg (update)
########################################################################

def send_sticker(previous_response, sticker):

    # write your code here
   
    # your code should end above this line
    return r.json()

# r = send_welcome_msg()
# send_sticker(r, 'CAADAgADRR8AAuCjggdtodK9EJyJsQI')