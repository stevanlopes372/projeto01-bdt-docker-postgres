{{
    config(
        materialized='incremental',
        unique_key='id_pedido'
    )
}}
WITH pedidos AS (
    SELECT * FROM {{ ref('stg_pedidos') }}
    
    {% if is_incremental() %}
    WHERE data_pedido > (SELECT MAX(data_pedido) FROM {{ this }})
    {% endif %}
),

clientes AS (
    SELECT * FROM {{ ref('stg_clientes') }}
),
fct_pedidos AS (
    SELECT
        p.id_pedido,
        p.id_cliente,
        c.nome_cliente,
        p.valor_pedido,
        p.status_pedido,
        p.data_pedido
    FROM pedidos p
    LEFT JOIN clientes c
        ON p.id_cliente = c.id_cliente
)

SELECT * FROM fct_pedidos