{{
    config(
        materialized='view'
    )
}}

WITH source AS(
    SELECT * FROM {{ref('raw_pedidos')}}
),

transformation AS (
    SELECT
        CAST(id_pedido AS INTEGER) as id_pedido,
        CAST(id_cliente AS INTEGER) AS id_cliente,
        CAST(valor AS DECIMAL(18,2)) as valor_pedido,
        CAST(status as VARCHAR(255)) as status_pedido,
        CAST(data_pedido AS DATE) as data_pedido
    FROM source
)

SELECT * FROM transformation