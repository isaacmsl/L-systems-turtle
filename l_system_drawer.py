import turtle

# Função para aplicar regras de produção
def apply_rules(axiom, rules):
    return ''.join(rules.get(char, char) for char in axiom)

# Função para gerar a sequência L-system
def generate_l_system(axiom, rules, iterations):
    result = axiom
    for _ in range(iterations):
        result = apply_rules(result, rules)

    return result

# Função para desenhar a sequência L-system usando Turtle
def draw_l_system(t, instructions, angle, distance):
    stack = []
    for cmd in instructions:
        if cmd == 'F':
            t.forward(distance)
        elif cmd == '+':
            t.right(angle)
        elif cmd == '-':
            t.left(angle)
        elif cmd == '[':
            stack.append((t.position(), t.heading()))
        elif cmd == ']':
            position, heading = stack.pop()
            t.penup()
            t.goto(position)
            t.setheading(heading)
            t.pendown()

# Parâmetros do L-system
axiom = "X"
rules = {
    "X": "F+[[X]-X]-F[-FX]+X",
    "F": "FF"
}
iterations = 4
angle = 25
distance = 5

# Gerar sequência L-system
l_system_string = generate_l_system(axiom, rules, iterations)
print(l_system_string)
# Configuração da tela do Turtle
screen = turtle.Screen()
screen.bgcolor('black')
t = turtle.Turtle()
t.pen(shown=False)
t.pencolor('white')
t.penup()
t.sety(-300)
t.pendown()
t.speed(0)
t.left(90)

# Desenhar L-system
draw_l_system(t, l_system_string, angle, distance)

# Finalizar desenho
turtle.done()
