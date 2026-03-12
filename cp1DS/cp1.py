import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('vgsales.csv')
print(df.head())
print(df.info())
print(df.isnull().sum())

# remover linhas sem ano ou editora
df_clean = df.dropna().copy()

# estatística descritiva
vendas = df_clean['Global_Sales']

print(f"Média de Vendas: {vendas.mean():.2f}")
print(f"Mediana de Vendas: {vendas.median():.2f}")
print(f"Desvio-Padrão: {vendas.std():.2f}")

#histogramas
plt.figure(figsize=(10, 5))
plt.hist(vendas, bins=50, range=(0, 2), edgecolor='black') # limitando para ver melhor o 'miolo'
plt.title('Distribuição de Vendas Globais')
plt.xlabel('Milhões de Unidades')
plt.ylabel('Frequência')
plt.show()

# outliers com IQR e boxplot
Q1 = vendas.quantile(0.25)
Q3 = vendas.quantile(0.75)
IQR = Q3 - Q1
limite_superior = Q3 + 1.5 * IQR
print(f"limite para Outliers: {limite_superior:.2f}")

#correlação e scatterplot
par_vendas = df_clean[['NA_Sales', 'EU_Sales']]
correlacao = par_vendas.corr(method='pearson')

print("\n--- Matriz de Correlação ---")
print(correlacao)

plt.figure(figsize=(7, 5))
plt.scatter(df_clean['NA_Sales'], df_clean['EU_Sales'], alpha=0.3)
plt.title('Scatterplot: Vendas NA vs Europa')
plt.xlabel('Vendas América do Norte (Mi)')
plt.ylabel('Vendas Europa (Mi)')
plt.show()

#boxplot antes de remover
plt.figure(figsize=(8, 4))
plt.boxplot(vendas, vert=False)
plt.title('boxplot: vendas globais (com Outliers)')
plt.show()
