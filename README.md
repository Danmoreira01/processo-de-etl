# processo-de-etl
Data Manipulation and SQL Connection Project
Este repositório contém um projeto que exemplifica como manipular dados no Python usando pandas, além de estabelecer conexão e enviar dados para um banco de dados SQL Server.

Pré-requisitos
Certifique-se de que você tenha as seguintes bibliotecas instaladas no seu ambiente Python:

pandas

pyodbc

sqlalchemy

openpyxl (para leitura de arquivos Excel)

Você pode instalar essas bibliotecas usando o pip:

pip install pandas pyodbc sqlalchemy openpyxl
Passos do Código
Verificar Drivers ODBC Instalados

Utiliza pyodbc.drivers() para listar todos os drivers ODBC disponíveis.

Manipulação de Dados com pandas

Lê um arquivo Excel e remove espaços em branco nos nomes das colunas.

Substitui valores nulos na coluna Telefone por 0.

Substitui valores nulos na coluna Valor por 0 e conta quantos valores 0 existem.

Remove entradas nulas na coluna Nome.

Configurações pandas

Ajusta a exibição de números para formato inteiro.

Conexão com SQL Server

Estabelece uma conexão com um banco de dados SQL Server utilizando sqlalchemy.

Cria uma tabela chamada Valor e insere os dados do DataFrame.

Configurações de Conexão
Os parâmetros para conexão com o SQL Server podem ser ajustados conforme sua configuração:

server: Nome do servidor SQL Server.

database: Nome do banco de dados.

driver: Driver ODBC atualizado (Ex.: ODBC Driver 18 for SQL Server).

Exemplo de String de Conexão

database_con = f'mssql+pyodbc://@{server}/{database}?driver={driver}&Encrypt=no'

Observação
Certifique-se de que seu servidor SQL Server está configurado corretamente e que o driver ODBC mencionado está instalado no sistema.

Execução
Para rodar o código, apenas execute o script Python. Certifique-se de ajustar os caminhos dos arquivos, como o arquivo Excel, e as configurações do banco de dados, conforme necessário.



processo de etl
