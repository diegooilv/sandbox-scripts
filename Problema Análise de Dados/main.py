import os
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np

diretorio_atual = os.path.dirname(os.path.abspath(__file__))
arquivo = os.path.join(diretorio_atual, 'ecommerce_data.csv')
df = pd.read_csv(arquivo)

# Data - Produto - Categoria - Quantidade - Preço Unitário - Cliente - Região

# Calculando as médias de vendas por mês.
df['Data'] = pd.to_datetime(df['Data'])
df['Vendas Totais'] = df['Quantidade'] * df['Preço Unitário']
medias = df.groupby(df['Data'].dt.month)['Vendas Totais'].sum().reset_index()

# Mostrando no gráfico.
plt.figure(figsize=(10, 6))

plt.plot(medias['Data'], medias['Vendas Totais'].round(2), marker='o', linestyle='-', color='r', label='Vendas')
plt.grid(True, linestyle='-', alpha=0.5)
plt.title('Vendas por mês')
plt.xlabel('Data')
plt.xlabel('Meses')
for i, valor in enumerate(medias['Vendas Totais']):
    plt.text(i, valor + 50, f'R$ {valor:.2f}', ha='left', va='bottom', rotation=35)
plt.show()


# Determinando as categorias de produtos que mais contribuíram para as vendas totais.
produtos = df.groupby('Categoria')['Vendas Totais'].sum().reset_index()
produtos['Vendas Totais'] = produtos['Vendas Totais'].round(2)
produtos = produtos.sort_values(by='Vendas Totais', ascending=False)

# Criação do Gráfico
plt.figure(figsize=(10,6))
plt.bar(produtos['Categoria'], produtos['Vendas Totais'].round(2), color='skyblue')
plt.title('Vendas por categoria.')

for i, valor in enumerate(produtos['Vendas Totais']):
    plt.text(i, valor + 50, f'R$ {valor:.2f}', ha='center', va='bottom')

plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.show()

# Clientes frequentes.
clientes = df.groupby('Cliente')['Vendas Totais'].sum().reset_index()  
for i in range(len(clientes['Cliente'])):
    print(f'Cliente: {clientes['Cliente'][i]} gastou {clientes['Vendas Totais'][i]:.2f} reais!')

# Variação de preços dos produtos.
# Analise a variação percentual média nos preços dos produtos de um mês para o outro.
var = []
medias = df.groupby(df['Data'].dt.month)['Preço Unitário'].mean().reset_index()

for i in range(1, len(medias)):
    var.append(((medias['Preço Unitário'].iloc[i] * 100) / medias['Preço Unitário'].iloc[i-1]) - 100)
medias['Variacao'] = [0] + var

medias = medias.sort_values(by='Data')

plt.figure(figsize=(8, 4))
plt.bar(medias['Data'], medias['Variacao'], color='r')
for i in range(len(medias)):
    if medias['Variacao'].iloc[i] > 0:
        plt.text(medias['Data'].iloc[i], medias['Variacao'].iloc[i], f'{medias['Variacao'].iloc[i]:.2f}%', ha='center', va='bottom')
    else:
        plt.text(medias['Data'].iloc[i], medias['Variacao'].iloc[i], f'{medias['Variacao'].iloc[i]:.2f}%', ha='center', va='top')
plt.xlabel('Meses')
plt.ylabel('Variação em %')
plt.title('Variação percentual média nos preços dos produtos de um mês para o outro.')
plt.xticks(np.arange(1, 13))
plt.show()

# Criação do Gráfico de preços médios por mês.
largura = 0.25
plt.figure(figsize=(10, 6))
plt.bar(medias['Data'], medias['Preço Unitário'].round(2), color='r')
plt.title('Gráfico de Médias de Preço')
plt.xticks(np.arange(1, 13))
plt.ylabel('Preço médio unitário.')
plt.xlabel('Mês')
for i, (data, valor) in enumerate(zip(medias['Data'], medias['Preço Unitário'])):
    plt.text(data, valor + 0.05, f'{valor:.2f} R$', ha='center', va='bottom')
plt.show()

# Análise Regional
regiao = df.groupby('Região')['Vendas Totais'].sum().reset_index()

plt.figure(figsize=(4,4))
plt.pie(regiao['Vendas Totais'], labels=regiao['Região'], autopct='%1.1f%%', startangle=140, colors=['lightcoral', 'lightskyblue', 'lightgreen', 'lightgray', 'gold'])
plt.title('Vendas por região')
plt.show()

# Padrões temporais de compras.
dias = df.groupby(df['Data'].dt.day)['Vendas Totais'].sum().reset_index()
print(dias)
plt.figure(figsize=(13, 4))

plt.bar(dias['Data'], dias['Vendas Totais'], color='b')
plt.xticks(np.arange(1, 32))
plt.ylabel('Vendas (R$)')
plt.xlabel('Dias do mês')
plt.title('Vendas por dia do mês.')
for i in range(len(dias)):
    plt.text(dias['Data'].iloc[i], dias['Vendas Totais'].iloc[i] + 2, f'{dias['Vendas Totais'].iloc[i]:.2f}', ha='center', va='bottom', fontsize=5)
plt.show()
