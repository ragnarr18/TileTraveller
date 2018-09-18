def north(direction):
    if direction=='n' and 'n' in possible_directions:
        return True
    else:
        return False


def south(direction):
    if direction == 's' and 's' in possible_directions:
        return True
    else:
        return False

def west(direction):
    if direction == 'w' and  'w' in possible_directions:
        return True
    else:
        return False

def east(direction):
    if direction == 'e' and 'e' in possible_directions:
        return True
    else:
        return False

def finish(victory):
    if victory:
        return "Victory!" 
    



possible_directions = 'n'

counter_for_x = 1 
counter_for_y = 1 

victory = False
print("You can travel: (N)orth.")
#print("You can travel: (N)orth.")
while not victory:
    
    direction = input("Direction: ")
    direction = direction.lower()
    if north(direction):
        counter_for_y +=1
    elif south(direction):
        counter_for_y -=1
    elif east(direction) :
        counter_for_x +=1
    elif west(direction) :
        counter_for_x -=1

    if not direction in possible_directions:
        print("Not a valid direction!")
    else:
        print("You can travel: ",end='')
    
        if counter_for_x ==1 and counter_for_y ==2:
            possible_directions = 'nes'
            print("(N)orth or (E)ast or (S)outh." )
        elif counter_for_x ==1 and counter_for_y ==3:
            possible_directions = 'se'
            print("(E)ast or (S)outh.")
        elif counter_for_x ==2 and counter_for_y ==1:
            possible_directions = 'n'
            print("(N)orth.")
        elif counter_for_x ==2 and counter_for_y ==2:
            possible_directions = 'sw'
            print("(S)outh or (W)est.")
        elif counter_for_x ==2 and counter_for_y ==3:
            possible_directions = 'ew'
            print("(E)ast or (W)est.")
        elif counter_for_x ==3 and counter_for_y ==1:
            victory = True 
            break
            
        elif counter_for_x ==3 and counter_for_y ==2:
            possible_directions = 'ns'
            print("(N)orth or (S)outh.")
        elif counter_for_x ==3 and counter_for_y ==3:
            possible_directions = 'ws'
            print(("S)outh or (W)est.")
    

print("Victory!")
