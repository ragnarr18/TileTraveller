def north(direction):
    if direction=='n':
        return True
    else:
        return False


def south(direction):
    if direction == 's':
        return True
    else:
        return False

def west(direction):
    if direction == 'w':
        return True
    else:
        return False

def east(direction):
    if direction == 'e':
        return True
    else:
        return False

print("You can travel: (N)orth")

possible_directions = 'n'

counter_for_x = 1 
counter_for_y = 1 

victory = False

while not victory:
    direction = input("Direction: ")
    direction = direction.lower()
    if not direction in possible_directions:
        print("Not a valid direction!")
    else:
        if counter_for_x == 1 and counter_for_y ==1 :
            possible_directions = 'n'
        elif counter_for_x ==1 and counter_for_y ==2:
            possible_directions = 'nes'
        elif counter_for_x ==1 and counter_for_y ==3:
            possible_directions = 'se'
        elif counter_for_x ==2 and counter_for_y ==1:
            possible_directions = 'n'
        elif counter_for_x ==2 and counter_for_y ==2:
            possible_directions = 'sw'
        elif counter_for_x ==2 and counter_for_y ==3:
            possible_directions = 'ew'
        elif counter_for_x ==3 and counter_for_y ==1:
            victory = True 
            print("Victory!")
        elif counter_for_x ==3 and counter_for_y ==2:
            possible_directions = 'ns'
        elif counter_for_x ==3 and counter_for_y ==3:
            possible_directions = 'ws'
    
    if north and north in possible_directions:
        counter_for_y +=1
    elif south and south in possible_directions:
        counter_for_y -=1
    elif east and east in possible_directions:
        counter_for_x +=1
    elif west and west in possible_directions:
        counter_for_x -=1
        
