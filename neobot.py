# -*- coding: utf-8 -*-
import functions

#Listener
def listener(messages):
    for m in messages:
        cid = m.chat.id
        title = m.chat.title
        if m.content_type == 'text':
            print ("[" + str(cid) + "]: " + m.text)
 
functions.bot.set_update_listener(listener)
#############################################

#Bot starts here
print('Bot Started')
functions.bot.polling(none_stop=True)
