import turtle

def config_turtle():
    screen = turtle.Screen()
    screen.bgcolor('black')
    t = turtle.Turtle()
    t.pen(shown=False)
    t.pencolor('white')
    t.penup()
    t.pendown()
    t.speed(0)
    t.left(90)

    return t

# Função para desenhar a sequência L-system usando Turtle
def draw_l_system(instructions, angle, distance):

    t = config_turtle()

    stack = []

    color_map = {
        'a': 'red', 'b': 'blue', 'c': 'green', 'd': 'yellow', 'e': 'purple',
        'f': 'orange', 'g': 'pink', 'h': 'brown', 'i': 'gray', 'j': 'cyan',
        'k': 'magenta', 'l': 'lime', 'm': 'maroon', 'n': 'navy', 'o': 'olive',
        'p': 'teal', 'q': 'coral', 'r': 'gold', 's': 'silver', 't': 'indigo',
        'u': 'violet', 'v': 'turquoise', 'w': 'tan', 'x': 'salmon', 'y': 'plum',
        'z': 'khaki'
    }

    colors = 'keg'
    current_color = -1

    for cmd in instructions:
        if cmd == 'L':
            t.forward(distance)
        elif cmd == 'T':
            t.backward(distance)
        elif cmd == '+':
            t.width(t.width()*2)
        elif cmd == '-':
            t.width(t.width()//2)
        elif cmd == '[':
            stack.append((t.position(), t.heading()))
        elif cmd == ']':
            position, heading = stack.pop()
            t.penup()
            t.goto(position)
            t.setheading(heading)
            t.pendown()
        elif cmd in '0123456789':
            t.right(int(cmd) * angle)
        elif cmd == 'r':
            t.right(angle)
        elif cmd == 'l':
            t.left(angle)
        elif cmd in 'abcdefghijklmnopqrstuvwxyz':
            t.pencolor(color_map.get(cmd, 'white'))
        elif cmd in '$':
            current_color += 1
            current_color = 1 if current_color >= len(colors) else current_color

            t.pencolor(color_map.get(colors[current_color], 'white'))

    turtle.done()