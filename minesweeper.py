import pygame
from pygame.locals import *
import random

campo = []
revelado = []
tamanho_campo = 10
bombas_totais = 10

def criar_campo():

    #Criando campo base

    for i in range(tamanho_campo):
        campo.append([])
    for i in range(tamanho_campo):
        for j in range(tamanho_campo):
            campo[i].append(0)

    #Criando campo visivel

    for i in campo:
        revelado.append([])
    for i in range(len(campo)):
        for j in range(len(campo[0])):
            revelado[i].append("#")

    colocar_bombas()
    numerando_campo()

def colocar_bombas():
    for i in range(bombas_totais):
        x = random.randint(0, tamanho_campo-1)
        y = random.randint(0, tamanho_campo-1)
        if campo[y][x] != 9:
            campo[y][x] = 9

def numerando_campo():
    for i in range(tamanho_campo):
        for j in range(tamanho_campo):
            if campo[i][j] == 9:
                if j != tamanho_campo-1 and campo[i][j+1] != 9:
                    campo[i][j+1] += 1
                if j != 0 and campo[i][j-1] != 9:
                    campo[i][j-1] += 1
                if i != tamanho_campo-1 and j != tamanho_campo-1  and campo[i+1][j+1] != 9:
                    campo[i+1][j+1] += 1
                if i != 0 and j != tamanho_campo-1 and campo[i-1][j+1] != 9:
                    campo[i-1][j+1] += 1
                if i != tamanho_campo-1 and j != 0 and campo[i+1][j-1] != 9:
                    campo[i+1][j-1] += 1
                if i != tamanho_campo-1 and campo[i+1][j] != 9:
                    campo[i+1][j] += 1
                if i != 0 and campo[i-1][j] != 9:
                    campo[i-1][j] += 1
                if i != 0 and j != 0 and campo[i-1][j-1] != 9:
                    campo[i-1][j-1] += 1

def mostrar_campo():
    for i in revelado:
        print()
        for j in i:
            print(j, end=" ")

# def mostrar_todo_campo():
#     for i in range(tamanho_campo):
#         for j in range(tamanho_campo):
#             if campo[i][j] == 0:
#                 campo[i][j] = "="
#
#     for i in campo:
#         print()
#         for j in i:
#             print(j, end=" ")

def revelando_campo(x, y, modo):
        if modo == "2":
            if revelado[y][x] == "#":
                revelado[y][x] = "B"
            elif revelado[y][x] == "B":
                revelado[y][x] = "#"
        elif modo == "1":

            revelado[y][x] = campo[y][x]

            if campo[y][x] == 9:
                return "BOOM"

            for _ in range(tamanho_campo):
                for i in range(len(campo)):
                    while 0 in revelado[i]:
                        for x in range(len(revelado[i])):
                            if revelado[i][x] == 0:

                                if x != 0 and revelado[i][x - 1] != "=":
                                    revelado[i][x - 1] = campo[i][x - 1]
                                if x != len(campo[0]) - 1 and revelado[i][x + 1] != "=":
                                    revelado[i][x + 1] = campo[i][x + 1]

                                if i != 0 and revelado[i - 1][x] != "=":
                                    revelado[i - 1][x] = campo[i - 1][x]

                                if i != len(campo[0]) - 1 and revelado[i + 1][x] != "=":
                                    revelado[i + 1][x] = campo[i + 1][x]

                                if x != 0 and i != 0 and revelado[i - 1][x - 1] != "=":
                                    revelado[i - 1][x - 1] = campo[i - 1][x - 1]
                                if x != len(campo[0]) - 1 and i != tamanho_campo - 1 and revelado[i + 1][x + 1] != "=":
                                    revelado[i + 1][x + 1] = campo[i + 1][x + 1]

                                if i != 0 and x != tamanho_campo - 1 and revelado[i - 1][x + 1] != "=":
                                    revelado[i - 1][x + 1] = campo[i - 1][x + 1]

                                if i != len(campo[0]) - 1 and x != 0 and revelado[i + 1][x - 1] != "=":
                                    revelado[i + 1][x - 1] = campo[i + 1][x - 1]

                                revelado[i][x] = "="

criar_campo()







#ADICIONANDO O PYGAME
pygame.init() #começando o pygame

altura_tela = 1000
largura_tela = 1000
tela = pygame.display.set_mode((largura_tela, altura_tela)) #criando a tela



grid = altura_tela//tamanho_campo

font = pygame.font.Font('freesansbold.ttf', grid//2) #Definindo a fonte


relogio = pygame.time.Clock()

while True:
    relogio.tick(15)


    for evento in pygame.event.get(): #Verificando eventos
        if evento.type == QUIT:
            pygame.quit()
            exit()
    if pygame.mouse.get_pressed() == (True, False, False):
        x, y = pygame.mouse.get_pos()
        x = x // grid
        y = y // grid
        revelando_campo(x, y, "1")
    elif pygame.mouse.get_pressed() == (False, False, True):
        x, y = pygame.mouse.get_pos()
        x = x // grid
        y = y // grid
        revelando_campo(x, y, "2")


    for i in range(tamanho_campo):
        for j in range(tamanho_campo):
            if revelado[i][j] == "=":
                pygame.draw.rect(tela, (200, 200, 200), (j*grid, i*grid, grid, grid))
            if revelado[i][j] == "#":
                pygame.draw.rect(tela, (130, 130, 130), (j*grid, i*grid, grid, grid))
            elif type(revelado[i][j]) == int:

                text = font.render(str(revelado[i][j]), True, (255, 255, 255))

                tela.blit(text, (j*grid+grid//3, i*grid+grid//3))
            elif revelado[i][j] == "B":
                pygame.draw.rect(tela, (255, 0, 0), (j * grid, i * grid, grid, grid))




    pygame.display.update() #Atualizando a tela
