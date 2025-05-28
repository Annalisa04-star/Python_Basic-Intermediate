print ("Hello World!")

x = "Hi everyone"
print (x)

y = "my name is Roberta"

print (x + " " + y)

## and if it was a number?

z = 33

# print (x + z)  # This will cause an error because you cannot concatenate a string and an integer directly
print (x + " " + str(z))  # Convert the integer to a string before concatenation

## funzione, va definita e poi "chiamata"

def function():
    print("This is a function")
function()

# creiamo una funzione per salutare qualcuno
def salutami(name):
    x = "Ciao "
    y = str(name) + "!"
    print(x + y)

name = input("Come ti chiami? ")
salutami(name)

# creiamo una funzione per salutare i colleghi
def saluta_colleghi(name):
    name = str(input("Come ti chiami? "))
    if name == "Roberta":
        print("Ehi capo! Come va?")
    elif name == "Giorgio":
        print("Bentornato Giorgio! Come stai?")
    elif name == "Simonetta":
        print("Ciao Mamma! Tutto bene?")
    else: print("Piacere di conoscerti! Benvenuto " + name + "!")

saluta_colleghi(name)

# creiamo funzione per calcolare area rettangolo

def area_rettangolo():
    base = float(input("Inserisci la base del rettangolo: "))
    altezza = float(input("Inserisci l'altezza del rettangolo: "))
    area = base * altezza
    return area

area_rettangolo()

########### LEZIONE 2

# creazione di una calcolatrice semplice

def calcolatrice():
    print("------------------------------\nBenvenuto nella Calcolatrice!\n------------------------------")
    print("Scegli un'operazione:\n 1. Addizione\n 2. Sottrazione\n 3. Moltiplicazione\n 4. Divisione\n------------------------------")

    scelta = input("> Seleziona l'operazione (1, 2, 3, 4): ")
    operazioni = {
        '1': 'Addizione',
        '2': 'Sottrazione',
        '3': 'Moltiplicazione',
        '4': 'Divisione'
    }
# nel caso di operazione non valida, richiediamo di ripetere la scelta
    if scelta not in operazioni: 
        print("Operazione non valida. Riprova.\n")
        return calcolatrice()
    # chiediamo la conferma dell'operazione scelta
    else:
        print(f"Hai scelto l'operazione: {operazioni.get(scelta)}")
        conferma = input("> è esatto? (Yes/No): ")
        if conferma.lower() != 'yes' and conferma.lower() != 'no':
            print("Risposta non valida. Si prega di rispondere con 'Yes' o 'No'.\n")
            return calcolatrice()  # Richiama la funzione per ripetere la scelta
        elif conferma.lower() != 'yes':
            print("Operazione annullata. Riprova.\n")
            return calcolatrice()  # Richiama la funzione per ripetere la scelta
        else:
            print("Operazione confermata.")

    if scelta in ['1', '2', '3', '4']:
        
        x = float(input("> Inserisci il primo numero: "))
        y = float(input("> Inserisci il secondo numero: "))
        print("------------------------------")
        if scelta == '1':
             print(f"Risultato di {x} + {y} è: {x+y}")
        elif scelta == '2':
            print(f"Risultato di {x} - {y} è: {x-y}")
        elif scelta == '3':
            print(f"Risultato di {x} * {y} è: {x*y}")
        elif scelta == '4':
            print(f"Risultato di {x} / {y} è: {x/y}")

# Chiamata alla funzione calcolatrice
calcolatrice()