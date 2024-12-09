<h1 align="center">Resolução do Desafio ✍️</h1>

## 📝 Explicação sobre o desafio

- O desafio é dividido em 3 etapas:
    - Etapa 1: Criar uma imagem Docker que execute um código Python chamado "carguru.py" e, em seguida, iniciar um container a partir da imagem criada.
    - Etapa 2: Responder á seguinte pergunta: "É possível reutilizar containers" e fornecer uma justificativa para a resposta.
    - Etapa 3: Desenvolver um script Python que gere um código hash a partir de uma string recebida via input. A partir desse script, criar uma imagem Docker que o execute e, então, rodar um container interativo utilizando a imagem criada.

 ###

## Etapas


### Etapa 1

 #### Criando a imagem Docker que execute o código "carguru.py"
 - Código responsável pela criação da imagem: [Dockerfile](./etapa1/Dockerfile)
 
 - Segue a explicação linha por linha do arquivo Dockerfile
    - ```` 
        FROM python
        ````
        - Essa linha especifica a imagem base que será utilizada para criar a nova imagem Docker, que no caso é a imagem oficial do Python pois o arquivo que será executado é um .py
    
    - ```` 
        WORKDIR /app 
        ````
        - Essa linha cria o diretório de trabalho "/app" dentro do container que executar essa imagem

    - ```` 
        COPY carguru.py .
        ````
        - Essa linha é responsável por criar uma cópia do arquivo "carguru.py" para dentro do diretório "/app" criado anteriormente

    - ```` 
        CMD ["python", "carguru.py"]
        ````
        - Essa linha é a responsável por efetivamente executar o arquivo "carguru.py". Ela executa  primeito o interpretador python, para após isso rodar o arquivo desejado.

###
- Após a criação do arquivo Dockerfile acima, foi necessário a utilizar o comando ``docker build`` no terminal para efetivamente criar a imagem

    - Evidência da execução do comando docker build
        - ![Imagem da execução do comando docker build](../Evidencias/ExecucaoBuild.png)
    - no caso, utilizei a flag -t para dar um nome a imagem. O "." no final da linha representa que o Docker deve usar o Dockerfile localizado no diretório atual para construir a imagem.

 #### Executando um container a partir da imagem criada

- Com a imagem criada, foi possível executar um container a partir dela
    - Evidência da execução do container a partir da imagem carguru-image
        - ![Imagem da execução do container a partir da imagem carguru-image](../Evidencias/ExecutandoContainerCarguru.png)
    - A saída da execução representa que o arquivo "carguru.py" foi executado com sucesso.


### Etapa 2

- É possível reutilizar containers?
    - Sim, é possível reutilizar containers no Docker. Quando um container é criado e executado, ele fica no estado parado após a sua execução, mas ainda fica disponível para ser reiniciado. Inclusive, todas as configurações e alterações feitas dentro do container durante sua execução são mantidas.

- Evidência da reutilização de um container:
    - Containers anteriormente criados:
        - ![Imagem containers anteriormente criados](../Evidencias/ContainersCriados.png)
        - Reutilizando o container cujo nome é "friendly_carson"
            - ![Imagem de Reinicialização do container](../Evidencias/ReiniciandoContainer.png)
            - Na imagem acima, podemos ver inicialmente todas as saidas do container "friendly_carson", exibidas utilizando o ``docker logs``. Após a execução do comando ``docker start``, que é responsável por iniciar um container parado, podemos perceber, com um novo uso do ``docker logs``, que uma nova saída foi adicionada ao log, ou seja, o container foi reutilizado com sucesso.