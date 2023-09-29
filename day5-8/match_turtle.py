# Python 3.10

# Pattern Match Estrutural

print(
"""\
Jogo da Tartaruga
comandos:
    move x y
    move steps
    turn angle (default 90)
    draw shape size (line|circle)
    write text
    stop | exit
"""
)

from turtle import Turtle

turtle = Turtle()
turtle.shape("turtle")
turtle.speed(3)
turtle.color("green", "blue")
turtle.penup()

# Antes do python match
##while True:
##    command = input("🐢>").strip().split()
##    # move 2 3 ["move", "2", "3"]
##    if command[0] in ("exit", "stop"):
##        break
##    if command[0] == "draw":
##        # draw line 40
##        shape = command[1]
##        size = float(command[2])
##        turtle.pendown()
##        if shape == "line":
##            turtle.forward(size)
##        elif shape == "circle":
#            turtle.circle(size)

while True:
    command: list[str] = input("🐢>").strip().split()
    # move 2 3 ["move", "2", "3"]

    # switch - case / Estrutural

    match command:

        case ["move", *points]:

            match points:

                case [x, y]:
                    turtle.goto(float(x), float(y))

                case [steps]:
                    turtle.forward(float(steps))

        case ["turn", *options]:

            match options:

                case[angle]:
                    turtle.right(float(angle))

                case _:
                    turtle.right(90)

        case ["draw", shape, size]:
            turtle.pendown()
            match shape:
                case "circle":
                    turtle.circle(float(size))

                case "line":
                    turtle.forward(float(size))
            turtle.penup()


        case ["write", *text]:
            turtle.write(" ".join(text), None, "center", "14pt 18")

        case ["exit" | "stop" | "quit"]:
            break

        case _:
            print("Invalid command")