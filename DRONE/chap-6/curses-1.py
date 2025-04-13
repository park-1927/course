import curses
import random
import time


def game_over():
    screen = curses.initscr()
    width = screen.getmaxyx()[1]
    height = screen.getmaxyx()[0]
    size = width * height
    char = [" ", ".", ":", "^", "*", "x", "s", "S", "#", "$"]
    b = []

    curses.curs_set(0)
    curses.start_color()
    curses.init_pair(1, 0, 0)
    curses.init_pair(4, 1, 0)
    curses.init_pair(3, 6, 0)
    curses.init_pair(2, 4, 0)
    screen.clear()

    for i in range(size + width + 1):
        b.append(0)

    while True:
        for i in range(int(width / 9)):
            b[int((random.random() * width) + width * (height - 1))] = 65
        for i in range(size):
            b[i] = int((b[i] + b[i + 1] + b[i + width] + b[i + width + 1]) / 4)
            color = (4 if b[i] > 15 else (3 if b[i] > 9 else (2 if b[i] > 4 else 1)))
            if i < size - 1:
                screen.addstr(int(i / width), i % width, char[(9 if b[i] > 9 else b[i])],
                              curses.color_pair(color) | curses.A_BOLD)

        screen.refresh()
        screen.timeout(30)
        if screen.getch() != -1: break

    curses.endwin()


def draw_title(stdscr, start_y, start_x):
    title = [
        "        ,----,",
        "      ,/   .`|",
        "    ,`   .'  :",
        "  ;    ;     /                    ,--,",
        ".'___,/    ,' __  ,-.           ,--.'|         ,---,",
        "|    :     |,' ,'/ /|           |  |,      ,-+-. /  |",
        ";    |.';  ;'  | |' | ,--.--.   `--'_     ,--.'|'   |",
        "`----'  |  ||  |   ,'/       \  ,' ,'|   |   |  ,\"' |",
        "    '   :  ;'  :  / .--.  .-. | '  | |   |   | /  | |",
        "    |   |  '|  | '   \__\/: . . |  | :   |   | |  | |",
        "    '   :  |;  : |   ,\" .--.; | '  : |__ |   | |  |/",
        "    ;   |.' |  , ;  /  /  ,.  | |  | '.'||   | |--'",
        "    '---'    ---'  ;  :   .'   \;  :    ;|   |/",
        "                   |  ,     .-./|  ,   / '---'",
        "                    `--`---'     ---`-'       "
    ]
    for i, line in enumerate(title):
        try:
            stdscr.addstr(start_y + i, start_x, line)
        except curses.error:
            pass

    return title


def draw_menu(stdscr, selected_row_idx, start_y, start_x):
    menu_items = ['Continue', 'New Game', 'Settings', 'Quit']
    menu_width = 20
    for idx, item in enumerate(menu_items):
        x = start_x + (menu_width - len(item)) // 2
        y = start_y + idx
        if idx == selected_row_idx:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, item)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, item)

    # Draw menu border
    stdscr.box()
    stdscr.addch(start_y - 1, start_x - 1, curses.ACS_ULCORNER)
    stdscr.addch(start_y - 1, start_x + 20, curses.ACS_URCORNER)
    stdscr.addch(start_y + 4, start_x - 1, curses.ACS_LLCORNER)
    stdscr.addch(start_y + 4, start_x + 20, curses.ACS_LRCORNER)
    for i in range(4):
        stdscr.addch(start_y + i, start_x - 1, curses.ACS_VLINE)
        stdscr.addch(start_y + i, start_x + 20, curses.ACS_VLINE)
    for i in range(menu_width):
        stdscr.addch(start_y - 1, start_x + i, curses.ACS_HLINE)
        stdscr.addch(start_y + 4, start_x + i, curses.ACS_HLINE)

    # draw_road(stdscr, start_y + len(menu_items), start_x, menu_width)


def draw_road(stdscr, y, x, menu_width):
    height, width = stdscr.getmaxyx()
    line_length = int(width * 0.4)

    road_start_x = x - (line_length - menu_width) // 2
    road_end_x = road_start_x + line_length

    for i in range(3):
        stdscr.addch(y + i, road_start_x + i, '\\')

    for i in range(3):
        stdscr.addch(y + i, road_end_x - i - 1, '/')


def new_game(stdscr, title, start_y, start_x):
    height, width = stdscr.getmaxyx()
    title_height = len(title)

    for i in range(title_height + start_y + 20):
        stdscr.clear()
        stdscr.box()
        for j, line in enumerate(title):
            y = start_y + title_height - i + j
            if 0 <= y < height:
                try:
                    stdscr.addstr(y, start_x, line)
                except curses.error:
                    pass
        stdscr.refresh()
        time.sleep(0.1)


def main(stdscr):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    selected_row_idx = 0

    while True:
        stdscr.clear()
        height, width = stdscr.getmaxyx()

        title_start_y = height // 10
        title_start_x = (width - 50) // 2  # 96 is the width of the title ASCII art

        # menu_start_y = title_start_y + 10
        menu_start_y = int(height // 1.3)
        menu_start_x = (width - 20) // 2

        # draw_title(stdscr, title_start_y, title_start_x)
        title = draw_title(stdscr, title_start_y, title_start_x)
        draw_menu(stdscr, selected_row_idx, menu_start_y, menu_start_x)

        key = stdscr.getch()

        if key == curses.KEY_UP and selected_row_idx > 0:
            selected_row_idx -= 1
        elif key == curses.KEY_DOWN and selected_row_idx < 3:
            selected_row_idx += 1
        elif key == 10:  # Enter key
            if selected_row_idx == 1:
                new_game(stdscr, title, title_start_y + 20, title_start_x)
            elif selected_row_idx == 2:
                game_over()
                break
            elif selected_row_idx == 3:  # Quit option
                break
            # Here you would typically handle other menu options

        stdscr.refresh()


curses.wrapper(main)