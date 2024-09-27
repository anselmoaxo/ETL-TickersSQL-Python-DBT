# Projeto: Integração de Dados de Ações com DBT e PostgreSQL

Este projeto tem como objetivo buscar dados históricos de ações de bancos brasileiros através da API `yfinance`, realizar o processamento desses dados e armazená-los em um banco de dados PostgreSQL. Para orquestrar as transformações e garantir a organização das tabelas, o projeto utiliza a ferramenta `DBT` (Data Build Tool).

## Visão Geral

O projeto se divide em três partes principais:
1. **Coleta de Dados**: Utilizamos o `yfinance` para coletar dados de fechamento de ações de alguns dos principais bancos brasileiros.
2. **Processamento e Armazenamento**: Os dados são processados e armazenados em uma tabela PostgreSQL.
3. **Transformação de Dados**: Utilizamos o DBT para transformar e organizar os dados no banco, facilitando futuras análises e visualizações.

## Stack Tecnológica

- **Python**: Utilizado para buscar e processar os dados da API `yfinance`.
- **PostgreSQL**: Banco de dados relacional para armazenar os dados.
- **SQLAlchemy**: Para conectar e realizar operações no banco PostgreSQL.
- **DBT**: Ferramenta de transformação de dados que organiza e gerencia o processo de transformação.
- **YFinance**: Biblioteca para obter dados financeiros de ações.
- **Pandas**: Manipulação e tratamento de dados.

## Instalação e Configuração

### Pré-requisitos

Antes de começar, certifique-se de ter os seguintes requisitos instalados:

- [Python 3.8+](https://www.python.org/downloads/)
- [PostgreSQL](https://www.postgresql.org/download/)
- [DBT](https://docs.getdbt.com/docs/installation)

### Passos de Instalação

1. Clone o repositório do projeto:

   ```bash
   git clone https://github.com/anselmoaxo/ETL-TickersSQL-Python-DBT.git
