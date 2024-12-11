import turtle

from leitor import read_file

# TODO: Permitir várias (no máximo 3?) regras para uma mesma variável
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
            t.width(0)
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
            current_color+=1
            current_color = 1 if current_color >= len(colors) else current_color

            t.pencolor(color_map.get(colors[current_color], 'white'))
        else:
            print(f'Invalid command: {cmd}')
        
variables, axiom, rules, iterations = read_file('in2')

language_symbols = ['L', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '+', '-', '[', ']']

def convert_to_rules_dict(rules_str):
    rules = {}
    for rule in rules_str:
        key, value = rule.split(' ')
        rules[key] = value
    return rules

# TODO: Permitir que variavel pode ser um simbolo da linguagem
def check_validity(variables, axiom, rules, iterations):
    if not axiom in variables:
        return False
    
    keys = []
    for rule in rules:
        key, value = rule.split(' ')
        if key in keys:
            return False
        
        keys.append(key)
        if key in language_symbols or not key in variables:
            return False
        
        for char in value:
            if not char in language_symbols and not char in variables:
                return False
            
    if not axiom in keys:
        return False
            
    if not iterations > 0:
        return False
    
    return True

valid_l_system = check_validity(variables, axiom, rules, iterations)
rules = convert_to_rules_dict(rules)

if not valid_l_system:
    print('Invalid L-system')

angle = 31
distance = 7

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
t.pendown()
t.speed(0)
t.left(90)

# Desenhar L-system
draw_l_system(t, l_system_string, angle, distance)

# Finalizar desenho
turtle.done()
