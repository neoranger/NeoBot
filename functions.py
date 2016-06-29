# -*- coding: utf-8 -*-
import telebot # Library of API bot.
from telebot import types # Types from API bot
import codecs
import sys
import json
from os.path import exists
import os
import token
import user
import feedparser
#import re
#import logging

TOKEN = token.token_id
bot = telebot.TeleBot(TOKEN) # Creating our bot object.
bot.skip_pending=True

#######################################
#Function for feedparser
#CODE TAKEN FROM:
#https://gist.github.com/Jeshwanth/99cf05f4477ab0161349
def get_feed(url):
    try:
        feed = feedparser.parse(url)
    except:
        return 'Invalid url.'
    y = len(feed[ "items" ])
    y = 10 if y > 10 else y
    if(y < 1):
        return 'Nothing found'
    lines = ['*Feed:*']
    for x in range(y):
        lines.append('- [{}]({})'.format(feed['items'][x]['title'].replace(']', ':').replace('[', '').encode('utf-8'), feed['items'][x]['link']))
    return '\n'.join(lines)

#######################################

#Functions
@bot.message_handler(content_types=['new_chat_member'])
def command_new_user(m):
    cid = m.chat.id
    bot.send_message(cid, 'Bienvenido!!' + '@' + str(m.new_chat_member.username) + ' al grupo!!')

@bot.message_handler(content_types=['left_chat_member'])
def command_left_user(m):
    cid = m.chat.id
    bot.send_message(cid, '@' + str(m.left_chat_member.username) + ' Gracias por pasar!! Bye!! ')


@bot.message_handler(commands=['acerca'])
def command_acerca(m):
    cid = m.chat.id
    bot.send_message( cid, 'Acerca de @InfoSerTecBot: Creado por NeoRanger - www.neositelinux.com.ar')

@bot.message_handler(commands=['help'])
def command_ayuda(m):
    cid = m.chat.id
    bot.send_message( cid, "Comandos Disponibles:\n /help\n /acerca\n /support\n /search\n") #

@bot.message_handler(commands=['support'])
def command_help(message):
    markup = types.InlineKeyboardMarkup()
    itembtnneo = types.InlineKeyboardButton('NeoRanger', url="telegram.me/NeoRanger")
    itembtnrepo = types.InlineKeyboardButton('Repo Github', url="http://github.com/neoranger/NeoBot")
    markup.row(itembtnneo)
    markup.row(itembtnrepo)
    bot.send_message(message.chat.id, "Choose one supporter:", reply_markup=markup)

@bot.message_handler(commands=['search'])
def command_search(m):
    cid = m.chat.id
    busqueda = 'http://www.infosertec.com.ar/search/%s/feed/rss'
    
    if len(m.text.split()) >= 2:
        palabras = m.text.split()
        palabras.pop(0)
        a_buscar = '+'.join(palabras)
        url = (busqueda % a_buscar)
        bot.send_message(cid, get_feed(url),disable_web_page_preview=True,parse_mode="markdown")
    else:
        bot.send_message( cid, "No hay argumento. Tenes que usar /search (busqueda)" )
        
###############################################################################
print('Functions loaded')
