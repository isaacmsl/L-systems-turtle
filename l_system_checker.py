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

language_symbols = ['L', '0', '1', '2', '3', '4', '5', '6', '7',
                    '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g',
                    'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                    'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                    'z', '+', '-', '[', ']']

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

axiom = "A"
rules = {"A": ["AB"], "B": ["A"]}
variables = ["A", "B"]
n = 7
s = "ABAABABAABAABABAABABAABAABABAABAAB"

print(verify_nth_string_with_stack(axiom, variables, rules, s, n))
