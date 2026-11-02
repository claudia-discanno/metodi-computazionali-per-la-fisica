#Calcolare l'età dell'utente

from datetime import datetime, timedelta
oggi=datetime.now()
data_di_nascita=input('Inserire la data di nascita (dd-mm-yyyy): ')
data_di_nascita=datetime.strptime(data_di_nascita, "%d-%m-%Y")
eta=oggi-data_di_nascita
eta_secondi=eta.total_seconds()
eta_secondi=int(eta_secondi)
eta_minuti=eta_secondi*60
eta_ore=eta_minuti*60
eta_giorni=eta_ore/24
eta_giorni=int(eta_giorni)
eta_anni=oggi.year-data_di_nascita.year
if oggi.month<data_di_nascita.month or (oggi.month==data_di_nascita.month and oggi.day<data_di_nascita.day):
	eta_anni=eta_anni-1
print('La tua età è ',eta_anni,' anni.')
print('La tua età è ',eta_giorni,' giorni.')
print('La tua età è ',eta_ore,' ore.')
print('La tua età è ',eta_minuti,' minuti.')
print('La tua età è ',eta_secondi,' secondi.')
