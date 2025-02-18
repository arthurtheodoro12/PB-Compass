CREATE TABLE Dim_Filme (
    id_filme SERIAL PRIMARY KEY,
    titulo VARCHAR(255),
    titulo_original VARCHAR(255),
    sinopse TEXT
);

CREATE TABLE Dim_Genero (
    id_genero SERIAL PRIMARY KEY,
    nome_genero VARCHAR(100) UNIQUE
);

CREATE TABLE Filme_Genero (
    id_filme INT,
    id_genero INT,
    FOREIGN KEY (id_filme) REFERENCES Dim_Filme(id_filme),
    FOREIGN KEY (id_genero) REFERENCES Dim_Genero(id_genero)
);

CREATE TABLE Dim_Idioma (
    id_idioma SERIAL PRIMARY KEY,
    codigo_idioma VARCHAR(10) UNIQUE
);

CREATE TABLE Dim_Tempo (
    id_tempo SERIAL PRIMARY KEY,
    data_lancamento DATE UNIQUE
);

CREATE TABLE Fato_Filme (
    id_fato_filme SERIAL PRIMARY KEY,
    id_filme INT,
    id_genero INT,
    id_idioma INT,
    id_tempo INT,
    popularidade FLOAT,
    nota_media FLOAT,
    total_votos INT,
    FOREIGN KEY (id_filme) REFERENCES Dim_Filme(id_filme),
    FOREIGN KEY (id_genero) REFERENCES Dim_Genero(id_genero),
    FOREIGN KEY (id_idioma) REFERENCES Dim_Idioma(id_idioma),
    FOREIGN KEY (id_tempo) REFERENCES Dim_Tempo(id_tempo)
);

