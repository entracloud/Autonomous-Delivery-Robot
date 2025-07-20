# dynamic_env.py
import random

def move_vehicles(env, count=10):
    env.update_vehicles(count)
    # obstacles remain static; vehicles are dynamic
    return env.vehicles

