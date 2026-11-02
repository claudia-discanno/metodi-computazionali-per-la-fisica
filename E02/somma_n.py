# Somma dei primi n numeri naturali

nmax=input('Inserire un numero: ')
nmax=int(nmax)
somma=0
for n in range(1,nmax+1):
	somma=somma+n
print('La somma dei primi ',n,' numeri naturali è ',somma)
