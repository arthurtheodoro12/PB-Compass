import json

arquivo = open("Sprint 3/Exercicios/arquivos_utilizados/person.json")

lista_json = json.load(arquivo)

print(lista_json)