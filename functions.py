# -*- coding: utf-8 -*-

import telebot # Library of API bot.
from telebot import types # Types from API bot
import time 
import random
import datetime
import token
import codecs
#import re
#import logging

TOKEN =  token.token_id # Our token (that's @BotFather give us).
bot = telebot.TeleBot(TOKEN) # Create the bot object.

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
    bot.send_gif( cid, open( './imagenes/hadouken.gif', 'rb')) 
    
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
    bot.send_message( cid, "Comandos Disponibles: /welcome /hola /hello /kick /uppercut /hadouken /windowsero /ubuntu /stallman /ok /yes /nsa /attack /gentoo /kde /flame /tabla /vicman /deletethat /coding /nelson /spoiler /quetefo /esssta /fede /litrona /vegetta /what /takataka /kill /viernes /roll /time /blogroll /format /tuxamigos /acerca /help") #
 
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
        
@bot.message_handler(content_types=['text'])
def handle_text(m):
    string_array = str(m.text).split(None,1)
    if string_array[0] == "python":
    	try:
    	   cid = m.chat.id
    	   username = m.from_user.username
    	   bot.send_message(cid, username + " ama a Python")

#@bot.message_handler(content_types=['text'])
#def handle_text(m):
#    string_array = str(m.text).split(None,1)
#    if string_array[0] == "/note":
#    	try:
#    	   codecs.open("./imagenes/notas.txt", "a", "utf8").write("\n" + string_array[1])
#    	except IndexError:
#    	   bot.send_message( cid, "Argumento invalido. Use /note y lo que quiera grabar" )

#@bot.message_handler(func=lambda m:
#    find_python("PYTHON", m.text.upper()))
#def love_python(m):
#    logging.info("%s: %s" % (m.from_user.username, "python"))
#    cid = m.chat.id
#    username = m.from_user.username
#    bot.send_message(cid, username + " loves Python")
