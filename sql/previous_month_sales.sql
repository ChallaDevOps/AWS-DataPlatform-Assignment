SELECT 
    product_id,
    SUM(amount_sold) AS total_sales,
    RANK() OVER (ORDER BY SUM(amount_sold) DESC) AS sales_rank
FROM 
    sales_data
WHERE 
    sale_date >= DATE_FORMAT(CURDATE() - INTERVAL 1 MONTH, '%Y-%m-01')
    AND sale_date < DATE_FORMAT(CURDATE(), '%Y-%m-01')
GROUP BY 
    product_id
ORDER BY 
    total_sales DESC;
