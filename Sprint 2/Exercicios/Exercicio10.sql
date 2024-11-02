SELECT 
	t2.nmvdd AS vendedor,
	SUM(t.qtd*t.vrunt) AS valor_total_vendas, 
	ROUND(SUM(t2.perccomissao*t.qtd*t.vrunt/100.00000000000001),2) AS comissao
FROM tbvendas t 
LEFT JOIN tbvendedor t2 ON t.cdvdd = t2.cdvdd 
WHERE status = 'Concluído'
GROUP BY t2.nmvdd 
ORDER BY comissao DESC