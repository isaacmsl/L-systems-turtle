import turtle
class LSystemDrawerMenager:
    def __init__(self) -> None:
        self.variables = None
        self.axiom = None
        self.rules = None
        self.log = None
        self.draw_rules = {"speed":0,"initial_xy":(0,-100),"left":90,"distance":10,"angle":10,
                           "drawer":"L","color_map": {'a': 'red', 'b': 'blue', 'c': 'green', 'd': 'yellow', 'e': 'purple','f': 'orange',
                                                        'g': 'pink', 'h': 'brown', 'i': 'gray', 'j': 'cyan','k': 'magenta', 'l': 'lime',
                                                        'm': 'maroon', 'n': 'navy', 'o': 'olive','p': 'teal', 'q': 'coral', 'r': 'gold',
                                                        's': 'silver', 't': 'indigo', 'u': 'violet', 'v': 'turquoise', 'w': 'tan',
                                                        'x': 'salmon', 'y': 'plum', 'z': 'khaki'}
                            }
    def read(self,file_path:str) -> None:
        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()
                self.variables = lines[0].replace('\n', '').split(',')
                self.axiom = lines[1].replace('\n', '')
                self.rules = {j[0]:j[1] for j in [i.split(" ") for i in lines[2].replace('\n', '').split(',')]}
                self.draw_rules["angle"] = int(lines[3])
        except FileNotFoundError:
            print(f"arquivo {file_path} não encontrado")
        except IOError:
            print(f"erro ao ler o arquivo {file_path}")

    def generate(self,iterations:int=1) -> str:
        result = self.axiom
        for i in range(iterations):
            templist = [self.rules[i] if i in self.rules.keys() else i for i in result]
            result = ''.join(templist)
        self.log = result

        return self.log

    def check(self, n:int, sequence:str=None) -> bool:
        stack = [('$', 0)]
        stack.append((self.axiom, 0))

        sequence_to_check = sequence or self.log

        for c in sequence_to_check:  
            while stack:
                top, iteration = stack.pop()
                if iteration < n and top in self.variables:
                    rule = self.rules[top]
                    stack.extend((symbol, iteration + 1) for symbol in reversed(rule))
                elif top == c: 
                    break
                else:
                    return False
        return all(item[0] == '$' for item in stack)
    
    def draw(self,trace:bool = False) -> None:
        screen = turtle.Screen()
        screen.setup(width=800, height=800)  # Tamanho visível da janela
        screen.screensize(3000, 3000) 
        screen.bgcolor('black')
        if trace:
            screen.tracer(0)
        t = turtle.Turtle()
        t.pen(shown=False)
        t.pencolor('white')
        t.penup()
        t.goto(self.draw_rules["initial_xy"])
        t.pendown()
        t.speed(self.draw_rules["speed"])
        t.left(self.draw_rules["left"])
        stack = []
        for cmd in self.log:
            if cmd == self.draw_rules["drawer"]:
                t.forward(self.draw_rules["distance"])
            elif cmd == '+':
                t.width(t.width() + 1)
            elif cmd == '-':
                if t.width() > 0:
                    t.width(t.width() - 1)
            elif cmd == '[':
                stack.append((t.position(), t.heading()))
            elif cmd == ']':
                position, heading = stack.pop()
                t.penup()
                t.goto(position)
                t.setheading(heading)
                t.pendown()
            elif cmd == '0':
                t.left(self.draw_rules["angle"])
            elif cmd == '1':
                t.right(self.draw_rules["angle"])
                
            elif cmd in 'abcdefghijklmnopqrstuvwxyz':
                t.pencolor(self.draw_rules["color_map"].get(cmd, 'white'))
        turtle.done()
        if trace:
            screen.update()

    def __str__(self) -> str:
        return f"Variables: {self.variables}\nAxiom: {self.axiom}\nRules: {self.rules}\nLog: {self.log}"