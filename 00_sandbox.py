import tkinter as tk
import turtle
# Define the initial coin count, the amount earned per click, and the earnings per second
coins = 0
per_click = 1
per_second = 0.25

# Define the initial cost of the upgrade and the upgrade per click value
upgrade_cost = 10
upgrade_per_click = 1

# Define the cost and ownership status of the Dragon Slayer Sword
sword_cost = 10000000
has_sword = False

# Define the cost and ownership status of the dragon
dragon_cost = 1000000000
has_dragon = False


def draw_dead_dragon():
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.pensize(2)
    t.fillcolor("brown")
    t.begin_fill()
    t.circle(50)
    t.end_fill()
    t.penup()
    t.goto(-30, -20)
    t.pendown()
    t.fillcolor("white")
    t.begin_fill()
    t.circle(10)
    t.end_fill()
    t.penup()
    t.goto(30, -20)
    t.pendown()
    t.fillcolor("white")
    t.begin_fill()
    t.circle(10)
    t.end_fill()
    t.penup()
    t.goto(-20, 10)
    t.pendown()
    t.fillcolor("red")
    t.begin_fill()
    t.circle(5)
    t.end_fill()
    t.penup()
    t.goto(20, 10)
    t.pendown()
    t.fillcolor("red")
    t.begin_fill()
    t.circle(5)
    t.end_fill()
    t.penup()
    t.goto(-40, -60)
    t.pendown()
    t.fillcolor("red")
    t.begin_fill()
    t.right(60)
    t.forward(60)
    t.right(60)
    t.forward(60)
    t.right(120)
    t.forward(60)
    t.end_fill()
    t.penup()
    t.goto(40, -60)
    t.pendown()
    t.fillcolor("red")
    t.begin_fill()
    t.left(60)
    t.forward(60)
    t.left(60)
    t.forward(60)
    t.left(120)
    t.forward(60)
    t.end_fill()
    turtle.done()

# Define the function for clicking the "earn" button
def earn_click():
    global coins, per_click
    coins += per_click
    coin_label.config(text="Coins: " + str("{:.2f}".format(coins)))

# Define the function for purchasing an upgrade
def buy_upgrade():
    global coins, per_click, upgrade_cost, upgrade_per_click
    if coins >= upgrade_cost:
        coins -= upgrade_cost
        per_click += upgrade_per_click
        coin_label.config(text="Coins: " + str("{:.2f}".format(coins)))
        per_click_label.config(text="Coins per click: " + str(per_click))
        upgrade_cost *= 1.1  # Increase the cost of the upgrade by 1.1 times
        upgrade_button.config(text="Buy Upgrade (Cost: " + str("{:.2f}".format(upgrade_cost)) + ")")


# Define the function for purchasing the Dragon Slayer Sword
def buy_sword():
    global coins, has_sword
    if coins >= sword_cost and not has_sword:
        coins -= sword_cost
        has_sword = True
        coin_label.config(text="Coins: " + str(coins))
        sword_button.config(text="Buy Dragon Slayer Sword (Owned)")
        dragon_button.config(state=tk.NORMAL)

# Define the function for purchasing the dragon
def buy_dragon():
    global coins, has_dragon
    if coins >= dragon_cost and has_sword and not has_dragon:
        coins -= dragon_cost
        has_dragon = True
        coin_label.config(text="Coins: " + str(coins))
        dragon_button.config(text="Defeat the Dragon")
        win_button.config(state=tk.NORMAL)

# Define the function for winning the game
def win_game():
    global coins
    coins += dragon_cost
    coin_label.config(text="Coins: " + str(coins))
    message_label.config(text="You have defeated the dragon and won the game!")
    win_button.config(state=tk.DISABLED)
    dragon_button.config(state=tk.DISABLED)
    draw_dead_dragon()


# Define the function for earning coins per second
def earn_second():
    global coins, per_second
    coins += per_second * per_click
    coin_label.config(text="Coins: " + str("{:.2f}".format(coins)))
    window.after(1000, earn_second)

# Set up the main window
window = tk.Tk()
window.title("Idle Game")

# Create the "earn" button
earn_button = tk.Button(window, text="Earn", command=earn_click)
earn_button.pack()

# Create the label for displaying the coin count
coin_label = tk.Label(window, text="Coins: " + str(coins))
coin_label.pack()

# Create the label for displaying the earnings per click
per_click_label = tk.Label(window, text="Coins per click: " + str(per_click))
per_click_label.pack()

# Create the upgrade button
upgrade_button = tk.Button(window, text="Buy Upgrade (Cost: " + str(upgrade_cost) + ")", command=buy_upgrade)
upgrade_button.pack()

# Create the Dragon Slayer Sword button
sword_button = tk.Button(window, text="Buy Dragon Slayer Sword (Cost: " + str(sword_cost) + ")", command=buy_sword)
sword_button.pack()

# Create the Dragon button
dragon_button = tk.Button(window, text="Buy the Dragon (Cost: " + str(dragon_cost) + ")", state=tk.DISABLED, command=buy_dragon)
dragon_button.pack()

# Create the win button
win_button = tk.Button(window, text="Defeat the Dragon", state=tk.DISABLED, command=win_game)
win_button.pack()

# Create the message label
message_label = tk.Label(window, text="")
message_label.pack()

# Start the earnings per second loop
window.after(1000, earn_second)

# Create a canvas
canvas = tk.Canvas(window, width=32, height=32)
canvas.pack(side=tk.LEFT)

# Draw a pixelated knight sprite
knight = canvas.create_rectangle(8, 8, 24, 24, fill="gray")
canvas.create_rectangle(10, 10, 22, 14, fill="black")
canvas.create_oval(10, 14, 14, 18, fill="black")
canvas.create_oval(18, 14, 22, 18, fill="black")
canvas.create_rectangle(10, 18, 22, 22, fill="black")

# Create a canvas
canvas2 = tk.Canvas(window, width=32, height=32)
canvas2.pack(side=tk.RIGHT)

# Draw a pixelated dragon sprite
head = canvas2.create_oval(8, 8, 24, 16, fill="green")
eye1 = canvas2.create_oval(11, 11, 13, 13, fill="white")
pupil1 = canvas2.create_oval(12, 12, 13, 13, fill="black")
eye2 = canvas2.create_oval(19, 11, 21, 13, fill="white")
pupil2 = canvas2.create_oval(20, 12, 21, 13, fill="black")
canvas2.create_polygon(8, 16, 24, 16, 16, 24, fill="green")
canvas2.create_oval(4, 20, 12, 28, fill="green")
canvas2.create_oval(20, 20, 28, 28, fill="green")

# Create a canvas
canvas4 = tk.Canvas(window, width=32, height=32)
canvas4.pack(side=tk.BOTTOM, pady=20)

# Draw a pixelated sword sprite
handle = canvas4.create_rectangle(12, 8, 20, 28, fill="brown")
blade = canvas4.create_polygon(8, 20, 24, 20, 20, 28, 12, 28, fill="gray")



# Start the main loop
window.mainloop()
