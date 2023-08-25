import random
from wordsForHangman import words
import string
from hangman_visual import lives_visual_dict

def get_vaild_word(words):
    word = random.choice(words)
    while ('-' in word) or (' ' in word):
        word = random.choice(words)
    return word.upper()

def hangman():
    lives = 6
    word = get_vaild_word(words)
    word_letters = set(word) # letters in word
    alphabetS = set(string.ascii_uppercase) # all 26 capital alphabets 
    used_letters = set() # what user has guessed
    
    while len(word_letters) > 0 and lives > 0:
        #Used letters
        #' '.join(['a','b','c']) --> 'a b c'
        print("You have",lives, " lives left and You have used these letters: ",' '.join(used_letters)) #letters used
        
        #what currect word is i.e.[W - R D]
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(lives_visual_dict[lives])
        print("Current word ", ''.join(word_list))

        # getting User input
        input_letter = input("\nGuess a letter: ")

        if input_letter in alphabetS - used_letters:
            used_letters.add(input_letter)
            if input_letter in word_letters:
                word_letters.remove(input_letter)
                print('')
            
            else:
                lives = lives - 1 # takes away life if wrong
                print("\nYour letter ", input_letter, "is not in the wrod")
        
        elif input_letter in used_letters:
            print("\nYou have already guessed the ", input_letter, ". Please try again")
        else:
            print("\nInvalied input. Please try again")
    
    #comes here when word_letters == 0 or when lives ==0
    if lives == 0:
        print(lives_visual_dict[lives])
        print("You are dead, sorry, the word is ", word)
    else:
        print("Yahu! You gussed the word ", word,"!!")
hangman()
