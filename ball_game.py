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
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                self.move()

    def calculate_position_delta(self):
        keys = pygame.key.get_pressed()
        up = keys[pygame.K_UP]
        down = keys[pygame.K_DOWN]
        left = keys[pygame.K_LEFT]
        right = keys[pygame.K_RIGHT]

        horizontal = -1 if left else 1 if right else 0
        vertical = -1 if up else 1 if down else 0

        return (horizontal, vertical)

    def restrict_movement(self, position_delta):
        horizontal, vertical = position_delta
        restrict_conditions = [
            self.ballrect.left + horizontal < 0,
            self.ballrect.right + horizontal > self.window_width,
            self.ballrect.top + vertical < 0,
            self.ballrect.bottom + vertical > self.window_height,
        ]

        for restrict_condition in restrict_conditions:
            if restrict_condition:
                return True

        return False

    def move(self):
        position_delta = self.calculate_position_delta()
        if self.restrict_movement(position_delta):
            return

        self.ballrect.move(position_delta)

    def draw(self):
        self.screen.fill(self.black_color)
        self.screen.blit(self.ball, self.ballrect)
        pygame.display.flip()

    def run(self):
        while True:
            self.process_events()
            self.draw()


if __name__ == '__main__':
    pygame.init()
    BallGame().run()
