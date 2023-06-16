#!/usr/bin/env python3


# debug com print
def repete_vogal_p(word: str) -> str:
    """Retorna a palavra com vogais repetidas."""
    final_word = ""
    for index, letter in enumerate(word):
        # usamos enumerate para ajudar a sabermos as voltas do loop
        print(f"{index=} {letter=}")
        if letter.lower() in "aeiouãõâêôáéíó":
            final_word = letter * 2
        else:
            final_word = letter

        print(f"{final_word=}")
    return final_word


# debug com pdb
# python -m pdb -c "until 31" tembug.py
# python -m pdb -c continue tembug.py
# import pdb;pdb.set_trace()
# __import__("pdb").set_trace()
# breakpoint() # A partir do python versão 3.7
# Para utilizar o ipdb como padrão: export PYTHONBREAKPOINT=ipdb.set_trace
# Opções pudb, winpdb


def repete_vogal(word: str) -> str:
    """Retorna a palavra com vogais repetidas."""
    final_word = ""
    for letter in word:
        if letter.lower() in "aeiouãõâêôáéíó":
            # import pdb;pdb.set_trace()
            # __import__("pdb").set_trace()
            #
            breakpoint()  # A partir do python versão 3.7
            1 / 0
            final_word = letter * 2
        else:
            final_word = letter
    return final_word


print(repete_vogal("banana"))
