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

def is_number(t):
    return isinstance(t, int) 

def is_operator(t):
    return t in ['+','-','*','/']

def push(s, x):
    s.append(x)

def pop(s):
    x = s[-1]
    del s[-1]
    return x

def top(s):
    return s[-1]

def is_lparen(t):
    return t == '('

def empty(s):
    return len(s) == 0

def is_rparen(t):
    return t == ')'

# Push, pop, top

def precedence(t):
    if t in ['+', '-']: return 1
    elif t in ['*', '/']: return 2

def parse(ts):
    ops = []
    output = []
    for t in ts:
        if is_number(t):
            push(output, t)
        elif is_operator(t):
            while not empty(ops) and \
                    not is_lparen(t) and \
                     precedence(top(ops)) >= precedence(t):
                x = pop(ops)
                push(output, x)
            push(ops, t)
        elif is_lparen(t):
            push(ops, '(')
        elif is_rparen(t):
            while not is_lparen(top(ops)):
                x = pop(ops)
                push(output, x)
            pop(ops)
    while not empty(ops):
        x = pop(ops)
        push(output, x)
    return output

def run(t, a, b):
    if t == '+':  return a+b
    elif t == '-': return a-b
    elif t == '*': return a*b
    elif t == '/': return a/b

def evaluate(ast):
    s = []
    for t in ast:
        if isinstance(t, int):
            s.append(t)
        else: # + - * /
            a, b = s[-2], s[-1]
            del s[-2], s[-1]
            s.append(run(t, a, b))
    return s[0]

# The main program:
user_input = input('Input: ')
tokens = lex(user_input)
ast = parse(tokens)
result = evaluate(ast)
print(result)

