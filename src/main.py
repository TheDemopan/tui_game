import curses
import curses.panel
from game import Game
from hud import draw_hud
from sidebar import draw_sidebar

def game_loop(stdscr):
    curses.curs_set(0)  # Hide cursor
    stdscr.nodelay(True)  # Non-blocking input

    max_y, max_x = stdscr.getmaxyx()
    sidebar_width = max_x // 4
    terminal_height = max_y // 4
    game_height = max_y - terminal_height
    game_width = max_x - sidebar_width

    # Create the windows
    sidebar_win = curses.newwin(game_height, sidebar_width, 0, 0)
    game_win = curses.newwin(game_height, game_width, 0, sidebar_width)
    terminal_win = curses.newwin(terminal_height, max_x, game_height, 0)

    # Create panels for layering
    sidebar_panel = curses.panel.new_panel(sidebar_win)
    game_panel = curses.panel.new_panel(game_win)
    terminal_panel = curses.panel.new_panel(terminal_win)

    # Initialize game
    game = Game(game_win)

    game.player.add_item("Battery")
    game.player.add_item("Wire")
    game.player.add_item("Battery")  # Adds a second "Battery"


    while True:
        key = stdscr.getch()
        if key == ord('q'):
            break
        
        elif key == ord('e'):
            game.place_allocator()
        
        elif key == ord('r'):
            game.remove_allocator()

        game.move_player(key)

        # Clear and redraw each section
        sidebar_win.erase()
        terminal_win.erase()
        game_win.erase()

        draw_sidebar(sidebar_win, game.player)
        draw_hud(terminal_win, game.player.x, game.player.y)  # Draw HUD
        game.draw()  # Draw game state

        # Refresh each window
        sidebar_win.refresh()
        terminal_win.refresh()
        game_win.refresh()

        # Update panels and refresh the screen
        curses.panel.update_panels()
        stdscr.refresh()

curses.wrapper(game_loop)
