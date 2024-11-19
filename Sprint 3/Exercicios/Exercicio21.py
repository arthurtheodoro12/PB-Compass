class Passaro:
    def __init__(self, especie):
        self.especie = especie

    def voar(self):
        print("Voando...")

    def emitir_som(self, som):
        raise NotImplementedError("Método implementado nas classes filhas")

class Pato(Passaro):
    def __init__(self):
        super().__init__("Pato")
        self.som = "Quack Quack"
        
    def emitir_som(self):
        print(f"{self.especie} emitindo som...")
        print(self.som)


class Pardal(Passaro):
    def __init__(self):
        super().__init__("Pardal")
        self.som = "Piu Piu"

    def emitir_som(self):
        print(f"{self.especie} emitindo som...")
        print(self.som)

pato = Pato()
pardal = Pardal()

print(pato.especie)
pato.voar()
pato.emitir_som()
print(pardal.especie)
pardal.voar()
pardal.emitir_som()


