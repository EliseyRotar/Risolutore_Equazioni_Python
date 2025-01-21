#Risolvere un' equazione di secondo grado

import os
#Ci servono i coefficenti a b e c reali
def acquisisci_coefficienti():
    a = float(input("Inserisci coefficiente a: "))
    b = float(input("Inserisci coefficiente b: "))
    c = float(input("Inserisci coefficiente c: "))
    return [a, b, c]
 
#Definisco una funzione che risolvi le equazioni di secondo grado
def risolvi_I_grado(b, c):
    if b==0 and c==0:
        print("Questa equazione è indeterminata")
    elif b == 0:
        print("Questa equazione è impossibile")
    else:
        print(f"soluzione: x= -c/b={-c/b}")
    
#Definisco una funzione che risolvi le equazioni di secondo grado
def risolvi_II_grado(a, b, c):
    delta = (b ** 2)- 4*a*c
    
    if delta < 0:
        print("Non esistono soluzioni reali")
    elif delta ==0:
        x1 = x2 = -b/(2*a)
        print(f"Soluzioni reali e coincidenti: \nx1 = {x1}\n x2={x2} ")
    else:
        x1 = (-b + delta ** (0.5)) / (2*a)
        x2 = (-b - delta **(0.5)) / (2*a)
        print(f"Soluzioni reali e distinte\nx1 = {x1}\nx2 = {x2}")
        
scelta=""
while scelta.lower() != "exit":
    a, b, c = acquisisci_coefficienti()
    if a == 0:
        print("Equazione di I grado: ")
        risolvi_I_grado(b, c)
    else:
        print("Equazione di II grado: ")
        risolvi_II_grado(a, b, c)
    scelta = input("premi un tasto per continuare, exit per terminare... \n")
    os.system("cls")
print("Programma terminato correttamente")
