{{ config(materialized='view') }}

WITH source AS (
    SELECT
        CAST("Date" as date) as data,
    "Close"AS valor_fechamento, 
        simbolo as ticker
    FROM {{ source('sources', 'tickers_banco') }}
)

SELECT
    data,
    valor_fechamento,
    ticker
FROM source
