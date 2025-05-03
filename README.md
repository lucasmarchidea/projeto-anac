# Projeto ANAC — Importação de Dados com Psycopg2

Este projeto é uma introdução prática ao uso de Python para ETL (Extract, Transform, Load) e demonstra o processo completo de importação de dados a partir de um arquivo JSON para um banco de dados PostgreSQL, utilizando Python e a biblioteca `psycopg2`.

---

## 🔧 Funcionalidades

- Leitura de arquivo `.json` com dados de ocorrências da ANAC.
- Seleção e tratamento das colunas relevantes.
- Conexão com o banco de dados PostgreSQL.
- Limpeza da tabela de destino antes da carga.
- Inserção de dados linha a linha no banco de dados.
- Confirmação e finalização da transação com segurança.

---

## 🧰 Tecnologias Utilizadas

- **Python** — linguagem de programação utilizada para processar os dados.
- **Pandas** — para leitura e manipulação dos dados.
- **psycopg2** — biblioteca usada para conectar e interagir com o PostgreSQL.
- **PostgreSQL** — banco de dados relacional onde os dados foram armazenados.

---

## 📁 Etapas do Processo

1. **Importação do arquivo JSON**
   - O arquivo foi lido utilizando `pandas.read_json()` com suporte para acentuação via `utf-8-sig`.

2. **Seleção e renomeação de colunas**
   - Apenas as colunas necessárias foram mantidas.
   - Foi feita a padronização de nomes para facilitar o uso no banco.

3. **Configuração da conexão**
   - Definidos os parâmetros de acesso ao banco de dados PostgreSQL.
   - Criada a conexão e o cursor com `psycopg2`.

4. **Limpeza da tabela**
   - Foi executado um `DELETE` para garantir que não houvesse dados duplicados antes da nova carga.

5. **Inserção dos dados**
   - Os dados foram inseridos linha por linha com `cursor.execute()`.

6. **Validação e encerramento**
   - A transação foi confirmada com `conn.commit()`.
   - A conexão foi encerrada com segurança.

---

## 🗂️ Estrutura Esperada da Tabela no Banco

A tabela `Anac` deve conter os seguintes campos:

- `Numero_da_Ocorrencia` — Inteiro
- `Classificacao_da_Ocorrencia` — Texto
- `Data_da_Ocorrencia` — Data
- `Municipio` — Texto
- `UF` — Texto
- `Regiao` — Texto
- `Nome_do_Fabricante` — Texto

