class Veiculo:
    def __init__(self, placa, tipo):
        self.placa = placa
        self.tipo = tipo
    
    def calcular_custo_estacionamento(self):
        pass  # Método a ser implementado nas classes derivadas

class Carro(Veiculo):
    def calcular_custo_estacionamento(self):
        return 5.00  # Custo de estacionamento por hora para carro: R$ 5,00

class Moto(Veiculo):
    def calcular_custo_estacionamento(self):
        return 3.00  # Custo de estacionamento por hora para moto: R$ 3,00

def calcular_custo_total_estacionamento(lista_veiculos):
    custo_total = 0
    for veiculo in lista_veiculos:
        custo_total += veiculo.calcular_custo_estacionamento()
    return custo_total

# Criando instâncias
carro1 = Carro("ABC1234", "Carro")
moto1 = Moto("DEF5678", "Moto")

# Criando lista de veículos
lista_veiculos = [carro1, moto1]

# Ca
