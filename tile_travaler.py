#you begin in the axes x=1 and y=1
#program gives you your position
#program tells you where you can go from (nsew)
#if your input is within the given directions available, you move
#if your input is not within the given directions available, you don't move
#the program finishes when you have reached x=3 and y=1
#program prints "Victory!"




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

       
            
        if counter_for_x ==1 and counter_for_y == 1 :
            print("You can travel: (N)orth.")
            possible_dir = 'n'
        
        elif counter_for_x ==1 and counter_for_y ==2:
            print("You can travel: (N)orth or (E)ast or (S)outh.")
            possible_dir = 'nes'
        
        elif counter_for_x ==1 and counter_for_y ==3:
            print("You can travel: (E)ast or (S)outh.")
            possible_dir = 'es'
        
        elif counter_for_x ==2 and counter_for_y ==1:
            print("You can travel: (N)orth.")
            possible_dir = 'n'
        
        elif counter_for_x ==2 and counter_for_y ==2:
            print("You can travel: (S)outh or (W)est.")
            possible_dir = 'ws'

        elif counter_for_x ==2 and counter_for_y ==3:
            print("You can travel: (E)ast or (W)est.")
            possible_dir= 'ew'
        
        elif counter_for_x ==3 and counter_for_y==1:
            
            victory = True
           
            

            
        elif counter_for_x == 3 and counter_for_y ==2:
            print("You can travel: (N)orth or (S)outh.")
            possible_dir = 'sn'
        
        elif counter_for_x == 3 and counter_for_y ==3:
            print("You can travel: (S)outh or (W)est.")
            possible_dir= 'sw'

print("Victory!")








    


