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
matplotlib.pyplot.plot(kepler_dataframe['TIME'], kepler_dataframe['PDCSAP_FLUX'], color='cornflowerblue')
matplotlib.pyplot.xlabel('Time (BJD - 2454833)')
matplotlib.pyplot.ylabel('Flux ($e^-/s$)')
matplotlib.pyplot.show()

# Grafico Flusso-Tempo senza linea

matplotlib.pyplot.subplots()
matplotlib.pyplot.plot(kepler_dataframe['TIME'], kepler_dataframe['PDCSAP_FLUX'], '.', color='cornflowerblue')
matplotlib.pyplot.xlabel('Time (BJD - 2454833)')
matplotlib.pyplot.ylabel('Flux ($e^-/s$)')
matplotlib.pyplot.show()

# Grafici con errori

# Grafico Flusso-Tempo salvato come .png e .pdf

matplotlib.pyplot.subplots()
matplotlib.pyplot.errorbar(kepler_dataframe['TIME'], kepler_dataframe['PDCSAP_FLUX'], yerr=kepler_dataframe['PDCSAP_FLUX_ERR'], fmt='.', color='cornflowerblue')
matplotlib.pyplot.xlabel('Time (BJD - 2454833)')
matplotlib.pyplot.ylabel('Flux ($e^-/s$)')
matplotlib.pyplot.savefig('kepler_k2.png')
matplotlib.pyplot.savefig('kepler_k2.pdf')
matplotlib.pyplot.show()

# Zoom del grafico Flusso-Tempo salvato come .png e .pdf

matplotlib.pyplot.subplots()
matplotlib.pyplot.errorbar(kepler_dataframe.loc[(kepler_dataframe['TIME']>947.9) & (kepler_dataframe['TIME']<948.35), 'TIME'], kepler_dataframe.loc[(kepler_dataframe['TIME']>947.9) & (kepler_dataframe['TIME']<948.35), 'PDCSAP_FLUX'], yerr=kepler_dataframe.loc[(kepler_dataframe['TIME']>947.9) & (kepler_dataframe['TIME']<948.35), 'PDCSAP_FLUX_ERR'], fmt='.',  color='cornflowerblue')
matplotlib.pyplot.xlabel('Time (BJD - 2454833)')
matplotlib.pyplot.ylabel('Flux ($e^-/s$)')
matplotlib.pyplot.savefig('kepler_k2_zoom.png')
matplotlib.pyplot.savefig('kepler_k2_zoom.pdf')
matplotlib.pyplot.show()

# Grafico Flusso-Tempo + riquadro con zoom salvato come .png e .pdf

fig, ax=matplotlib.pyplot.subplots(figsize=(12,6))
matplotlib.pyplot.errorbar(kepler_dataframe['TIME'], kepler_dataframe['PDCSAP_FLUX'], yerr=kepler_dataframe['PDCSAP_FLUX_ERR'], fmt='.', color='cornflowerblue')
matplotlib.pyplot.xlabel('Time (BJD - 2454833)')
matplotlib.pyplot.ylabel('Flux ($e^-/s$)')
matplotlib.pyplot.ylim(1.012e6, 1.032e6)

# Inset

inset = ax.inset_axes([.65, .62, .32, .32])
inset.errorbar(kepler_dataframe.loc[(kepler_dataframe['TIME']>947.9) & (kepler_dataframe['TIME']<948.35), 'TIME'], kepler_dataframe.loc[(kepler_dataframe['TIME']>947.9) & (kepler_dataframe['TIME']<948.35), 'PDCSAP_FLUX'], yerr=kepler_dataframe.loc[(kepler_dataframe['TIME']>947.9) & (kepler_dataframe['TIME']<948.35), 'PDCSAP_FLUX_ERR'], fmt='.',  color='cornflowerblue')

# Salvataggio file

matplotlib.pyplot.savefig('kepler_k2_inset.png')
matplotlib.pyplot.savefig('kepler_k2_inset.pdf')
matplotlib.pyplot.show()
