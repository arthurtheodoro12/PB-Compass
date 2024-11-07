-- Migração dos dados da tabela tb_locacao para as demais tabelas


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

SELECT * FROM tb_carros tc 

SELECT * FROM tb_locacao tl 