import pandas as pd
import yfinance as yf
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv


def create_postgres_engine():
    # Carrega variáveis de ambiente do arquivo .env
    load_dotenv()

    # Obtém as variáveis de ambiente
    username = os.getenv('DB_USERNAME')
    password = os.getenv('DB_PASSWORD')
    host = os.getenv('DB_HOST')
    port = os.getenv('DB_PORT')
    database = os.getenv('DB_NAME')

    # Cria a URL de conexão
    url = f'postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}'
    
    # Cria e retorna o engine
    engine = create_engine(url)
    return engine

# lista de tickers 
tickers_banco = [
    'ITUB4.SA',
    'BBDC4.SA',
    'BBAS3.SA',
    'SANB11.SA',
    'BPAC11.SA'
]

def buscar_dados_tickers(simbolo, periodo= '5d', intervalo='1d'):
    ticker = yf.Ticker(simbolo)
    dados = ticker.history(period=periodo, interval=intervalo)[['Close']]
    dados['simbolo']= simbolo
    return dados

    
def buscar_todos_dados_tickers(tickers_banco):
    todos_dados= []
    for simbolo in tickers_banco:
        dados = buscar_dados_tickers(simbolo)
        todos_dados.append(dados)
    return pd.concat(todos_dados)

def salvar_postgres(df, engine):
    df.to_sql('tickers_banco', engine, schema='public', if_exists='replace', index=True, index_label=None)

if __name__ == '__main__':
    dados_tickers = buscar_todos_dados_tickers(tickers_banco)
    engine = create_postgres_engine()
    salvar_postgres(dados_tickers, engine)
    
    