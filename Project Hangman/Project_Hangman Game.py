#!/usr/bin/env python
# coding: utf-8

# HANGMAN GAME

# In[2]:


import random
import json
def hangman():
    data=json.load(open("data.json"))
    word = random.choice(list(data.keys()))
    word=word.lower()
    validLetters = 'abcdefghijklmnopqrstuvwxyz'
    turns = 10
    guessmade = ''

    while len(word) > 0:
        main = ""
        missed = 0
        count=0
        for letter in word:
            if letter in guessmade:
                count+=1
                main = main + letter + " "
                if count==len(word):
                    main="".join(main.split())                            #split() method split the string by seperating the string by whitespaces
            else:                                                         #"".join() method  
                main = main + "_" + " "
        if main == word:
            print(main)
            print("You win!")
            break
        print("Guess the word:" , main)
        guess = input()

        if guess in validLetters:
            guessmade = guessmade + guess
        else:
            print("Enter a valid character")
            guess = input()

        if guess not in word:
            turns = turns - 1
            if turns == 9:
                print("9 turns left")
                print("  --------  ")
            if turns == 8:
                print("8 turns left")
                print("  --------  ")
                print("     O      ")
            if turns == 7:
                print("7 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
            if turns == 6:
                print("6 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
                print("    /       ")
            if turns == 5:
                print("5 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
                print("    / \     ")
            if turns == 4:
                print("4 turns left")
                print("  --------  ")
                print("   \ O      ")
                print("     |      ")
                print("    / \     ")
            if turns == 3:
                print("3 turns left")
                print("  --------  ")
                print("   \ O /    ")
                print("     |      ")
                print("    / \     ")
            if turns == 2:
                print("2 turns left")
                print("  --------  ")
                print("   \ O /|   ")
                print("     |      ")
                print("    / \     ")
            if turns == 1:
                print("1 turns left")
                print("Last breaths counting, Take care!")
                print("  --------  ")
                print("   \ O_|/   ")
                print("     |      ")
                print("    / \     ")
            if turns == 0:
                print("You loose, The word was {0}".format(word))
                print("You let a kind man die")
                print("  --------  ")
                print("     O_|    ")
                print("    /|\      ")
                print("    / \     ")
                break


print("Welcome to Hangman, Fate lies in your action !")
print("-------------------")
print("try to guess the word in less than 10 attempts")
hangman()
print()



# In[ ]:




