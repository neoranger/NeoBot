# -*- coding: utf-8 -*-
 
import telebot # Librería de la API del bot.
from telebot import types # Tipos para la API del bot.
import time # Librería para hacer que el programa que controla el bot no se acabe.
import random
import datetime
import token
 
TOKEN =  token.token_id # Nuestro tokken del bot (el que @BotFather nos dió).
 
bot = telebot.TeleBot(TOKEN) # Creamos el objeto de nuestro bot.
#############################################
#Listener
def listener(messages): # Con esto, estamos definiendo una función llamada 'listener', que recibe como parámetro un dato llamado 'messages'.
    for m in messages: # Por cada dato 'm' en el dato 'messages'
        cid = m.chat.id # Almacenaremos el ID de la conversación.
        if m.content_type == 'text':
            print "[" + str(cid) + "]: " + m.text # Y haremos que imprima algo parecido a esto -> [52033876]: /start
 
bot.set_update_listener(listener) # Así, le decimos al bot que utilice como función escuchadora nuestra función 'listener' declarada arriba.
#############################################
#Funciones
@bot.message_handler(commands=['kick']) # Indicamos que lo siguiente va a controlar el comando.
def command_kick(m): # Definimos una función que resuelva lo que necesitemos.
    cid = m.chat.id # Guardamos el ID de la conversación para poder responder.
    bot.send_photo( cid, open( 'kick.jpg', 'rb')) # Con la función 'send_photo()' del bot, enviamos al ID de la conversación que hemos almacenado previamente la foto

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
    bot.send_message( cid, "Comandos Disponibles: /hola /hello /kick /uppercut /hadouken /windowsero /stallman /ok /yes /nsa /attack /gentoo /kde /flame /vicman /deletethat /coding /nelson /spoiler /quetefo /viernes /roll /time /blogroll /tuxamigos /acerca /help") #
 
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


@bot.message_handler(commands=['quetefo']) 
def command_quetefo(m): 
    cid = m.chat.id 
    bot.send_photo( cid, open( 'quetefo.jpg', 'rb')) 
 
@bot.message_handler(commands=['viernes']) 
def command_viernes(m): 
    cid = m.chat.id 
    bot.send_photo( cid, open( 'viernes.jpg', 'rb')) 

@bot.message_handler(commands=['kde']) 
def command_kde(m): 
    cid = m.chat.id 
    bot.send_photo( cid, open( 'kderock.jpg', 'rb')) 
 
#############################################
#Peticiones
bot.polling(none_stop=True) # Con esto, le decimos al bot que siga funcionando incluso si encuentra algun fallo.
