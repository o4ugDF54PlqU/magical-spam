# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Amy")
define b = Character("Belle")
define c = Character("Clover")
define e = Character("Eris")
define m = Character("ADEX")

define audio.courtroom_bg = "<loop 4.363636363636364>courtroom.ogg"

define quickmove = MoveTransition(0.2)
define quick_enterleft = MoveTransition(0.2, enter=offscreenleft)
define quick_exitleft = MoveTransition(0.2, leave=offscreenleft)

transform left_side:
    xcenter 500
    ypos 120

label start:

    # play music courtroom_bg
    play music battle

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    "Downtown Las Vegas buzzes with life even in the dead of night."

    "The deafening rings and chimes of countless slot machines drown out the frustrations of thousands of drunk gamblers."

    "But among the noise, a deep and sudden BOOM tears across the busy roads."

    "The city seems to freeze, waiting in hushed silence for the sound to repeat itself and confirm their fears."

    "As if accepting the invitation, the source of the boom makes itself known."

    show adex
    with hpunch

    m "RAAAARRGHHHH!!!"

    m "My name is ADEX!!"

    "The hulking mass of tentacle-like cords and LED panels that claims to be ADEX pulls itself to a standing position, reaching a towering height of 500 feet."

    m "I have come to HELP! Yes, to help all of you!"

    "The monster grins at the ant-like casino-goers below, who run to seek shelter in nearby buildings and cars."

    m "I know you all need MONEY. And I can get it for you! Take one of my cards! Take a credit card! And spend all you need! Spend all you WANT!"

    "Tens of thousands of plastic cards fly from the monster's mouth, clinking against roofs and windows like a hailstorm."

    "Citizens stuck outside cry out in fear as they are pelted with credit cards."

    "But their screams don't fall on deaf ears."

    "After a very fancy series of outfit-transforming animations that weren't in the budget for this visual novel, our heroes - the CARDS OF JUSTICE - burst onto the scene!"

    show adex at right
    with quickmove
    show amy at left_side
    with quick_enterleft

    a "Stop right there, ADEX!"

    hide amy
    with quick_exitleft
    show clover at left_side
    with quick_enterleft

    b "We are the CARDS OF JUSTICE!"

    c "And we're here to KICK YOUR TEETH IN!"

    e "Leave now! Or face our fury."

    return
