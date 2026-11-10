import sys
import os

# Importa il modulo somme.py e usa le sue funzioni

import somme
print('Uso il modulo somme.')
n=input('Inserire un numero: ')
n=int(n)

# Stampa a schermo la somma dei primi n numeri naturali

somma=somme.somma(n)
print('La somma dei primi ',n,' numeri naturali è ',somma)

# Stampa a schermo la somma delle radici dei primi n numeri naturali

somma_radici=somme.somma_radici(n)
print('La somma delle radici dei primi ',n,' numeri naturali è ',somma_radici)

# Stampa a schermo la somma e il prodotto dei primi n numeri naturali

somma_prodotto=somme.somma_e_prodotto(n)
print('Somma e prodotto dei primi ',n,' numeri naturali: ', somma_prodotto)

# Stampa a schermo la somma di i^alfa con i compreso tra 1 e n

print('Esecuzione somma di i^alfa con i compreso tra 1 e n.')
somma_i_alfa_1=somme.somma_esponenziale_n(n)
print('La somma di i^alfa con i compreso tra 1 e n e alfa pari a 1 è: ', somma_i_alfa_1)
alfa=input('Inserire esponente alfa: ')
alfa=int(alfa)
somma_i_alfa=somme.somma_esponenziale_n(n,alfa)
print('La somma di i^alfa con i compreso tra 1 e n e alfa pari a ', alfa,' è: ', somma_i_alfa)
