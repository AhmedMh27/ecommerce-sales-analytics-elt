SELECT
    order_id,
    customer_id,
    product_id,
    CAST(order_date AS DATE) AS order_date,
    quantity,
    sales_amount,
    status
FROM {{ ref('raw_orders') }}
WHERE status = 'Completed' AND sales_amount > 0