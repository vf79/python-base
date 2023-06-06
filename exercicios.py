#!/bin/usr/env python3

import sys
import logging

"""
Faça um programa que imprime os números pares de 1 a 200
"""
def numeros_pares():
    for n in range(1,201):
        if n % 2 !=0:
            continue
        print(n)

"""
Alarme de temperatura
Faça um script que pergunta ao usuário qual a temperatura atual e o indice de 
umidade do ar sendo que caso será exibida uma mensagem de alerta dependendo das 
condições

Se temp maior 45: ALERTA!!! Perigo calor extremo
Senão, se temp vezes 3 for maior ou igual a umidade: ALERTA!!! Perigo de calor úmido
...temp entre 10 e 30: Normal
...temp entre 0 e 10: Frio
...temp <0: ALERTA: Frio extremo
"""

log = logging.Logger("alerta")

def alarme_temp_opt():
    info = {
        "temperatura": None,
        "umidade": None,
    }

    keys = info.keys()
    for key in keys:
        try:
            info[key] = float(input(f"Qual a {key}? ").strip())
        except ValueError:
            log.error(f"{key.capitalize()} inválida")
            sys.exit(1)

    temperatura = info["temperatura"]
    umidade = info["umidade"]

    if temperatura > 45:
        print("ALERTA!!! Perigo calor extremo")
    elif temperatura * 3 >= umidade:
        print("ALERTA!!! Perigo calor úmido")
    elif temperatura >= 10 and  temperatura <=30:
        print("Normal")
    elif temperatura >= 0 and  temperatura <=10:
        print("Frio")
    elif temperatura < 0:
        print("ALERTA!!! Frio Extremo")



def alarme_temp():
    try:
        temp = float(input("Qual a temperatura?").strip())
    except ValueError:
        log.error("Temperatura inválida")
        sys.exit(1)
    
    try:
        umidade = float(input("Qual a umidade do ar").strip())
    except ValueError:
        log.error("Umidade inválida")
        sys.exit(1)

"""
Repete vogais
Faça um programa que pede ao usuário que digite uma ou mais palavras e imprime
cada uma das palavras com suas vogais duplicadas.
"""
def repete_vogal():
    words = []
    while True:
        word = input("Digite uma plavra (ou enter para sair):").strip()
        if not word:
            break

        final_word = ""
        for letter in word:
            # TODO: Remover acentuação usando função
            # Usando if tradicional
            """
            if letter.lower() in "aeiou":
                final_word += letter * 2
            else:
                final_word += letter
            """
            # Usando if Ternário
            final_word += letter * 2 if letter.lower() in "aeiouãêóíá" else letter

        words.append(final_word)

    #for word in words:
    #    print(word)
    print(*words, sep="\n")

"""
Faça um programa de terminal que exibe ao usuário um listas dos quartos disponíveis 
para alugar e o preço de cada quarto, esta informação está disponível em um arquivo 
de texto separado por vírgulas.

`quartos.txt`
# codigo, nome, preço
1,Suite Master,500
2,Quarto Familia,200
3,Quarto Single,100
4,Quarto Simples,50

O programa pergunta ao usuário o nome, qual o número do quarto a ser reservado
e a quantidade de dias e no final exibe o valor estimado a ser pago.

`reservas.txt`
# cliente, quarto, dias
Bruno,3,12

Se outro usuário tentar reservar o mesmo quarto o programa deve exibir uma 
mensagem informando que já está reservado.

"""
def reserva_quarto():
    ocupados = {}
    try:
        for line in open("reservas.txt"):
            nome, num_quarto, dias = line.strip().split(",")
            ocupados[int(num_quarto)] = {
                "nome": nome,
                "dias": dias,
            }
    except FileNotFoundError:
        logging.error("Arquivo reservas.txt não existe")
        sys.exit(1)

    quartos = {}
    try:
        for line in open("quartos.txt"):
            codigo,nome,preco = line.strip().split(",")
            quartos[int(codigo)] = {
                "nome": nome,
                "preco": float(preco), # TODO: Decimal,
                "disponivel": False if int(codigo) in ocupados else True
            }
    except FileNotFoundError:
        logging.error("Arquivo quartos.txt não existe")
        sys.exit(1)



    print("Reserva Hotel Pythonico")
    print("-" * 80)
    
    if len(ocupados) == len(quartos):
        print("Hotel Lotado")
        sys.exit(1)

    nome = input("Nome do cliente:").strip()

    print("Lista de quartos disponíveis")
    for codigo, dados in quartos.items():
        nome_quarto = dados["nome"]
        preco = dados["preco"]
        # disponivel = dados['disponivel'] and "👍" or "⛔"
        disponivel = "⛔" if not dados["disponivel"] else "👍"
        # TODO: Substituir casa decimal por virgula
        print(f"{codigo} - {nome_quarto} - R$ {preco:.2f} - {disponivel}")

    print("-" * 80)
    try:
        num_quarto = int(input("Número do quarto: ").strip())
        if not quartos[num_quarto]["disponivel"]:
            print(f"O quarto {num_quarto} está ocupado.")
            sys.exit(1)
    except ValueError:
        logging.error("Número inválido, digite apenas digitos.")
        sys.exit(1)
    except KeyError:
        print(f"O quarto {num_quarto} não existe.")
        sys.exit()
    
    try:
        dias = int(input("quantos dias:").strip())
    except ValueError:
        logging.error("Número inválido, digite apenas digitos.")
        sys.exit(1)

    nome_quarto = quartos[num_quarto]["nome"]
    preco_quarto = quartos[num_quarto]["preco"]
    disponivel = quartos[num_quarto]["disponivel"]
    total = preco_quarto * dias

    #print(f"{nome},{num_quarto},{dias}")
    #print(",".join([nome, str(num_quarto), str(dias)]))
    with open("reservas.txt", "a") as file_:
        file_.write(f"{nome},{num_quarto},{dias}\n")
    print(f"{nome} voce escolheu o quarto {nome_quarto} e vai custa: R${total:.2f}")

# numeros_pares()
# alarme_temp_opt()
# repete_vogal()
reserva_quarto()