

# Procedural
def heron(a, b, c):
    perimeter = a + b + c
    s = perimeter / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** (1 / 2)
    return area


triangulos = [
    (3,4,5),
    (5,12,13),
    (8,15,17),
    (12,35,37),
]

for t in triangulos:
    print("A área do triângulo é: ", heron(*t))

# Orientado objetos
class Triangle:
    side_qtd = 3

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


    def area(self):
        perimeter = self.a + self.b + self.c
        s = perimeter / 2
        area = (s * (s - self.a) * (s - self.b) * (s - self.c)) ** (1 / 2)
        return area


triangle = Triangle(5,6,7)
print(triangle.area())

triangle.a = 10
print(triangle.area())