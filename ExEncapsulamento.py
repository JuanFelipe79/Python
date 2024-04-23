class ContaBancaria:
    def __init__(self, numero_conta, saldo_inicial=0):
        self._numero_conta = numero_conta
        self._saldo = saldo_inicial
    
    def get_saldo(self):
        return self._saldo
    
    def set_saldo(self, novo_saldo):
        if novo_saldo >= 0:
            self._saldo = novo_saldo
        else:
            print("O saldo não pode ser negativo.")
    
    def depositar(self, quantia):
        if quantia > 0:
            self._saldo += quantia
        else:
            print("A quantia de depósito deve ser positiva.")
    
    def sacar(self, quantia):
        if quantia > 0 and quantia <= self._saldo:
            self._saldo -= quantia
        else:
            print("Quantia inválida ou saldo insuficiente.")

# Criando instância de ContaBancaria
minha_conta = ContaBancaria("123456", 1000)

# Testando operações
print("Saldo inicial:", minha_conta.get_saldo())  # Saída: Saldo inicial: 1000

minha_conta.depositar(500)
print("Saldo após depósito:", minha_conta.get_saldo())  # Saída: Saldo após depósito: 1500

minha_conta.sacar(200)
print("Saldo após saque:", minha_conta.get_saldo())  # Saída: Saldo após saque: 1300

minha_conta.sacar(2000)  # Saída: Quantia inválida ou saldo insuficiente.
minha_conta.depositar(-100)  # Saída: A quantia de depósito deve ser positiva.
minha_conta.set_saldo(-500)  # Saída: O saldo não pode ser negativo.
