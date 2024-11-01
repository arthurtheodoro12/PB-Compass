select a.codautor, a.nome, COUNT(a.nome) as quantidade_publicacoes 
from livro l 
LEFT JOIN autor a on l.autor = a.codautor
GROUP BY a.nome 
ORDER BY quantidade_publicacoes DESC 
LIMIT 1