import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import matplotlib.pyplot as plt

# Carregar dataset
df = pd.read_csv("student/student-mat.csv", sep=';')

# Criando uma nova coluna 'media'
df['media'] = (df['G1'] + df['G2'] + df['G3']) / 3

# Classificar desempenho
def classificar_desempenho(nota):
    if nota <= 10:
        # 10
        return "baixo desempenho"
    elif nota <= 15:
        return "medio desempenho"
    else:
        return "alto desempenho"

df['desempenho'] = df['media'].apply(classificar_desempenho)
print(df['desempenho'])
# Consumo total de álcool
df['consumo_fim_emana'] = df['Walc']
print(df['consumo_fim_emana'])

# Classificar consumo
def classificar_consumo(consumo):
    if consumo <= 2:
        return "baixo consumo"
    elif consumo <= 3:
        return "medio consumo"
    else:
        return "alto consumo"

df['consumo'] = df['consumo_fim_emana'].apply(classificar_consumo)

# Variáveis explicativas
X = df[['Walc']]

# Variável alvo
y = df['desempenho']

# Modelo
modelo = DecisionTreeClassifier(
    criterion='entropy',
    max_depth=3,
    random_state=42
)

modelo.fit(X, y)

# ---------------------------
# ÁRVORE DE DECISÃO
# ---------------------------

plt.figure(figsize=(12,7))

tree.plot_tree(
    modelo,
    feature_names=['Álcool Fim Semana (Walc)'],
    class_names=modelo.classes_,
    filled=True,
    rounded=True
)

plt.title("Árvore de Decisão: Consumo de Álcool vs Desempenho")
plt.show()

