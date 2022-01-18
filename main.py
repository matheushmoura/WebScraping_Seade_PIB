import pandas as pd
import matplotlib.pyplot as plt
from downloadTabelas import downloadTabela
import os

datasp = pd.DataFrame(columns=['ano', 'sp', 'pp', 'g', 'c'])
# Reading data downloaded in'seade.gov.br'
downloadTabela()
# Plotting

import glob, os
os.chdir("C:/Users/Matheus/Documents/PIBbrasil/SeadeFiles/")
for file in glob.glob("*.xlsx"):
    filesplit = file.split('pib_')[1]
    filesplit2 = filesplit.split('.')[0]
    year = filesplit2.split('-')[0]
    #print(year)

    df = pd.read_excel(file, header=10)
    os.remove(file)
    df.columns = ['MUNICIPIO', 'AGROPECUARIA', 'INDUSTRIA', 'ADM PUBLICA', 'SUBTOTAL', 'TOTAL', 'IMPOSTOS', 'PIB', 'PIB CAPITA']
    #print(df)
    datasp = datasp.append({
        'ano': str(year),
        'sp': df.loc[df['MUNICIPIO'] == "São Paulo"]['PIB CAPITA'].values * 1000,
        'pp': df.loc[df['MUNICIPIO'] == "Presidente Prudente"]['PIB CAPITA'].values * 1000,
        'g': df.loc[df['MUNICIPIO'] == "Guarulhos"]['PIB CAPITA'].values * 1000,
        'c': df.loc[df['MUNICIPIO'] == "Campinas"]['PIB CAPITA'].values * 1000
    }, ignore_index=True)

print(datasp)

# plotting
ax = plt.gca()
ax.set_facecolor('#F6F9ED')
datasp['sp'] = datasp['sp'].astype(float)
datasp['pp'] = datasp['pp'].astype(float)
datasp['g'] = datasp['g'].astype(float)
datasp['c'] = datasp['c'].astype(float)
datasp.plot(kind='line', x='ano', y='sp', label='São Paulo (SP)', ax=ax, color='#42124C')
datasp.plot(kind='line', x='ano', y='c', label='Campinas (SP)', ax=ax, color='#FE0472')
datasp.plot(kind='line', x='ano', y='g', label='Guarulhos (SP)', ax=ax, color='#8AFF00')
datasp.plot(kind='line', x='ano', y='pp', label='Presidente Prudente (SP)', ax=ax, color='#C3FF13')

ax.grid(False)
plt.title(' Gross Domestic Product (GDP) \n Of the 5 largest cities in São Paulo (State)', fontsize=14, alpha=0.8)
plt.ylabel('GDP Per Capita in Real(R$)', fontsize=13, alpha=0.8)
plt.xlabel('Year', fontsize=13, alpha=0.8)
plt.tick_params(top='off', right='off', labelbottom='on')
plt.show()