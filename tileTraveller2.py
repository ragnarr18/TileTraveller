def north(direction):
    direction = direction.lower()
    if direction=='n':
        return True
    else:
        return False


def south(direction):
    direction =direction.lower()
    if direction == 's':
        return True
    else:
        return False

def west(direction):
    direction = direction.lower()
    if direction == 'w':
        return True
    else:
        return False

def east(direction):
    direction = direction.lower()
    if direction == 'e':
        return True
    else:
        return False

print("You can travel: (N)orth")

counter_for_x = 1 
counter_for_y = 1 

victory = False

while not victory:
    direction = input("Direction: ")
    if counter_for_x == 1 and counter_for_y == 1:
        
