# Lettura file CSV di un catalogo di esopianeti e produzione scatter plot e istogrammi

import sys
import os
import numpy
import pandas
import matplotlib.pyplot

# Lettura file

esopianeti='https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica-2025/refs/heads/main/dati/moduli_scientifici/ExoplanetsPars_2025.csv'
esopianeti_dataframe=pandas.read_csv(esopianeti, comment='#')

# Stampa nomi colonne

print('Columns: ', esopianeti_dataframe.columns)

# Parametri pianeti

