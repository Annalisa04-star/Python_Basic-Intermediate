# Esercizio calcolatrice
def calculator():
     print("---------------------------\nWelcome to the calculator!")

     while True:
        operation = input("---------------------------\nChoose the operation:\n1. Sum\n2. Subtraction\n3. Multiplication\n4. Division\nE. Exit\nSelected operation: ")
        if operation == "E":
               break
        if operation != "1" and operation != "2" and operation != "3" and operation != "4":
                print_error("Invalid operation")
                continue
        a = input("First number: ")
        b = input("Second number: ")
        n_a = to_number(a)
        n_b = to_number(b)
        if n_a == None:
                print(f"Invalid input, is not a number: {a}")
                continue
        if n_b == None:
                print(f"Invalid input, is not a number: {b}")
                continue
        if operation == "4" and n_b == 0.0:
                print(f"Invalid operation, cannot divide by zero")
                continue
        
        result = ""

        match operation:
                case "1":
                        result = n_a + n_b
                
                case "2":
                        result = n_a - n_b
                
                case "3":
                        result = n_a * n_b

                case "4":
                        result = n_a / n_b

                case _:
                        break

        print_result(f"The result is {result}")

               
def to_number(s):
    try:
        return float(s)
    except ValueError:
        return None
    
def print_error(e):
       print(f"\033[91m{e}\033[0m")

def print_result(r):
       print(f"\033[92m{r}\033[0m")
          
calculator()