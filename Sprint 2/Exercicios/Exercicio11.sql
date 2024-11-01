SELECT cdcli, nmcli, SUM(qtd * vrunt) AS gasto  
FROM tbvendas t 
GROUP BY nmcli 
ORDER BY gasto DESC 
LIMIT 1