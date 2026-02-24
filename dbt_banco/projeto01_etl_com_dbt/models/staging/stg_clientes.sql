{{
    config(
        materialized='view'
    )
}}

/*
    A primeira CTE sempre deve importar os dados crus.
    Usamos a macro ref() para referenciar a seed. Isso garante
    que o dbt construa o DAG e a linhagem de dados corretamente.
*/
WITH source AS (

    SELECT * FROM {{ ref('raw_clientes') }}

),

/*
    A segunda CTE e onde fazemos a limpeza.
    Padronizacao de nomes (snake_case), tipagem explicita de colunas,
    e tratamento inicial de nulos.
*/
renamed AS (

    SELECT
        CAST(id AS INTEGER) AS id_cliente,
        CAST(nome AS VARCHAR(255)) AS nome_cliente,
        CAST(email AS VARCHAR(255)) AS email_cliente,
        CAST(data_cadastro AS DATE) AS data_cadastro

    FROM source

)

/*
    A query final sempre e um SELECT simples da ultima CTE.
    Isso facilita muito o debug. Se voce quiser ver como os dados
    estavam antes da limpeza, basta trocar 'FROM renamed' para 'FROM source'.
*/
SELECT * FROM renamed