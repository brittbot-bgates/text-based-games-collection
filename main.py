#!/usr/bin/env python3
"""
Title: Text Games Collection
Creator: Brittany Gates (https://github.com/brittbot-bgates)
About: A collection of text-based games:
- Rock, Paper, Scissors
"""
from modules.sleep_print import sleep_print
from modules.clear_screen import clear_screen
from sys import exit
from modules.rock_paper_scissors import rock_paper_scissors
from modules.guess_the_number import guess_the_number


def main():
    """
    The menu for the game.
    :return: The specified game chosen by the player.
    """
    print("*" * 40)
    print(" -- Text Games Collection -- ")
    print("\nEnter \"0\" to quit.")
    print("\nGames:\n1) Rock, Paper, Scissors\n2) Guess The Number")
    print("*" * 40)

    game_choice = int(input("Your Choice: "))

    if game_choice == 0:
        print("Thanks for playing!")
        exit()
    elif game_choice == 1:
        rock_paper_scissors()
    elif game_choice == 2:
        guess_the_number()
    else:
        print("Invalid choice.")
        sleep_print()
        clear_screen()
        main()


if __name__ == '__main__':
    main()
