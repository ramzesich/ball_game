import pygame
import sys


SLEEP_INTERVAL_IN_MILLISECONDS = 2


class DrawableObject:
    def __init__(self):
        self._image = None
        self._rect = None

        self.vertical_speed = 0
        self.horizontal_speed = 0

    @property
    def rect(self):
        return self._rect

    @property
    def image(self):
        return self._image


class Ball(DrawableObject):
    def __init__(self):
        super().__init__()
        self._image = pygame.image.load('intro_ball.gif')
        self._rect = self.ball_image.get_rect()


class Window:
    def __init__(self):
        self.width = 800
        self.height = 600
        self.size = (self.width, self.height)
        self.black_color = (0, 0, 0)

        self.screen = pygame.display.set_mode(self.size)

    def restrict_movement(self, drawable_object, position_delta):
        horizontal, vertical = position_delta
        restrict_conditions = [
            self.drawable_object.rect.left + horizontal < 0,
            self.drawable_object.rect.right + horizontal > self.width,
            self.drawable_object.rect.top + vertical < 0,
            self.drawable_object.rect.bottom + vertical > self.height,
        ]

        for restrict_condition in restrict_conditions:
            if restrict_condition:
                return True

        return False

    def move(self, drawable_object, position_delta):
        if self.restrict_movement(drawable_object, position_delta):
            return

        self.drawable_object.rect.move_ip(position_delta)

    def draw(self, *drawable_objects):
        self.screen.fill(self.black_color)

        for drawable_object in drawable_objects:
            self.screen.blit(drawable_object.image, drawable_object.rect)

        pygame.display.flip()


class BallGame:
    def __init__(self):
        self.window = Window()
        self.ball = Ball()

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        self.window.process_events

    def calculate_position_delta(self):
        keys = pygame.key.get_pressed()
        up = keys[pygame.K_UP]
        down = keys[pygame.K_DOWN]
        left = keys[pygame.K_LEFT]
        right = keys[pygame.K_RIGHT]

        horizontal = -1 if left else 1 if right else 0
        vertical = -1 if up else 1 if down else 0

        return (horizontal, vertical)

    def draw(self):
        self.window.draw(*[self.ball])

    def run(self):
        while True:
            self.process_events()
            self.draw()
            pygame.time.delay(SLEEP_INTERVAL_IN_MILLISECONDS)


if __name__ == '__main__':
    pygame.init()
    BallGame().run()
