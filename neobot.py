# -*- coding: utf-8 -*-
import functions
#import download_function

#Listener
def listener(messages):
    for m in messages:
        cid = m.chat.id
        if m.content_type == 'text':
            print ("[" + str(cid) + "]: " + m.text)
 
functions.bot.set_update_listener(listener)
#############################################

#Bot starts here
print('Bot Started')
functions.bot.polling(none_stop=True)
#download_funtion.polling(none_stop=True)
