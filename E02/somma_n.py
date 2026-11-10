# Somma dei primi n numeri naturali

n_max=input('Inserire un numero: ')
n_max=int(n_max)
somma=0
for n in range(1,n_max+1):
	somma=somma+n
print('La somma dei primi ',n,' numeri naturali è ',somma)
