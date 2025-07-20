# visualization.py
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class Visualizer:
    def __init__(self, env, robot):
        self.env = env
        self.robot = robot
        self.fig, self.ax = plt.subplots()

    def draw(self):
        self.ax.clear()
        grid = self.env.grid
        size = self.env.size
        # draw obstacles
        for x,y in self.env.obstacles:
            self.ax.add_patch(plt.Rectangle((x,y),1,1,color='gray'))
        # draw deliveries
        for x,y in self.env.delivery_points:
            self.ax.add_patch(plt.Rectangle((x,y),1,1,color='red'))
        # draw path
        path = self.robot.path
        if path:
            xs = [p[0]+0.5 for p in path]
            ys = [p[1]+0.5 for p in path]
            self.ax.plot(xs, ys)
        # draw robot
        x,y = self.robot.position
        self.ax.add_patch(plt.Circle((x+0.5,y+0.5),0.3,color='blue'))
        self.ax.set_xlim(0, size)
        self.ax.set_ylim(0, size)
        self.ax.set_aspect('equal')

    def animate(self):
        ani = animation.FuncAnimation(self.fig, lambda i: self.draw(), interval=200)
        plt.show()