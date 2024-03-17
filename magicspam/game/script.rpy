# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define config.menu_include_disabled = True

define a = Character("Amy")
define b = Character("Belle")
define c = Character("Clover")
define e = Character("Eris")
define m = Character("ADEX")

define audio.courtroom_bg = "<loop 4.363636363636364>courtroom.ogg"

define quickmove = MoveTransition(0.2)
define quick_enter_left = MoveTransition(0.2, enter=offscreenleft)
define quick_exit_left = MoveTransition(0.2, leave=offscreenleft)

transform left_first:
    xcenter 360
    ypos 120

transform left_second:
    xcenter 710
    ypos 120

screen alpha_magic:
    add Charge("test.png", 1):
        xalign 0.5
        yalign 0.5


###############################################################################
#  #                                                                       #  #
#  #                     __     _     __   ___     _                       #  #
#  #                    | _|   /_\   | _|   |       |                      #  #
#  #                    |     /   \  |  \   |      _|_                     #  #
#  #                                                                       #  #
###############################################################################

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

    show screen alpha_magic

    "charge by spamming C"

    hide screen alpha_magic

    if decreasing_charge >= 1:
        "we win"
    else:
        "lose"

    "The deafening rings and chimes of countless slot machines drown out the frustrations of thousands of drunk gamblers."

    with hpunch

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

    show adex at right with quickmove
    show amy at left_first with quick_enter_left

    a "Stop right there, ADEX!"

    show belle at left_second
    with quick_enter_left

    b "We are the CARDS OF JUSTICE!"

    hide amy
    with quick_exit_left
    show clover at left_first
    with quick_enter_left

    c "And we're here to KICK YOUR TEETH IN!"

    hide belle
    with quick_exit_left
    show eris at left_second
    with quick_enter_left

    e "Leave now! Or face our fury."

    m "HA! Don't make me laugh! Ha! Look, you're making me laugh!"

    hide clover
    hide eris
    with quick_exit_left

    $ choice1 = True
    $ choice2 = True
    $ choice3 = True
    $ choice4 = True
    jump start_menu

    return


label start_menu:
    
    define key_gofundme = False

    menu:
        
        "Fight the rampaging monster!"

        "♡ Sparkle 'Splosion! ♡" if choice1:
            show amy at left_first
            with quick_enter_left

            a "Don't worry everybody! We're here to help!"
            "Todo <3"

            hide amy
            with quick_exit_left

            $ choice1 = False
            jump start_menu
        
        "♢ Start live-streaming ♢" if choice2:
            "Todo <3"
            $ key_gofundme = True
            $ choice2 = False
            jump start_menu

        "♣ Start charging Glitter Cannon ♣":
            jump part1_stage2
        
        "♠ Shimmering Strike! ♠" if choice4:
            "Todo <3"
            $ choice4 = False
            jump start_menu

    return



label part1_stage2:

    "Todo <3"

    $ choice1 = True
    $ choice2 = True
    $ choice3 = True
    $ choice4 = True
    jump part1_stage2_menu

    return


label part1_stage2_menu:

    define key_calm_the_people = False
    define key_speak_with_victim = False
    define key_happy_eris = False

    menu:

        "♡♢ Rescue civilians in the building ♢♡" if choice1:
            "Todo <3"
            $ key_calm_the_people = True
            $ choice1 = False
            jump part1_stage2_menu
        
        "♠ Save the monster's victim ♠":
            "Todo <3"
            $ key_speak_with_victim = True
            jump part1_stage3
        
        "♣ Call for Eris' help ♣":
            "Todo <3"
            $ key_happy_eris = True
            jump part1_stage3
    
    return


label part1_stage3:

    "Todo <3"

    $ choice1 = True
    $ choice2 = True
    $ choice3 = True
    $ choice4 = True
    jump part1_stage3_menu

    return


label part1_stage3_menu:

    define key_appeal_to_court = False
    define key_guilty_villain = False

    menu:

        "♡ Calm the people ♡" if key_calm_the_people:
            "Todo <3"
            $ key_appeal_to_court = True
            jump part1_stage4
        
        "♠ Talk with the victim ♠" if key_speak_with_victim:
            "Todo <3"
            $ key_guilty_villain = True
            jump part1_stage4
        
        "♢ Blue Brilliance! ♢":
            "Todo <3"
            jump part1_stage4

    return


label part1_stage4:

    "Todo <3"

    jump part2_stage1

    return


###############################################################################
#  #                                                                       #  #
#  #                     __     _     __   ___    ___                      #  #
#  #                    | _|   /_\   | _|   |      __]                     #  #
#  #                    |     /   \  |  \   |     |___                     #  #
#  #                                                                       #  #
###############################################################################

label part2_stage1:

    return
