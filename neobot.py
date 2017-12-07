# -*- coding: utf-8 -*-
import functions

#Listener
def listener(messages):
    for m in messages:
        cid = m.chat.id
        title = u"m.chat.title"
        if m.content_type == 'text':
            print ("[" + title.encode("utf-8") + "]: " + m.text)
 
functions.bot.set_update_listener(listener)
#############################################

#Bot starts here
print('NeoBot Started')
print('Please visit us on www.neositelinux.com')
functions.bot.polling(none_stop=True)
