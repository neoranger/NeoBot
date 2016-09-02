# -*- coding: utf-8 -*-
import telebot
import time
import urllib
#import logging

API_TOKEN = token.token_id
bot = telebot.TeleBot(API_TOKEN)
admin = 5482488
bot.skip_pending=True

#logger = telebot.logger
#telebot.logger.setLevel(logging.DEBUG) # Outputs debug messages to console.

knownUsers = [] #todo: save these in a file, 
userStep = {}   #so they won't reset every time the bot restarts

def getUserStep(uid): 
	if uid in userStep:
		return userStep[uid]
	else: 
		knownUsers.append(uid)
		userStep[uid] = 0
		print "Nuevo usuario detectado que todavia no ha usado \"/start\""

def next_step_handler(uid):
	if uid not in userStep:
		userStep[uid] = 0
	return userStep[uid]

@bot.message_handler(commands=['start'])
def send_welcome(m):
	cid = m.chat.id
	if not cid in knownUsers:
		bot.send_message(cid, "Bienvenido " + m.from_user.first_name)
	if cid < 0:
		print str(m.chat.title) + " [" + "@" + str(m.from_user.username) + "]: " + m.text
		print str(m.chat.title) + " [" + str(m.from_user.first_name) + " - @" + str(m.from_user.username) + "]: " + m.text

	elif m.content_type == 'text' and cid > 0:
		print "[" + str(m.chat.id) + " - @" + str(m.from_user.username) + "]: " + m.text
		print str(m.chat.first_name) + " [" + str(m.chat.id) + "]: " + m.text

@bot.message_handler(commands=['cancelar'])
def command_cancelar(m):
	cid = m.chat.id
	uid = m.from_user.id

	if next_step_handler(cid) != 0:
		userStep[cid] = 0
		bot.send_chat_action(cid, 'typing')
		bot.send_message(cid, "Comando cancelado")

	else:
		bot.send_chat_action(cid, 'typing')
		bot.send_message(cid, "No hay nada que cancelar")


@bot.message_handler(commands=['descargar'])
def command_descargar(m):
	cid = m.chat.id
	if cid == admin:
		bot.send_chat_action(cid, 'typing')
		bot.send_message(cid, "Envia el archivo que quieras descargar")
		userStep[cid] = 'descargar'

	else:
		bot.send_chat_action(cid, 'typing')
		bot.send_message(cid, "No tienes permiso para hacer esto")


@bot.message_handler(func=lambda msg: next_step_handler(msg.chat.id) == 'descargar', content_types=['document'])
def step_descargar(m):
	cid = m.chat.id
	userStep[cid] = 0
	name = m.document.file_name
	info = bot.get_file(m.document.file_id)
	bot.send_chat_action(cid, 'typing')
	bot.send_message(cid, "Descargando: " + name)
	downloaded_file = bot.download_file(info.file_path)
	with open(name, 'wb') as new_file:
		new_file.write(downloaded_file)
	bot.send_chat_action(cid, 'typing')
	bot.send_message(cid, "Descarga completada")


@bot.message_handler(commands=['descargar_link'])
def command_descargar_link(m):
	cid = m.chat.id
	if cid == admin:
		bot.send_chat_action(cid, 'typing')
		bot.send_message(cid, "Envia el link que quieras descargar")
		userStep[cid] = 'descargar_link'

	else:
		bot.send_chat_action(cid, 'typing')
		bot.send_message(cid, "No tienes permiso para hacer esto")


@bot.message_handler(func=lambda msg: next_step_handler(msg.chat.id) == 'descargar_link', content_types=['text'])
def step_descargar_link(m):
	cid = m.chat.id
	userStep[cid] = 0
	url = m.text
	slashes = url.count ('/')
	name = url.split("/")[slashes]
	bot.send_chat_action(cid, 'typing')
	bot.send_message(cid, "Descargando: " + name)
	urllib.urlretrieve(url, name)
	bot.send_chat_action(cid, 'typing')
	bot.send_message(cid, "Descarga completada")

###############################################################################
print('Download Functions loaded')

