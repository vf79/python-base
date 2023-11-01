# Abstração: Capacidade de abstrair implementações
# Herança: Capacidade de herdar de outras classes
# Polimorfismo: Capacidade de uma implementação se comportar de maneira
#               similar independente da forma do objeto
# Encapsulamento: Capacidade de esconder/proteger atributos dentro da classe
#                 publico, protegidas, privadas

from abc import ABC

class Person:
    kingdom = "animalia"

class Fruits:
    kingdom = "vegetalia"

class Animal:
    kingdom = "animalia"

# Herança

## super classe
class Fruit(ABC): # Classe Abstrata / base
    kingdom = "vegetalia"


#derivadas (sub classe)

class Apple(Fruit): # herança em uma classe material
    internal_colors = "white"


class RedApple(Apple):
    external_color = "red"


class GreenApple(Apple):
    external_color = "green"

# Exemplo de super especificidade com herança
class MinhaMacaQueEstaEmCimaDaMesa(GreenApple):
    ...

minha_maca = MinhaMacaQueEstaEmCimaDaMesa()
print(minha_maca.kingdom)
print(minha_maca.internal_colors)
print(minha_maca.external_color)

# Simplificar com um nivel de herança já e suficiente para a maioria dos casos.

class SimpleApple(Fruit):
    def __init__(self, colors):
        self.colors = colors

minha_maca = SimpleApple(colors=['green', 'white'])
print(minha_maca.kingdom)
print(minha_maca.colors)

class Watermelon(Fruit):
    ...


# Mixins
class Food(ABC):
    price = 4.5

class Radioactive:
    power = 10

# Polimorfismo


class Dog:
    def make_sound(self):
        return "woof woof"


class Cat:
    def make_sound(self):
        return "meow meow"


class Guitar:
    def make_sound(self):
        return "🎶 🎶 🎶"



def print_sound(obj): # Soundable
    if not hasattr(obj, "make_sound"):
        raise TypeError(f"{obj} is not Soundable")
    print(obj.make_sound())  # implementa make_sound



rex = Dog()
print_sound(rex)


lili = Cat()
print_sound(lili)

guitar = Guitar()
print_sound(guitar)

# print_sound(42)

# Duck Typing
"""
Se o objeto anda como um pato,
parece um pato, faz quack como um pato
então é um pato!
"""

# Encapsulamento
class Conta2:

    _tipo_de_conta = "corrente" # protegido / protected
    __id_interno = 456789 # Privado

    def __init__(self, cliente):
        self.cliente = cliente
        if self._tipo_de_conta == "corrente":
            self.saldo = 500


conta = Conta2(cliente="Ana")
conta._tipo_de_conta = 1000

print(dir(conta))

print(conta.cliente)
conta.cliente = "Outro"
print(conta.cliente)
print(conta.saldo)


class Conta:

    _tipo_de_conta = "corrente" # protegido / protected
    __id_interno = 456789 # Privado

    def __init__(self, cliente):
        self.cliente = cliente
        self._saldo = 0 # protegido

    def depositar(self,value):
        self._saldo += value

    def sacar(self, value):
        self._saldo -= value

    def consultar(self):
        if self._saldo < 0:
            print("AVISO: saldo negativo...")
        return self._saldo

conta = Conta("Exemplo")
conta.depositar(100)
conta.depositar(50)
print(conta.consultar())

conta.sacar(30)
print(conta.consultar())

conta.sacar(130)
print(conta.consultar())