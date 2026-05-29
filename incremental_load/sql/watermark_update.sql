UPDATE watermark_table
SET last_order_number = (
    SELECT MAX(ORDERNUMBER)
    FROM sales_incremental
);
