class Calculo:
    def somar(x, y):
        return x + y

    def subtrair(x, y):
        return x - y
    
x = 4
y = 5

print(f"Somando: {x}+{y} = {Calculo.somar(x, y)}")
print(f"Subtraindo: {x}-{y} = {Calculo.subtrair(x, y)}")
