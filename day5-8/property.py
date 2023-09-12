

class Conta:

    _tipo_de_conta = "corrente" # protegido / protected
    __id_interno = 456789 # Privado

    def __init__(self, cliente):
        self.cliente = cliente
        self.__saldo = 0 # protegido

    @property  # getter
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, value):
        self.__saldo += value

    @saldo.deleter
    def saldo(self):
        self.__saldo = 0


conta = Conta("Prop")
print(conta.cliente)
print(conta.saldo)

conta.saldo = 100
print(conta.saldo)

conta.saldo = -10
print(conta.saldo)

del conta.saldo
print(conta.saldo)