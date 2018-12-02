import math
import check
import random

welcome = "welcome to Guess-The-Word Game"
info = "The word has {0} letters"
inst1 = "To quit: type bye"
inst2 = "Enter your guess - one letter: "
end = "bye"
feedback = "Good guess"
game_over = "You won. Game over. The word was {0}"
bad = "Bad guess"


def play(st):
    '''play consumes a string 
    and prompts the user to enter letters until the user wins the game 
    or says bye
    
    play(st): Str -> None
    
    Effects:
    *takes in user input until the user types in "bye" or
    wins the game by completing the function.
    
    Examples:
    start()
welcome to Guess-The-Word Game
The word has 8 letters
To quit: type bye
Enter your guess - one letter: r
Bad guess
Enter your guess - one letter: l
Bad guess
Enter your guess - one letter: i
Good guess
Enter your guess - one letter: l
Bad guess
Enter your guess - one letter: p
Bad guess
Enter your guess - one letter: t
Good guess
Enter your guess - one letter: e
Bad guess
Enter your guess - one letter: c
Good guess
Enter your guess - one letter: o
Good guess
Enter your guess - one letter: n
Good guess
Enter your guess - one letter: d
Bad guess
Enter your guess - one letter: s
Bad guess
Enter your guess - one letter: r
Bad guess
Enter your guess - one letter: f
Good guess
Enter your guess - one letter: i
Good guess
Enter your guess - one letter: l
Bad guess
Enter your guess - one letter: u
Good guess
You won. Game over. The word was function

start()
welcome to Guess-The-Word Game
The word has 5 letters
To quit: type bye
Enter your guess - one letter: c
Good guess
Enter your guess - one letter: s
Good guess
Enter your guess - one letter: l
Good guess
Enter your guess - one letter: a
Good guess
You won. Game over. The word was class
    '''
    ##body of play(st)
    print(welcome)
    print(info.format(len(st)))
    print(inst1)        
    listOfChars = list(st)
    letter = input(inst2)
    def removeAllGuess(letter,listOfChars):
        '''removeAllGuess takes in a user input and
        a list of characters and removes all the input
        characters from the list of characters
        
        removeAllGuess: None -> None'''
    ##body of removeAllGuess
        while letter in listOfChars:
            listOfChars.remove(letter) 
            
    while listOfChars != []:
        if letter == "bye":
            return        
        if letter in listOfChars:
            print(feedback)
            removeAllGuess(letter,listOfChars)
            if listOfChars != []:
                letter = input(inst2)
        else:
            print(bad)
            letter = input(inst2)
    print(game_over.format(st))    
   

## don't change the following function


def start():
    all_words=['programming', 'loops', 'list', 'testing', 'condition', 
               'string','recursion', 'function', 'class', 'file', 'input',
               'output']
    word = random.choice(all_words)
    play(word)

##Tests
    
check.set_input(["l","i","s","t"])
check.set_screen(["The word takes in 4 user inputs and ends the game!"])
check.expect("Q3T1",play("list"),None)

check.set_input(["bye"])
check.set_screen(["The user exits at the first go"])
check.expect("Q3T2",play("programming"),None)

check.set_input(["l","o","i","s","t"])
check.set_screen(["The word takes in 5 user inputs and ends the game!"])
check.expect("Q3T3",play("list"),None)

check.set_input(["l","o","o","p","s"])
check.set_screen(["the user guesses the word with one bad guess and wins!"])
check.expect("Q3T4",play("loops"),None)
