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

def calc_parse(line):
    """Parse a line of calculator input and return an expression tree."""
    pass

def calc_eval(exp):
    """Evaluate a Calculator expression"""
    pass

def main():
    read_eval_print_loop()
    sys.exit(0)

if __name__ == "__main__":
    main()
