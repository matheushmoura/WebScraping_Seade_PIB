import pandas as pd
import matplotlib.pyplot as plt
from downloadTabelas import downloadTabela
import os

datasp = pd.DataFrame(columns=['ano', 'sp', 'sbc', 'g', 'c', 'sjc'])
# Reading data downloaded in'seade.gov.br'
downloadTabela()
# Plotting

import glob, os
os.chdir("C:/Users/Matheus/Documents/PIBbrasil/SeadeFiles/")
for file in glob.glob("*.xlsx"):
    filesplit = file.split('pib_')[1]
    filesplit2 = filesplit.split('.')[0]
    year = filesplit2.split('-')[0]
    print(year)

    df = pd.read_excel(file, header=10)
    os.remove(file)
    df.columns = ['MUNICIPIO', 'AGROPECUARIA', 'INDUSTRIA', 'ADM PUBLICA', 'SUBTOTAL', 'TOTAL', 'IMPOSTOS', 'PIB', 'PIB CAPITA']
    print(df)
    datasp = datasp.append({
        'ano': str(year),
        'sp': df.loc[df['MUNICIPIO'] == "São Paulo"]['PIB CAPITA'].values,
        'sbc': df.loc[df['MUNICIPIO'] == "São Bernardo do Campo"]['PIB CAPITA'].values,
        'g': df.loc[df['MUNICIPIO'] == "Guarulhos"]['PIB CAPITA'].values,
        'c': df.loc[df['MUNICIPIO'] == "Campinas"]['PIB CAPITA'].values,
        'sjc': df.loc[df['MUNICIPIO'] == "São José dos Campos"]['PIB CAPITA'].values
    }, ignore_index=True)

print(datasp)

# plotting
ax = plt.gca()
ax.set_facecolor('#F6F9ED')
datasp['sp'] = datasp['sp'].astype(float)
datasp['sbc'] = datasp['sbc'].astype(float)
datasp['g'] = datasp['g'].astype(float)
datasp['c'] = datasp['c'].astype(float)
datasp['sjc'] = datasp['sjc'].astype(float)

datasp.plot(kind='line', x='ano', y='sp', label='São Paulo (SP)', ax=ax, color='#42124C')
datasp.plot(kind='line', x='ano', y='c', label='Campinas (SP)', ax=ax, color='#2FF3E0')
datasp.plot(kind='line', x='ano', y='g', label='Guarulhos (SP)', ax=ax, color='#F8D210')
datasp.plot(kind='line', x='ano', y='sbc', label='São Bernardo do Campo (SP)', ax=ax, color='#FA26A0')
datasp.plot(kind='line', x='ano', y='sjc', label='São José dos Campos (SP)', ax=ax, color='#F51720')

ax.grid(False)
plt.title(' Gross Domestic Product (GDP) \n of the 5 largest cities in São Paulo (State)', fontsize=14, alpha=0.8)
plt.ylabel('GDP Per Capita in Real(R$)', fontsize=13, alpha=0.8)
plt.xlabel('Year', fontsize=13, alpha=0.8)
plt.tick_params(top='off', right='off', labelbottom='on')
plt.show()