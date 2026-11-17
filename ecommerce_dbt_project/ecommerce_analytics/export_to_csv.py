import duckdb

# الاتصال بقاعدة بيانات DuckDB
con = duckdb.connect('ecommerce_analytics.duckdb')

# 1. إنشاء جدول التقويم (dim_date) داخل DuckDB باستخدام generate_series
con.execute("""
    CREATE OR REPLACE TABLE dim_date AS
    SELECT 
        CAST(d AS DATE) AS date_key,
        CAST(d AS DATE) AS date,
        EXTRACT(YEAR FROM d) AS year,
        EXTRACT(MONTH FROM d) AS month_number,
        MONTHNAME(d) AS month,
        EXTRACT(QUARTER FROM d) AS quarter,
        EXTRACT(DOW FROM d) AS day
    FROM generate_series(DATE '2024-01-01', DATE '2026-12-31', INTERVAL '1 day') t(d);
""")

# 2. تصدير جميع الجداول إلى ملفات CSV
con.execute("COPY fct_sales TO 'fct_sales.csv' (HEADER, DELIMITER ',')")
con.execute("COPY dim_customers TO 'dim_customers.csv' (HEADER, DELIMITER ',')")
con.execute("COPY dim_date TO 'dim_date.csv' (HEADER, DELIMITER ',')")

print("Dim_Date created and all tables exported successfully!")