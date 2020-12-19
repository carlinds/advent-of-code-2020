precedence_level = {'+': 2, '*': 1}

def calculate_equation(eq):
    eq = eq.replace('(', '( ')
    eq = eq.replace(')', ' )')
    tokens = eq.split()

    terms = []
    operators = []

    def eval_terms():
        a, b = terms.pop(), terms.pop()
        op = operators.pop()
        if op == '+':
            terms.append(a + b)
        elif op == '*':
            terms.append(a * b)

    for token in tokens:
        if token == '(':
            operators.append(token)

        elif token == ')':
            while operators[-1] != '(':
                eval_terms()
            operators.pop()
    
        elif token in {'+', '*'}:
            while (len(operators) and
                  (operators[-1] != '(') and
                  (precedence_level[operators[-1]] > precedence_level[token])):
                eval_terms()
            operators.append(token)

        else:
            terms.append(int(token))

    while(len(operators)):
        eval_terms()

    return terms[-1]


def main():
    with open('homework.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    s = 0
    for eq in lines:
       s += calculate_equation(eq)

    print(s)

if __name__ == "__main__":
    main()