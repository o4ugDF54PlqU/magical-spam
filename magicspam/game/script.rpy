# The script of the game goes in this file.
init python:
    # Define the variable to be decreased
    decreasing_charge = 0
    last_event_time = pygame.time.get_ticks()

    def check_win():
        global decreasing_charge
        if decreasing_charge >= 1:
            renpy.jump("part1_stage4.aftermath")

    def decrease_charge(amount):
        global decreasing_charge
        if decreasing_charge < 1:
            decreasing_charge -= amount
        if decreasing_charge < 0:
            decreasing_charge = 0

    def increase_charge(amount):
        global decreasing_charge
        decreasing_charge += amount
        check_win()


# Declare characters used by this game. The color argument colorizes the
# name of the character.

define config.menu_include_disabled = True

define a = Character("Amy")
define b = Character("Belle")
define c = Character("Clover")
define e = Character("Eris")
define m = Character("ADEX")

define audio.courtroom_bg = "<loop 4.363636363636364>courtroom.ogg"

define quickleft = MoveTransition(0.2, enter=offscreenleft, leave=offscreenleft)

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

    "The deafening rings and chimes of countless slot machines drown out the frustrations of thousands of drunk gamblers."

    with hpunch

    "But among the noise, a deep and sudden BOOM tears across the busy roads."

    "The city seems to freeze, waiting in hushed silence for the sound to repeat itself and confirm their fears."

    "As if accepting the invitation, the source of the boom makes itself known."

    show adex
    with hpunch

    m "RAAAARRGHHHH!!!"

    m "My name is ADEX!!"

    "The hulking mass of tentacle-like cords and LED panels that claims to be ADEX pulls itself to a standing position, reaching a towering height of 200 feet."

    m "I have come to HELP! Yes, to help all of you!"

    "The monster grins at the ant-like casino-goers below, who run to seek shelter in nearby buildings and cars."

    m "I know you all need MONEY. And I can get it for you! Take one of my cards! Take a credit card! And spend all you need! Spend all you WANT!"

    "Tens of thousands of plastic cards fly from the monster's mouth, clinking against roofs and windows like a hailstorm."

    "Citizens stuck outside cry out in fear as they are pelted with credit cards."

    "But their screams don't fall on deaf ears."

    "After a very fancy series of outfit-transforming animations that aren't in the budget for this visual novel, our heroes - the CARDS OF JUSTICE - burst onto the scene!"

    show adex at right
    show amy at left_first
    with quickleft

    a "Stop right there, ADEX!"

    show belle at left_second
    with quickleft

    b "We are the CARDS OF JUSTICE!"

    hide amy
    show clover at left_first
    with quickleft

    c "And we're here to KICK YOUR TEETH IN!"

    hide belle
    show eris at left_second
    with quickleft

    e "Leave now! Or face our fury."

    m "HA! Don't make me laugh! Ha! Look, you're making me laugh!"

    hide clover
    hide eris
    with quickleft

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
            show amy at left_second
            with quickleft

            a "Don't worry everybody! We're here to help!"

            show eris at left_first
            with quickleft

            e "This monster is huge. We need to give Clover the chance to charge up Glitter Cannon or we don't stand a chance."

            hide eris
            show belle at left_first
            with quickleft

            b "Amy! Distract it with one of your attacks! Give it as many rainbows as you can!"

            a "Right!"

            hide belle
            with quickleft

            a "SPARKLE-"

            a "'SPLOOOSION!!"

            "Amy gathers a ball of blinding light around her chest, closing her eyes as tightly as she can as the white beams streaming from it grow ever stronger."

            with hpunch

            "Finally, she thrusts her hands forward, channeling the light into a laser that crackles with electric energy, piercing through the monster's eye."

            "ADEX stumbles backwards as burnt pieces of wire and rubber fall from its face, but it holds its ground and turns away from the light."

            if key_gofundme:

                show belle at left_first
                with quickleft

                "Belle brings her phone to Amy's face."

                b "Say hi to the chat, Amy!"

                a "(rgh) Hi chat! Um. Subscribe!"

                hide belle
                with quickleft
            
            "The monster leans back towards the Cards of Justice and releases an ear-shattering roar."

            show amy at left_first
            with quickleft
            with hpunch

            "Amy loses her focus on the attack, which bursts into an explosion of light, knocking Amy off her feet."

            a "Shoot! I'm sorry guys, I hope that was enough time! I couldn't hold him for long!"

            show amy at left_second
            show eris at left_first
            with quickleft

            e "Don't worry. You did what you needed."

            hide eris
            show clover at left_first
            with quickleft

            if preferences.clover_swear:
                c "Get his ass, Amy!"
            else:
                c "Get his a**, Amy!"

            hide clover
            hide amy
            with quickleft

            $ choice1 = False
            jump start_menu
        
        "♢ Start live-streaming ♢" if choice2:
            
            show belle at left_second
            with quickleft

            b "Hang on, guys. This is a great chance to stream for our Twitch channel!"

            show clover at left_first
            with quickleft
            
            c "Really?! Now?"

            hide clover
            show amy at left_first
            with quickleft

            a "Hey, we made Belle the Social Media Director for a reason. She knows what she's doing!"

            b "I'll handle it. You guys keep focusing on the fight, and I'll make sure I get good shots!"

            hide amy
            with quickleft

            b "Ok, let's see. \"Big Monster in Las Vegas! | ~*~ New emotes for subscribers ~*~\". And then we'll say this is \"Just Chatting\"..."

            hide belle
            with quickleft

            $ key_gofundme = True
            $ choice2 = False
            jump start_menu

        "♣ Start charging Glitter Cannon ♣":
            jump part1_stage2
        
        "♠ Shimmering Strike! ♠" if choice4:
            
            show belle at left_first
            with quickleft

            b "Look! There's a giant red bulb on the back of its neck! Maybe that's its weak spot!"

            show eris at left_second
            with quickleft

            e "Stand back. I'm on it."

            hide belle
            with quickleft

            "Eris leaps across the neon signs that illuminate the Las Vegas street and draws a humming violet saber from behind her back."

            "She reaches a hotel behind the monster and climbs up the wall to a balcony on the 20th floor, scaring a cat that had been calmly watching the chaos through a window."

            e "Shimmering Strike!"

            "Eris propels herself off the balcony and plunges her blade into the red bulb, which shatters into thousands of glimmering scarlet shards."
            
            "ADEX reaches a massive arm towards its back, which Eris swiftly dodges."

            "The monster lightly scratches its back where the bulb was, then returns to the fight, apparently unbothered."

            show belle at left_first
            with quickleft

            b "Huh. I guess that was just... a big red bulb or something. Sorry, that was a bad call."

            e "No, I thought it would do something, too. I guess we need to try something else."

            hide belle
            hide eris
            with quickleft

            $ choice4 = False
            jump start_menu

    return



label part1_stage2:

    "ADEX moves towards the hotel behind it and peers through the windows. Firefighters and volunteers are desperately trying to escort everybody out of the building as quickly as possible."

    show clover at left_second
    with quickleft

    if preferences.clover_swear:
        c "Shit, this guy is an actual beast. Back away, guys! I'm gonna do it!"
    else:
        c "Jeez, this guy is an actual beast. Back away, guys! I'm gonna do it!"

    show amy at left_first
    with quickleft

    a "Whoo! Glitter Cannon!"

    hide amy
    show belle at left_first
    with quickleft

    b "You're right. For once, the situation calls for Glitter Cannon. Just be careful."

    c "I know, I know. Now buy me time while I charge up!"

    hide belle
    show eris at left_first
    with quickleft

    e "WAIT! Look in that thing's hand! There's someone there!"

    "Amidst the tangled cables that compose ADEX's hand, a man struggles against the monsters grip and yells unintelligibly at its face."

    if preferences.clover_swear:
        c "Damn it. I'll try to aim the cannon to not hit him. But it won't be easy if this dude keeps throwing stupid credit cards at me!"
    else:
        c "Uh oh. I'll try to aim the cannon to not hit him. But it won't be easy if this dude keeps throwing stupid credit cards at me!"

    hide eris
    hide clover
    with quickleft

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

    show screen alpha_magic

    "charge by spamming C"

label .aftermath:

    hide screen alpha_magic

    if decreasing_charge >= 1:
        "we win"
    else:
        "lose"

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
