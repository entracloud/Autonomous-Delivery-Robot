# main.py
from environment import Environment
from robot import Robot
from visualization import Visualizer
from dynamic_env import move_vehicles

if __name__ == '__main__':
    env = Environment()
    robot = Robot(env, algorithm='A*')
    viz = Visualizer(env, robot)

    for goal in env.delivery_points:
        path, cost, expanded = robot.plan(goal)
        robot.path = path
        print(f"Planned path to {goal} cost={cost} expanded={expanded}")
        viz.animate()
        robot.execute(path)
        # update dynamic environment
        env.start = robot.position
        move_vehicles(env)
    print("All deliveries completed.")
