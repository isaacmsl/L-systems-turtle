def expand_string(string, rules, n):
    for _ in range(n):
        expanded_string = ''  
        for c in string:
            rule = decision(rules, c) 
            expanded_string += "".join(rule)  
        string = expanded_string  
    print(expanded_string)
    return expanded_string


def decision(rules, key):
    return rules[key][0]  # Para este caso, iremos ter só uma regra (determinístico)

def verify_nth_string_with_stack(axiom, variables, rules, word, n):

    stack = [('$', 0)]  # Pilha inicial com delimitador e iteração 0
    stack.append((axiom, 0))

    for c in word:  
        while stack:
            top, iteration = stack.pop()
            if iteration < n and top in variables:
                rule = decision(rules, top)
                stack.extend((symbol, iteration + 1) for symbol in reversed(rule))
            elif top == c: 
                break
            else:
                return False
    return all(item[0] == '$' for item in stack)




axiom = "A"
rules = {"A": ["AB"], "B": ["A"]}
variables = ["A", "B"]
n = 7
s = "ABAABABAABAABABAABABAABAABABAABAAB"

print(verify_nth_string_with_stack(axiom, variables, rules, s, n))
