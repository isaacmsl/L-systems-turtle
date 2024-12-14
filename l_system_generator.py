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