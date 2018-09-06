#!/bin/bash
while true
do
python2 /home/pi/Documents/git/neobot/neobot.py
echo "¡The bot is crashed!"
#echo "NeoBot is crashed" | mail -s "Aviso" elgranpote@gmail.com
echo "Rebooting in:"
for i in 1
do
echo "$i..."
done
echo "###########################################"
echo "#NeoBot is restarting now                 #"
echo "###########################################"
done
