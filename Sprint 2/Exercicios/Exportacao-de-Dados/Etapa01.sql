SELECT l.cod as CodLivro, l.titulo, a.codautor, a.nome as NomeAutor, l.valor,  editora.codeditora, editora.nome as NomeEditora 
from livro l
LEFT JOIN autor a on l.autor = a.codautor 
LEFT JOIN editora on l.editora = editora.codeditora 
ORDER BY l.valor DESC
LIMIT 10