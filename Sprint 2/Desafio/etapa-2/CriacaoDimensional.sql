--Cricação do Modelo Dimensional
--Dimensão Clientes
CREATE TABLE dim_clientes (
	idCliente INT PRIMARY KEY, 
	nomeCliente VARCHAR(255),
	cidadeCliente VARCHAR(255),
	estadoCliente VARCHAR(255),
	paisCliente VARCHAR(255)
);

--Dimensão Carros
CREATE TABLE dim_carros (
	idCarro INT PRIMARY KEY,
	kmCarro INT,
	chassiCarro VARCHAR(255),
	marcaCarro VARCHAR(255),
	modeloCarro VARCHAR(255),
	anoCarro INT,
	idCombustivel INT,
	tipoCombustivel VARCHAR(255)
);

--Dimensão Vendedores
CREATE TABLE dim_vendedores (
	idVendedor INT PRIMARY KEY,
	nomeVendedor VARCHAR(255),
	sexoVendedor INT,
	estadoVendedor VARCHAR(255)
);

--Fato Locacao (principal)
CREATE TABLE fato_locacao(
	idLocacao INT PRIMARY KEY,
	dataLocacao DATE,
	horaLocacao TIME,
	qtdDiaria INT,
	vlrDiaria DECIMAL(10,2),
	dataEntrega DATE,
	horaEntrega TIME,
	idCliente INT,
	idCarro INT,
	idVendedor INT,
	idCombustivel INT,
	FOREIGN KEY (idCliente) REFERENCES dim_clientes(idCliente),
	FOREIGN KEY (idCarro) REFERENCES dim_carros(idCarro),
	FOREIGN KEY (idVendedor) REFERENCES dim_vendedores(idVendedor)
);