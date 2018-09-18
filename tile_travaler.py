counter_for_x = 1
counter_for_y = 1

victory = False


possible_dir = 'n'

print("You can travel: (N)orth.")

while not victory:
    direction=input("Direction: ")
    direction = direction.lower()

    if not direction in possible_dir:
        print("Not a valid direction!")
    else:
        if direction == 'n':
            counter_for_y += 1
        elif direction == 's':
            counter_for_y -= 1
        elif direction == 'e':
            counter_for_x += 1
        else:
            counter_for_x -= 1

        print("You can travel: ", end='')
            
        if counter_for_x ==1 and counter_for_y == 1 :
            print("(N)orth.")
            possible_dir = 'n'
        
        elif counter_for_x ==1 and counter_for_y ==2:
            print("(N)orth or (E)ast or (S)outh.")
            possible_dir = 'nes'
        
        elif counter_for_x ==1 and counter_for_y ==3:
            print("(E)ast or (S)outh.")
            possible_dir = 'es'
        
        elif counter_for_x ==2 and counter_for_y ==1:
            print("(N)orth.")
            possible_dir = 'n'
        
        elif counter_for_x ==2 and counter_for_y ==2:
            print("(S)outh or (W)est.")
            possible_dir = 'ws'

        elif counter_for_x ==2 and counter_for_y ==3:
            print("(E)ast or (W)est.")
            possible_dir= 'ew'
        
        elif counter_for_x ==3 and counter_for_y==1:
            victory = True
            
        elif counter_for_x == 3 and counter_for_y ==2:
            print("(N)orth or (S)outh.")
            possible_dir = 'sn'
        
        elif counter_for_x == 3 and counter_for_y ==3:
            print("(S)outh or (W)est.")
            possible_dir= 'sw'


print("Victory!") 
    # elif counter_for_x ==1 and counter_for_y ==3:
    #     print("You can travel: (E)ast or (S)outh.")
    #     possible_dir = 'seSE'
    #     direction=input("Direction: ")
    #     if direction == 's' or direction =='S' and direction in possible_dir:
    #         counter_for_y -=1
    #     elif direction == 'e' or direction == 'E' and direction in possible_dir:
    #         counter_for_x +=1 
    #     else:
    #         print("Not a valid direction!")
    # elif counter_for_x ==2 and counter_for_y == 1:
    #     print("You can travel: (N)orth.")
    #     possible_dir = 'nN'
    #     direction=input("Direction: ")
    #     if direction == 'n' or direction =='N' and direction in possible_dir:
    #         counter_for_y +=1
    #     else:
    #         print("Not a valid direction!")
    # elif counter_for_x ==2 and counter_for_y == 2:
    #     print("You can travel: (W)est or (S)outh.")
    #     possible_dir = 'swSW'
    #     direction=input("Direction: ")
    #     if direction == 's' or direction == 'S' and direction in possible_dir:
    #         counter_for_y -=1
    #     elif direction == 'w' or direction == 'W' and direction in possible_dir:
    #         counter_for_x -=1 
    #     else:
    #         print("Not a valid direction")

    # elif counter_for_x ==2 and counter_for_y ==3:
    #     print("You can travel: (E)ast or (W)est.")
    #     possible_dir = 'weWE'
    #     direction=input("Direction: ")
    #     if direction == 'w' or direction =='W' and direction in possible_dir:
    #         counter_for_x -=1
    #     elif direction == 'e' or direction == 'E' and direction in possible_dir:
    #         counter_for_x +=1
    #     else:
    #         print("Not a valid direction!") 

    # elif counter_for_x ==3 and counter_for_y ==1:
    #     print("Victory!")
    #     victory = True
    
    # elif counter_for_x ==3 and counter_for_y ==2:
    #     print("You can travel: (N)orth or (S)outh.")
    #     possible_dir = 'snSN'
    #     direction=input("Direction: ")
    #     if direction == 's' or direction=='S' and direction in possible_dir:
    #         counter_for_y -=1
    #     elif direction == 'n'or direction =='N' and direction in possible_dir:
    #         counter_for_y +=1 
    #     else:
    #         print("Not a valid direction")
    # elif counter_for_x ==3 and counter_for_y ==3:
    #     print("You can travel: (W)est or (S)outh.")
    #     possible_dir = 'wsWS'
    #     direction=input("Direction: ")
    #     if direction =='s' or direction == 'S' and direction in possible_dir:
    #         counter_for_y-=1
    #     elif direction =='w' or direction == 'W' and direction in possible_dir:
    #         counter_for_x -=1
    #     else:
    #         print("Not a valid direction!")
        
    


