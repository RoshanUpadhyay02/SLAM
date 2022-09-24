import pickle
import pygame
from room import Room
from lidar import distance
from robots import Mouse
from constants import *


class BuildEnvironment(object):
    def __init__(self, robot=Mouse, dimensions=(1200, 600), filename= r"/home/roshanupahdyay/Documents/ExtraS/Clubs/Optizen/SLAM/Code/With image from webcam/img.jpg"):
        pygame.init()
        self.pointcloud = set()
        self.data = []
        self.filename = filename or Room(dimensions).filename
        self.image = pygame.image.load(self.filename)
        self.data_layer = self.image.copy()
        self.data_layer.fill(BLACK)
        pygame.display.set_caption(f"SLAM ({self.filename.split('.')[0]})")
        self.w, self.h = dimensions
        self.robot = robot(self)
        self.map = pygame.display.set_mode(dimensions)
        self.map.blit(self.image, (0, 0))
        pygame.display.update()

    def in_collision(self, x, y, dist=5):
        for point in self.data:
            if distance(x, y, *point) <= dist:
                return True
        return False

    def iterate(self):
        self.data = self.robot.scan()
        for i in self.data:
            self.pointcloud.add(i)
        self.robot.update(self.in_collision)

    def render_map(self):
        for point in self.pointcloud:
            self.data_layer.set_at(point, RED)
        pygame.draw.circle(self.data_layer, BLUE, self.robot.position, self.robot.bubble)

    def update(self):
        self.map.blit(self.data_layer, (0, 0))
        self.data_layer.fill(BLACK)

    def save(self):
        with open(self.filename.split('.')[0] + '.pickle', 'wb') as f:
            pickle.dump(self.pointcloud, f)






