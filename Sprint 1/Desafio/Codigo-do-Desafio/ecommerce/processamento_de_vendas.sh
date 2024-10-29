#!/usr/bin/env bash

#variáveis de data/nome
dataHoje=$(date +%Y%m%d)
dataRelatorio=$(date +%Y/%m/%d\ %H:%M)
nomeBackup=dados-$dataHoje
nomeRelatorio=relatorio-$dataHoje

#variáveis de caminhos
caminhoRelatorio=/home/arthur/ecommerce/vendas/backup/$nomeRelatorio.txt
caminhoDadosVendas=/home/arthur/ecommerce/dados_de_vendas.csv
caminhoBackup=/home/arthur/ecommerce/vendas/backup
caminhoPastaVendas=/home/arthur/ecommerce/vendas

if [ ! -d "/home/arthur/ecommerce/vendas" ];then
	#criação de diretórios/subdiretórios e renomeação dos arquivos
	mkdir $caminhoPastaVendas
	cp $caminhoDadosVendas $caminhoPastaVendas
	cd $caminhoPastaVendas
	mkdir backup
	cp dados_de_vendas.csv $nomeBackup.csv
	mv $nomeBackup.csv backup
	cd backup
	mv $nomeBackup.csv backup-$nomeBackup.csv
	touch $nomeRelatorio.txt

	#relatório
	echo "Data do sistema operacional:" >> $caminhoRelatorio
	echo $dataRelatorio >> $caminhoRelatorio

	echo "Data do primeiro registro de venda: " >> $caminhoRelatorio
	awk -F "," 'NR==2 {print $5}' $caminhoDadosVendas >> $caminhoRelatorio

	echo "Data do último registro de venda: " >> $caminhoRelatorio
	awk -F "," 'END {print $5}' $caminhoDadosVendas  >> $caminhoRelatorio 

	echo "Quantidade total de itens diferentes vendidos:" >> $caminhoRelatorio
	quantidade=$(sort $caminhoDadosVendas |uniq|wc -l)
	echo $((quantidade - 1)) >> $caminhoRelatorio

	echo "10 primeiras linhas do arquivo backup-dados" >> $caminhoRelatorio
	awk -F "," 'NR>=2 && NR<=11 {print}' $caminhoBackup/backup-$nomeBackup.csv  >> $caminhoRelatorio

	#compactação/exclusão de arquivos
	zip -r backup-$nomeBackup.zip backup-$nomeBackup.csv
	rm $caminhoBackup/backup-$nomeBackup.csv
	rm $caminhoPastaVendas/dados_de_vendas.csv
 else
	#movimentando/renomeando arquivos
	cp $caminhoDadosVendas $caminhoPastaVendas
	cd $caminhoPastaVendas
	cp dados_de_vendas.csv $nomeBackup.csv
	mv $nomeBackup.csv backup
	cd backup
	mv $nomeBackup.csv backup-$nomeBackup.csv
	touch $nomeRelatorio.txt

	#relatório
	echo "Data do sistema operacional:" >> $caminhoRelatorio
	echo $dataRelatorio >> $caminhoRelatorio

	echo "Data do primeiro registro de venda: " >> $caminhoRelatorio
	awk -F "," 'NR==2 {print $5}' $caminhoDadosVendas >> $caminhoRelatorio

	echo "Data do último registro de venda: " >> $caminhoRelatorio
	awk -F "," 'END {print $5}' $caminhoDadosVendas  >> $caminhoRelatorio 

	echo "Quantidade total de itens diferentes vendidos:" >> $caminhoRelatorio
	quantidade=$(cut -d"," -f2 $caminhoDadosVendas|sort|uniq|wc -l)
	echo $((quantidade - 1)) >> $caminhoRelatorio

	echo "10 primeiras linhas do arquivo backup-dados" >> $caminhoRelatorio
	awk -F "," 'NR>=2 && NR<=11 {print}' $caminhoBackup/backup-$nomeBackup.csv  >> $caminhoRelatorio

	#compactação/exclusão de arquivos
	zip -r backup-$nomeBackup.zip backup-$nomeBackup.csv
	rm $caminhoBackup/backup-$nomeBackup.csv
	rm $caminhoPastaVendas/dados_de_vendas.csv
 fi
