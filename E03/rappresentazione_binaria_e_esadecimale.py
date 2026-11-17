# Operazioni AND e OR bitwise

# Rappresentazione binaria e esadecimale del primo numero intero

n=input('Inserire il primo numero: ')
n=int(n)
print('Rappresentazione binaria: ', bin(n))
print('Rappresentazione esadecimale: ', hex(n))

# Rappresentazione binaria e esadecimale del secondo numero intero

m=input('Inserire il secondo numero: ')
m=int(m)
print('Rappresentazione binaria: ', bin(m))
print('Rappresentazione esadecimale: ', hex(m))

# Operazione OR bitwise

print('Eseguo operazione OR bitwise tra i due numeri inseriti.')
nORm=n|m
print('Rappresentazione decimale: ', nORm)
print('Rappresentazione binaria: ', bin(nORm))
print('Rappresentazione esadecimale: ', hex(nORm))

# Operazione AND bitwise

print('Eseguo operazione AND bitwise tra i due numeri inseriti.')
nANDm=n&m
print('Rappresentazione decimale: ', nANDm)
print('Rappresentazione binaria: ', bin(nANDm))
print('Rappresentazione esadecimale: ', hex(nANDm))
