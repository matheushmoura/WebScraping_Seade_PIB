import pandas as pd
import matplotlib.pyplot as plt
from downloadTabelas import downloadTabela
import os

datasp = pd.DataFrame(columns=['ano', 'sp', 'pp', 'g', 'c'])
# Reading data downloaded in'seade.gov.br'
downloadTabela()
# Plotting
for x in range(2002, 2019):
    df = pd.read_excel("SeadeFiles/tab_pib_" + str(x) + ".xlsx", header=10)
    os.remove("SeadeFiles/tab_pib_" + str(x) + ".xlsx")
    df.columns = ['MUNICIPIO', 'AGROPECUARIA', 'INDUSTRIA', 'ADM PUBLICA', 'SUBTOTAL', 'TOTAL', 'IMPOSTOS', 'PIB', 'PIB CAPITA']
    print(df)
    datasp = datasp.append({
        'ano': str(x),
        'sp': df.loc[df['MUNICIPIO'] == "São Paulo"]['PIB CAPITA'].values * 1000,
        'pp': df.loc[df['MUNICIPIO'] == "Presidente Prudente"]['PIB CAPITA'].values * 1000,
        'g': df.loc[df['MUNICIPIO'] == "Guarulhos"]['PIB CAPITA'].values * 1000,
        'c': df.loc[df['MUNICIPIO'] == "Campinas"]['PIB CAPITA'].values * 1000
    }, ignore_index=True)

print(datasp)

# plotting
ax = plt.gca()

ax.set_facecolor('#F6F9ED')

datasp = datasp.astype(float)
datasp.plot(kind='line', x='ano', y='sp', label='São Paulo (SP)', ax=ax, color='#42124C')
datasp.plot(kind='line', x='ano', y='c', label='Campinas (SP)', ax=ax, color='#FE0472')
datasp.plot(kind='line', x='ano', y='g', label='Guarulhos (SP)', ax=ax, color='#8AFF00')
datasp.plot(kind='line', x='ano', y='pp', label='Presidente Prudente (SP)', ax=ax, color='#C3FF13')

ax.grid(False)
plt.title(' Gross Domestic Product (GDP) \n Of the 5 largest cities in São Paulo (State)',
          fontsize=14, alpha=0.8)
plt.ylabel('GDP Per Capita in Real(R$)', fontsize=13, alpha=0.8)
plt.xlabel('Year', fontsize=13, alpha=0.8)

plt.tick_params(top='off', right='off', labelbottom='on')
plt.show()