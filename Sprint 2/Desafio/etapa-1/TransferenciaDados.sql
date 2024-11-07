-- Migração dos dados da tabela tb_locacao (tabela que contém todos os dados originalmente) para as demais tabelas

-- migração da tb_locacao para a tb_clientes
INSERT INTO tb_clientes (
	idCliente,
	nomeCliente,
	cidadeCliente,
	estadoCliente,
	paisCliente
)
SELECT DISTINCT 
	idCliente,
	nomeCliente,
	cidadeCliente,
	estadoCliente,
	paisCliente
FROM tb_locacao 


-- migração da tb_locacao para a tb_combustível
INSERT INTO tb_combustivel (
	idCombustivel,
	tipoCombustivel 
)
SELECT DISTINCT 
	idCombustivel, 
	tipoCombustivel 
from tb_locacao 

-- migração da tb_locacao para a tb_carros
INSERT INTO tb_carros (
	idCarro,
	idCombustivel,
	chassiCarro,
	marcaCarro, 
	modeloCarro,
	anoCarro
)
SELECT DISTINCT 
	idCarro,
	idCombustivel,
	classiCarro,
	marcaCarro, 
	modeloCarro,
	anoCarro
FROM tb_locacao 

--Atualizando a coluna kmCarro da tabela Carros, para que somente a maior quilometragem presente na tb_locacao seja extraida.
UPDATE tb_carros 
SET kmCarro = (
	SELECT MAX(kmCarro)
	FROM tb_locacao 
	WHERE tb_locacao.idCarro = tb_carros.idCarro 
)
WHERE kmCarro is not NULL;

-- migração da tb_locacao para a tb_vendedores
INSERT INTO tb_vendedores (
	idVendedor,
	nomeVendedor,
	sexoVendedor,
	estadoVendedor
)
SELECT DISTINCT 
	idVendedor,
	nomeVendedor,
	sexoVendedor,
	estadoVendedor
FROM tb_locacao 

-- migração da tb_locacao para a tb_locacao_novo
INSERT INTO tb_locacao_novo  (
	idLocacao,
	dataLocacao,
	horaLocacao,
	qtdDiaria,
	vlrDiaria,
	dataEntrega,
	horaEntrega,
	idCliente,
	idCarro,
	idVendedor,
	idCombustivel
)
SELECT 
	idLocacao,
	dataLocacao, 
	horaLocacao,
	qtdDiaria,
	vlrDiaria,
	dataEntrega, 
	horaEntrega,
	idCliente,
	idCarro,
	idVendedor,
	idCombustivel
FROM tb_locacao 

--Setando a dataLocacao no formato "YYYY-mm-dd"
UPDATE tb_locacao_novo 
SET dataLocacao = SUBSTRING(dataLocacao, 1, 4)  || '-' || SUBSTRING(dataLocacao, 5, 2) || '-' || SUBSTRING(dataLocacao, 7, 2); 
 
--Setando a dataEntrega no formato "YYYY-mm-dd"
UPDATE tb_locacao_novo 
SET dataEntrega = SUBSTRING(dataEntrega , 1, 4)  || '-' || SUBSTRING(dataEntrega , 5, 2) || '-' || SUBSTRING(dataEntrega , 7, 2); 
