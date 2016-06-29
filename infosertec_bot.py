# -*- coding: utf-8 -*-
import functions

#Bot for www.inforsertec.com.ar
#Developed by NeoRanger (Natanael Andrés Garrido)
#Web: www.neositelinux.com.ar

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
print('Bot for www.inforsertec.com.ar')
print('Developed by NeoRanger (Natanael Andrés Garrido)')
print('Web: www.neositelinux.com.ar')
functions.bot.polling(none_stop=True)
