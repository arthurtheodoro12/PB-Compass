<h1 align="center">Resolução Desafio ✍️</h1>

###

### 📝 Explicação sobre o desafio
O desafio consiste no tratamento de dados de uma tabela, um arquivo .csv, a qual contem informações de vendas de um e-commerce. O objetivo é extrair dados específicos, como a data da primeira e última venda, o número de produtos diferentes vendidos, entre outros, para gerar relatórios diários utilizando esses dados.
Como a tabela é atualizada diariamente, os relatórios também mudam a cada dia.

### 🚀 Primeiros passos
Para organizar melhor o processo, foi criada uma estrutura de diretórios. O diretório principal é chamado "ecommerce", que contém um subdiretório "vendas". Dentro de "vendas", há um subdiretório "backup", onde são armazenados todos os relatórios gerados.

![estrutura de diretórios e subdiretórios](/Sprint%201/Evidencias/Estrutura%20de%20Pastas%20.png)

A geração automática dos relatórios e a criação da estrutura de diretórios foram feitas por meio de um script chamado [processamento_de_vendas.sh](/Sprint%201/Desafio/Codigo-do-Desafio/ecommerce/processamento_de_vendas.sh).

## 💻 Codificação do Script processamento_de_vendas
O script começa com uma linha essencial para sua execução em sistemas Unix/Linux.
```
#!/usr/bin/env bash
```

### 🔧 Configuração inicial

 Antes de iniciar a lógica principal, todas as variáveis foram definidas, como a data formatada, nomes e caminhos de arquivos que são consumidos várias vezes durante o código. Tudo para melhorar a legibilidade e compreensão do código.

````
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
````
### 📂  Criação da Estrutura de Diretórios
O script é executado durante quatro dias consecutivos, mas a estrutura de diretórios precisa ser criada apenas uma vez. Para garantir isso, foi utilizado um bloco condicional if-else: se a estrutura ainda não foi gerada, o script executa o bloco if; 

#### Erro caso não utilize o condicional if-else

![imagem do erro sem if-else](/Sprint%201/Evidencias/ErroCriacaoDiretorios.jpeg)

#### Correção, implementando o conficional if-else no código
```
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
```

caso contrário, ele executa o bloco else.

### 📊 Extração de Dados

A extração dos dados da tabela começa após a criação da estrutura de diretórios e subdiretórios.

O primeiro dado adicionado ao relatório é a data do sistema operacional, formatada de acordo com a variável dataRelatorio.

````
echo "Data do sistema operacional:" >> $caminhoRelatorio
echo $dataRelatorio >> $caminhoRelatorio
````

A maioria dos dados são extraidos com o comando awk, que manipula textos com base em padrões. Como os dados na tabela seguem um padrão, é possível identificar e concatenar exatamente o que é necessário no relatório.

```
echo "Data do primeiro registro de venda: " >> $caminhoRelatorio
awk -F "," 'NR==2 {print $5}' $caminhoDadosVendas >> $caminhoRelatorio

echo "Data do último registro de venda: " >> $caminhoRelatorio
awk -F "," 'END {print $5}' $caminhoDadosVendas  >> $caminhoRelatorio 

echo "10 primeiras linhas do arquivo backup-dados" >> $caminhoRelatorio
awk -F "," 'NR>=2 && NR<=11 {print}' $caminhoBackup/backup-$nomeBackup.csv
````
###

Para calcular a quantidade total de itens diferentes vendidos, a linha de comando usa uma combinação de comandos: **cut** para selecionar a segunda coluna da tabela, **sort** para ordenar alfabeticamente, uniq para eliminar duplicatas consecutivas (daí a necessidade de ordenação), e wc -l para contar o número total de linhas restantes. A subtração "-1" no resultado final é aplicado para descontar a linha do cabeçalho.

```
echo "Quantidade total de itens diferentes vendidos:" >> $caminhoRelatorio
quantidade=$(sort $caminhoDadosVendas |uniq|wc -l)
echo $((quantidade - 1)) >> $caminhoRelatorio
````

### 📦 Compactação de arquivos

Como uma cópia da tabela é gerada como backup, visando economizar memória, é feito uma compactação desse backup de .csv para .zip.

Além disso, são excluidas todas as demais cópias feitas da tabela durante a execução do script.

````
#compactação/exclusão de arquivos
zip -r backup-$nomeBackup.zip backup-$nomeBackup.csv
rm $caminhoBackup/backup-$nomeBackup.csv
rm $caminhoPastaVendas/dados_de_vendas.csv
````

### ⏰ Agendamento do Script Processamento_de_Dados

O script precisou ser executado durante 4 dias seguidos, de forma automática e em um horário fixo, para isso foi utilizado o **crontab** que é um agendador de tarefas linux.

### 📅 Após execução

Após 4 dias de execução, foram gerados 4 relatórios diferentes, como é possível vizualizar na pasta [ecommerce/vendas/backup](/Sprint%201/Desafio/Codigo-do-Desafio/ecommerce/vendas/backup/) e a partir desses 4 relatórios foi gerado um relatório final, o qual possui a concatenação do conteúdo dos 4 relatórios.

### 📜Relatório Final

O relatório final foi gerado pelo script [consolidador_de_processamento_de_vendas.sh](/Sprint%201/Desafio/Codigo-do-Desafio/ecommerce/consolidador_de_processamento_de_vendas.sh), o qual possui um código muito mais simples se comparado com o script [processamento_de_vendas](/Sprint%201/Desafio/Codigo-do-Desafio/ecommerce/processamento_de_vendas.sh) pois a sua função é somente de concatenar os 4 relatórios em um único arquivo chamado [relatorio_final.txt](/Sprint%201/Desafio/Codigo-do-Desafio/ecommerce/vendas/backup/relatorio_final.txt)
````
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
````