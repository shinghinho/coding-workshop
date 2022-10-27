# calculator.py

def how_many_leading_digits(s):
    # Description: returns the number of leading digits in a string
    # Examples:
    #   1. how_many_leading_digits("") == 0
    #   2. how_many_leading_digits("hello") == 0
    #   3. how_many_leading_digits("2022") == 4
    #   4. how_many_leading_digits("20222022hello") == 8
    i = 0
    for c in s:
        if not c.isnumeric():
            return i
        i += 1
    return i

def leading_digits(s):
    # Description: returns the leading digits
    # Examples:
    #   1. leading_digits("") == ""
    #   2. leading_digits("hello") == ""
    #   3. leading_digits("2022") == "2022"
    #   4. leading_digits("20222022hello") == "20222022"
    i = how_many_leading_digits(s)
    return s[:i]

def lex(s):
    # Description: splits the string into "tokens"
    # Examples:
    #   1. lex("2022") == [2022]
    #   2. lex("1+1") == [1, '+', 1]
    #   3. lex("1*(2+3)") == [1, '*', '(', 2, '+', 3, ')']
    #   4. lex("1+2*(3+4)") == [1, '+', 2, '*', '(', 3, '+', 4, ')']
    i = 0
    ts = []
    while i < len(s):
        c = s[i]
        if c.isnumeric():
            digits = leading_digits(s[i:])
            ts.append(int(digits))
            i += len(digits)
        else:
            i += 1
            if c == ' ':
                continue # do nothing and skip to the next iteration
            elif c in ['(', ')', '+', '*', '-', '/']:
                # ^^^ or similarly, c == '(' or c == ')' or ... or c == '/'
                ts.append(c)
            else: # invalid character
                print('Error: unexpected character,', c)
                exit(-1) # Python function to exit the program early
    return ts

# Stack operations
def push(s, x):
    s.append(x)

def top(s):
    return s[-1]

def pop(s):
    x = s[-1]
    del s[-1]
    return x

def empty(s):
    return len(s) == 0

def is_num(t):
    return isinstance(t, int)

def is_operator(t):
    return t in ['+', '-', '*', '/']

def is_lparen(t):
    return t == '('

def is_rparen(t):
    return t == ')'

def precedence(op):
    if op in ['+', '-']:
        return 1
    elif op in ['*', '/']:
        return 2
    print('Impossible')

def parse(ts):
    ops = []
    output = []
    for t in ts:
        if is_num(t):
            push(output, t)
        elif is_operator(t):
            while not empty(ops) and \
             not is_lparen(top(ops)) and \
              precedence(top(ops)) >= precedence(t):
                e = pop(ops)
                push(output, e)
            push(ops, t)
        elif is_lparen(t):
            push(ops, t)
        elif is_rparen(t):
            while top(ops) != '(':
                e = pop(ops)
                push(output, e)
            pop(ops)
    while not empty(ops):
        e = pop(ops)
        push(output, e)
    return output

def apply(op, a, b):
    if op == '+':
        return a+b
    elif op == '-':
        return a-b
    elif op == '*':
        return a*b
    elif op == '/':
        return a/b
    return 'Error'

def evaluate(ast):
    s = []
    for t in ast:
        if is_num(t):
            push(s, t)
        elif is_operator(t):
            b = pop(s)
            a = pop(s)
            push(s, apply(t, a, b))
    return s[0]

# The main program:
user_input = input('Input: ')
tokens = lex(user_input)
ast = parse(tokens)
result = evaluate(ast)
print(result)
