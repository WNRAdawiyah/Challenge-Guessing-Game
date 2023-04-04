#!/usr/bin/env python

import random

def main():
    """Start a Taylor Swift's song guessing game."""
    print("Lets guess a Taylor Swift's song!")
    
    song = [
        "Shake it Off",
        "Blank Space",
        "Enchanted",
        "Anti-Hero",
        "Love Story",
        "Bejeweled",
        "Me",
        "Bad Blood"
        ]
    
    x = random.choice(song)
    print(x)
    guess = None
    
    while x != guess:
        
        guess = str(input("What Taylor Swift's song am I thinking of? "))
        
        if x == guess:
            print("You guessed {}. Congratulations you nailed it!".format(guess))
            break
        else:
            print("You guessed {}. Unfortunately you got it wrong. Please try again!".format(guess))
            
main()