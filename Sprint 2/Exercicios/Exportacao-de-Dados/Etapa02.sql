SELECT  editora.codeditora, editora.nome as NomeEditora, COUNT(l.cod) as QuantidadeLivros
from livro l
LEFT JOIN editora on l.editora = editora.codeditora 
GROUP BY codeditora, editora.nome
ORDER BY l.valor 
LIMIT 5


