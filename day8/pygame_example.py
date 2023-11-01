import os
import random
import pygame as pg
import pygame.locals as keys

DIR = os.path.abspath(os.path.dirname(__file__))
TAMANHO_JANELA = (800, 800)

# Cores
VERDE = (0, 77, 64)
CINZA = (112, 112, 112)
AMARELO = (255, 240, 60)
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)

largura, altura = TAMANHO_JANELA
largura_estrada = int(largura / 1.6)
largura_separador = int(largura / 200)
lado_direito = largura / 2 + largura_estrada / 4
lado_esquerdo = largura / 2 - largura_estrada / 4

pg.init()
pg.display.set_caption("Catch a Beer")

tela = pg.display.set_mode(TAMANHO_JANELA)
tela.fill(VERDE)
pg.display.update()

# Fontes
letra = pg.font.SysFont("Comic Sans MS", 30)
letra_grande = pg.font.SysFont("Comic Sans MS", 90)

jogador = pg.image.load(os.path.join(DIR, "assets", "player01.png"))
jogador = pg.transform.scale(jogador, (150, 150))
posicao_do_jogador = jogador.get_rect()
posicao_do_jogador.center = lado_direito, altura * 0.8


def carrega_cerveja_aleatoria():
    n = random.randint(1, 5)
    i = f"beer{n:02}.png"
    cerveja = pg.image.load(os.path.join(DIR, "assets", i))
    cerveja = pg.transform.scale(cerveja, (75, 75))
    posicao_da_cerveja = cerveja.get_rect()
    if random.randint(0, 1) == 0:
        posicao_da_cerveja.center = lado_direito, altura * 0.2
    else:
        posicao_da_cerveja.center = lado_esquerdo, altura * 0.2

    return cerveja, posicao_da_cerveja


def gameover():
    msg = letra_grande.render("GAME OVER", True, AMARELO, PRETO)
    tela.blit(msg, (largura / 2 - msg.get_rect().w / 2, 200))
    pg.display.update()
    pg.mixer.music.load(os.path.join(DIR, "assets", "gameover.mp3"))
    pg.mixer.music.play(0)
    wait_key = True
    while wait_key:
        for event in pg.event.get():
            if event.type == keys.QUIT:
                wait_key = False
            if event.type == keys.KEYDOWN:
                wait_key = False


cerveja, posicao_da_cerveja = carrega_cerveja_aleatoria()

executando = True
velocidade = 1.0
bebeu = 0
perdeu = 0
rodadas = 0

while executando:
    # determina o estado do jogo no loop
    # # Colisao
    if (posicao_do_jogador.center == posicao_da_cerveja.center):
        bebeu += 1
        pg.mixer.music.load(os.path.join(DIR, "assets", "drink.mp3"))
        pg.mixer.music.play(0)
        cerveja, posicao_da_cerveja = carrega_cerveja_aleatoria()

    rodadas += 1
    if rodadas == 5000:
        velocidade += 0.1

    posicao_da_cerveja[1] += velocidade

    # captura eventos
    for event in pg.event.get():
        if event.type == keys.QUIT:
            executando = False
        if event.type == keys.KEYDOWN:
            if event.key in (keys.K_a, keys.K_LEFT):

                posicao_do_jogador = posicao_do_jogador.move(
                    (- int(largura_estrada / 2), 0)
                )
            elif event.key in (keys.K_d, keys.K_RIGHT):
                posicao_do_jogador = posicao_do_jogador.move(
                    (int(largura_estrada / 2), 0)
                )

    # estrada
    pg.draw.rect(
        tela,
        CINZA,
        (largura / 2 - largura_estrada / 2, 0, largura_estrada, altura)
    )

    # separador
    pg.draw.rect(
        tela,
        AMARELO,
        (largura / 2 - largura_separador / 2, 0, largura_separador, altura)
    )

    # bordas
    pg.draw.rect(
        tela,
        BRANCO,
        (
            largura / 2 - largura_estrada / 2 + largura_separador * 2,
            0,
            largura_separador,
            altura
        )
    )

    pg.draw.rect(
        tela,
        BRANCO,
        (
            largura / 2 + largura_estrada / 2 - largura_separador * 3,
            0,
            largura_separador,
            altura
        )
    )

    titulo = letra.render(
        f"Catch a beer! bebeu: {bebeu} vacilou: {perdeu}", True, BRANCO, PRETO
    )
    tela.blit(titulo, (largura / 2 - titulo.get_rect().w / 2, 0))

    tela.blit(jogador, posicao_do_jogador)
    tela.blit(cerveja, posicao_da_cerveja)

    pg.display.update()

    if posicao_da_cerveja[1] > altura:
        pg.mixer.music.load(os.path.join(DIR, "assets", "break.mp3"))
        pg.mixer.music.play(0)
        perdeu += 1
        cerveja, posicao_da_cerveja = carrega_cerveja_aleatoria()

    if perdeu > 3:
        gameover()
        break


pg.quit()
