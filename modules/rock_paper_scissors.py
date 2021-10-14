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
        rock_paper_scissors()
    elif play_game_again == 2:
        print("\n** Thanks for playing! **")
        exit()
    else:
        print("Invalid choice.")
        sleep_print()
        clear_screen()
        play_again()


def rock_paper_scissors():
    """
    Takes an `int` from the player to determine their choice and compares it to the computer's choice to determine
    the winner.
    :return: A string showing the winner of the match.
    """
    clear_screen()
    print("*" * 40)
    print("-- Rock, Paper, Scissors --")
    print("\nRules:\nRock crushes Scissors\nScissors cuts Paper\nPaper covers Rock.")
    print("*" * 40)

    rock = 1
    paper = 2
    scissors = 3

    # Determine the computer's choice via random number
    random_number = random.randint(1, 3)
    computer_choice = ""
    if random_number == rock:
        computer_choice = rock
    elif random_number == paper:
        computer_choice = paper
    else:
        computer_choice = scissors

    try:
        player_choice = int(input("\nWhat's your choice?\n1) Rock\n2) Paper\n3) Scissors\nEnter choice here: "))
        if player_choice == 1:
            player_choice = rock
        elif player_choice == 2:
            player_choice = paper
        elif player_choice == 3:
            player_choice = scissors
        else:
            print("Invalid choice.")
            sleep_print()
            clear_screen()
            rock_paper_scissors()

        # Determine the winning by comparing the choices
        if computer_choice == player_choice:
            print("\nIt's a tie!\n¯\\_(ツ)_/¯")
            sleep_print()
            play_again()
        elif computer_choice == rock and player_choice == scissors:
            print("\nComputer chooses Rock")
            print("Rock crushes Scissors.\nYOU LOSE!\nಥ_ಥ")
            sleep_print()
            play_again()
        elif computer_choice == paper and player_choice == rock:
            print("\nComputer chooses Paper")
            print("Paper covers Rock.\nYOU LOSE!\nಥ_ಥ")
            sleep_print()
            play_again()
        elif computer_choice == scissors and player_choice == paper:
            print("\nComputer chooses Scissors")
            print("Scissors cuts Paper.\nYOU LOSE!\nಥ_ಥ")
            sleep_print()
            play_again()
        elif player_choice == rock and computer_choice == scissors:
            print("\nComputer chooses Scissors")
            print("Rock crushes Scissors.\nYOU WIN!\nヽ(´▽`)/")
            sleep_print()
            play_again()
        elif player_choice == paper and computer_choice == rock:
            print("\nComputer chooses Rock")
            print("Paper covers Rock.\nYOU WIN!\nヽ(´▽`)/")
            sleep_print()
            play_again()
        elif player_choice == scissors and computer_choice == paper:
            print("\nComputer chooses Paper")
            print("Scissors cuts Paper.\nYOU WIN!\nヽ(´▽`)/")
            sleep_print()
            play_again()
    except ValueError:
        print("\nThat's not a number. Enter either 1, 2, or 3.")
        sleep_print()
        clear_screen()
        rock_paper_scissors()

    if play_again():
        rock_paper_scissors()
