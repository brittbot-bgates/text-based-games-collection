#!/usr/bin/env python3
from modules.clear_screen import clear_screen
from modules.sleep_print import sleep_print
from sys import exit
import random


def play_again():
    """
    Takes an `int` and asks the player to play the game again.
    :return: The player plays the game again or goes back to the menu.
    """
    clear_screen()
    play_game_again = int(input("Do you want to play again?\n1) Yes\n2) No\nEnter choice here: "))
    if play_game_again == 1:
        clear_screen()
        guess_the_number()
    elif play_game_again == 2:
        clear_screen()
        print("\n** Thanks for playing! **")
        exit()
    else:
        print("Invalid choice.")
        sleep_print()
        clear_screen()
        play_again()


def guess_the_number():
    """
    Takes an `int` from the player to determine their choice and compares it to the random choice to determine
    the winner.
    :return: The winner of the match.
    """
    clear_screen()
    print("*" * 40)
    print("-- Guess The Number --")
    print("\nRules:\nGuess the number (1 - 500) within 5 tries.")
    print("*" * 40)

    tries = 5
    random_number = random.randint(1, 500)

    try:
        player_guess = int(input("\nTries Left = {}\nWhat's your guess?\nEnter it here: ".format(tries)))
        while tries > 1:
            if player_guess == random_number and tries == 5:
                print("\n** Whoa! You guess the number on the first try! **")
                sleep_print()
                play_again()
                break
            elif player_guess == random_number:
                print("\n** Woo hoo! You guess the number in {} tries ** ".format(tries))
                sleep_print()
                play_again()
                break
            elif player_guess != random_number and player_guess > random_number:
                print("\nThat guess is incorrect. Try a lower number.")
                tries -= 1
                player_guess = int(input("\nTries Left = {}\nWhat's your guess?\nEnter it here: ".format(tries)))
            elif player_guess != random_number and player_guess < random_number:
                print("\nThat guess is incorrect. Try a higher number.")
                tries -= 1
                player_guess = int(input("\nTries Left = {}\nWhat's your guess?\nEnter it here: ".format(tries)))

        if player_guess == random_number and tries == 1:
            print("\n** Whew! You guess the number with your final try! ** ".format(tries))
            sleep_print()
            play_again()
        elif tries == 1:
            print("\n!! Game Over !!\nThe number was {}\nBetter luck next time.".format(random_number))
            sleep_print()
            play_again()
    except ValueError:
        print("That's not a number. Enter a number between 1 and 500.")
        sleep_print()
        clear_screen()
        guess_the_number()
