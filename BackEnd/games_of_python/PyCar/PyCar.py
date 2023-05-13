import pygame
import os
import random
from time import sleep

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 800

# 색 지정
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (150, 150, 150)
RED = (255, 0, 0)

# 게임 경로 설정하기
GAME_ROOT_FOLDER = os.path.dirname(__file__)
IMAGE_FOLDER = os.path.join(GAME_ROOT_FOLDER, "images")
SOUND_FOLDER = os.path.join(GAME_ROOT_FOLDER, "sounds")

class Car:
    image_car = ['RacingCar01.png', 'RacingCar02.png', 'RacingCar03.png', 'RacingCar04.png', \
                 'RacingCar05.png', 'RacingCar06.png', 'RacingCar07.png', 'RacingCar08.png', \
                 'RacingCar09.png', 'RacingCar10.png', 'RacingCar11.png', 'RacingCar12.png', \
                 'RacingCar13.png', 'RacingCar14.png', 'RacingCar15.png', 'RacingCar16.png', \
                 'RacingCar17.png', 'RacingCar18.png', 'RacingCar19.png', 'RacingCar20.png' ]

    def __init__(self, x=0, y=0, dx=0, dy=0):
        self.image = ""
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

    def load_image(self):
        self.image = pygame.image.load(os.path.join(IMAGE_FOLDER, random.choice(self.image_car)))
        self.width = self.image.get_rect().size[0]
        self.height = self.image.get_rect().size[1]

    def draw_image(self):
        screen.blit(self.image, [self.x, self.y])

    def move_x(self):
        self.x += self.dx

    def move_y(self):
        self.y += self.dy

    def check_out_of_screen(self):
        if self.x + self.width > WINDOW_WIDTH or self.x < 0 :
            self.x -= self.dx

    def check_crash(self, car):
        if (self.x + self.width > car.x) and (self.x < car.x + car.width) \
            and (self.y < car.y+car.height) and (self.y + self.height) :
            return True
        else :
            return False

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("PyCar: Racing Car Game")
    clock = pygame.time.Clock()

    # 게임 사운드
    pygame.mixer.music.load(os.path.join(SOUND_FOLDER, "race.wav"))
    sound_crash = pygame.mixer.Sound(os.path.join(SOUND_FOLDER, "crash.wav"))
    sound_engine = pygame.mixer.Sound(os.path.join(SOUND_FOLDER, "engine.wav"))

    # 사용자 레이싱 카 생성
    player = Car(WINDOW_WIDTH / 2, (WINDOW_HEIGHT - 150), 0, 0)
    player.load_image()

    # 컴퓨터 레이싱 카 생성
    cars = []
    car_count = 3
    for i in range(car_count):
        x = random.randrange(0, WINDOW_WIDTH-55)
        y = random.randrange(-150, -50)
        car = Car(x, y, 0, random.randint(5, 10))
        car.load_image()
        cars.append(car)

    # 도로 차선 생성
    lanes = []
    lane_width = 10
    lane_height = 80
    lane_margin = 20
    lane_count = 10
    lane_x = (WINDOW_WIDTH - lane_width) / 2
    lane_y = -10
    for i in range(lane_count):
        lanes.append([lane_x, lane_y])
        lane_y += lane_height + lane_margin