class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    
    def calcular_salario_extra(self):
        return 0  

class Gerente(Funcionario):
    def __init__(self, nome, salario, area):
        super().__init__(nome, salario)
        self.area = area
    
    def calcular_salario_extra(self):
        return self.salario * 0.1  # Bônus de 10% para gerentes

class Atendente(Funcionario):
    def __init__(self, nome, salario, turno):
        super().__init__(nome, salario)
        self.turno = turno
    
    def calcular_salario_extra(self):
        if self.turno == "noite":
            return self.salario * 0.2  # Adicional noturno de 20%
        else:
            return 0

# Criando instâncias
gerente1 = Gerente("João", 5000, "Vendas")
atendente1 = Atendente("Maria", 2000, "noite")

# Calculando salário total
salario_total_gerente = gerente1.salario + gerente1.calcular_salario_extra()
salario_total_atendente = atendente1.salario + atendente1.calcular_salario_extra()

# Exibindo resultados
print("Salário total do gerente {}: R$ {:.2f}".format(gerente1.nome, salario_total_gerente))
print("Salário total do atendente {}: R$ {:.2f}".format(atendente1.nome, salario_total_atendente))
