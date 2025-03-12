# %%
import pandas as pd 
# %%
df = pd.read_csv('fatura-inter-2025-04.csv', sep= ',')
df.head()
# %%
df.to_excel('cartãomarco.xlsx', index=False)
# %%
df['Valor'] = df['Valor'].str.replace('R$', '', regex=False).str.replace('.', '').str.replace(',', '.').astype(float)
# %%
soma_valores = df['Valor'].sum()

print(f'A soma total dos valores é: R$ {soma_valores:.2f}')


# %%
df.describe
# %%
df['Tipo'].unique
# %%
gasto_por_categoria = df.groupby('Categoria')['Valor'].sum().sort_values(ascending=False)
gasto_por_categoria

# %%
maior_gasto = df.loc[df['Valor'].idxmax()]
print(maior_gasto)

# %%
import matplotlib.pyplot as plt
import seaborn as sns

# Gráfico de gastos por categoria
plt.figure(figsize=(10, 5))
sns.barplot(x=gasto_por_categoria.index, y=gasto_por_categoria.values)
plt.xticks(rotation=45)
plt.title('Total gasto por categoria')
plt.show()

# %%
df_compras = df[df['Categoria'] == 'COMPRAS']
df_compras
# %%
