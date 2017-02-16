import pygame
import sys


class BallGame:
    def __init__(self):
        self.window_width = 640
        self.window_height = 480
        self.window_size = (self.window_width, self.window_height)
        self.black_color = (0, 0, 0)

        self.screen = pygame.display.set_mode(self.window_size)

        self.ball = pygame.image.load('intro_ball.gif')
        self.ballrect = self.ball.get_rect()

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                pass

    def move(self):
        if (
            self.ballrect.left <= 0
            or self.ballrect.right >= self.window_width
            or self.ballrect.top <= 0
            or self.ballrect.bottom >= self.window_height
        ):
            return

    def draw(self):
        self.screen.fill(self.black_color)
        self.screen.blit(self.ball, self.ballrect)
        pygame.display.flip()

    def run(self):
        while True:
            self.process_events()
            self.move()
            self.draw()

            pygame.time.delay(10)


if __name__ == '__main__':
    pygame.init()
    BallGame().run()
