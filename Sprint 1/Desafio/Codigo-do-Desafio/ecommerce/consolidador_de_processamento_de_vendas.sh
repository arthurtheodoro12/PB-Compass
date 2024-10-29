#!/usr/bin/env bash

caminhoPastaBackup=/home/arthur/ecommerce/vendas/backup
caminhoRelatorioFinal=$caminhoPastaBackup/relatorio_final.txt

echo -e "-------------------------------------------------Relatório 1--------------------------------------------------\n" >> $caminhoRelatorioFinal
cat $caminhoPastaBackup/relatorio-20241022.txt >> $caminhoRelatorioFinal

echo -e "\n-------------------------------------------------Relatório 2--------------------------------------------------\n" >> $caminhoRelatorioFinal
cat $caminhoPastaBackup/relatorio-20241023.txt >> $caminhoRelatorioFinal

echo -e "\n-------------------------------------------------Relatório 3--------------------------------------------------\n" >> $caminhoRelatorioFinal
cat $caminhoPastaBackup/relatorio-20241024.txt >> $caminhoRelatorioFinal

echo -e "\n-------------------------------------------------Relatório 4--------------------------------------------------\n" >> $caminhoRelatorioFinal
cat $caminhoPastaBackup/relatorio-20241025.txt >> $caminhoRelatorioFinal
