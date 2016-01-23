# -*- coding: utf-8 -*-
 
import telebot # Librería de la API del bot.
from telebot import types # Tipos para la API del bot.
import time # Librería para hacer que el programa que controla el bot no se acabe.
import random
import datetime
 
TOKEN = 'Here's the token' # Nuestro tokken del bot (el que @BotFather 
nos 
dió).
 
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

@bot.message_handler(commands=['uppercut']) # Indicamos que lo siguiente va a controlar el comando.
def command_uppercut(m): # Definimos una función que resuelva lo que necesitemos.
    cid = m.chat.id # Guardamos el ID de la conversación para poder responder.
    bot.send_photo( cid, open( 'uppercut.jpg', 'rb')) # Con la función 'send_photo()' del bot, enviamos al ID de la conversación que hemos almacenado previamente la foto    
 
@bot.message_handler(commands=['hadouken']) # Indicamos que lo siguiente va a controlar el comando.
def command_hadouken(m): # Definimos una función que resuelva lo que necesitemos.
    cid = m.chat.id # Guardamos el ID de la conversación para poder responder.
    bot.send_photo( cid, open( 'hadouken.gif', 'rb')) # Con la función 'send_photo()' del bot, enviamos al ID de la conversación que hemos almacenado previamente la foto
    
@bot.message_handler(commands=['windowsero']) # Indicamos que lo siguiente va a controlar el comando.
def command_windowsero(m): # Definimos una función que resuelva lo que necesitemos.
    cid = m.chat.id # Guardamos el ID de la conversación para poder responder.
    bot.send_photo( cid, open( 'windowsero.jpg', 'rb')) # Con la función 'send_photo()' del bot, enviamos al ID de la conversación que hemos almacenado previamente la foto    
    
@bot.message_handler(commands=['acerca']) # Indicamos que lo siguiente va a controlar el comando.
def command_acerca(m): # Definimos una función que resuleva lo que necesitemos.
    cid = m.chat.id # Guardamos el ID de la conversación para poder responder.
    bot.send_message( cid, 'Acerca de @RootAdminBot: Creado por NeoRanger - www.neositelinux.com.ar') # Con la función 'send_message()' del bot, enviamos al ID almacenado el texto que queremos.
    
@bot.message_handler(commands=['help']) # Indicamos que lo siguiente va a controlar el comando.
def command_ayuda(m): # Definimos una función que resuleva lo que necesitemos.
    cid = m.chat.id # Guardamos el ID de la conversación para poder responder.
    bot.send_message( cid, "Comandos Disponibles: /hola /hello /kick /uppercut /hadouken /windowsero /stallman /ok /yes /nsa /attack /gentoo /kde /flame /vicman /deletethat /coding /nelson /spoiler /quetefo /viernes /roll /time /blogroll /tuxamigos /acerca /help") #
 
@bot.message_handler(commands=['hola']) # Indicamos que lo siguiente va a controlar el comando.
def command_hola(m): # Definimos una función que resuleva lo que necesitemos.
    cid = m.chat.id # Guardamos el ID de la conversación para poder responder.
    bot.send_message( cid, 'Hola, bienvenido!') # Con la función 'send_message()' del bot, enviamos al ID almacenado el texto que queremos.    

@bot.message_handler(commands=['hello']) # Indicamos que lo siguiente va a controlar el comando.
def command_hello(m): # Definimos una función que resuleva lo que necesitemos.
    cid = m.chat.id # Guardamos el ID de la conversación para poder responder.
    bot.send_message( cid, 'Hello and welcome!') # Con la función 'send_message()' del bot, enviamos al ID almacenado el texto que queremos.        

@bot.message_handler(commands=['attack']) # Indicamos que lo siguiente va a controlar el comando.
def command_attack(m): # Definimos una función que resuelva lo que necesitemos.
    cid = m.chat.id # Guardamos el ID de la conversación para poder responder.
    bot.send_photo( cid, open( 'dictionary_attack.jpg', 'rb')) # Con la función 'send_photo()' del bot, enviamos al ID de la conversación que hemos almacenado previamente la foto

@bot.message_handler(commands=['nsa']) # Indicamos que lo siguiente va a controlar el comando.
def command_nsa(m): # Definimos una función que resuelva lo que necesitemos.
    cid = m.chat.id # Guardamos el ID de la conversación para poder responder.
    bot.send_photo( cid, open( 'tiosam.jpg', 'rb')) # Con la función 'send_photo()' del bot, enviamos al ID de la conversación que hemos almacenado previamente la foto

@bot.message_handler(commands=['roll']) # Indicamos que lo siguiente va a controlar el comando.
def command_roll(m): # Definimos una función que resuleva lo que necesitemos.
    cid = m.chat.id # Guardamos el ID de la conversación para poder responder.
    bot.send_message( cid, random.randint(1,6) ) # Con la función 'send_message()' del bot, enviamos al ID almacenado el texto que queremos.        
@bot.message_handler(commands=['time']) # Indicamos que lo siguiente va a controlar el comando.
def command_time(m): # Definimos una función que resuleva lo que necesitemos.
    cid = m.chat.id # Guardamos el ID de la conversación para poder responder.
    bot.send_message( cid, str(datetime.datetime.now())) # Con la función 'send_message()' del bot, enviamos al ID almacenado el texto que queremos.        

@bot.message_handler(commands=['blogroll']) # Indicamos que lo siguiente va a controlar el comando.
def command_blogroll(m): # Definimos una función que resuleva lo que necesitemos.
    cid = m.chat.id # Guardamos el ID de la conversación para poder responder.
    bot.send_message( cid, 'BlogRoll: https://pad.riseup.net/p/blogroll') # Con la función 'send_message()' del bot, enviamos al ID almacenado el texto que queremos.
 
@bot.message_handler(commands=['gentoo']) # Indicamos que lo siguiente va a controlar el comando.
def command_gentoo(m): # Definimos una función que resuelva lo que necesitemos.
    cid = m.chat.id # Guardamos el ID de la conversación para poder responder.
    bot.send_photo( cid, open( 'gentoo.jpg', 'rb')) # Con la función 'send_photo()' del bot, enviamos al ID de la conversación que hemos almacenado previamente la foto


@bot.message_handler(commands=['vicman']) # Indicamos que lo siguiente va a controlar el comando.
def command_vicman(m): # Definimos una función que resuelva lo que necesitemos.
    cid = m.chat.id # Guardamos el ID de la conversación para poder responder.
    bot.send_photo( cid, open( 'vicman2.jpg', 'rb')) # Con la función 'send_photo()' del bot, enviamos al ID de la conversación que hemos almacenado previamente la foto

@bot.message_handler(commands=['tuxamigos']) # Indicamos que lo siguiente va a controlar el comando.
def command_tuxamigos(m): # Definimos una función que resuelva lo que necesitemos.
    cid = m.chat.id # Guardamos el ID de la conversación para poder responder.
    bot.send_photo( cid, open( 'tuxamigos.jpg', 'rb')) # Con la función 'send_photo()' del bot, enviamos al ID de la conversación que hemos almacenado previamente la foto

@bot.message_handler(commands=['deletethat']) # Indicamos que lo siguiente va a controlar el comando.
def command_deletethat(m): # Definimos una función que resuelva lo que necesitemos.
    cid = m.chat.id # Guardamos el ID de la conversación para poder responder.
    bot.send_photo( cid, open( 'deletethat.jpg', 'rb')) # Con la función 'send_photo()' del bot, enviamos al ID de la conversación que hemos almacenado previamente la foto

@bot.message_handler(commands=['flame']) # Indicamos que lo siguiente va a controlar el comando.
def command_flame(m): # Definimos una función que resuelva lo que necesitemos.
    cid = m.chat.id # Guardamos el ID de la conversación para poder responder.
    bot.send_photo( cid, open( 'popcorn.jpg', 'rb')) # Con la función 'send_photo()' del bot, enviamos al ID de la conversación que hemos almacenado previamente la foto

@bot.message_handler(commands=['stallman']) # Indicamos que lo siguiente va a controlar el comando.
def command_stallman(m): # Definimos una función que resuelva lo que necesitemos.
    cid = m.chat.id # Guardamos el ID de la conversación para poder responder.
    bot.send_photo( cid, open( 'dancingstallman.jpg', 'rb')) # Con la función 'send_photo()' del bot, enviamos al ID de la conversación que hemos almacenado previamente la foto    
 
@bot.message_handler(commands=['ok']) # Indicamos que lo siguiente va a controlar el comando.
def command_ok(m): # Definimos una función que resuelva lo que necesitemos.
    cid = m.chat.id # Guardamos el ID de la conversación para poder responder.
    bot.send_photo( cid, open( 'ok.jpg', 'rb')) # Con la función 'send_photo()' del bot, enviamos al ID de la conversación que hemos almacenado previamente la foto    

@bot.message_handler(commands=['coding']) # Indicamos que lo siguiente va a controlar el comando.
def command_coding(m): # Definimos una función que resuelva lo que necesitemos.
    cid = m.chat.id # Guardamos el ID de la conversación para poder responder.
    bot.send_photo( cid, open( 'coding.jpg', 'rb')) # Con la función 'send_photo()' del bot, enviamos al ID de la conversación que hemos almacenado previamente la foto    
 
@bot.message_handler(commands=['nelson']) # Indicamos que lo siguiente va a controlar el comando.
def command_nelson(m): # Definimos una función que resuelva lo que necesitemos.
    cid = m.chat.id # Guardamos el ID de la conversación para poder responder.
    bot.send_photo( cid, open( 'nelson.jpg', 'rb')) # Con la función 'send_photo()' del bot, enviamos al ID de la conversación que hemos almacenado previamente la foto    
 
@bot.message_handler(commands=['yes']) # Indicamos que lo siguiente va a controlar el comando.
def command_fuckyeah(m): # Definimos una función que resuelva lo que necesitemos.
    cid = m.chat.id # Guardamos el ID de la conversación para poder responder.
    bot.send_photo( cid, open( 'fuckyeah.jpg', 'rb')) # Con la función 'send_photo()' del bot, enviamos al ID de la conversación que hemos almacenado previamente la foto    
 
@bot.message_handler(commands=['spoiler']) # Indicamos que lo siguiente va a controlar el comando.
def command_spoiler(m): # Definimos una función que resuelva lo que necesitemos.
    cid = m.chat.id # Guardamos el ID de la conversación para poder responder.
    bot.send_photo( cid, open( 'spoileralert.jpg', 'rb')) # Con la función 'send_photo()' del bot, enviamos al ID de la conversación que hemos almacenado previamente la foto    


@bot.message_handler(commands=['quetefo']) # Indicamos que lo siguiente va a controlar el comando.
def command_quetefo(m): # Definimos una función que resuelva lo que necesitemos.
    cid = m.chat.id # Guardamos el ID de la conversación para poder responder.
    bot.send_photo( cid, open( 'quetefo.jpg', 'rb')) # Con la función 'send_photo()' del bot, enviamos al ID de la conversación que hemos almacenado previamente la foto    
 
@bot.message_handler(commands=['viernes']) # Indicamos que lo siguiente va a controlar el comando.
def command_viernes(m): # Definimos una función que resuelva lo que necesitemos.
    cid = m.chat.id # Guardamos el ID de la conversación para poder responder.
    bot.send_photo( cid, open( 'viernes.jpg', 'rb')) # Con la función 'send_photo()' del bot, enviamos al ID de la conversación que hemos almacenado previamente la foto    

@bot.message_handler(commands=['kde']) # Indicamos que lo siguiente va a controlar el comando.
def command_kde(m): # Definimos una función que resuelva lo que necesitemos.
    cid = m.chat.id # Guardamos el ID de la conversación para poder responder.
    bot.send_photo( cid, open( 'kderock.jpg', 'rb')) # Con la función 'send_photo()' del bot, enviamos al ID de la conversación que hemos almacenado previamente la foto    
 


 
#############################################
#Peticiones
bot.polling(none_stop=True) # Con esto, le decimos al bot que siga funcionando incluso si encuentra algun fallo.
