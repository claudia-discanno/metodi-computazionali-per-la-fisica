# Operazioni di bit shift

n=input('Inserire il numero: ')
n=int(n)
n_bin=bin(n)
print('Rappresentazione binaria: ', n_bin)
print('Rappresentazione esadecimale: ', hex(n))
b=input('Inserire il numero di bit a cui applicare il bit shift: ')
b=int(b)
n_plus_b=n<<b
n_minus_b=n>>b
print('n<<b: ', n_plus_b)
print('Rappresentazione binaria: ', bin(n_plus_b))
print('Rappresentazione esadecimale: ', hex(n_plus_b))
print('n>>b: ', n_minus_b)
print('Rappresentazione binaria: ', bin(n_minus_b))
print('Rappresentazione esadecimale: ', hex(n_minus_b))
