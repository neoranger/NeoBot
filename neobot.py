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

#############################################
#Catch every message, for triggers.
@bot.message_handler(func=lambda m: True)
def response(m):
    if(m.chat.type in ['group', 'supergroup']):
        trg = get_triggers(m.chat.id)
        if(trg):
            for t in trg.keys():
                if t.lower() in m.text.lower():
                    bot.reply_to(m, trg[t])
#############################################

################################################################## 
#Bot starts here
print('Bot Started')
functions.bot.polling(none_stop=True)
