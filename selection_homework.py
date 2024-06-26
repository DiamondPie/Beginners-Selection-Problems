print("You are exploring a rainforest in search of treasure. Legend has it that there are some buried on a nearby island.")
option = ""
score = 1

while option not in ['swim', 'wait']: # To insure that the user input is valid
    option = input("You come across a lake. Do you want to swim across, or wait for a boat? (swim/wait)\n>> ")
    
if option == "swim":
    print("You get eaten by a hungry shark. Game over. Your score:", score)
elif option == "wait":
    score += 1
    print("A boat arrives and you arrive at the island safely.")
    
    while option not in ['venture', 'walk']: # To insure that the user input is valid
        option = input("You come to a cave. Do you want to venture inside or walk on? (venture/walk)\n>> ")
        
    if option == "venture":
        print("You are squished by boulders never to be seen again. Game over. Your score:", score)
    elif option == "walk":
        score += 1
        while option not in ['left', 'straight', 'right']: # To insure that the user input is valid
            option = input("You're at a crossroads. Do you go left, right, or straight? (left/right/straight)\n>> ")
            
        if option == "left":
            print("You are trampled by a herd of wildebeest. Game over. Your score:", score)
        elif option == "straight":
            print("You get stung by a poisonous wasp. Game over. Your score:", score)
        elif option == "right":
            score += 1
            print("You march on and find the buried treasure! Yippee!! Your score:", score)
