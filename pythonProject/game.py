import turtle
import random
import math

# Screen setup
turtle.setup(width=800, height=600)
turtle.bgcolor("black")
turtle.title("Space Shooter Game")

# Player setup
player = turtle.Turtle()
player.shape("triangle")
player.color("white")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)
player_speed = 20

# Player bullet setup
bullet = turtle.Turtle()
bullet.shape("triangle")
bullet.color("yellow")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(stretch_wid=0.5, stretch_len=0.5)
bullet.hideturtle()
bullet_speed = 30

# Asteroid setup
num_asteroids = 5
asteroids = []

for _ in range(num_asteroids):
    asteroid = turtle.Turtle()
    asteroid.shape("square")
    asteroid.color("red")
    asteroid.penup()
    asteroid.speed(0)
    x = random.randint(-380, 380)
    y = random.randint(100, 250)
    asteroid.setposition(x, y)
    asteroids.append(asteroid)

asteroid_speed = 2

# Scoring
score = 0

# Player movement functions
def move_left():
    x = player.xcor()
    x -= player_speed
    if x < -380:
        x = -380
    player.setx(x)

def move_right():
    x = player.xcor()
    x += player_speed
    if x > 380:
        x = 380
    player.setx(x)

def fire_bullet():
    global bullet_speed
    if not bullet.isvisible():
        bullet.setposition(player.xcor(), player.ycor())
        bullet.showturtle()

# Collision checking function
def is_collision(t1, t2):
    distance = math.sqrt((t1.xcor() - t2.xcor()) ** 2 + (t1.ycor() - t2.ycor()) ** 2)
    if distance < 20:
        return True
    return False

# Keyboard bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")

# Score display
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("Score: {}".format(score), align="center", font=("Arial", 24, "normal"))

# Main game loop
while True:
    for asteroid in asteroids:
        y = asteroid.ycor()
        y -= asteroid_speed
        asteroid.sety(y)

        # Check for collision with bullet
        if is_collision(bullet, asteroid):
            bullet.hideturtle()
            bullet.setposition(0, -400)
            asteroid.setposition(random.randint(-380, 380), random.randint(100, 250))
            score += 10
            score_display.clear()
            score_display.write("Score: {}".format(score), align="center", font=("Arial", 24, "normal"))

        # Check for collision with player
        if is_collision(player, asteroid):
            player.hideturtle()
            asteroid.hideturtle()
            score_display.clear()
            score_display.write("Game Over. Your Score: {}".format(score), align="center", font=("Arial", 24, "normal"))
            turtle.done()

        # Reset asteroids when they reach the bottom
        if asteroid.ycor() < -300:
            asteroid.setposition(random.randint(-380, 380), random.randint(100, 250))

    # Move the bullet
    if bullet.isvisible():
        y = bullet.ycor()
        y += bullet_speed
        bullet.sety(y)

        # Check if bullet reached the top
        if bullet.ycor() > 275:
            bullet.hideturtle()

turtle.mainloop()
