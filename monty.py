import random

def setup_doors():
    doors = ['goat','goat','car']
    random.shuffle(doors)
    return doors

def select_door():
    return random.choice(range(3))
