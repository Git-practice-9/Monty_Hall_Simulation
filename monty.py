import random

def setup_doors():
    doors = ['goat','goat','car']
    random.shuffle(doors)
    return doors

def select_door():
    return random.choice(range(1,3+1))

def monty_choice(doors, selected_door):
    remaining_goat_doors = [i for i, prize in enumerate(doors) if prize == 'goat' and i != selected_door]
    return random.choice(remaining_goat_doors)
