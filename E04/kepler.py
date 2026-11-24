# Lettura file CSV della missione Kepler/K2 e produzione di grafici di flusso in funzione del tempo

import sys
import os
import numpy
import pandas
import matplotlib.pyplot

# Lettura file

kepler_k2='https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica-2025/refs/heads/main/dati/moduli_scientifici/kplr010666592-2011240104155_slc.csv'
kepler_dataframe=pandas.read_csv(kepler_k2)

# Stampa nomi colonne

print('Columns: ', kepler_dataframe.columns)

# Grafici senza errori

# Grafico Flusso-Tempo

matplotlib.pyplot.subplots()
matplotlib.pyplot.plot(kepler_dataframe['TIME'], kepler_dataframe['PDCSAP_FLUX'])
matplotlib.pyplot.xlabel('Time (BJD - 2454833)')
matplotlib.pyplot.ylabel('Flux ($e^-/s$)')
matplotlib.pyplot.show()

# Grafico Flusso-Tempo senza linea

matplotlib.pyplot.subplots()
matplotlib.pyplot.plot(kepler_dataframe['TIME'], kepler_dataframe['PDCSAP_FLUX'], '.')
matplotlib.pyplot.xlabel('Time (BJD - 2454833)')
matplotlib.pyplot.ylabel('Flux ($e^-/s$)')
matplotlib.pyplot.show()

# Grafico con errori salvato come .png e .pdf

matplotlib.pyplot.subplots()
matplotlib.pyplot.plot(kepler_dataframe['TIME'], kepler_dataframe['PDCSAP_FLUX'], '.')
matplotlib.pyplot.xlabel('Time (BJD - 2454833)')
matplotlib.pyplot.ylabel('Flux ($e^-/s$)')
matplotlib.pyplot.errorbar(kepler_dataframe['TIME'], kepler_dataframe['PDCSAP_FLUX'], yerr=kepler_dataframe['PDCSAP_FLUX_ERR'], fmt='.')
matplotlib.pyplot.savefig('kepler_k2.png')
matplotlib.pyplot.savefig('kepler_k2.pdf')
matplotlib.pyplot.show()
