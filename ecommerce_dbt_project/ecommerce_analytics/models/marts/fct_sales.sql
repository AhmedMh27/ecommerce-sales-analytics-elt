{{ config(materialized='table') }}

SELECT
    o.order_id,
    o.order_date,
    o.customer_id,
    o.product_id,
    o.quantity,
    o.sales_amount,
    p.category,
    p.unit_price
FROM {{ ref('stg_orders') }} AS o
LEFT JOIN {{ ref('raw_products') }} AS p
    ON o.product_id = p.product_id