import pygame
from settings import *

class ImageButton():

    def __init__(self, screen, image1, image2):
            """initialise image attributes."""
            self.screen = screen
            self.screen_rect = self.screen.get_rect()
            self.image1 = image1
            self.image2 = image2
            #self.image = image

            #set dimensions and properties of the images.
            self.width, self.height = 300, 300
            self.rect = pygame.Rect(0,0,self.width,self.height)

            #build images' rect object and position it.
            #self.img1_rect = pygame.Rect(0,200,self.width,self.height)
            #self.img2_rect = pygame.Rect(375,200,self.width, self.height)
            #self.rect.center = self.screen_rect.center
            
            self._prep_image()

    def _prep_image(self):
        """position images."""
        #load images here or in main?
        self.img1_rect = self.image1.get_rect()
        self.img2_rect = self.image2.get_rect()
        self.img1_rect.center = (187.5, 350)
        self.img2_rect.center = (562.5, 350)

    def draw_images(self):
        #draw images to screen.
        self.screen.fill(BLACK)
        self.screen.blit(self.image1, self.img1_rect)
        self.screen.blit(self.image2, self.img2_rect)



    def check_answer(self,mouse_pos):
        img1_clicked = self.img1_rect.collidepoint(mouse_pos)
        if img1_clicked:
            print('yay') #return score
        img2_clicked = self.img2_rect.collidepoint(mouse_pos)
        if img2_clicked:
            print('eureka!') #return score

        if img1_clicked or img2_clicked:
            self.round_mc = True #change active round


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.fill(BLACK)
    image1 = pygame.image.load('dandelion.jpg')
    image2 = pygame.image.load('dan2.jpg')

    #image1 = ImageButton.image1
    #image2 = ImageButton.image2
    mouse_pos = pygame.mouse.get_pos()
    imagebutton = ImageButton(screen, image1, image2)


    running = True
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                answer = ImageButton.check_answer(mouse_pos)


        screen.fill(BLACK)
        imagebutton.draw_images()
        pygame.display.update()
        clock.tick(60)






if __name__ == '__main__':
    main()
