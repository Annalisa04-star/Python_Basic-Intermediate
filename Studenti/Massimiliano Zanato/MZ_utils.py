def to_float(s):
    try:
        return float(s)
    except ValueError:
        return None
    
def print_error(e):
       print(f"\033[91m{e}\033[0m")

def print_result(r):
       print(f"\033[92m{r}\033[0m")

def is_input_float(s):
        if s == None:
                print(f"Invalid input, is not a number: {s}")
                return False
        return True