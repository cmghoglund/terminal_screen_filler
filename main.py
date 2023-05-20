# Toy program to fill terminal screen with random characters

import os
import random
import sys
import functions

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def fill_screen():
    columns, rows = os.get_terminal_size()
    lines = []
    for _ in range(rows):
        # Randomly fill each line with '0's or '1's
        line = ''.join(str(random.randint(0, 1)) for _ in range(columns))
        lines.append(line)
    return lines

def print_screen(lines):
    for line in lines:
        print(line)

def main():
    while True:
        clear_screen()
        lines = fill_screen()
        print_screen(lines)
        print("\nPress any key to redraw screen, or 'q' to quit.\n")
        pressed_key = functions.get_pressed_key().lower()
        if pressed_key == 'q':
            sys.exit()

if __name__ == '__main__':
    main()
