# Protocolos / Data Model
# Printable

from cor import Azul, Amarelo, Vermelho, Verde


obj = Azul()
new = str(obj)

print(new)

print("Cores primárias")
print(Amarelo())
print(Azul())
print(Vermelho())

# Addible - __add__ / __radd__

print(1 + 2)
print("Concatena" + "String")
print([1,2,3] + [4,5,6])

print("Cores Secundárias")
amarelo = Amarelo()
azul = Azul()
vermelho = Vermelho()
verde = Verde()

print(amarelo, azul, vermelho)
print("Amarelo + Vermelho", amarelo + vermelho)  # Tipagem Forte
print("Vermelho + Azul", vermelho + azul)
print("Azul + Amarelo", azul + amarelo)
print("Amarelo + Azul", amarelo + azul)

# Iterable - __iter__

nome = "Nome da Pessoa" # str

for letra in nome:
    print(letra)


print(list(nome))

class Paleta:
    def __init__(self, *cores):
        self._cores = cores

    def __len__(self):
        return len(self._cores)

    def __iter__(self):
        return iter([cor for cor in self._cores])

    def __contains__(self, item):
        return item in [cor.icon for cor in self._cores]

    def __getitem__(self, item):
        if isinstance(item, (int, slice)): # 0, 2:4
            return self._cores[item]
        if isinstance(item, str):
            for cor in self._cores:
                if cor.__class__.__name__.lower() == item.lower():
                    return cor



rgb = Paleta(Vermelho(), Verde(), Azul())

# Container - __contains__ -> bool

print("🟥" in rgb)
print("🟩" in rgb)
print("🟦" in rgb)

# Sized

print(len(rgb))

for cor in rgb:
    print(cor, len(cor))
#    # print(cor, len(cor))

# Subscriptable

nome = ["Tiburcio", "Juvenal"]
print(nome[0])

person = {"name": "Tiburcio", "last_name": "Juvenal"}
print(person["last_name"])

print(rgb[0])
print(rgb["verde"])

verde + vermelho # __add__
verde - vermelho # __sub__
verde * vermelho # __mul__
verde / vermelho # __div__