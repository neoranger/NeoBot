import telebot 
from telebot import types 
import time 
import datetime
import token
import user
import os
import sys
import json
from os.path import exists
import StringIO

TOKEN = token.token_id
bot = telebot.TeleBot(TOKEN) # Creating our bot object.

triggers = {}
tfile = "triggers.json"
ignored = []
separator = '/'
#user = [line.rstrip('\n') for line in open('user.txt','rt')]

def is_recent(m):
    return (time.time() - m.date) < 60

#Check if Triggers file exists.
if exists(tfile):
    with open(tfile) as f:
        triggers = json.load(f)
else:
    print("Triggers file not found, creating.")
    with open(tfile,'w') as f:
        json.dump({}, f)

#Function to add new Trigger - Response
def newTrigger(trigger, response):
    triggers[trigger.lower()] = response
    with open(tfile, "w") as f:
        json.dump(triggers, f)
    print("triggers file saved")
    
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

#Adds another trigger-response. ex: "/add Hi / Hi!! :DD"
@bot.message_handler(commands=['add'])
def add(m):
    cid = m.chat.id
    text = m.text[4:]
    print("Apending :" + text)
    try:
        i = text.rindex(separator)
        print("I value = " + str(i))
        tr = text[:i]
        re = text[i+1:]
        tr = trim(tr)
        re = trim(re)
        print("TR = [" + tr + "] - RE = [" + re + "]")
        newTrigger(tr,re)
        bot.send_message(cid, "Trigger Added: Trigger["+tr+"] - Response["+re+"]")
    except:
        bot.send_message(cid, "Bad Arguments.")

#Answers with the size of triggers.
@bot.message_handler(commands=['size'])
def size(m):
    cid = m.chat.id
    bot.send_message(cid, "Size of Triggers list = " + str(len(triggers)))

#Catch every message, for triggers :D
@bot.message_handler(func=lambda m: True)
def response(m):
    if(m.from_user.id in ignored):
        return
    print("Checking for triggers in Message [" + m.text + "]")
    for t in triggers:
        if t in m.text:
            bot.reply_to(m, triggers[t])
    pass
