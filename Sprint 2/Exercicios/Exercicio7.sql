select a.nome
from autor a 
LEFT JOIN livro l on l.autor = a.codautor
GROUP BY a.nome, a.codautor 
HAVING COUNT(l.autor) = 0
ORDER BY a.nome
