SELECT a.nome, a.codautor, a.nascimento, COUNT(l.autor) as quantidade
from autor a 
LEFT JOIN livro l on a.codautor = l.autor 
GROUP BY a.codautor 
ORDER BY a.nome 
