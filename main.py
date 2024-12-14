from reader import read_file
import l_system_generator as generator
import l_system_checker as checker
import l_system_drawer as drawer

def convert_to_rules_dict(rules_str):
    rules = {}
    for rule in rules_str:
        key, value = rule.split(' ')
        rules[key] = value
    return rules

# Reading File
variables, axiom, rules, iterations = read_file('in')

valid_l_system = checker.check_validity(variables, axiom, rules, iterations)
rules = convert_to_rules_dict(rules)

# Generating L-system sequence
l_system_string = generator.generate_l_system(axiom, rules, iterations)
print(l_system_string)

if not valid_l_system:
    print('Invalid L-system')

# Drawing
angle = 31
distance = 7
drawer.draw_l_system(l_system_string, angle, distance)