select DISTINCT a.nome
from livro l 
LEFT JOIN autor a on l.autor = a.codautor
LEFT JOIN editora e on l.editora = e.codeditora 
LEFT JOIN endereco e2 on e.endereco = e2.codendereco 
WHERE e2.estado NOT IN ('PARANÁ', 'SANTA CARAINA', 'RIO GRANDE DO SUL')
ORDER BY a.nome 