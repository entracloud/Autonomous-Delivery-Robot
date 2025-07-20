# environment.py
import random
from math import hypot

def generate_grid(size=15):
    # 0: free, 1: obstacle
    grid = [[0 for _ in range(size)] for _ in range(size)]
    return grid

class Environment:
    def __init__(self, size=15, num_obstacles=40, num_deliveries=5):
        self.size = size
        self.grid = generate_grid(size)
        self.obstacles = set()
        self.delivery_points = []
        self.vehicles = set()
        self.start = (0, 0)
        self._place_obstacles(num_obstacles)
        self.place_delivery_points(num_deliveries)

    def _place_obstacles(self, count):
        while len(self.obstacles) < count:
            x = random.randrange(self.size)
            y = random.randrange(self.size)
            if (x, y) != self.start:
                self.obstacles.add((x, y))
        for x, y in self.obstacles:
            self.grid[y][x] = 1

    def place_delivery_points(self, n=5):
        pts = set()
        while len(pts) < n:
            x = random.randrange(self.size)
            y = random.randrange(self.size)
            if (x,y) not in self.obstacles and (x,y) != self.start:
                pts.add((x,y))
        self.delivery_points = list(pts)

    def update_vehicles(self, count=10):
        # simulate dynamic obstacles (vehicles)
        self.vehicles = set()
        while len(self.vehicles) < count:
            x = random.randrange(self.size)
            y = random.randrange(self.size)
            if self.grid[y][x] == 0 and (x,y) != self.start:
                self.vehicles.add((x,y))

    def is_free(self, node):
        x,y = node
        return 0 <= x < self.size and 0 <= y < self.size and self.grid[y][x] == 0

    def get_neighbors(self, node):
        x,y = node
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        result = []
        for dx,dy in dirs:
            nx, ny = x+dx, y+dy
            if self.is_free((nx,ny)):
                cost = random.randint(1,20)
                result.append(((nx,ny), cost))
        return result