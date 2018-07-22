import keyWordChecker
room_numbers = [0, 1, 2]
cardinal_directions = ['north', 'south', 'east', 'west']
entered = False
ran = False

def room1():
    #print('sup')
    while entered == False:
        userInput = input('>').lower().strip()
        #for i in range(0,1):
        print(entered)
        if userInput == 'leave':
            print('You open the door, and it locks behind you.')
            entered == True
            return False
        if userInput == 'search':
            print('You find a shank next to you, you hear grumbling in the distance')
            ran = True
        elif ran == True:
            print('You already found the shank')
        else:
            print('>I didn\'t quite get that Dave.')
        #if userInput == cardinal_directions:
         #   print('sup')
       # if keyWordChecker.listChecker(cardinal_directions):
        #    print('There is a wall to the North, East and West of you. You appear to be in some kind of \n'
         #         'infirmary. There is a door to your south.')

