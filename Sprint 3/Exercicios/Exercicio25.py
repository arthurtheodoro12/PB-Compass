class Aviao:
    def __init__(self, modelo, velocidade_maxima, capacidade):
        self.modelo = modelo
        self.velocidade_maxima = velocidade_maxima
        self.cor = "azul"
        self.capacidade = capacidade

aviao1 = Aviao("BOIENG456", 1500, 400)
aviao2 = Aviao("Embraer Praetor 600", 863, 14)
aviao3 = Aviao("Antonov An-2", 258, 12)

lista_avioes = [aviao1, aviao2, aviao3]

for aviao in lista_avioes:
    mensagem = f'O avião de modelo {aviao.modelo} possui uma velocidade máxima de {aviao.velocidade_maxima} km/h, capacidade para  {aviao.capacidade} passageiros e é da cor {aviao.cor}'
    print(mensagem)



