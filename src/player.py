import curses
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direction = ">"  # Default facing right
        self.inventory = {}  # Stores items as { 'item_name': count }

    def move(self, key, walls, max_x, max_y):
        """Move using WASD, rotate with arrow keys."""
        new_x, new_y = self.x, self.y

        if key == ord('w'):  # Move UP
            new_y -= 1
        elif key == ord('s'):  # Move DOWN
            new_y += 1
        elif key == ord('a'):  # Move LEFT
            new_x -= 1
        elif key == ord('d'):  # Move RIGHT
            new_x += 1
        elif key == curses.KEY_UP:  # Rotate UP
            self.direction = "^"
        elif key == curses.KEY_DOWN:  # Rotate DOWN
            self.direction = "v"
        elif key == curses.KEY_LEFT:  # Rotate LEFT
            self.direction = "<"
        elif key == curses.KEY_RIGHT:  # Rotate RIGHT
            self.direction = ">"

        # Prevent movement into walls
        if (new_y, new_x) not in walls and 1 <= new_y < max_y - 1 and 1 <= new_x < max_x - 1:
            self.x, self.y = new_x, new_y

    def add_item(self, item_name):
        """Adds an item to inventory, increasing count if it already exists."""
        if item_name in self.inventory:
            self.inventory[item_name] += 1
        else:
            self.inventory[item_name] = 1
    
    def remove_item(self, item_name):
        """Removes one of the given items from inventory."""
        if item_name in self.inventory:
            self.inventory[item_name] -= 1
            if self.inventory[item_name] <= 0:
                del self.inventory[item_name]

    def draw(self, game_win):
        """Draw the player body and face in the correct position."""
        game_win.addch(self.y, self.x, '&')  # Body

        # Face position
        if self.direction == "^":  # Face is above
            face_y, face_x = self.y - 1, self.x
        elif self.direction == "v":  # Face is below
            face_y, face_x = self.y + 1, self.x
        elif self.direction == "<":  # Face is left
            face_y, face_x = self.y, self.x - 1
        elif self.direction == ">":  # Face is right
            face_y, face_x = self.y, self.x + 1

        # Draw face if within bounds
        max_y, max_x = game_win.getmaxyx()
        if 1 <= face_x < max_x - 1 and 1 <= face_y < max_y - 1:
            game_win.addch(face_y, face_x, self.direction)
