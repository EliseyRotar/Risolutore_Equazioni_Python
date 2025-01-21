#Risolvere un' equazione di secondo grado
import os
from math import sqrt, pow
 #Ci servono i coefficenti a b e c reali
def acquisisci_coefficienti():
    a = float(input("Inserisci coefficiente a: "))
    b = float(input("Inserisci coefficiente b: "))
    c = float(input("Inserisci coefficiente c: "))
    return [a, b, c]

#Definisco una funzione che risolvi le equazioni di secondo grado
def risolvi_I_grado(b, c):
    if b == 0 and c == 0:
        print("Equazione indeterminata")
    elif b == 0:
        print("Equazione impossibile")
    else:
        x = -c/b
        print(f"La soluzione dell'equazione è {x}")

#Definisco una funzione che risolvi le equazioni di secondo grado
def risolvi_II_grado(a, b, c):
    delta = pow(b,2) - 4 * a * c
 
    if delta < 0:
        print("Non esistono soluzioni reali")
 
    elif delta == 0:
        print("Le due soluzioni reali sono coincidenti")
        x = -b / (2 * a)
        print(f"La soluzione dell'equazione è {x}")
 
    elif delta > 0:
        print("Le due soluzioni reali sono distinte")
        x1 = (-b - sqrt(delta)) / (2 * a)
        x2 = (-b + sqrt(delta)) / (2 * a)
        print(f"Le due soluzioni sono: {x1} e {x2}")
 
scelta = ""
 
while scelta.lower() != "exit":
 
    a, b, c = acquisisci_coefficienti()
    if a == 0:
        risolvi_I_grado(b, c)
    else:
        risolvi_II_grado(a, b, c)
    scelta = input("Premi un tasto per continuare, exit per terminare...\n")
    os.system("cls")
 
print("Programma terminato correttamente")
