import time
import sys
import os

def typewriter(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

os.system("cls" if os.name == "nt" else "clear")

lyrics = [
    "Yeah, I miss you",
    "You know it's true",
    "So, what if I call?",
    "And you pick up the phone?",
    "And I use this holiday to make my way to your ghost",
    "But, what if you're lonely?",
    "And you know I am too?",
    "And I get the chance to say",
    "\"I wish I didn't, but I miss you\"",
    "I miss you"
]

for i, line in enumerate(lyrics):

    delay = 0.07

    typewriter(line, delay=delay)

    if i == 2 or i == 3:
        time.sleep(3.0)
    elif i == 7:
        time.sleep(0.5)
    elif i == 8:
        time.sleep(3.0)
    else:
        time.sleep(4.0)