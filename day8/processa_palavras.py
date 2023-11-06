"""Filtrar palavras que contem 5 letras e remove os acentos."""
import os
import unicodedata


def tira_acento(s):
    one = unicodedata.normalize("NFD", s)
    two = one.encode('ascii', "ignore")
    return two.decode("utf-8")


DIR = os.path.abspath(os.path.dirname(__file__))
filename = os.path.join(DIR, "assets", "br-utf8.txt")
original = open(file=filename, encoding="utf-8").readlines()

with open(os.path.join(DIR, "palavras.txt"), "w", encoding="utf-8") as palavras:
    palavras.write(
        "\n".join(
            tira_acento(p.strip().upper())
            for p in original if len(p.strip()) == 5
        )
    )
