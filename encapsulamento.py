class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca            # Atributo público
        self.modelo = modelo          # Atributo público
        self.__quilometragem = 0     # Atributo privado (encapsulado)

    def dirigir(self, distancia):
        print(f"Dirigindo {distancia} km...")
        self.__quilometragem += distancia

    def obter_quilometragem(self):
        return self.__quilometragem


# Criando uma instância da classe Carro
meu_carro = Carro("Toyota", "Corolla")

# Acessando os atributos públicos
print("Marca:", meu_carro.marca)
print("Modelo:", meu_carro.modelo)

# Tentando acessar diretamente o atributo privado (encapsulado) - isso resultará em um erro
# print("Quilometragem:", meu_carro.__quilometragem)  # Isso resultará em um erro AttributeError

# Dirigindo o carro e atualizando a quilometragem
meu_carro.dirigir(100)
meu_carro.dirigir(50)

# Obtendo a quilometragem através de um método público
print("Quilometragem total:", meu_carro.obter_quilometragem())
