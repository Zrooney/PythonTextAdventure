#have a dark room, player searches
#sees a blaster, then an alien shows up
#give option to blast enemy, run(alien sprints, eats you)

#have the keyword checker iterate through defined dictionaries
import keyWordChecker
import rooms
cardinal_directions = ['north', 'south', 'east', 'west']
gameInProgress = True


while gameInProgress == True:
    print("You wake up in the cold floor of a spaceship, unaware of what has \n"
        "happened in the past 48 hours")
    gameInProgress = rooms.room1()

# while currentRoom <= 20 :
#     keyWordChecker.keyWordChecker('search')


#
# print(keyWordChecker.listChecker(cardinal_directions))
# print('There is a wall to the North, East and West of you. You appear to be in some kind of \n'
#       'infirmary. There is a door to your south.')
