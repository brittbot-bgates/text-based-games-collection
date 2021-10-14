#!/usr/bin/env python3
from os import system, name


def clear_screen():
    """
    Clears the screen/terminal using commands depending on the player's operating system.
    :return: None
    """
    # Windows OS
    if name == "nt":
        _ = system("clear")
    # MacOS & Linux OS
    else:
        _ = system("clear")
