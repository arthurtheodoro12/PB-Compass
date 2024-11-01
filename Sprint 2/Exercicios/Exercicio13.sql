SELECT cdpro, nmcanalvendas ,nmpro, SUM(qtd) AS quantidade_vendas
FROM tbvendas t 
WHERE status = 'Concluído'
GROUP BY nmpro, nmcanalvendas, cdpro 
ORDER BY quantidade_vendas
 