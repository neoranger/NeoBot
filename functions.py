# -*- coding: utf-8 -*-

import telebot # Library of API bot.
from telebot import types # Types from API bot
import time 
import random
import datetime
import token

TOKEN =  token.token_id # Our token (that's @BotFather give us).
bot = telebot.TeleBot(TOKEN) # Create the bot object.

#Functions
@bot.message_handler(commands=['kick']) # Command
def command_kick(m): 
    cid = m.chat.id # Store the user id
    bot.send_photo( cid, open( './imagenes/kick.jpg', 'rb')) # With the 'send_photo()' function we can send any image

@bot.message_handler(commands=['uppercut'])
def command_uppercut(m): 
    cid = m.chat.id 
    bot.send_photo( cid, open( 'uppercut.jpg', 'rb')) 
 
@bot.message_handler(commands=['hadouken']) 
def command_hadouken(m): 
    cid = m.chat.id 
    bot.send_photo( cid, open( 'hadouken.gif', 'rb')) 
    
@bot.message_handler(commands=['windowsero']) 
def command_windowsero(m): 
    cid = m.chat.id 
    bot.send_photo( cid, open( 'windowsero.jpg', 'rb'))
    
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
    bot.send_photo( cid, open( 'dictionary_attack.jpg', 'rb')) 

@bot.message_handler(commands=['nsa']) 
def command_nsa(m): 
    cid = m.chat.id 
    bot.send_photo( cid, open( 'tiosam.jpg', 'rb'))

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
    bot.send_photo( cid, open( 'gentoo.jpg', 'rb')) 

@bot.message_handler(commands=['vicman']) 
def command_vicman(m): 
    cid = m.chat.id 
    bot.send_photo( cid, open( 'vicman2.jpg', 'rb')) 

@bot.message_handler(commands=['tuxamigos']) 
def command_tuxamigos(m): 
    cid = m.chat.id 
    bot.send_photo( cid, open( 'tuxamigos.jpg', 'rb')) 
    
@bot.message_handler(commands=['deletethat']) 
def command_deletethat(m): 
    cid = m.chat.id 
    bot.send_photo( cid, open( 'deletethat.jpg', 'rb')) 

@bot.message_handler(commands=['flame']) 
def command_flame(m): 
    cid = m.chat.id 
    bot.send_photo( cid, open( 'popcorn.jpg', 'rb')) 

@bot.message_handler(commands=['stallman']) 
def command_stallman(m): 
    cid = m.chat.id 
    bot.send_photo( cid, open( 'dancingstallman.jpg', 'rb')) 
 
@bot.message_handler(commands=['ok']) 
def command_ok(m): 
    cid = m.chat.id 
    bot.send_photo( cid, open( 'ok.jpg', 'rb')) 

@bot.message_handler(commands=['coding']) 
def command_coding(m): 
    cid = m.chat.id 
    bot.send_photo( cid, open( 'coding.jpg', 'rb')) 
 
@bot.message_handler(commands=['nelson']) 
def command_nelson(m): 
    cid = m.chat.id 
    bot.send_photo( cid, open( 'nelson.jpg', 'rb')) 
 
@bot.message_handler(commands=['yes']) 
def command_fuckyeah(m): 
    cid = m.chat.id 
    bot.send_photo( cid, open( 'fuckyeah.jpg', 'rb')) 
 
@bot.message_handler(commands=['spoiler']) 
def command_spoiler(m): 
    cid = m.chat.id 
    bot.send_photo( cid, open( 'spoileralert.jpg', 'rb')) 

@bot.message_handler(commands=['viernes']) 
def command_viernes(m): 
    cid = m.chat.id 
    bot.send_photo( cid, open( 'viernes.jpg', 'rb')) 

@bot.message_handler(commands=['kde']) 
def command_kde(m): 
    cid = m.chat.id 
    bot.send_photo( cid, open( 'kderock.jpg', 'rb')) 

@bot.message_handler(commands=['esssta']) 
def command_esssta(m): 
    cid = m.chat.id 
    bot.send_photo( cid, open( 'esssta.jpg', 'rb')) 

@bot.message_handler(commands=['what']) 
def command_what(m): 
    cid = m.chat.id 
    bot.send_photo( cid, open( 'what.jpg', 'rb')) 
 
@bot.message_handler(commands=['vegetta']) 
def command_vegetta(m): 
    cid = m.chat.id 
    bot.send_photo( cid, open( 'vegetta.jpg', 'rb')) 
 
@bot.message_handler(commands=['litrona']) 
def command_litrona(m): 
    cid = m.chat.id 
    bot.send_photo( cid, open( 'litrona.jpg', 'rb')) 
 
@bot.message_handler(commands=['fede']) 
def command_fede(m): 
    cid = m.chat.id 
    bot.send_photo( cid, open( 'fede.jpg', 'rb'))
    
@bot.message_handler(commands=['welcome']) 
def command_welcome(m): 
    cid = m.chat.id 
    bot.send_photo( cid, open( 'welcome.jpg', 'rb'))

@bot.message_handler(commands=['tabla']) 
def command_tabla(m): 
    cid = m.chat.id 
    bot.send_photo( cid, open( 'tabla.jpg', 'rb'))

@bot.message_handler(commands=['takataka']) 
def command_taka(m): 
    cid = m.chat.id 
    bot.send_photo( cid, open( 'takataka.jpg', 'rb'))

@bot.message_handler(commands=['ubuntu']) 
def command_ubuntu(m): 
    cid = m.chat.id 
    bot.send_message( cid, 'http://www.youtube.com/watch?v=xK-_OdlCGBg') 
@bot.message_handler(commands=['kill']) 
def command_kill(m): 
    cid = m.chat.id 
    bot.send_photo( cid, open( 'rambo.jpg', 'rb'))

@bot.message_handler(commands=['format'])
def command_format(m): 
    cid = m.chat.id 
    try:
	bot.send_message( cid, m.text.split(None,1)[1],parse_mode='markdown')
    except IndexError:
        bot.send_message( cid, "Argument missing" )
    except Exception:
        bot.send_message( cid, "Invalid argument" )

#find_match("RUBY", message.text.upper())
#def love_ruby(m):
#    logging.info("%s: %s" % (message.from_user.username, "ruby"))
#    cid = m.chat.id
#    username = m.from_user.username
#    bot.send_message(cid, username + " loves Ruby")
