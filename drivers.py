# %%
from pyodbc import drivers
for driver in drivers():
    print(driver)
# %%
import pandas as pd 
#%%
from sqlalchemy import create_engine
# %%
pd.set_option('display.float_format', '{:.0f}'.format)
dados = pd.read_excel(r'C:\Users\dadam\OneDrive\Área de Trabalho\projetos\pasta1.xlsx')
dados.columns = dados.columns.str.strip()
dados.head()
# %%
dados['Valor'].sum()
# %%
dados['Nome']
# %%
dados['Telefone'] = dados['Telefone'].fillna(0)
dados['Telefone'].head(50)
# %%
dados['Valor'] = dados['Valor'].fillna(0)
quantidade_zero = (dados['Valor'] == 0).sum
quantidade_zero
# %%
quantidade_zero = (dados['Valor'] == 0).sum()
quantidade_zero
# %%
dados = dados.dropna(subset=['Nome'])
dados['Nome'].head(50)
# %%
from sqlalchemy import create_engine

# Configurar as informações do banco de dados SQL Server
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
dados.to_sql('Valor', con=con, index = False, if_exists = 'append')