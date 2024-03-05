from pygame import *
from cmu_graphics import *

app.stepsPerSecond = 10
app.timer = Label("timer " + str(1), 40, 40, size=20)
app.timer.count = 0
# app.paused = False

pause_label = Label("", 200, 200, size=30)

player = Group()
player.add(
    Rect(200, 200, 40, 40, fill="black", align="center")
)
player.health = 200
player.damage = 10
player.speed = 7
player.shield = 1
player.SurvivalTime = 100
player.kills = 0
hp = Rect(160, 40, 200, 20, fill="darkred")
score = Label("kills: " + str(player.kills), 40, 20, fill=rgb(255, 0, 0), bold=True, size=20)
enemy = Group()
enemy.add(
    Circle(200, -20, 20, fill="darkgreen")
)
enemies = Group()
for e in range(50, 351, 50):
    mob = Group()
    mob.add(Circle(e, 60, 20, fill="green"))
    mob.speed = randrange(2, 6, 1)
    enemies.add(
        mob
    )


# Pause menu function
# def pause_menu():
#     if app.paused == True:
#       # Draw the pause menu
#       pause_label.value = "Game Paused press p to resume"
#     else:
#       pause_label.value = ""

# Write your code here
# Not sure where to start?
# Check out README.md under "Files"
# def onKeyPress(key):

#  if key == 'p':# Pause the game when 'p' is pressed

# pause_menu()
# #if app.paused == False:
#   app.stepsPerSecond = 0
#   app.paused = True
# elif app.paused == True:
#   app.stepsPerSecond = 60
#   app.paused = False=
def onKeyHold(keys):
    if "right" in keys or "d" in keys:
        player.centerX += player.speed
    if "left" in keys or "a" in keys:
        player.centerX += -player.speed
    if "up" in keys or "w" in keys:
        player.centerY += -player.speed
    if "down" in keys or "s" in keys:
        player.centerY += player.speed


def onStep():
    app.timer.count += 1
    app.timer.value = "timer " + str(app.timer.count // 60)
    for e in enemies:
        # chase logic
        if e.centerY > player.centerY:
            e.centerY -= e.speed
        elif e.centerY < player.centerY:
            e.centerY += e.speed
        if e.centerX > player.centerX:
            e.centerX -= e.speed
        elif e.centerX < player.centerX:
            e.centerX += e.speed
        # hiting logic
        if e.hitsShape(player) and player.health > 0.6:
            player.health -= .1
            hp.width = player.health
            # function for pacman affect to make it shorter


def pacmanAffect(shape):
    # pac-man affect
    if (shape.top > 400):
        shape.bottom = 0
    if shape.bottom < 0:
        shape.top = 400
    if (shape.left > 400):
        shape.right = 0
    if (shape.right < 0):
        shape.left = 400


cmu_graphics.run()