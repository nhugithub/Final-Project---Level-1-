import pygame
import os
import random
pygame.init()
width = 1280
height = 720
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Name Of The game")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 64)

#main_dir = os.path.split(os.path.abspath(__file__))[0]
#data_dir = os.path.join(main_dir, "data")
#dishita - made change
#Nhu - made change 
def main():
    # pygame setup    
    p1 = PlayerWasd("./breadman2.png")
    p2 = CatPaw("./cat_paw.png")
    allsprites = pygame.sprite.RenderPlain((p1, p2))
    running = True
    bg_img = pygame.image.load('starter-background.png')
    bg_img = pygame.transform.scale(bg_img,(width, height))
    i = 0
    count = 0

    while running:
        screen.fill((0,0,0))
        screen.blit(bg_img,(i,0))
        screen.blit(bg_img,(width+i,0))
        count+=1
        if(count%random.randint(60, 100)==0):
            allsprites.add(CatPaw("./cat_paw.png"))
        if(i==-width):
           screen.blit(bg_img,(width+i,0))
           i=0
        i-=10

        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               running = False
        
    #################################################################
        # RENDER YOUR GAME HERE
        allsprites.update()
        allsprites.draw(screen)


    ##############################################################
        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()


class CatPaw(pygame.sprite.Sprite):
    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
#        self.speed = 15
        self.image, self.rect = load_image(image,scale=.2)#adjust scale to get character sizing right
        self.rect.topleft = pygame.Vector2(screen.get_width()-70, screen.get_height()-120)#adjust arugments for disired starting position
    def update(self):
        (x,y) = self.rect.topleft
        self.rect.topleft = (x-10,y)

class PlayerWasd(pygame.sprite.Sprite):

    def __init__(self,image):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 15
        self.gravity = 5
        self.jumped = False
        self.jumpCount=20
        self.image, self.rect = load_image(image,scale=1)#adjust scale to get character sizing right
        self.rect.topleft = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)#adjust arugments for disired starting position
    def update(self):
        keys = pygame.key.get_pressed()
        (x,y) = self.rect.topleft
        yvol = self.gravity
        xvol = 0

        if keys[pygame.K_SPACE] and not self.jumped:
            yvol -=150
            self.jumped = True
            self.gravity = 8
        if y > screen.get_height()-290:
            self.jumped = False
            self.gravity = 0

        self.rect.topleft = (x+ xvol, y +yvol)


def writeToScreen(msg, x, y):
        text = font.render(msg, True, (10, 10, 10))
        textpos = text.get_rect(centerx=x, y=y)
        screen.blit(text, textpos)


def load_image(name, colorkey=None, scale=1):
    #fullname = os.path.join(data_dir, name)
    image = pygame.image.load(name)
    size = image.get_size()
    size = (size[0] * scale, size[1] * scale)
    image = pygame.transform.scale(image, size)

    image = image.convert_alpha()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, pygame.RLEACCEL)
    return image, image.get_rect()

#create cat paws w/ collision coding stuff - make a class "cat paw" (same as player class - update/constructor but change location + have ex parameter to change location)
#boolean value at top of file that is 'lost' (to indicate winning or losing), start as false, if anything causes loss set to true
#if(lost): -> print "you lost" on screen or something 












main()