import tkinter as tk
import random

# Define the game window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Create the player object
class Player:
    def __init__(self, canvas):
        self.canvas = canvas
        self.id = self.canvas.create_rectangle(50, WINDOW_HEIGHT - 50, 100, WINDOW_HEIGHT - 100, fill="blue")
        self.x_velocity = 0
        self.y_velocity = 0
        self.is_jumping = False
        self.canvas.bind_all("<KeyPress-w>", self.jump)
        self.canvas.bind_all("<KeyPress-a>", self.move_left)
        self.canvas.bind_all("<KeyPress-d>", self.move_right)

    def update(self):
        self.x_velocity = max(-5, min(5, self.x_velocity))
        self.y_velocity += 1
        self.canvas.move(self.id, self.x_velocity, self.y_velocity)
        pos = self.canvas.coords(self.id)
        if pos[3] >= WINDOW_HEIGHT:
            self.y_velocity = 0
            self.is_jumping = False
            self.canvas.move(self.id, 0, WINDOW_HEIGHT - pos[3])
        if pos[0] <= 0 or pos[2] >= WINDOW_WIDTH:
            self.x_velocity = 0
            self.canvas.move(self.id, -self.x_velocity, 0)
        if self.is_jumping:
            if self.y_velocity < 0:
                self.is_jumping = False
            elif self.y_velocity > 0:
                for platform in platforms:
                    if platform.is_colliding(pos):
                        self.is_jumping = False
                        break

    def jump(self, event):
        if not self.is_jumping:
            self.is_jumping = True
            self.y_velocity = -20

    def move_left(self, event):
        self.x_velocity -= 2

    def move_right(self, event):
        self.x_velocity += 2

# Create the platform object
class Platform:
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.id = self.canvas.create_rectangle(x, y, x + 200, y + 25, fill="red")

    def is_colliding(self, bbox):
        overlapping_items = self.canvas.find_overlapping(*bbox)
        return len(overlapping_items) > 1

# Create the game canvas
root = tk.Tk()
root.title("2D Platformer")
canvas = tk.Canvas(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg="white")
canvas.pack()

# Create the player and platforms
player = Player(canvas)
platforms = []
for i in range(5):
    x = random.randint(0, WINDOW_WIDTH - 200)
    y = random.randint(50, WINDOW_HEIGHT - 150)
    platforms.append(Platform(canvas, x, y))

# Main game loop
while True:
    player.update()
    root.update()
    tk.Canvas.delete(canvas, tk.ALL)
    canvas.create_rectangle(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT, fill="white")
    canvas.create_text(WINDOW_WIDTH - 50, 20, text="Score: 0", anchor=tk.NE)
    for platform in platforms:
        canvas.move(platform.id, 0, 0.5)
        if canvas.coords(platform.id)[3] > WINDOW_HEIGHT:
            x = random.randint(0, WINDOW_WIDTH - 200)
            y = random.randint(-200, -50)
            canvas.move(platform.id, x - canvas.coords(platform.id)[0], y - canvas.coords
