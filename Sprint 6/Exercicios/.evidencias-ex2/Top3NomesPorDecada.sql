SELECT nome, total, decada
FROM (
    SELECT nome, 
    SUM(total) AS total, 
    (FLOOR(ano / 10) * 10) AS decada, 
    ROW_NUMBER() OVER (PARTITION BY(FLOOR(ano / 10) * 10) ORDER BY SUM(total) DESC) AS rank
    FROM 
        nomes
    WHERE 
        ano >= 1950
    GROUP BY 
        nome, (FLOOR(ano / 10) * 10)
) AS Ranked
WHERE 
    rank <= 3
ORDER BY 
    decada, total DESC;