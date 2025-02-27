import curses

class Building:
    def __init__(self, game_win, x, y, width, height, rotation):
        self.game_win = game_win
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rotation = rotation
    
    def draw(self, game_win):
        """Draw the building."""
        for int in range(self.width):
            for jnt in range(self.height):
                if self.rotation == 0:
                    game_win.addch(self.y + jnt, self.x + int, "#")
                elif self.rotation == 90:
                    game_win.addch(self.y + self.height - int - 1, self.x + jnt, "#")
                elif self.rotation == 180:
                    game_win.addch(self.y + self.height - jnt - 1, self.x + self.width - int - 1, "#")
                elif self.rotation == 270:
                    game_win.addch(self.y + int, self.x + self.width - jnt - 1, "#")