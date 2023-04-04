import random

def main():
    """Start a music genre guessing game."""
    print("Guess the music genre!")
    
    genre = [
        "rock",
        "hip hop",
        "jazz",
        "pop",
        "heavy metal",
        "blues",
        "indie rock"
        ]
    
    x = random.choice(genre)
    print(x)
    guess = None
    
    while x != guess:
        
        guess = str(input("What genre am I thinking of? "))
        
        if x == guess:
            print("You guessed {}. Congratulations you got it right!".format(guess))
            break
        else:
            print("You guessed {}. Unfortunately you got the wrong answer. Please try again!".format(guess))
            
main()