import os
import random
from rich.prompt import Prompt
from rich.console import Console


EMOJIS = {
    "posicao_correta": "🟩",
    "letra_correta": "🟨",
    "letra_errada": "⬜",
}

DIR = os.path.abspath(os.path.dirname(__file__))


def posicao_correta(letra):
    return f"[black on green]{letra}[/]"


def letra_correta(letra):
    return f"[black on yellow]{letra}[/]"


def letra_errada(letra):
    return f"[black on white]{letra}[/]"


MENSAGEM = (
    f'{posicao_correta("Boas vindas ")}'
    f'{letra_correta("ao ")}'
    f'{letra_errada("Pylavras!")}'
)

INSTRUCAO = "Adivinhe a palavra de 5 letras"

palavra_correta = random.choice(
    open(os.path.join(DIR, "palavras.txt")).readlines()
).strip().upper()

tentativas = 6
rodadas = 0

console = Console()
console.print(MENSAGEM)
console.print(INSTRUCAO)
console.print(palavra_correta)


def computa_tentativa(tentativa):
    acertos = []
    emojis = []
    for i, letra in enumerate(tentativa):
        if tentativa[i] == palavra_correta[i]:
            acertos += posicao_correta(letra)
            emojis.append(EMOJIS["posicao_correta"])
        elif letra in palavra_correta:
            acertos += letra_correta(letra)
            emojis.append(EMOJIS["letra_correta"])
        else:
            acertos += letra_errada(letra)
            emojis.append(EMOJIS["letra_errada"])
    return "".join(acertos), "".join(emojis)


acertados = []
todos_os_emojis = []
while rodadas < tentativas:
    tentativa = Prompt.ask("Digite [green]5[/] letras").strip().upper()
    if len(tentativa) != 5:
        console.print("Erro: Digite [red]5[/] letras.")
        continue
    rodadas += 1

    # calcula
    acertos, emojis = computa_tentativa(tentativa)
    acertados.append(acertos)
    todos_os_emojis.append(emojis)
    console.clear()
    for acerto in acertados:
        console.print(acerto)

    if tentativa == palavra_correta:
        break

console.print(f"Pylavras: {rodadas}/{tentativas}\n")
for item in todos_os_emojis:
    console.print(item)
