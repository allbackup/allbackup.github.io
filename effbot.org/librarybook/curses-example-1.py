# File: curses-example-1.py

import curses

text = [
    "a very simple curses demo",
    "",
    "(press any key to exit)"
]

# connect to the screen
screen = curses.initscr()

# setup keyboard
curses.noecho() # no keyboard echo
curses.cbreak() # don't wait for newline

# screen size
rows, columns = screen.getmaxyx()

# draw a border around the screen
screen.border()

# display centered text
y = (rows - len(text)) / 2

for line in text:
    screen.addstr(y, (columns-len(line))/2, line)
    y = y + 1

screen.getch()

curses.endwin()
