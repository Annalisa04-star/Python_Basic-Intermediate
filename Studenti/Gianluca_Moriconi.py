#----------------------------------------------------------------------inizio funzione--------------------------------------------------------

def salutami(name): #definisco la funzione salutami, dichiarando la variabile name
    x ="ciao \n"    #definisco x
    y = name        #definisco y come valore preso da input
    frase = x + y   #definisco frase come somma dei valori di x e y
    print(frase)    #stampo frase

#----------------------------------------------------------------------fine funzione--------------------------------------------------------

name = input("inserisci il tuo nome:") #richiede in input un valore string che finisce all'interno 

salutami(name) #richiamo la funzione salutami che prende il valore di Nome e lo trasferisce a name

if name == "gian":                 #creo un if con condizione name == gian
    print("come stai, capo?") # se vero, stampo a schermo questo
elif name == "giovanni":           #elif è alternativa ad else if. se invece name=giovanni stampo altro
    print("piacere!")
else:                              #altrimenti in tutti gli altri casi faccio altro
    print("piacere di conoscerti, come stai?")

#----------------------------------------------------------------------inizio funzione--------------------------------------------------------

def somma():                                         #definisco la funzione somma
    primnum= input ("inserisci il primo numero: ")   #inserisco in input un numero a primnum
    secnum= input ("inserisci il secondo numero: ")  #inserisco in input un numero a secnum. tutti i dati presi da input() sono inizialmente di tipo sting..
                                                     #perciò vanno convertiti in diverso tipo se servono int, float ecc
    somma= int(primnum) + int(secnum)                #creo la variabile somma che è il risultato della somma di primnum e secnum convertiti in int
    risultato= f"La somma è: {somma}\n"                #creo la variabile testuale risultato che è una fstring contenente testo + somma
    return risultato                                 #imposto il return su risultato così da restituire il suo valore quando la funzione termina
                                                     #il return poi si reimposta in un valore null

#----------------------------------------------------------------------fine funzione--------------------------------------------------------

print(somma())
print(f"questo è un altro modo di scrivere a schermo il risultato: {name}\n")
totale = name + " " + name
print(f"questo stampa due stringhe separate da spazi: {totale}\n")
print(f"questo è un altro modo che stampa due stringhe separate da spazi: {name} {name}\n")