import pygame


pygame.init()

screen_width = 800
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))

font = pygame.font.SysFont("Kristen ITC", 50)
font2 = pygame.font.SysFont("Kristen ITC", 30)
jpg = pygame.image.load("fon.jpg")
perc = pygame.image.load("perc.png")
size = (60,50)
new_size = pygame.transform.scale(perc, size)
zvuk = pygame.mixer.Sound("shagi.mp3")


x,y = 140, 40
x1,y1 = 140, 80
x2,y2 = 140, 120
x3, y3 = 100, 200

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.blit(jpg, (0, 0))
    text = font.render("Welcome to game!!", True, (0, 0, 100))
    screen.blit(text, (x, y))
    text2 = font2.render("Welcome to game2!!", True, (110, 10, 100))
    screen.blit(text2, (x1, y1))
    textadsf = font.render("Welcome to game3!!", True, (110, 110, 100))
    screen.blit(textadsf, (x2, y2))
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
    if not keys[pygame.K_w] and not keys[pygame.K_s] and not keys[pygame.K_a] and not keys[pygame.K_d]:
        zvuk.stop()



    pygame.display.update()
