class Veiculo:
    def mover(self):
        pass


class Carro(Veiculo):
    def mover(self):
        return "O carro está se movendo sobre rodas."


class Aviao(Veiculo):
    def mover(self):
        return "O avião está voando pelos céus."


class Barco(Veiculo):
    def mover(self):
        return "O barco está navegando sobre as águas."


# Função que faz um veículo se mover
def mover_veiculo(veiculo):
    print(veiculo.mover())


# Criando instâncias das classes
carro = Carro()
aviao = Aviao()
barco = Barco()

# Chamando a função com diferentes tipos de veículos
mover_veiculo(carro)  # Saída: O carro está se movendo sobre rodas.
mover_veiculo(aviao)  # Saída: O avião está voando pelos céus.
mover_veiculo(barco)  # Saída: O barco está navegando sobre as águas.
