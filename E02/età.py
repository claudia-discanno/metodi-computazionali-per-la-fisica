# Calcolare l'età dell'utente

# Importa la data di oggi e la data di nascita dell'utente

from datetime import datetime, timedelta
oggi=datetime.now()
data_di_nascita=input('Inserire la data di nascita (dd-mm-yyyy): ')
data_di_nascita=datetime.strptime(data_di_nascita, "%d-%m-%Y")

# Età

eta=oggi-data_di_nascita

# Età misurata in secondi

eta_secondi=eta.total_seconds()
eta_secondi=int(eta_secondi)

# Età misurata in minuti

eta_minuti=eta_secondi*60

# Età misurata in ore

eta_ore=eta_minuti*60

# Età misurata in giorni

eta_giorni=eta_ore/24
eta_giorni=int(eta_giorni)

# Età misurata in anni

eta_anni=oggi.year-data_di_nascita.year
if oggi.month<data_di_nascita.month or (oggi.month==data_di_nascita.month and oggi.day<data_di_nascita.day):
	eta_anni=eta_anni-1

#Stampa a schermo

print('La tua età è ',eta_anni,' anni.')
print('La tua età è ',eta_giorni,' giorni.')
print('La tua età è ',eta_ore,' ore.')
print('La tua età è ',eta_minuti,' minuti.')
print('La tua età è ',eta_secondi,' secondi.')
