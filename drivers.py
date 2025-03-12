# %%
# importando as bibliotecas para saber qual a versão do meu Driver ODBC
from pyodbc import drivers
for driver in drivers():
    print(driver)
# %%
# Importando pandas para fazer a manipulação dos dados
import pandas as pd 
#%%
# Importando sqlalchemy para fazer a conexão com o SQL
from sqlalchemy import create_engine
# %%
# Ajustando a exibição dos numeros para int
pd.set_option('display.float_format', '{:.0f}'.format)
# Lendo o arquivo em Excel pelo pandas
dados = pd.read_excel(r'C:\Users\dadam\OneDrive\Área de Trabalho\projetos\pasta1.xlsx')
#removendo os espaços em branco no nome das colunas 
dados.columns = dados.columns.str.strip()
# lendo as 10 primeiras linhas do meu dataframe
dados.head(10)
# %%
# Trocando os valores nulos da coluna Telefone por 0
dados['Telefone'] = dados['Telefone'].fillna(0)
dados['Telefone']
# %%
# mudando os valores nulos da coluna Valor por 0
dados['Valor'] = dados['Valor'].fillna(0)
quantidade_zero = (dados['Valor'] == 0).sum
quantidade_zero
# %%
# exibindo quantos valores 0 tem na coluna Valor
quantidade_zero = (dados['Valor'] == 0).sum()
quantidade_zero
# %%
# apagando os nomes da coluna Nome onde a informação é nula
dados = dados.dropna(subset=['Nome'])
dados['Nome'].head(50)
# %%
# Criando a conexão com o banco de dados no Sql


server = 'DESKTOP-09DJ67M\\SQLEXPRESS'  # Nome do servidor SQL Server
database = 'Estudos'  # Nome do banco de dados
driver = 'ODBC Driver 18 for SQL Server'  # Driver ODBC atualizado

# String de conexão
database_con = f'mssql+pyodbc://@{server}/{database}?driver={driver}&Encrypt=no'

# Criar a engine
engine = create_engine(database_con, fast_executemany=True)

# Estabelecer a conexão
con = engine.connect()

print("Conexão com SQL Server estabelecida com sucesso!")

# %%
dados.columns
# %%
# criando uma tabela no sql com o nome de Valor
dados.to_sql('Valor', con=con, index = False, if_exists = 'append')

