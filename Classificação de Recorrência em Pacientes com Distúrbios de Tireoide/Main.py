import pandas as pd
from sklearn.preprocessing import LabelEncoder  
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import os
import numpy as np 

# Buscando os dados no arquivo "Thyroid_Diff.csv" e os transformando em DataFrame.
diretorio_atual = os.path.dirname(os.path.abspath(__file__))
aquivoscv = os.path.join(diretorio_atual, 'Thyroid_Diff.csv')

data = pd.read_csv(aquivoscv)

data = pd.get_dummies(data, columns=['Age','Gender','Smoking','Hx Smoking','Hx Radiothreapy','Thyroid Function','Physical Examination','Adenopathy','Pathology','Focality','Risk','T','N','M','Stage','Response'])

# Criação e treinamento da máquina.
x = data.drop(columns=['Recurred'])
label_encoder = LabelEncoder()
data['Recurred'] = label_encoder.fit_transform(data['Recurred'])
y = data['Recurred']
x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.3, random_state=34)
model = RandomForestClassifier(n_estimators=100, random_state=34)
model.fit(x_treino, y_treino)
previsao = model.predict(x_teste)
presisao = accuracy_score(y_teste, previsao)

# Mostrando o relatório de testes da máquina.
print(f'Acurácia do modelo: {presisao}\n')
print('Relátorio:')
print(classification_report(y_teste, previsao))

# Testando com novos dados, a resposta esperada é "0" ou nesse caso, "Não".
dados = pd.DataFrame({'Age': [27],
                      'Gender': ['F'],
                      'Smoking': ['No'],
                      'Hx Smoking': ['No'],
                      'Hx Radiothreapy': ['No'],
                      'Thyroid Function': ['Euthyroid'],
                      'Physical Examination': ['Single nodular goiter-left'],
                      'Adenopathy': ['No'],
                      'Pathology': ['Micropapillary'],
                      'Focality': ['Uni-Focal'],
                      'Risk': ['Low'],
                      'T': ['T1a'],
                      'N': ['N0'],
                      'M': ['M0'],
                      'Stage': ['I'],
                      'Response': ['Indeterminate']})

amostra = pd.get_dummies(dados, columns=['Age','Gender','Smoking','Hx Smoking','Hx Radiothreapy','Thyroid Function','Physical Examination','Adenopathy','Pathology','Focality','Risk','T','N','M','Stage','Response'])
amostra = amostra.reindex(columns = x.columns, fill_value=0)
nova_previsao = model.predict(amostra)
nova_previsao_rotulada = np.where(nova_previsao == 0, 'Nao', 'Sim')

print(nova_previsao_rotulada) # Saída: ['Não']

# Funcionou adequadamente.