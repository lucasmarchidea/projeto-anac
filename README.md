# Projeto ANAC

Este projeto tem como objetivo demonstrar a importação de dados de um arquivo JSON para um banco de dados PostgreSQL, realizando a limpeza e transformação dos dados.

## Passos realizados

1. **Importação do arquivo JSON**: O arquivo JSON foi carregado para um DataFrame utilizando a biblioteca 'pandas'.

2. **Seleção e tratamento de dados**: 
   - Foram selecionadas as colunas mais relevantes do arquivo.
   - Algumas colunas foram renomeadas para remover acentos e melhorar a compatibilidade com o banco de dados.

3. **Criação do banco de dados e da tabela**:
   - O banco de dados foi criado no PostgreSQL (usando o 'pgAdmin').
   - A tabela foi definida com as colunas necessárias para armazenar as informações.

4. **Configuração da conexão com o banco de dados**:
   - Foi estabelecida uma conexão com o banco de dados PostgreSQL utilizando a biblioteca 'psycopg2'.

5. **Importação dos dados para o banco**:
   - Antes da importação, a tabela foi limpa utilizando o comando 'DELETE'.
   - Os dados foram então inseridos no banco de dados por meio de um loop que percorre o DataFrame.

6. **Validação e fechamento da conexão**:
   - Após a importação, as alterações foram confirmadas com 'conn.commit()'.
   - A conexão foi encerrada corretamente para garantir que os dados fossem gravados de forma segura.

7. **Refatoração do código**:
   - O código foi refatorado para melhorar a legibilidade e a eficiência.

## Tecnologias utilizadas

- **Python**: Linguagem utilizada para o processamento de dados e a conexão com o banco de dados.
- **Pandas**: Para manipulação de dados e criação do DataFrame.
- **psycopg2**: Biblioteca Python para conexão e manipulação de dados em PostgreSQL.
