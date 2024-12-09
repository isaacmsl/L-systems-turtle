def decision(rules, character, key):
    for rule in rules[key]:
        if rule[0] == character:
            return rule
    return rules[key][0]

def read_l_system(axiom, variables, rules, word, n = 10):
    stack = ['$', axiom]

    for c in word:
        top = stack[-1]

        if top in variables:
            rule = decision(rules, c, top)
            del stack[-1]
            stack += [c for c in rule[::-1]]
        elif top != c:
            return False

        del stack[-1]

        n -= 1
        if n <= 0:
            return True

    return stack == ['$']

s = "aaaab"
rules = {"A":["aA", "b"]}
variables = ["A"]

print(read_l_system("A", variables, rules, s))