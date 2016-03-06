import sys

def read_eval_print_loop():
    """Run a read-eval-print loop for calculator."""
    while True:
        try:
            expression_tree = calc_parse(input('calc> '))
            #print(calc_eval(expression_tree))
        except (SyntaxError, TypeError, ZeroDivisionError) as err:
            print(type(err).__name__ + ":", err)
        except (EOFError, KeyboardInterrupt): # <Control>-D, etc.
            sys.exit(0)
        except:
            print('Unable to handle the input. Terminated.')
            sys.exit(1)

def calc_parse(line):
    """Parse a line of calculator input and return an expression tree."""
    tokens = tokenize(line)
    expression_tree = analyze(tokens)
    if len(tokens) > 0:
        raise SyntaxError('Extra token(s): ' + ' '.join(tokens))
    return expression_tree

def tokenize(line):
    """Convert a string into a list of tokens."""
    spaced = line.replace('(', ' ( ').replace(')', ' ) ').replace(',', ' , ')
    return spaced.split()
    
def analyze(tokens):
    """Create a tree of nested lists from a sequence of tokens."""
    token = analyze_token(tokens.pop())
    if type(token) in (int, float):
        return token
    else:
        tokens.pop(0) # Remove (
        return Exp(token, analyze_operands(tokens))

def analyze_operands(tokens):
    """Read a list of comma-separated operands."""
    pass

def analyze_token(token):
    """Return the value of token if it can be analyzed as a number, or token."""
    try:
        return int(token)
    except (TypeError, ValueError):
        try:
            return float(token)
        except (TypeError, ValueError):
            return token

def calc_eval(exp):
    """Evaluate a Calculator expression"""
    pass

def main():
    read_eval_print_loop()
    sys.exit(0)

if __name__ == "__main__":
    main()
