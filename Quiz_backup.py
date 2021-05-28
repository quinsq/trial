import pygame
from settings import *
from random import randrange

class Question:
    def __init__(self, question, alternatives, correct_answer, screen):
        self.question = question
        self.alternatives = alternatives
        self.correct_answer = correct_answer
        self.screen = screen

    def draw(self):
        myfont = pygame.font.SysFont("Arial", 30)
        question = myfont.render(self.question, 1, GREEN)
        self.screen.blit(question, (100, 100))


        alternative_1 = myfont.render("1: " + self.alternatives[0], 1, RED)
        self.screen.blit(alternative_1, (100, 200))

        alternative_x = myfont.render("X: " + self.alternatives[1], 1, RED)
        self.screen.blit(alternative_x, (100, 300))

        alternative_2 = myfont.render("2: " + self.alternatives[2], 1, RED)
        self.screen.blit(alternative_2, (100, 400))

    def check_answer(self):
        mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()
        if 150 < mouse_pos_y < 250:
            return self.correct_answer == 0
        elif 250 < mouse_pos_y < 350:
            return self.correct_answer == 1
        elif 350 < mouse_pos_y < 450:
            return self.correct_answer == 2




def run():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.fill(BLACK)
    answer = None

    questions = [["Population of Norway?", ["100", "10000", "5000000"], 2],
     ["Population of Sweden?", ["100", "1000000", "3000"], 1],
     ["What color is the sky?", ["Blue", "Red", "Grey"], 0],
     ["What number i Pi?", ["3,14", "3,96","4,15"], 0]
     ]


    q_num = randrange(0, len(questions))
    question = Question(questions[q_num][0], questions[q_num][1], questions[q_num][2], screen)
    #question = Question(["Population of Norway?", ["100", "10000", "5000000"], 2], screen)

    running = True
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                answer = question.check_answer()

        if answer == True:
            print("Frage richtig")
            #q_num = randrange(0, len(questions))
            #question = Question(questions[q_num][0], screen) #<, questions[q_num][1], questions[q_num][2], screen)


        screen.fill(BLACK)
        question.draw()
        pygame.display.update()
        clock.tick(60)


def main():
    run()


if __name__ == '__main__':
    main()

#class Question:
    #def __init__(self, question, alternatives, correct_answer, screen):
        #self.question = question
        #self.alternatives = alternatives
        #self.correct_answer = correct_answer
        #self.screen = screen

    #def draw(self):
        #myfont = pygame.font.SysFont("Arial", 30)
        #question = myfont.render(self.question, 1, GREEN)
        #self.screen.blit(question, (100, 100))


        #alternative_1 = myfont.render("1: " + self.alternatives[0], 1, RED)
        #self.screen.blit(alternative_1, (100, 200))

        #alternative_x = myfont.render("X: " + self.alternatives[1], 1, RED)
        #self.screen.blit(alternative_x, (100, 300))

        #alternative_2 = myfont.render("2: " + self.alternatives[2], 1, RED)
        #self.screen.blit(alternative_2, (100, 400))

    #def check_answer(self):
        #mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()
        #if 150 < mouse_pos_y < 250:
            #return self.correct_answer == 0
        #elif 250 < mouse_pos_y < 350:
            #return self.correct_answer == 1
        #elif 350 < mouse_pos_y < 450:
        #    return self.correct_answer == 2




#def run():
    #pygame.init()
    #screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    #screen.fill(BLACK)
    #answer = None

    #questions = [["Population of Norway?", ["100", "10000", "5000000"], 2],
    # ["Population of Sweden?", ["100", "1000000", "3000"], 1],
     #["What color is the sky?", ["Blue", "Red", "Grey"], 0],
     #["What number i Pi?", ["3,14", "3,96","4,15"], 0]
    # ]


    #q_num = randrange(0, len(questions))
    #question = Question(questions[q_num][0], questions[q_num][1], questions[q_num][2], screen)


    #running = True
    #clock = pygame.time.Clock()
    #while running:
        #for event in pygame.event.get():
            #if event.type == pygame.QUIT:
                #running = False
            #elif event.type == pygame.MOUSEBUTTONDOWN:
                #answer = question.check_answer()

        #if answer == True:
            #q_num = randrange(0, len(questions))
            #question = Question(questions[q_num][0], questions[q_num][1], questions[q_num][2], screen)

        #screen.fill(BLACK)
        #question.draw()
        #pygame.display.update()
        #clock.tick(60)


#def main():
    #run()


#if __name__ == '__main__':
    #main()"""
