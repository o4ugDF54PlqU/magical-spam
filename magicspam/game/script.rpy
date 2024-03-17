# The script of the game goes in this file.
init python:
    # Define the variable to be decreased
    decreasing_charge = 0
    last_event_time = pygame.time.get_ticks()

    def check_win(label):
        global decreasing_charge
        if decreasing_charge >= 1:
            renpy.jump(label)
    
    def check_faded(alpha, label):
        if alpha <= 0:
            renpy.jump(label)

    def decrease_charge(amount):
        global decreasing_charge
        if decreasing_charge < 1:
            decreasing_charge -= amount
        if decreasing_charge < 0:
            decreasing_charge = 0

    def increase_charge(amount):
        global decreasing_charge
        decreasing_charge += amount


# Declare characters used by this game. The color argument colorizes the
# name of the character.

define config.menu_include_disabled = True

define a = Character("Amy", color="#d60a1b")
define b = Character("Belle", color="#1049ce")
define c = Character("Clover", color="#10a341")
define e = Character("Eris", color="#bb0ed6")
define m = Character("ADEX", color="#FFFFFF")
define v = Character("Victim", color="#f5c255")
define j = Character("Judge", color="#d39a20")

define audio.courtroom_bgm = "<loop 4.363636363636364>courtroom.ogg"

define quickleft = MoveTransition(0.2, enter=offscreenleft, leave=offscreenleft)

transform left_first:
    xalign 0.15
    xanchor 0.5
    ypos 120

transform left_second:
    xalign 0.35
    xanchor 0.5
    ypos 120

define charge_mult = 1

screen alpha_magic_p1:
    add Charge("magicball.png", "part1_stage4.fadeout", charge_mult):
        xalign 0.5
        yalign 0.5

screen after_magic_p1:
    add Fadeout("white.png", "part1_stage4.aftermath"):
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

    # play music courtroom_bgm
    play music battle
    # jump part2_stage1

    scene bg city

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

    "A hulking mass of tentacle-like cords and LED panels pulls itself to a standing position, reaching a towering height of 200 feet."

    m "My name is ADEX!!"

    m "I have come to HELP! Yes, to HELP all of you!"

    "ADEX grins at the scrambling ant-like casino-goers below."

    m "I know you all need MONEY. And I can get it for YOU!"

    "A hailstorm of plastic cards came from the monster's mouth, smashing into roofs and windows."

    m "TAKE one of my cards! OPEN a credit line! SPEND all you need! SPEND all you WANT!"

    "Those still stuck outside cry out in fear as they are pelted with credit cards."

    "But their screams didn't fall on deaf ears."

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

    m "HA! Don't make me laugh! HA! Look, you're making me LAUGH!"

    hide clover
    hide eris
    with quickleft

    $ choice1 = True
    $ choice2 = True
    $ choice3 = True
    $ choice4 = True

label .choices:
    
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
                c "Get him, Amy!"

            hide clover
            hide amy
            with quickleft

            $ choice1 = False
            jump .choices
        
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
            jump .choices

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
            jump .choices

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

    b "You're right. For once, the situation calls for Glitter Cannon."

    hide belle
    show eris at left_first
    with quickleft

    e "Just be careful."

    c "I know, I know. Now buy me time while I charge up!"

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

label .choices:

    define key_calm_the_people = False
    define key_speak_with_victim = False
    define key_happy_eris = False
    define key_blame_clover = True

    menu:

        "♡♢ Rescue civilians in the building ♢♡" if choice1:
            "Todo <3"
            $ key_calm_the_people = True
            $ choice1 = False
            jump .choices
        
        "♠ Save the monster's victim ♠":
            "Todo <3"
            $ key_speak_with_victim = True
            jump part1_stage3
        
        "♣ Call for Eris' help ♣":
            "Todo <3"
            $ key_happy_eris = True
            $ key_blame_clover = False
            jump part1_stage3
    
    return


label part1_stage3:

    "Todo <3"

    $ choice1 = True
    $ choice2 = True
    $ choice3 = True
    $ choice4 = True

label .choices:

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

    call screen alpha_magic_p1

    # "charge by spamming C"

label .fadeout:

    hide screen alpha_magic_p1
    call screen after_magic_p1

label .aftermath:
    
    hide screen after_magic_p1

    "Todo <3"

    jump part2_A1

    return


###############################################################################
#  #                                                                       #  #
#  #                     __     _     __   ___    ___                      #  #
#  #                    | _|   /_\   | _|   |      __]                     #  #
#  #                    |     /   \  |  \   |     |___                     #  #
#  #                                                                       #  #
###############################################################################

label part2_A1:
    
    $ charge_multiplier = 1
    # reset multiplier

    show bg jail
    play music jail

    "The girls end up in jail."

    "todo <3"

    "todo <3"

    $ choice2 = True

label .choices:

    menu:

        "♢ Go peacefully ♢":
            "Todo <3"
            jump part2_A2
        
        "♡ Summon a puppy ♡" if choice2:
            "Todo <3"
            $ choice2 = False
            jump .choices
        
        "♣ Start charging Glitter Cannon ♣":
            "Todo <3"
            jump part2_A2
        
        "♠ Blame Clover ♠" if key_blame_clover:
            jump bad_ending1

    "court"
    return


label part2_A2:

    show bg court
    play music audio.courtroom_bgm

    "You are charged with vandalism."

    "How do you plead?"

    menu:

        "♢♠ Guilty ♠♢":
            jump part2_A3
        
        "♡♣ Not guilty ♣♡":
            jump part2_B3


label part2_A3:

    "We plead guilty, BUT..."

    $ choice1 = True

label .choices:

    menu:

        "♡ Look! A puppy! ♡" if choice1:
            "Todo <3"
            $ choice1 = False
            jump .choices
        
        "♠ We only meant to do the right thing ♠":
            jump part2_A4
        
        "♢ We can fix our mistakes ♢":
            jump part2_C4
        
        "♣ *Stick out your tongue* ♣":
            jump bad_ending2


label part2_A4:
    
    "Do you have anybody to vouch for you?"

label .choices:

    menu:

        "♡ The citizens in the hotel ♡" if key_calm_the_people:
            "Todo <3"
            jump part_A5
        
        "♠ The monster's victim ♠" if key_speak_with_victim:
            "Todo <3"
            jump part2_A5
        
        "♢ Twitch chat ♢" if key_gofundme:
            "Todo <3"
            jump bad_ending2
        
        "♣ Your mom! ♣":
            "Todo <3"
            jump bad_ending2


label part2_A5:

    "Very well. We will let you off with some fines as a warning. Wait in the holding cell."

    scene bg jail
    play music jail

    e "I don't want to get in trouble again. I want to leave the group."
    
    if key_happy_eris:
        jump part2_A6
    else:
        jump neutral_ending2
    
    return


label part2_A6:

    c "No!" 
    
    e "Well, what do you want to do with your life?"

    $ choice1 = True
    $ choice2 = True
    $ choice3 = True

    define confessions_made = 0

label .choices:

    menu:
        
        "♡ Be remembered as a good person ♡" if choice1:
            $ choice1 = False
            $ confessions_made = confessions_made + 1

            if confessions_made >= 3:
                jump good_ending3
            
            jump .choices
        
        "♢ Keep doing things with you guys ♢" if choice2:
            $ choice2 = False
            $ confessions_made = confessions_made + 1

            if confessions_made >= 3:
                jump good_ending3
            
            jump .choices
        
        "♣ Become a better version of me ♣" if choice3:
            $ choice3 = False
            $ confessions_made = confessions_made + 1

            if confessions_made >= 3:
                jump good_ending3
            
            jump .choices


# Plead not guilty
label part2_B3:

    "Well, we have a witness here. *Brings in ADEX*"

    menu:

        "♠ Call the victim to the stand ♠" if key_speak_with_victim:
            "Todo <3"
            jump part2_B4
        
        "♣ Try to enrage the monster ♣":
            "Todo <3"
            jump bad_ending2
        
        "♢ Accuse the monster ♢":
            "Todo <3"
            jump bad_ending2
        
        "♡ Appeal to ADEX's empathy ♡":
            "Todo <3"
            jump bad_ending2


label part2_B4:

    "You may ask the victim one question."

    $ choice4 = True

label .choices:

    menu:
        
        "♢ Why did you agree to ADEX's terms? ♢":
            "*Judge victim blames*"
            jump bad_ending2
        
        "♠ Are you still in debt? ♠":
            "*Judge victim blames*"
            jump bad_ending2

        "♡ Are you ok? ♡":
            jump part2_B5

        "♣ Ok, but the Glitter Cannon was pretty sick, right?" if choice4:

            v "Haha yeah, it was pretty cool actually."

            c "Right?!?"

            $ choice4 = False
            jump .choices


label part2_B5:

    v "No, I'm in debt."

    j "Ah. ADEX is bad."

    a "And with that, we have one thing left to say."

    menu:

        "♡♠♢ We did the right thing! ♢♠♡":
            jump good_ending1

        "♣ GLITTEERRRRR CANNOOOOOOONN!!! ♣":
            jump good_ending2


label part2_C4:

    j "How do you propose fixing $2.5 million dollars in damage?"

    $ choice4 = True

label .choices:

    menu:

        "♡ With Sparkle 'Splosions! ♡":
            "Todo <3"
            jump bad_ending2
        
        "♢ With a Gofundme campaign ♢" if key_gofundme:
            "Todo <3"
            jump neutral_ending1
        
        "♣ With a car wash ♣":
            "Todo <3"
            jump bad_ending2
        
        "♠ Start crying ♠" if choice4:
            # look, Eris is having a rough time. give her a moment
            "Todo <3"
            $ choice4 = False
            jump .choices


label bad_ending1:

    play music defeat

    "Bad ending 1 ♠:  Eris leaves the group, Belle becomes depressed, Amy falls deeper into addiction, and Clover gets revenge on the government and falls into the crippling debt"

    jump credits

    return


label bad_ending2:

    play music defeat

    "Bad ending 2 ♡: Court case is not taken seriously so it is lost. Amy is in denial that they lost, Eris fears she will be in debt forever and fears for life, Clover destroys the city, Belle"

    jump credits

    return


label bad_ending3:

    play music defeat

    "Bad ending 3 ♣: charge beam is used, but at the wrong time, so the other girls only get upset with Clover "

    jump credits

    return


label neutral_ending1:

    play music battle

    "Neutral Ending 1 ♢: team pleads guilty, but some debt still has to be paid. Debt is repaid through gofundme"

    jump credits

    return


label neutral_ending2:

    play music battle

    "Neutral Ending 2 ♠: team pleads guilty to receive a lesser sentence, they receive a warning, Eris isolates herself from the group, rest of the group remains and tries to find a replacement"

    jump credits

    return


label good_ending1:
    
    # play music victory

    "Good Ending 1 ♡♢♣♠: court case is won, debt does not have to be repaid"

    jump credits

    return


label good_ending2:

    # play music victory

    "Good Ending 2 ♣(♢): charge beam is used at correct time when villains arrive, judge forgives them for destroying the city"

    jump credits

    return


label good_ending3:

    # play music victory

    "Good Ending 3 ♠: team pleads guilty to receive a lesser sentence, they receive a warning, Eris learns to find fun in the silliness and recenters her focus on the sparkly- eyed idealism the group embodies, the group accepts that debt is a side effect of doing good"

    jump credits

    return


label credits:

    "Writers: Brighton Pauli, Zoie Tuinstra, KB Tran\nProgramming: KB Tran, Brighton Pauli\nArt: Lili Omilian"

    "Music: SC Klein, Michael Eaton\nBackgrounds: KB Tran"

    return
