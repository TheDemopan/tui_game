import curses
from player import Player
import building

class Game:
    def __init__(self, game_win):
        self.game_win = game_win
        self.max_y, self.max_x = game_win.getmaxyx()
        self.player = Player(self.max_x // 2, self.max_y // 2)
        self.building = building(self.game_win, 5, 5, 3, 3, 0)  # Example building with rotation 0 (north)

        # Define walls
        self.walls = {(5, 10), (5, 11), (5, 12), (6, 10), (7, 10)}

    def draw(self):
        """Draw game environment, walls, and player."""
        self.game_win.erase()
        self.game_win.border()

        # Draw walls
        for (y, x) in self.walls:
            self.game_win.addch(y, x, '#')
        
        building.draw(building, self.game_win)

        # Draw player (delegated to Player class)
        self.player.draw(self.game_win)

        self.game_win.refresh()

    def move_player(self, key):
        """Move player while preventing wall collisions."""
        self.player.move(key, self.walls, self.max_x, self.max_y)
