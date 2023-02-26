#! /bin/bash

echo "Would you like to play rock, paper, scissors?"
read answer
if [ $answer == "yes" ]
then 
   python3 rockpaperscissors.py
else
echo "That's too bad, maybe next time"
fi




