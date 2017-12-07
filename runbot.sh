#!/bin/bash
while true
do
python3 /home/pi/Documents/git/neobot/neobot.py
echo "¡The bot is crashed!"
echo "Rebooting in:"
for i in 1
do
echo "$i..."
done
echo "###########################################"
echo "#Bot is restarting now                    #"
echo "###########################################"
done
