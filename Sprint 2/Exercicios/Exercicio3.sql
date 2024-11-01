SELECT COUNT(l.editora) as quantidade , e.nome, e2.estado, e2.cidade 
from livro l 
LEFT JOIN editora e  on l.editora = e.codEditora
LEFT JOIN endereco e2 on e.endereco = e2.codendereco  
GROUP BY e.nome 
LIMIT 5