-- Write your query below
SELECT c.name FROM customers as c
LEFT JOIN orders as o
ON c.id = o.customer_id
where customer_id IS NULL