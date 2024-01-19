import pygame
from threading import Thread


pygame.init()

screen_width = 800
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))

def Bullet():
    global x4
    global x3
    x4 = x3
    if storona == "left":
        for i in range(int(x4)):
            screen.blit(jpg, (0, 0))
            screen.blit(perconak, (x3, y3))
            screen.blit(new_size2, (x5, y5))
            text = font.render("Welcome to game!!", True, (0, 0, 100))
            screen.blit(text, (x, y))
            screen.blit(new_bullet, (x4, y3 + 17))
            x4 -= 2
            pygame.display.update()

    else:
        for i in range(800 - (int(x4))):
            screen.blit(jpg, (0, 0))
            screen.blit(perconak, (x3, y3))
            screen.blit(new_size2, (x5, y5))
            text = font.render("Welcome to game!!", True, (0, 0, 100))
            screen.blit(text, (x, y))
            screen.blit(new_bullet, (x4 + 50, y3 + 17))
            x4 += 2
            pygame.display.update()

def Perc():
    global x3
    global y3
    global perconak
    global keys
    global storona
    screen.blit(jpg, (0, 0))
    text = font.render("Welcome to game!!", True, (0, 0, 100))
    screen.blit(text, (x, y))
    screen.blit(perconak, (x3, y3))
    screen.blit(new_size2, (x5, y5))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        y3 -= 0.5
        zvuk.play()

    if keys[pygame.K_s]:
        zvuk.play()
        y3 += 0.5

    if keys[pygame.K_d]:
        x3 += 0.5
        zvuk.play()
        storona = "right"
        perconak = new_rot_size

    if keys[pygame.K_a]:
        x3 -= 0.5
        zvuk.play()
        storona = "left"
        perconak = new_size


font = pygame.font.SysFont("Kristen ITC", 50)
font2 = pygame.font.SysFont("Kristen ITC", 30)
jpg = pygame.image.load("fon.jpg")
perc = pygame.image.load("perc.png")
rot_repc = pygame.image.load("rot_perc.png")
perc2 = pygame.image.load(("perc2.png"))
bullet = pygame.image.load("pylya.png")
size = (60,50)
new_size = pygame.transform.scale(perc, size)
new_rot_size = pygame.transform.scale(rot_repc,size)
new_size2 = pygame.transform.scale(perc2, size)
size2 = (10,10)
new_bullet = pygame. transform.scale(bullet, size2)
zvuk = pygame.mixer.Sound("shagi.mp3")
perconak = new_size
storona = "left"


x,y = 140, 40
x1,y1 = 140, 80
x2,y2 = 140, 120
x3, y3 = 100, 200
x5, y5 = 500, 200

try:
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        Perc()

        if keys[pygame.K_SPACE]:
            thread1 = Thread(target=Bullet)
            thread2 = Thread(target=Perc)

            thread1.start()
            thread2.start()
            thread1.join()
            thread2.join()





        if not keys[pygame.K_w] and not keys[pygame.K_s] and not keys[pygame.K_a] and not keys[pygame.K_d]:
            zvuk.stop()



        pygame.display.update()
except NameError:
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()






        screen.blit(jpg, (0, 0))
        text = font.render("Welcome to game!!", True, (0, 0, 100))
        screen.blit(text, (x, y))
        screen.blit(new_size, (x3, y3))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            y3 -=0.3
            zvuk.play()

        if keys[pygame.K_s]:
            zvuk.play()
            y3 +=0.3

        if keys[pygame.K_d]:
            x3 +=0.3
            zvuk.play()
        if keys[pygame.K_a]:
            x3 -=0.3
            zvuk.play()
        if keys[pygame.K_SPACE]:
            x4 = x3
            for i in range(800):
                screen.blit(jpg, (0, 0))
                screen.blit(new_size, (x3, y3))
                text = font.render("Welcome to game!!", True, (0, 0, 100))
                screen.blit(text, (x, y))
                screen.blit(new_bullet, (x4, y3 + 17))
                x4 -= 1
                pygame.display.update()




        if not keys[pygame.K_w] and not keys[pygame.K_s] and not keys[pygame.K_a] and not keys[pygame.K_d]:
            zvuk.stop()



        pygame.display.update()
