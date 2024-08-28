#!/bin/bash
#Don't forget to "chmod +x bot.sh" 
while true; do
    python3 bot.py
    echo "Bot crashed. Restarting..."
    sleep 1  # Adjust sleep duration as needed
done
