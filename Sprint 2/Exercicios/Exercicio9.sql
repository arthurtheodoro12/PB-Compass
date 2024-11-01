SELECT cdpro, nmpro 
FROM tbvendas t 
WHERE dtven BETWEEN '2014-02-03' AND '2018-02-02' AND status = 'Concluído'
GROUP BY nmpro 
ORDER BY COUNT(nmpro) DESC
LIMIT 1