SELECT estado, ROUND(AVG(qtd * vrunt),2) AS gastomedio
FROM tbvendas t 
WHERE status = 'Concluído'
GROUP BY estado 
ORDER BY gastomedio DESC 