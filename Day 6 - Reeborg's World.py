# PASTE THE BELOW CODE IN:
# http://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
# THIS WILL NOT WORK OUTSIDE OF THAT LINK
def turn_right():
    turn_left()
    turn_left()
    turn_left()


def move_right():
    while right_is_clear():
        turn_right()
        move()


while not at_goal():
    if right_is_clear():
        move_right()
    elif front_is_clear():
        move()
    else:
        turn_left()
