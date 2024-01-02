# Passo a Passo para Criar um Modelo de Machine Learning para Prever Recorrência em Câncer de Tireoide

Vamos utilizar um conjunto de dados com as seguintes características: Age, Gender, Smoking, Hx Smoking, Hx Radiotherapy, Thyroid Function, Physical Examination, Adenopathy, Pathology, Focality, Risk, T, N, M, Stage, Response, Recurred.

### 1. Importar Bibliotecas

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
```

### 2. Carregar e Explorar o Conjunto de Dados

```python
# Carregar o conjunto de dados
data = pd.read_csv("seu_dataset.csv")

# Visualizar as primeiras linhas do conjunto de dados
print(data.head())

# Verificar informações sobre o conjunto de dados
print(data.info())
```

### 3. Pré-processamento de Dados

```python
# Remover colunas desnecessárias (se necessário)
data = data.drop(columns=['Patient_ID', 'Other_Unnamed_Columns'])

# Converter variáveis categóricas em numéricas usando one-hot encoding
data = pd.get_dummies(data, columns=['Gender', 'Smoking', 'Hx Smoking', 'Hx Radiotherapy', 'Thyroid Function', 'Physical Examination', 'Adenopathy', 'Pathology', 'Focality', 'Risk', 'Stage', 'Response'])

# Dividir o conjunto de dados em recursos (X) e rótulos (y)
X = data.drop(columns=['Recurred'])
y = data['Recurred']
```

### 4. Dividir o Conjunto de Dados em Treino e Teste

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```

### 5. Criar e Treinar o Modelo

```python
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
```

### 6. Fazer Previsões e Avaliar o Modelo

```python
predictions = model.predict(X_test)

# Avaliar a precisão do modelo
accuracy = accuracy_score(y_test, predictions)
print(f'Acurácia do modelo: {accuracy}')

# Exibir relatório de classificação
print(classification_report(y_test, predictions))
```

### 7. Otimizar Hiperparâmetros (Opcional)

```python
from sklearn.model_selection import GridSearchCV

param_grid = {'n_estimators': [50, 100, 200], 'max_depth': [None, 10, 20]}
grid_search = GridSearchCV(RandomForestClassifier(random_state=42), param_grid, cv=3)
grid_search.fit(X_train, y_train)

best_params = grid_search.best_params_
print(f'Melhores Hiperparâmetros: {best_params}')
```

## Link do conjunto de dados:
- https://archive.ics.uci.edu/dataset/915/differentiated+thyroid+cancer+recurrence
- https://archive.ics.uci.edu/static/public/915/differentiated+thyroid+cancer+recurrence.zip