# Importar bibliotecas

# Ler o arquivo Json
import pandas as pd 
# Conexão com o banco de dados
import psycopg2

# Importar o arquivo Json
caminho_do_arquivo = r"C:\Users\Luq\Downloads\Curso eng dados\Arquivos\01. Postgree\Origem de dados\V_OCORRENCIA_AMPLA.json"
df = pd.read_json(caminho_do_arquivo, encoding='utf-8-sig')

# Selecionar colunas
colunas = ['Numero_da_Ocorrencia', 'Classificacao_da_Ocorrência', 'Data_da_Ocorrencia', 'Municipio', 'UF', 'Regiao', 'Nome_do_Fabricante']
df = df[colunas]

# Renomear colunas
df.rename(columns={'Classificacao_da_Ocorrência':'Classificacao_da_Ocorrencia'}, inplace=True)

# Parâmetros de conexão
dbname   = 'python'
user     = 'postgres'
password = '123456'
host     = 'localhost'
port     = '5432'

# Criar a conexão
conn = psycopg2.connect(dbname=dbname,user=user,password=password,host=host,port=port)

# Criar um cursor para poder manipular os dados
cur = conn.cursor()

# Deleta a base antes da carga
cur.execute('delete from public.Anac')
cur.execute('delete from public.Anac')

# Carga de dados
for indice,coluna_df in df.iterrows(): 
    cur.execute( """    insert into Anac (     
                Numero_da_Ocorrencia, 
                Classificacao_da_Ocorrencia, 
                Data_da_Ocorrencia, 
                Municipio, 
                UF, 
                Regiao, 
                Nome_do_Fabricante
            ) VALUES (%s,%s,%s,%s,%s,%s,%s)              

            """ ,(
                coluna_df["Numero_da_Ocorrencia"],
                coluna_df["Classificacao_da_Ocorrencia"],
                coluna_df["Data_da_Ocorrencia"],
                coluna_df["Municipio"],
                coluna_df["UF"],
                coluna_df["Regiao"],
                coluna_df["Nome_do_Fabricante"]
            )
            )


# Validar alterações realizadas e subir para o banco de dados
conn.commit()

# Fechar o cursor e a conexão
cur.close()
conn.close()


