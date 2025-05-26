# Stampa "Hello World!"
import logging

# Configurazione di base del logging
logging.basicConfig(level=logging.INFO, format='%(message)s')

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

sum()