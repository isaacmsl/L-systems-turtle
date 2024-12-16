from lsdm import LSystemDrawerMenager
lsdm = LSystemDrawerMenager()
file = "./testes/in9.txt"
iterations = 5
lsdm.read(file)
lsdm.generate(iterations)
if lsdm.check(iterations):
    print(f"A string '{lsdm.log}' pertence a linguagem descrita por '{file}'")
else:
    print(f"A string '{lsdm.log}' NÃO pertence a linguagem descrita por '{file}'")
lsdm.draw(True)