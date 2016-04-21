# -*- coding: utf-8 -*-
import telebot # Library of API bot.
from telebot import types # Types from API bot
import time 
import random
import datetime
import codecs
import sys
import json
from os.path import exists
import os
#import re
#import logging

TOKEN = '193495980:AAHBS2z77Y9W4eSrQrgWwHaNiCrFX7hgzHg'
bot = telebot.TeleBot(TOKEN) # Creating our bot object.
bot.skip_pending=True
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
    
#Function to check if a message is too old(60 seconds) to answer.
def is_recent(m):
    return (time.time() - m.date) < 60   


added_message = '''
New Trigger Created:
Trigger [{}]
Response [{}]
'''
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
                bot.reply_to(m, 'Bad Arguments. Try with /add [trigger] / [response]')
                return
            trigger_word = m.text.split(' ', 1)[1].strip()
            trigger_response = m.reply_to_message.text.strip()
        else:
            bot.reply_to(m, 'Only text triggers are supported.')
            return
    else:    
        if(len(m.text.split()) < 2):
            bot.reply_to(m, 'Bad Arguments. Try with /add [trigger] / [response]')
            return
        if(m.text.find(separator, 1) == -1):
            bot.reply_to(m, 'Separator not found. Try with /add [trigger] / [response]')
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

# Search function used as easter eggs
#find_python = re.compile(r"(?i)\bPYTHON\b").search

#Functions
@bot.message_handler(commands=['kick']) # Command
def command_kick(m): 
    cid = m.chat.id # Store the user id
    bot.send_photo( cid, open( './imagenes/kick.jpg', 'rb')) # With the 'send_photo()' function we can send any image

@bot.message_handler(commands=['uppercut'])
def command_uppercut(m): 
    cid = m.chat.id 
    bot.send_photo( cid, open( './imagenes/uppercut.jpg', 'rb')) 

@bot.message_handler(commands=['hadouken']) 
def command_hadouken(m): 
    cid = m.chat.id 
    bot.send_document( cid, open( './imagenes/hadouken.gif', 'rb')) 

@bot.message_handler(commands=['windowsero']) 
def command_windowsero(m): 
    cid = m.chat.id 
    bot.send_photo( cid, open( './imagenes/windowsero.jpg', 'rb'))

@bot.message_handler(commands=['acerca']) 
def command_acerca(m):
    cid = m.chat.id 
    bot.send_message( cid, 'Acerca de @RootAdminBot: Creado por NeoRanger - www.neositelinux.com.ar') 

@bot.message_handler(commands=['help']) 
def command_ayuda(m): 
    cid = m.chat.id 
    bot.send_message( cid, "Comandos Disponibles: /welcome /hola /hello /kick /uppercut /hadouken /windowsero /ubuntu /stallman /ok /yes /nsa /attack /gentoo /kde /flame /tabla /vicman /deletethat /coding /nelson /spoiler /quetefo /esssta /fede /litrona /vegetta /what /takataka /kill /viernes /roll /time /blogroll /format /fuckyou /arch /tuxamigos /acerca /help") #

@bot.message_handler(commands=['hola']) 
def command_hola(m): 
    cid = m.chat.id 
    bot.send_message( cid, 'Hola, bienvenido!') 

@bot.message_handler(commands=['hello']) 
def command_hello(m): 
    cid = m.chat.id 
    bot.send_message( cid, 'Hello and welcome!') 

@bot.message_handler(commands=['attack']) 
def command_attack(m): 
    cid = m.chat.id 
    bot.send_photo( cid, open( './imagenes/dictionary_attack.jpg', 'rb')) 

@bot.message_handler(commands=['nsa']) 
def command_nsa(m): 
    cid = m.chat.id 
    bot.send_photo( cid, open( './imagenes/tiosam.jpg', 'rb'))

@bot.message_handler(commands=['roll']) 
def command_roll(m): 
    cid = m.chat.id 
    bot.send_message( cid, random.randint(1,6) )

@bot.message_handler(commands=['time'])
def command_time(m): 
    cid = m.chat.id 
    bot.send_message( cid, str(datetime.datetime.now())) 

@bot.message_handler(commands=['blogroll']) 
def command_blogroll(m): 
    cid = m.chat.id 
    bot.send_message( cid, 'BlogRoll: https://pad.riseup.net/p/blogroll') 

@bot.message_handler(commands=['gentoo']) 
def command_gentoo(m): 
    cid = m.chat.id 
    bot.send_photo( cid, open( './imagenes/gentoo.jpg', 'rb')) 

@bot.message_handler(commands=['vicman']) 
def command_vicman(m): 
    cid = m.chat.id 
    bot.send_photo( cid, open( './imagenes/vicman2.jpg', 'rb')) 

@bot.message_handler(commands=['tuxamigos']) 
def command_tuxamigos(m): 
    cid = m.chat.id 
    bot.send_photo( cid, open( './imagenes/tuxamigos.jpg', 'rb')) 

@bot.message_handler(commands=['deletethat']) 
def command_deletethat(m): 
    cid = m.chat.id 
    bot.send_photo( cid, open( './imagenes/deletethat.jpg', 'rb')) 

@bot.message_handler(commands=['flame']) 
def command_flame(m): 
    cid = m.chat.id 
    bot.send_photo( cid, open( './imagenes/popcorn.jpg', 'rb')) 

@bot.message_handler(commands=['stallman']) 
def command_stallman(m): 
    cid = m.chat.id 
    bot.send_photo( cid, open( './imagenes/dancingstallman.jpg', 'rb')) 

@bot.message_handler(commands=['ok']) 
def command_ok(m): 
    cid = m.chat.id 
    bot.send_photo( cid, open( './imagenes/ok.jpg', 'rb')) 

@bot.message_handler(commands=['coding']) 
def command_coding(m): 
    cid = m.chat.id 
    bot.send_photo( cid, open( './imagenes/coding.jpg', 'rb')) 

@bot.message_handler(commands=['nelson']) 
def command_nelson(m): 
    cid = m.chat.id 
    bot.send_photo( cid, open( './imagenes/nelson.jpg', 'rb')) 

@bot.message_handler(commands=['yes']) 
def command_fuckyeah(m): 
    cid = m.chat.id 
    bot.send_photo( cid, open( './imagenes/fuckyeah.jpg', 'rb')) 

@bot.message_handler(commands=['spoiler']) 
def command_spoiler(m): 
    cid = m.chat.id 
    bot.send_photo( cid, open( './imagenes/spoileralert.jpg', 'rb')) 

@bot.message_handler(commands=['viernes']) 
def command_viernes(m): 
    cid = m.chat.id 
    bot.send_photo( cid, open( './imagenes/viernes.jpg', 'rb')) 

@bot.message_handler(commands=['kde']) 
def command_kde(m): 
    cid = m.chat.id 
    bot.send_photo( cid, open( './imagenes/kderock.jpg', 'rb')) 

@bot.message_handler(commands=['esssta']) 
def command_esssta(m): 
    cid = m.chat.id 
    bot.send_photo( cid, open( './imagenes/esssta.jpg', 'rb')) 

@bot.message_handler(commands=['what']) 
def command_what(m): 
    cid = m.chat.id 
    bot.send_photo( cid, open( './imagenes/what.jpg', 'rb')) 

@bot.message_handler(commands=['vegetta']) 
def command_vegetta(m): 
    cid = m.chat.id 
    bot.send_photo( cid, open( './imagenes/vegetta.jpg', 'rb')) 

@bot.message_handler(commands=['litrona']) 
def command_litrona(m): 
    cid = m.chat.id 
    bot.send_photo( cid, open( './imagenes/litrona.jpg', 'rb')) 

@bot.message_handler(commands=['fede']) 
def command_fede(m): 
    cid = m.chat.id 
    bot.send_photo( cid, open( './imagenes/fede.jpg', 'rb'))

@bot.message_handler(commands=['welcome']) 
def command_welcome(m): 
    cid = m.chat.id 
    bot.send_photo( cid, open( './imagenes/welcome.jpg', 'rb'))

@bot.message_handler(commands=['tabla']) 
def command_tabla(m): 
    cid = m.chat.id 
    bot.send_photo( cid, open( './imagenes/tabla.jpg', 'rb'))

@bot.message_handler(commands=['takataka']) 
def command_taka(m): 
    cid = m.chat.id 
    bot.send_photo( cid, open( './imagenes/takataka.jpg', 'rb'))

@bot.message_handler(commands=['ubuntu']) 
def command_ubuntu(m): 
    cid = m.chat.id 
    bot.send_message( cid, 'http://www.youtube.com/watch?v=xK-_OdlCGBg') 

@bot.message_handler(commands=['kill'])
def command_kill(m):
    cid = m.chat.id
    bot.send_photo( cid, open( './imagenes/rambo.jpg', 'rb'))

@bot.message_handler(commands=['format'])
def command_format(m):
    cid = m.chat.id
    try:
        bot.send_message( cid, m.text.split(None,1)[1],parse_mode='markdown')
    except IndexError:
        bot.send_message( cid, "Argument missing" )
    except Exception:
        bot.send_message( cid, "Invalid argument" )

@bot.message_handler(commands=['maestruli']) 
def command_maestruli(m): 
    cid = m.chat.id 
    bot.send_document( cid, open( './imagenes/maestruli.mp4', 'rb')) 

@bot.message_handler(commands=['fuckyou']) 
def command_fuckyou(m): 
    cid = m.chat.id 
    bot.send_document( cid, open( './imagenes/fuckyou.mp4', 'rb')) 

@bot.message_handler(commands=['arch'])
def command_arch(m):
    cid = m.chat.id
    bot.send_photo( cid, open( './imagenes/arch.jpg', 'rb'))

#@bot.message_handler(content_types=['text'])
#def handle_text(m):
#    string_array = str(m.text).split(None,1)
#    if string_array[0] == 'python':
#         try:
#             cid = m.chat.id
#             username = m.from_user.username
#             bot.send_message( cid, username + " ama a Python" )

#@bot.message_handler(content_types=['text'])
#def handle_text(m):
#    string_array = str(m.text).split(None,1)
#    if string_array[0] == "/note":
#        try:
#            codecs.open("./imagenes/notas.txt", "a", "utf8").write("\n" + string_array[1])
#        except IndexError:
#            bot.send_message( cid, "Argumento invalido. Use /note y lo que quiera grabar" )

#@bot.message_handler(func=lambda m:
#    find_python("PYTHON", m.text.upper()))
#def love_python(m):
#    logging.info("%s: %s" % (m.from_user.username, "python"))
#    cid = m.chat.id
#    username = m.from_user.username
#    bot.send_message(cid, username + " loves Python")

@bot.message_handler(func=lambda m: True)
def response(m):
    if(m.chat.type in ['group', 'supergroup']):
        trg = get_triggers(m.chat.id)
        if(trg):
            for t in trg.keys():
                if t.lower() in m.text.lower():
                    bot.reply_to(m, trg[t])

print('Functions loaded')
