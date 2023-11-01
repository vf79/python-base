class Cor:  # Base Class
    english_name = "color"
    icon = "⬜"

    def __str__(self):
        return f"{self.icon} - {self.english_name}"

    def __add__(self, other):
        mixtable = [
            ((Amarelo, Vermelho), Laranja),
            ((Azul, Amarelo), Verde),
            ((Vermelho, Azul), Violeta),
        ]
        for mix, result in mixtable:
            if isinstance(self, mix) and isinstance(other, mix):
                return result()


class Amarelo(Cor):  # Base Class
    english_name = "yellow"
    icon = "🟨"


class Azul(Cor):
    english_name = "blue"
    icon = "🟦"

    def __len__(self):
        return 3


class Vermelho(Cor):
    english_name = "red"
    icon = "🟥"

    def __len__(self):
        return 1


class Laranja(Cor):
    english_name = "orange"
    icon = "🟧"


class Verde(Cor):
    english_name = "green"
    icon = "🟩"

    def __len__(self):
        return 2


class Violeta(Cor):
    english_name = "purple"
    icon = "🟪"