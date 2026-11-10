# Lettura file CSV della missione Kepler/K2 e produzione di grafici di flusso in funzione del tempo

import sys
import os
import numpy
import pandas
import matplotlib.pyplot

kepler_k2='https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica-2025/refs/heads/main/dati/moduli_scientifici/kplr010666592-2011240104155_slc.csv'
kepler_dataframe=pd.read_csv(kepler_k2)
print('Columns: ', kepler_dataframe.columns)

#############################  Grafici senza errori  #####################################


## grafico Flusso vs. Tempo
plt.subplots(figsize=(12,6))
plt.plot(kepler_dataframe['TIME'], kepler_dataframe['PDCSAP_FLUX'] )
plt.xlabel('Time (BJD - 2454833)', fontsize=14)
plt.ylabel(r'Flux ($e^-/s$)', fontsize=14)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.show()


## grafico Flusso vs. Tempo con simbolo (no linea)
plt.subplots(figsize=(12,6))
plt.plot(kplrdf['TIME'], kplrdf['PDCSAP_FLUX'], 'o')
plt.xlabel('Time (BJD - 2454833)', fontsize=14)
plt.ylabel(r'Flux ($e^-/s$)',      fontsize=14)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.show()



#############################  Grafici con  errori  #####################################

## grafico Flusso vs. Tempo salvato come png e pdf
plt.subplots(figsize=(12,6))
plt.errorbar(kepler_dataframe['TIME'], kepler_dataframe['PDCSAP_FLUX'], yerr=kepler_dataframe['PDCSAP_FLUX_ERR'], fmt='.' )
plt.xlabel('Time (BJD - 2454833)', fontsize=14)
plt.ylabel(r'Flux ($e^-/s$)',      fontsize=14)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.savefig('curva_luce.png')
plt.savefig('curva_luce.pdf')
plt.show()




## Zoom grafico Flusso vs. Tempo salvato come png e pdf
plt.subplots(figsize=(12,6))
plt.errorbar(      kepler_dataframe.loc[ (kepler_dataframe['TIME']> 947.9) & (kepler_dataframe['TIME']< 948.35), 'TIME'],
                   kepler_dataframe.loc[ (kepler_dataframe['TIME']> 947.9) & (kepler_dataframe['TIME']< 948.35), 'PDCSAP_FLUX'],
              yerr=kepler_dataframe.loc[ (kepler_dataframe['TIME']> 947.9) & (kepler_dataframe['TIME']< 948.35), 'PDCSAP_FLUX_ERR'], fmt='.',  color='royalblue')

plt.xlabel('Time (BJD - 2454833)', fontsize=14)
plt.ylabel(r'Flux ($e^-/s$)',      fontsize=14)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.savefig('curva_luce_zoom.png')
plt.savefig('curva_luce_zoom.pdf')
plt.show()




## grafico Flusso vs. Tempo con riquadro, salvato come png e pdf 
fig, ax = plt.subplots(figsize=(12,6))
plt.errorbar(kepler_dataframe['TIME'], kepler_dataframe['PDCSAP_FLUX'], yerr=kepler_dataframe['PDCSAP_FLUX_ERR'], fmt='.', color='cornflowerblue' )
plt.xlabel('Time (BJD - 2454833)', fontsize=14)
plt.ylabel(r'Flux ($e^-/s$)',      fontsize=14)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.ylim(1.012e6, 1.030e6)

# creo inset 
ins_ax = ax.inset_axes([.65, .62, .32, .32])  # [x, y, width, height] w.r.t. ax
ins_ax.errorbar(      kepler_dataframe.loc[ (kepler_dataframe['TIME']> 947.9) & (kepler_dataframe['TIME']< 948.35), 'TIME'],
                      kepler_dataframe.loc[ (kepler_dataframe['TIME']> 947.9) & (kplrdf['TIME']< 948.35), 'PDCSAP_FLUX'],
                 yerr=kplrdf.loc[ (kplrdf['TIME']> 947.9) & (kplrdf['TIME']< 948.35), 'PDCSAP_FLUX_ERR'], fmt='.',  color='royalblue')


# salvataggio su file
plt.savefig('curva_luce_inset.png')
plt.savefig('curva_luce_inset.pdf')

plt.show()
