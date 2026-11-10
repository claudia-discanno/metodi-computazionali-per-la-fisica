import sys
import os
import numpy

# Funzione che restituisce la somma dei primi n numeri naturali

def somma(n_max):
	somma=0
	for n in range(1,n_max+1):
		somma=somma+n
	return somma

# Funzione che restituisce la somma delle radici dei primi n numeri naturali

def somma_radici(m_max):
	somma_radici=0
	for m in range(1,m_max+1):
		somma_radici=somma_radici+m**0.5
	return somma_radici

# Funzione che restituisce il prodotto dei primi n numeri naturali

def prodotto(p_max):
	prodotto=1
	for p in range(1,p_max+1):
		prodotto=prodotto*p
	return prodotto

# Funzione che restituisce la somma e il prodotto dei primi n numeri naturali

def somma_e_prodotto(n_max):
	s=somma(n_max)
	p=prodotto(n_max)
	return s, p

# Funzione che restituisce la somma di i^alfa con i compreso tra 1 e n

def somma_esponenziale_n(n_max, alfa=1, **kwargs):
	"""
	Funzione che calcola la somma di i^alfa con i compreso tra 1 e n
	
	Parametri:
		n_max: valore massimo dell'intervallo di numeri naturali
		alfa: esponente dei termini della somma
	Risultato:
		somma_i_alfa: sommatoria di i^a con i compreso tra 1 e n
	"""
	array_n=numpy.arange(n_max+1)
	somma_i_alfa=numpy.power(array_n,alfa)
	return numpy.sum(somma_i_alfa)
