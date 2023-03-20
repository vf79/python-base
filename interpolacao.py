#!/usr/bin/env python3

email_tpl = """
    Olá, %(nome)s

    Tem interesse em comprar %(produto)s?

    Este produto é ótimo para resolver %(texto)s

    Clique agora em %(link)s

    Apenas %(quantidade)d disponíveis!

    Preço promocional %(preco).2f
    """

clientes = ["Maria", "Joao", "Bruno"]


for cliente in clientes:
    print(email_tpl % {
        "nome": cliente,
        "produto": "caneta",
        "texto": "Escrever muito bem",
        "link": "https://canetaslegais.com",
        "quantidade": 1,
        "preco": 50.5, 
    })