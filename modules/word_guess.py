#!/usr/bin/env python3
from sys import exit
from random import choice
from modules.clear_screen import clear_screen
from modules.sleep_print import sleep_print
from modules.words import word_dict


def play_again() -> None:
    """
    Takes an `int` and asks the player to play the game again. The player plays the game again or exits the program.
    :return: None
    """
    clear_screen()
    play_game_again = int(input("Do you want to play again?\n1) Yes\n2) No\nEnter choice here: "))
    if play_game_again == 1:
        clear_screen()
        word_guess()
    elif play_game_again == 2:
        print("\n** Thanks for playing! **")
        exit()
    else:
        print("Invalid choice.")
        sleep_print()
        clear_screen()
        play_again()


def word_guess() -> None:
    """
    Takes a `str` from the player and compares it to randomly chosen word.
    :return: None
    """
    clear_screen()
    print("*" * 40)
    print("-- Word Guess --")
    print("\nRules:\nYou have three tries to guess the word.\nDon't worry about case sensitivity."
          "\nType 'quit' to quit.")
    print("*" * 40)

    tries = 3

    # Convert the dictionary into a list to choose a random entry
    dict_list = list(word_dict.items())
    random_pair = choice(dict_list)
    word = random_pair[0]
    hint = ""

    # To display the hint in the game which is always at index 1
    for value in random_pair:
        hint = random_pair[1]

    print("\nTries left = {}".format(tries))
    print("\nGet ready to guess in 3...2...1")
    sleep_print()
    clear_screen()
    print("Your hint: {}".format(hint))
    # Show the number of letters in the word to guess
    print("Number of letters in the word: {}".format(len(word)))

    try:
        while tries > 0:
            player_guess = input("\nWhat's your guess? Enter it here: ").lower()
            if player_guess == "quit":
                print("\n** Thanks for playing! **")
                exit()
            elif player_guess == word:
                print("** Congrats! You guessed the word in {} tries! **".format(tries))
                sleep_print()
                clear_screen()
                play_again()
            elif player_guess != word:
                tries -= 1
                print("That's not the word. Try again.\nTries left: {}".format(tries))
        if tries == 0:
            print("\nGame Over. The word was {}.".format(word))
            sleep_print()
            clear_screen()
            play_again()
    except ValueError:
        print("Only words are accepted.")
        sleep_print()
        clear_screen()
        word_guess()
