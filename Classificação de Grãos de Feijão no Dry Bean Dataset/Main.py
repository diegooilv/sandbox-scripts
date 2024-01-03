import pandas as pd 
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Importando os dados do arquivo 'Dry_Bean_Dataset.xlsx' e o transformando em DataFrame
diretorio_atual = os.path.dirname(os.path.abspath(__file__))
arquivo = os.path.join(diretorio_atual, 'Dry_Bean_Dataset.xlsx')
data = pd.read_excel(arquivo)

x = data.drop(columns=['Class'])
y = data['Class']

# Criando e treinando a máquina.
x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.2, random_state=34)
modelo = RandomForestClassifier(n_estimators=110, random_state=34)
modelo.fit(x_treino, y_treino)

# Testando a máquina.
previsoes = modelo.predict(x_teste)

# Verificando a acurácia da máquina.
acuracia = accuracy_score(y_teste, previsoes)
print(f'Acurácia: {acuracia}\n')
print('Relátorio de Classificação:')
print(classification_report(y_teste, previsoes))

# Testando com outros valores.
teste = pd.DataFrame({
    'Area': [28.395],
    'Perimeter': [610.29],
    'MajorAxisLength': [208.18],
    'MinorAxisLength': [173.89],
    'AspectRation': [1.20],
    'Eccentricity': [0.55],
    'ConvexArea': [28715],
    'EquivDiameter': [190.14],
    'Extent': [0.76],
    'Solidity': [0.99],
    'roundness': [0.96],
    'Compactness': [0.91],
    'ShapeFactor1': [0.01],
    'ShapeFactor2': [0.00],
    'ShapeFactor3': [0.83],
    'ShapeFactor4': [1.00]
})
nova_previsao = modelo.predict(teste)
print(nova_previsao)