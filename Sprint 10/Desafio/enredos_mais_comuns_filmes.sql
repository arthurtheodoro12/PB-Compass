CREATE OR REPLACE VIEW "refined-db"."enredos_mais_comuns_filmes" AS
WITH filmes_filtrados AS (
    SELECT 
        DISTINCT(f.id_filme),
        f.titulo,
        f.titulo_original,
        f.sinopse,
        t.data_lancamento,
        g.nome_genero
    FROM 
        "refined-db"."dim_filme" f
    JOIN 
        "refined-db"."filme_genero" fg ON f.id_filme = fg.id_filme
    JOIN 
        "refined-db"."dim_genero" g ON fg.id_genero = g.id_genero
    JOIN 
        "refined-db"."fato_filme" ff ON f.id_filme = ff.id_filme
    JOIN 
        "refined-db"."dim_tempo" t ON ff.id_tempo = t.id_tempo
    WHERE 
        (g.nome_genero = 'Crime' OR g.nome_genero = 'Guerra')
        AND (
            (YEAR(t.data_lancamento) = 1962) 
            OR (YEAR(t.data_lancamento) BETWEEN 1955 AND 1975) 
        )
),
palavras AS (
    SELECT 
        id_filme,
        palavra
    FROM 
        filmes_filtrados,
        UNNEST(SPLIT(REGEXP_REPLACE(LOWER(sinopse), '[^a-záàâãéèêíïóôõöúçñ]', ' '), ' ')) AS t(palavra)
)
SELECT 
    p.palavra,
    f.titulo AS filme,
    f.data_lancamento,
    f.nome_genero
FROM 
    palavras p
JOIN 
    filmes_filtrados f ON p.id_filme = f.id_filme
WHERE 
    p.palavra IN (
        'guerra', 'soldados', 'missão', 'exército', 'aliados', 'nazistas', 'batalha', 'campo', 
        'resistencia', 'vietnã', 'misseis', 'cuba', 'mísseis', 'míssil', 'russo', 'eua', 
        'russia', 'estados unidos'
    );