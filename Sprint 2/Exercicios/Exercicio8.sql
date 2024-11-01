SELECT t.cdvdd, t2.nmvdd 
FROM tbvendas t 
LEFT JOIN tbvendedor t2 ON t.cdvdd = t2.cdvdd 
WHERE t.status = 'Concluído'
GROUP BY t2.nmvdd 
ORDER BY COUNT(t.cdvdd) DESC
LIMIT 1

