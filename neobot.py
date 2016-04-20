# -*- coding: utf-8 -*-
import telebot
from telebot import types
import functions
import token

#######################################
TOKEN = token.token_id
bot = telebot.TeleBot(TOKEN) # Creating our bot object.
functions.bot.skip_pending=True
#######################################

#############################################
#Listener
def listener(messages):
    for m in messages:
        cid = m.chat.id
        if m.content_type == 'text':
            print "[" + str(cid) + "]: " + m.text
 
functions.bot.set_update_listener(listener)
#############################################

################################################################## 
#Peticiones
functions.bot.polling(none_stop=True)
