class Lampada:
    def __init__(self, estado_inicial=False):
        self.ligada = estado_inicial

    def liga(self):
        self.ligada = True

    def desliga(self):
        self.ligada = False

    def esta_ligada(self):
        if self.ligada == True:
            return True
        else:
            return False
            
lampada1 = Lampada()

lampada1.liga()

print(f"A lâmpada está ligada? {Lampada.esta_ligada(lampada1)}")

lampada1.desliga()

print(f"A lâmpada ainda está ligada? {Lampada.esta_ligada(lampada1)}")

