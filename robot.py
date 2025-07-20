# robot.py
import time
from heuristics import a_star, rbfs

class Robot:
    def __init__(self, env, algorithm='A*'):
        self.env = env
        self.algorithm = algorithm
        self.position = env.start
        self.path = []

    def plan(self, goal):
        if self.algorithm == 'A*':
            return a_star(self.position, goal, self.env)
        else:
            return rbfs(self.position, goal, self.env)

    def execute(self, path):
        for step in path[1:]:
            self.position = step
            time.sleep(0.1)  # simulate movement
