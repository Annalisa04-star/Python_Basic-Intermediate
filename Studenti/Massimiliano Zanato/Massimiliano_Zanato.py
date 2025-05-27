# Stampa "Hello World!"
import logging

# Configurazione di base del logging
logging.basicConfig(level=logging.INFO, format='%(message)s')

print(round(3.14159, 2))

print("Hello World!")

# Stampa "Hello World 2!" tramite variabile
x = "Hello World 2!"
print(x)

# Stampa stringa concatenata
y = "Hello World 3"
z = "!"
label = y + z
print(label)

# Prima funzione
def sum():
        first = input("Insert firt number: ")
        second = input("Insert second number: ")
        sum = int(first) + int(second)
        logging.info(f"The sum is {sum}")
        print(sum)

# sum()

# Funzione con commento descrizione (simil Doxygen)
def sum(a, b):
    """
    Calcola la somma di due numeri.

    Args:
        a: Primo numero.
        b: Secondo numero.

    Returns:
        La somma di a e b.
    """
    return a + b

print(sum(1,2))

# Funzione con commento descrizione (simil Doxygen) e variabili tipizzate
def sum(a: float, b: float) -> float:
    """
    Calcola la somma di due numeri.

    Args:
        a (float): Primo numero.
        b (float): Secondo numero.

    Returns:
        float: La somma di a e b.
    """
    return a + b

print(sum(3,4))

# Esercizio calcolatrice
def calculator():
     print("Welcome to the calculator!")
     operation = input("Choose the operation:\n1. Sum\n2. Subtraction\n3. Multiplication\n4. Division\n")
     a = input("First number: ")
     b = input("Second number: ")
     if toNumber(a) == None:
        print(f"Invalid input, is not a number: {a}")
        return
     if toNumber(b) == None:
        print(f"Invalid input, is not a number: {b}")
        return
     
     result = ""

     match operation:
          case "1":
               result = toNumber(a)+toNumber(b)
               
          case "2":
               result = toNumber(a)-toNumber(b)
               
          case "3":
               result = toNumber(a)*toNumber(b)

          case "4":
               result = toNumber(a)/toNumber(b)

     print(f"The result is {result}")

               
def toNumber(s):
    try:
        return float(s)
    except ValueError:
        return None
    
calculator()