import curses

def draw_hud(terminal_win, player_x, player_y):
    """Draws the HUD inside the terminal window."""
    terminal_win.erase()
    terminal_win.border()
    terminal_win.addstr(1, 1, f"Player Position: ({player_x}, {player_y})", curses.A_BOLD)
    terminal_win.addstr(2, 1, "Use arrow keys to move, 'q' to quit.")
    terminal_win.refresh()
