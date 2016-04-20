# -*- coding: utf-8 -*-
import telebot
from telebot import types
import functions
import token
import sys
import json
from os.path import exists
import StringIO
import user
import os

#######################################
TOKEN = token.token_id
bot = telebot.TeleBot(TOKEN) # Creating our bot object.
functions.bot.skip_pending=True
#######################################

#######################################
#TRIGGERS SECTION
triggers = {}
tfile = "triggers.json"
ignored = []
separator = '/'
#user = [line.rstrip('\n') for line in open('user.txt','rt')]

#Check if Triggers file exists and load, if not, is created.
if exists('triggers.json'):
    with open('triggers.json') as f:
        triggers = json.load(f)
    print('Triggers file loaded.')
else:
    with open('triggers.json', 'w') as f:
        json.dump({}, f)

#Function to save Triggers - Response
def save_triggers():
    with open('triggers.json', 'w') as f:
        json.dump(triggers, f)
    print('Triggers file saved.')
    
#Function to get triggers list for a group.
def get_triggers(group_id):
    if(str(group_id) in triggers.keys()):
        return triggers[str(group_id)]
    else:
        return False
    
#Delete whitespaces at start & end
def trim(s):
    i = 0
    while(s[i] == ' '):
        i += 1
    s = s[i:]
    i = len(s)-1
    while(s[i] == ' '):
        i-= 1
    s = s[:i+1]
    return s    

#Function to check if a message is too old(60 seconds) to answer.
def is_recent(m):
    return (time.time() - m.date) < 60   

#END TRIGGERS SECTION
#######################################

#######################################
#Triggers Management Section
#Adds another trigger-response. ex: "/add Hi / Hi!! :DD"
@bot.message_handler(commands=['add'])
def add(m):
    if(m.reply_to_message):
        if(m.reply_to_message.text):
            if(len(m.reply_to_message.text.split()) < 2):
                bot.reply_to(m, 'Bad Arguments')
                return
            trigger_word = m.text.split(' ', 1)[1].strip()
            trigger_response = m.reply_to_message.text.strip()
        else:
            bot.reply_to(m, 'Only text triggers are supported.')
            return
    else:    
        if(len(m.text.split()) < 2):
            bot.reply_to(m, 'Bad Arguments')
            return
        if(m.text.find(separator, 1) == -1):
            bot.reply_to(m, 'Separator not found')
            return
        rest_text = m.text.split(' ', 1)[1]
        trigger_word = rest_text.split(separator)[0].strip()
        trigger_response = rest_text.split(separator, 1)[1].strip()

    if(len(trigger_word) < 4):
        bot.reply_to(m, 'Trigger too short. [chars < 4]')
        return
    if(len(trigger_response) < 1):
        bot.reply_to(m, 'Invalid Response.')
        return
    if(m.chat.type in ['group', 'supergroup']):
        if(get_triggers(m.chat.id)):
            get_triggers(m.chat.id)[trigger_word] = trigger_response
        else:
            triggers[str(m.chat.id)] = {trigger_word : trigger_response}
        msg = added_message.format(trigger_word, trigger_response)
        bot.reply_to(m, msg)
        save_triggers()
    else:
        if(m.chat.id != owner):
            return

@bot.message_handler(commands=['del'])
def delete(m):
    if(len(m.text.split()) < 2):
        bot.reply_to(m, 'Bad Arguments')
        return
    del_text = m.text.split(' ', 1)[1].strip()
    if(m.chat.type in ['group', 'supergroup']):
        trg = get_triggers(m.chat.id)
        if(trg and del_text in trg.keys()):
            trg.pop(del_text)
            bot.reply_to(m, 'Trigger [{}] deleted.'.format(del_text))
            save_triggers()
        else:
            bot.reply_to(m, 'Trigger [{}] not found.'.format(del_text))

#Answers with the size of triggers.
@bot.message_handler(commands=['size'])
def size(m):
    if(m.chat.type in ['group', 'supergroup']):
        trg = get_triggers(m.chat.id)
        if(trg):
            msg = 'Size of Triggers List = {}'.format(len(trg))
            bot.reply_to(m, msg)
        else:
            bot.reply_to(m, 'Size of Triggers List = 0')

@bot.message_handler(commands=['all'])
def all(m):
    if(m.chat.type in ['group', 'supergroup']):
        trg = get_triggers(m.chat.id)
        if(trg):
            if(len(trg.keys()) == 0):
                bot.reply_to(m, 'This group doesn\'t have triggers.')
            else:
                bot.reply_to(m,'Trigers:\n' + '\n'.join(trg))
        else:
            bot.reply_to(m, 'This group doesn\'t have triggers.')

#End Triggers Management Section
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
