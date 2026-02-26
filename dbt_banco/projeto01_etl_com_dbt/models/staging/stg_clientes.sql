{{
    config(
        materialized='view'
    )
}}

WITH source AS (
    SELECT * FROM {{ ref('raw_clientes') }}
),

transformation AS (
    SELECT
        CAST(id AS INTEGER) AS id_cliente,
        TRIM(
            REGEXP_REPLACE(CAST(nome as VARCHAR(255)), '^(Sr\.|Sra\.|Srta\.|Dr\.|Dra\.)\s*', '', 'gi')
        ) AS nome_cliente,
        TRIM(CAST(email AS VARCHAR(255))) AS email_cliente,
        CAST(datacadastro AS DATE) AS data_cadastro
    FROM source
)

SELECT * FROM transformation