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

    while True:
        info_size = len(info.values())
        filled_size = len([value for value in info.values() if value is not None])
        if info_size == filled_size:
            break

        keys = info.keys()
        for key in keys:
            if info[key] is not None:
                continue
            try:
                info[key] = int(input(f"{key}:").strip())
            except ValueError:
                log.error("%s inválida, digite números", key)
                break

    temperatura, umidade = info.values()

    if temperatura > 45:
        print("ALERTA!!! Perigo calor extremo")
    elif temperatura >30 and temperatura * 3 >= umidade:
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

    RESERVAS_FILE = "reservas.txt"
    QUARTOS_FILE = "quartos.txt"

    # Acesso ao banco de dados

    # TODO: Usar pacote csv

    ocupados = {} # acumulador
    try:
        for line in open(RESERVAS_FILE):
            nome_cliente, num_quarto, dias = line.strip().split(",")
            ocupados[int(num_quarto)] = {
                "nome_cliente": nome_cliente,
                "dias": int(dias),
            }
    except FileNotFoundError:
        logging.error("Arquivo %s não existe", RESERVAS_FILE)
        sys.exit(1)
    
    # TODO: Usar função para ler os arquivos

    quartos = {}
    try:
        for line in open(QUARTOS_FILE):
            num_quarto, nome_quarto, preco = line.strip().split(",")
            quartos[int(num_quarto)] = {
                "nome_quarto": nome_quarto,
                "preco": float(preco), # TODO: Usar decimal,
                "disponivel": False if int(num_quarto) in ocupados else True,
            }
    except FileNotFoundError:
        logging.error("Arquivo %s não existe", QUARTOS_FILE)
        sys.exit(1)

    # Programa principal

    print("Reservas no Hotel Pythonico do curso Python Base LinuxTips")
    print("-" * 80)
    
    if len(ocupados) == len(quartos):
        print("Hotel está lotado, volte depois.")
        sys.exit(0)

    nome_cliente = input("Qual é o seu nome:").strip()
    print()

    # TODO: Usar rich. Table

    print("Lista de quartos")
    print()
    head = ["Número", "Nome do Quarto", "Preço", "Disponível"]
    print(f"{head[0]:<6} - {head[1]:<15} - R$ {head[2]:<9} - {head[3]:<10}")
    for num_quarto, dados_quarto in quartos.items():
        nome_quarto = dados_quarto["nome_quarto"]
        preco = dados_quarto["preco"]
        disponivel = "⛔" if not dados_quarto["disponivel"] else "👍"
        # TODO: Substituir casa decimal por virgula
        print(f"{num_quarto:<6} - {nome_quarto:<14} - R$ {preco:<9.2f} - {disponivel:<10}")

    print("-" * 80)

    # reserva

    try:
        num_quarto = int(input("Qual o quarto desejado: ").strip())
        if not quartos[num_quarto]["disponivel"]:
            print(f"O quarto {num_quarto} está ocupado, escolha outro.")
            sys.exit(0)
    except KeyError:
        print(f"O quarto {num_quarto} não existe.")
        sys.exit(0)
    except ValueError:
        print("Número inválido, digite apenas digitos.")
        sys.exit(0)
    
    try:
        dias = int(input("Quantos dias: ").strip())
    except ValueError:
        logging.error("Número inválido, digite apenas digitos.")
        sys.exit(0)

    nome_quarto = quartos[num_quarto]["nome_quarto"]
    preco_quarto = quartos[num_quarto]["preco"]
    total = dias * preco_quarto

    print(
        f"Olá {nome_cliente}, você escolheu o quarto {nome_quarto} "
        f"o valor total estimado será R$ {total:.2f}"
    )

    if input("Confirma? (digite y)").strip().lower() in ("y", "yes", "sim", "s"):
        with open(RESERVAS_FILE, "a") as reserva_file:
            reserva_file.write(f"{nome_cliente},{num_quarto},{dias}\n")


# numeros_pares()
#alarme_temp_opt()
# repete_vogal()
reserva_quarto()