--Cricação das Tabelas que estruturarão o BD
--Tabela Clientes
CREATE TABLE tb_clientes (
	idCliente INT PRIMARY KEY, 
	nomeCliente VARCHAR(255),
	cidadeCliente VARCHAR(255),
	estadoCliente VARCHAR(255),
	paisCliente VARCHAR(255)
);

-- Tabela Combustivel
CREATE TABLE tb_combustivel (
	idCombustivel INT PRIMARY KEY,
	tipoCombustivel VARCHAR(255)
);


--Tabela Carros
CREATE TABLE tb_carros (
	idCarro INT PRIMARY KEY,
	idCombustivel INT,
	kmCarro INT,
	chassiCarro VARCHAR(255),
	marcaCarro VARCHAR(255),
	modeloCarro VARCHAR(255),
	anoCarro INT,
	FOREIGN KEY (idCombustivel) REFERENCES tb_combustivel(idCombustivel)
);

--Tabela Vendedores
CREATE TABLE tb_vendedores (
	idVendedor INT PRIMARY KEY,
	nomeVendedor VARCHAR(255),
	sexoVendedor INT,
	estadoVendedor VARCHAR(255)
);

--Tabela Locacao (principal)
CREATE TABLE tb_locacao_novo (
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
	FOREIGN KEY (idCliente) REFERENCES tb_clientes(idCliente),
	FOREIGN KEY (idCarro) REFERENCES tb_carros(idCarro),
	FOREIGN KEY (idVendedor) REFERENCES tb_vendedores(idVendedor),
	FOREIGN KEY (idCombustivel) REFERENCES tb_combustivel(idCombustivel)
);

