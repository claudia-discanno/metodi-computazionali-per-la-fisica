# Lista dei giorni della settimana

giorni_della_settimana=['Lunedì', 'Martedì', 'Mercoledì', 'Giovedì', 'Venerdì', 'Sabato', 'Domenica']

# Lista dei giorni della settimana per il mese di Ottobre 2026

giorni_della_settimana_Ottobre=giorni_della_settimana[3:]+giorni_della_settimana*3+giorni_della_settimana[0:6]

# Dizionario che mette in relazione il giorno del mese con quello della settimana per Ottobre 2026

i=0
dizionario_Ottobre={}
for i in range(len(giorni_della_settimana_Ottobre)):
	dizionario_Ottobre.update({giorni_della_settimana_Ottobre[i]:i+1})

# Stampa calendario Ottobre 2026

j=0
print('Ottobre 2026')
for j in dizionario_Ottobre:
	print(dizionario_Ottobre[j],j)
