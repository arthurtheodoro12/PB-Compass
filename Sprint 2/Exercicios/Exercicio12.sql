SELECT t2.cddep, t2.nmdep, t2.dtnasc, sum(qtd * vrunt) AS valor_total_vendas 
FROM tbvendas t
LEFT JOIN tbdependente t2 ON t.cdvdd = t2.cdvdd
WHERE status = 'Concluído'
GROUP BY t.cdvdd 
ORDER BY valor_total_vendas 
LIMIT 1
