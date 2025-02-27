import curses

def draw_sidebar(sidebar_win, player):
    sidebar_win.border()
    sidebar_win.addstr(1, 1, "Inventory", curses.A_BOLD)

    if not player.inventory:
        sidebar_win.addstr(3, 2, "(empty)")
    else:
        for idx, (item, count) in enumerate(player.inventory.items(), start=3):
            sidebar_win.addstr(idx, 2, f"{item}: {count}")

    sidebar_win.refresh()
