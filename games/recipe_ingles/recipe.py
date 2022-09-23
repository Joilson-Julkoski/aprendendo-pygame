import pygame
from pygame.locals import *

# Lista com os ingredientes chave = nome do ingrediente, valor = lista com x, y, imagem, e se esse ingrediente esta sendo mechido
ingredientes = {"egg" : [[100, 200], pygame.image.load("ovos-removebg-preview-removebg-preview.png"), False],
                "cocoa_powder" : [[400, 50], pygame.image.load("chocolate_em_pó-removebg-preview.png"), False],
                "butter" : [[700, 200], pygame.image.load("manteiga-removebg-preview.png"), False],
                "flour" : [[700, 600], pygame.image.load("farinha_de_trigo-removebg-preview.png"), False],
                "sugar" : [[100, 600], pygame.image.load("866394_1.jpg"), False],
                "beking_powder" : [[300, 800], pygame.image.load("fermento-removebg-preview.png"), False],
                "milk" : [[600, 800], pygame.image.load("leite-removebg-preview.png"), False],
                }
ordem = ["egg", "cocoa_powder", "butter", "flour", "sugar", "beking_powder", "milk"]
receita_txt = ["First, break 4 eggs in the blender", "Put 4 spoons of cocoa powder in the blender",
               "Put 2 spoons of butter", "Add 3 cups of whole wheat flour to the mix", "Let's add 2 cups of sugar",
               "Add 2 spoons of baking powder", "Pour 1 cup of milk", "Pour the mix into the pan",
               "Take it to the preheated oven for 40 minutes at 356 ºF"]

animacao_liquidificador = [pygame.image.load("0.png"),
                           pygame.image.load("1.png"),
                           pygame.image.load("2.png"),
                           pygame.image.load("3.png"),
                           pygame.image.load("4.png"),
                           pygame.image.load("5.png"),
                           pygame.image.load("7 (2).png"),
                           pygame.image.load("9.png")]

# funcao para desenhar os igredientes
def desenhar(pos, color):
    try:
        color = pygame.transform.scale(color, (200, 200))
        tela.blit(color, (pos[0], pos[1]))
    except:
        pygame.draw.rect(tela, color, (pos[0], pos[1], 200, 200))


pygame.init()

tela = pygame.display.set_mode((1000, 1000))

counter, text = 30, '30'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)

relogio = pygame.time.Clock()

font = pygame.font.Font('freesansbold.ttf', 32)

receita_terminou = False

movendo_algo = False

def verificar_colisao(objeto_1, objeto_2):


    if (objeto_1[0] + 1 >= objeto_2[0] and objeto_1[1] + 1 >= objeto_2[1] and objeto_1[0] - 200 <= objeto_2[0] and objeto_1[1] - 200 <= objeto_2[1]) or (objeto_2[0] + 1 >= objeto_1[0] and objeto_2[1] + 1 >= objeto_1[1] and objeto_2[0] - 200 <= objeto_1[0] and objeto_2[1] - 200 <= objeto_1[1]):

        return True
    else:
        return False

fundo =pygame.image.load("fundo.png")
fundo = pygame.transform.scale(fundo, (1000, 1000))
gameover = False
menu = True
while menu:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
        elif evento.type == MOUSEBUTTONUP:

            menu = False
    fundoinicio = pygame.image.load("inicio.png")
    fundoinicio = pygame.transform.scale(fundoinicio, (1000, 1000))
    tela.blit(fundoinicio, (0, 0))
    pygame.display.update()


while True:
    if counter == 0:
        gameover = True
        break
    relogio.tick(64)
    tela.blit(fundo, (0, 0))

    for evento in pygame.event.get():
        if evento.type == pygame.USEREVENT:
            counter -= 1
            text = str(counter).rjust(3)
        if evento.type == QUIT:
            pygame.quit()



    for i in ingredientes.values():
        desenhar(i[0], i[1])


    x_mouse = pygame.mouse.get_pos()[0]
    y_mouse = pygame.mouse.get_pos()[1]

    if pygame.mouse.get_pressed(3) == (True, False, False): #Se o botão do mouse estiver precionado
        for i in ingredientes.values(): #Verifico para todos os ingredientes
            if verificar_colisao((x_mouse, y_mouse), i[0]) and movendo_algo == False: #Se algum esta com o mouse dentro dele e se o mouse ja não estava movendo algo
                movendo_algo = True #Se o mouse não estava movendo algo, agora ta
                i[2] = True # E para saber qual ingrediente ele esta movendo

    else: # Caso o mouse não esteja clicado
        movendo_algo = False #Ele vai parar de mover algo
        for i in ingredientes.values(): # E todos os ingredientes vão deixar de se mover
            i[2] = False
    for i in ingredientes.values(): #Verifico todos os ingredientes
        if i[2] == True: # Proucurando aquele que esteja sendo movido
            i[0][0] = x_mouse - 100 #Então defino o x e y dele para q seja igual ao do mouse
            i[0][1] = y_mouse - 100



    if receita_terminou == False:
        desenhar((400, 400), animacao_liquidificador[0])
        try:
            if verificar_colisao(ingredientes[ordem[0]][0], (400, 400)) and ingredientes[ordem[0]][2] == False:
                animacao_liquidificador.pop(0)
                ingredientes.pop(ordem[0])
                ordem.pop(0)
                receita_txt.pop(0)
        except:
            receita_terminou = True
            ingredientes["liquidificador"] = [[400, 400], pygame.image.load("9.png"), False]
            ingredientes["forma"] = [[100, 600], pygame.image.load("Forma_de_Bolo.png"), False]

    if receita_terminou:
        try:
            if verificar_colisao(ingredientes["liquidificador"][0], ingredientes["forma"][0]):
                ingredientes.pop("liquidificador")

                ingredientes["forma"][1] = pygame.image.load("Forma_de_Bolo-cheia.png")
                receita_txt.pop(0)
        except:
            ingredientes["forno"] = [[800, 600], pygame.image.load("forno.png"), False]
            if verificar_colisao(ingredientes["forma"][0], ingredientes["forno"][0]):
                print(f"Seu tempo foi {30 - counter} segundos")
                break




    tela.blit(font.render(receita_txt[0], True, (255, 255, 255)), (5, 5))
    tela.blit(font.render(text, True, (255, 255, 255)), (5, 50))



    pygame.display.update()


if gameover == False:
    while True:
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
        fundo = pygame.image.load("game win.png")
        fundo = pygame.transform.scale(fundo, (1000, 1000))
        tela.blit(fundo, (0, 0))
        pygame.display.update()
else:
    while True:
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
        fundo = pygame.image.load("game_over.png")
        fundo = pygame.transform.scale(fundo, (1000, 1000))
        tela.blit(fundo, (0, 0))
        pygame.display.update()