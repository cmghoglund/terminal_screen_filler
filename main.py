# Toy program to fill terminal screen with random characters

import os
import random
import sys
import msvcrt

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def fill_screen():
    columns, lines = os.get_terminal_size()
    for _ in range(lines):
        # Randomly fill each line with '0' or '1'
        line = ''.join(str(random.randint(0, 1)) for _ in range(columns))
        print(line)

def main():
    while True:
        clear_screen()
        fill_screen()
        print("\nPress any key to redraw screen, or 'q' to quit.\n")
        key = msvcrt.getch().decode('utf-8').lower()
        if key == 'q':
            sys.exit()

if __name__ == '__main__':
    main()
