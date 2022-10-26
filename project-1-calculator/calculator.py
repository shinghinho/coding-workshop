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

def parse(ts):
    # TODO: Implement this using the shunting yard algorithm!
    return []

def evaluate(ast):
    # TODO: How should we evaluate reverse Polish notation?
    return 27102022

# The main program:
user_input = input('Input: ')
tokens = lex(user_input)
ast = parse(tokens)
result = evaluate(ast)
print(result)
