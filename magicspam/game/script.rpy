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
define l = Character("Bailiff", color="#b4790a")

define audio.courtroom_bgm = "<loop 4.363636363636364>courtroom.ogg"
define audio.victory = "<loop 5.53>victory.ogg"

define quickleft = MoveTransition(0.2, enter=offscreenleft, leave=offscreenleft)
define quickright = MoveTransition(0.2, enter=offscreenright, leave=offscreenright)

define cannon_charge = 0

transform left_first:
    xalign 0.15
    xanchor 0.5
    ypos 120

transform left_second:
    xalign 0.35
    xanchor 0.5
    ypos 120

transform right_first:
    xalign 0.85
    xanchor 0.5
    ypos 120

transform right_second:
    xalign 0.65
    xanchor 0.5
    ypos 120

define charge_mult = 1
define impulsive_clover = True

screen alpha_magic_p1:
    add Charge("magicball.png", "part1_stage4.fadeout", charge_mult):
        xalign 0.5
        yalign 0.5

screen after_magic_p1:
    add Fadeout("white.png", "part1_stage4.aftermath"):
        xalign 0.5
        yalign 0.5

screen alpha_magic_good:
    add Charge("magicball.png", "good_ending2.fadeout", charge_mult):
        xalign 0.5
        yalign 0.5

screen after_magic_good:
    add Fadeout("white.png", "good_ending2.aftermath"):
        xalign 0.5
        yalign 0.5

screen alpha_magic_bad:
    add Charge("magicball.png", "bad_ending3.fadeout", charge_mult):
        xalign 0.5
        yalign 0.5

screen after_magic_bad:
    add Fadeout("white.png", "bad_ending3.aftermath"):
        xalign 0.5
        yalign 0.5

label charge_cannon:

    $ cannon_charge = cannon_charge + 1

    if cannon_charge == 1:
        play sound charge volume 0.6
        "{color=#10a341}Clover starts charging the Glitter Cannon.{/color}"

    elif cannon_charge == 2:
        play sound charge volume 0.6
        "{color=#10a341}The Glitter Cannon is almost charged.{/color}"
    
    else:
        play sound charge volume 0.6
        "{color=#10a341}The Glitter Cannon is fully charged!{/color}"
        if impulsive_clover:
            menu:
                "Activate the Glitter Cannon?"

                "Yes":
                    jump bad_ending3

                "No":
                    return

    return


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

    play sound roar volume 0.4
    "But among the noise, a deep and sudden BOOM tears across the busy roads."

    "The city seems to freeze, waiting in hushed silence for the sound to repeat itself and confirm their fears."

    "As if accepting the invitation, the source of the boom makes itself known."

    show adex
    with hpunch

            
    play sound roar volume 0.7
    m "RAAAARRGHHHH!!!"

    "A hulking mass of tentacle-like cords and LED panels pulls itself to a standing position, reaching a towering height of 200 feet."

    m "My name is ADEX!!"

    m "I have come to HELP! Yes, to HELP all of you!"

    "ADEX grins at the scrambling ant-like casino-goers below."

    m "I know you all need MONEY. And I can get it for YOU!"

    "A hailstorm of plastic cards erupts from the monster's mouth, smashing into roofs and windows."

    m "TAKE one of my cards! OPEN a credit line! SPEND all you need! SPEND all you WANT!"

    "Those still stuck outside cry out in fear as they are pelted with credit cards."

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
            play sound attack

            "Finally, she thrusts her hands forward, channeling the light into a laser that crackles with electric energy, piercing through the monster's eye."

            "ADEX stumbles backwards as chunks of charred wire and rubber fall from its face, but it holds its ground and turns away from the light."

            if key_gofundme:

                show belle at left_first
                with quickleft

                b "That shot was pretty poggers don't you guys think."

                "Belle brings her phone to Amy's face."

                b "Say hi to the chat, Amy!"

                a "(rgh) Hi chat! Um... Subscribe!"

                hide belle
                with quickleft
            
            play sound roar volume 0.6

            "The monster leans back towards the Cards of Justice and releases an ear-shattering roar."

            show amy at left_first
            with quickleft
            with hpunch

            "Amy loses her focus on the attack, which bursts into an explosion of light, knocking Amy off her feet."

            a "Shoot! Sorry guys, I hope that was enough time! I couldn't hold him for long!"

            show amy at left_second
            show eris at left_first
            with quickleft

            e "Don't worry. That was just what we needed."

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

            "Eris wall jumps from an alley to get to the roof of an apartment."
            
            "She dashes from roof to roof beneath the neon glow and draws a humming violet saber from behind her."

            "The path takes her in an arc around the monster. Its back is now in her sight."

            play sound attack
            e "Shimmering Strike!"

            "Eris propels herself off a radiator block, scaring a nearby cat that had been calmly watching the chaos, and plunges her blade into the red bulb, which shatters into thousands of glimmering scarlet shards."
            
            "ADEX reaches a massive arm towards its back, which Eris swiftly dodges."

            "The monster scratches its wound for a few seconds before returning to the fight, apparently unbothered."

            show belle at left_first
            with quickleft

            b "Huh. I guess that was just... a big red bulb or something. Sorry, that was a bad call. I've been playing too many games lately."

            e "No, I thought it would do something, too. I guess we need to try something else."

            hide belle
            hide eris
            with quickleft

            $ choice4 = False
            jump .choices

    return



label part1_stage2:

    "ADEX turns towards the hotel behind it and peers through the windows. Firefighters and volunteers are urgently escorting everybody out of the building."

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
        c "Damn it. I'll try to aim the cannon to not hit him. But it won't be easy if ADEX keeps throwing stupid credit cards at me!"
    else:
        c "Uh oh. I'll try to aim the cannon to not hit him. But it won't be easy if ADEX keeps throwing stupid credit cards at me!"

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

            show belle at left_first
            show amy at left_second
            with quickleft

            
            b "We need to rescue all of the civilians in the building! We can get this on stream for publicity"

            a "Right! Let's save them while we let Clover charge up Glitter Cannon."

            hide adex
            with quickright
            
            if key_gofundme:

                "Belle and Amy help the terrified victims out of the building. On the way out, Belle shoves her phone in the face of a poor victim."

                b "Say hi to the Twitch stream! Go ahead and tell them how you're feeling!"

                v "You destroyed my room and now you're profiting off of it through Twitch?!?"
            
            else:

                "Belle and Amy help the victims out of the building. Amy spawns puppies out of thin air to lighten the mood of the situation."

                v "You destroyed my room and now you think that you can cheer me up with puppies?!?"

            hide belle
            hide amy
            with quickleft

            show adex at right
            with quickright

            $ key_calm_the_people = True
            $ choice1 = False
            jump .choices
        
        "♠ Save the monster's victim ♠":
            
            show eris at left_first
            with quickleft

            e "You guys keep fighting! I'll rescue them."
            
            "Eris slams her saber into the ground and rockets herself toward the monster's hand."

            play sound attack

            "With a quick *SHLING!*, she slices through ADEX's thumb. The monster recoils and draws its hand back, dropping the man."

            play sound roar volume 0.4

            m "Ow! What the- OW!"

            "Eris pushes off of the falling thumb and catches the falling man in midair, tumbling onto a hotel balcony."

            show victim at left_second
            with quickleft

            e "Are you ok?"

            v "Ugh... ow."

            hide eris
            hide victim
            with quickleft
            
            $ key_speak_with_victim = True
            jump part1_stage3
        
        "♣ Call for Eris' help ♣":
            
            show clover at left_first
            with quickleft

            c "Eris! I need you!"

            show eris at left_second
            with quickleft

            c "I can't focus. Make him stop with the credit cards!"

            e "Right."

            hide clover
            show eris at left_first
            with quickleft

            "Eris leaps from balcony to balcony up to the roof of the hotel."

            e "HEY! LOOK OVER HERE, YOU- you THING!"

            "ADEX turns its head slowly to face Eris, peering at her through narrowed eyes."

            e "I would just LOVE to open a credit account with you! I need to buy SO MUCH STUFF! And I can't AFFORD it!"

            m "Oh? Oh! Well, I would be MORE than happy to help! Mwahahaha!!!"

            "The onslaught of flying credit cards focuses on Eris, like a jet of peltering plastic."

            "Eris slashes at the air impossibly quickly to deflect the incoming polymer projectiles. Most bounce off the shimmering veil but a few get through and scratches her."

            e "Keep charging, Clover! Try not to hit anything other than ADEX!"

            hide eris
            with quickleft

            $ key_happy_eris = True
            $ key_blame_clover = False
            jump part1_stage3
    
    return


label part1_stage3:

    # "Todo <3"

    $ choice1 = True
    $ choice2 = True
    $ choice3 = True
    $ choice4 = True

label .choices:

    define key_appeal_to_court = False
    define key_guilty_villain = False

    menu:

        "♡ Calm the people ♡" if key_calm_the_people:
            
            hide adex
            with quickright

            show amy at left_first
            show belle at left_second
            with quickleft

            v "Where am I going to sleep tonight? I don't have any money left to stay somewhere else and everything is destroyed anyways."

            v "All of my belongings were in my room, and I'll never get them back."

            a "Noooo don't worry about it! We shouldn't focus on all of the bad things that are happening."

            a "We're all safe and sound with my puppies! I'll say it again, look at how cute they are!"

            b "Yeah you all don't have to worry about it. We're going to throw the villain in the slammer and make them pay for it."

            b "Then we'll replace your belongings with upgraded versions and the damaged buildings will be built better than before."

            v "That's right. We should make the rich bad guys pay for all of us who are cheated by their system."

            "The civilians begin chanting to eat the rich"

            hide amy
            hide belle
            with quickleft

            show adex at right
            with quickright

            $ key_appeal_to_court = True
            jump part1_stage4
        
        "♠ Talk with the victim ♠" if key_speak_with_victim:
            
            show eris at left_first
            show victim at left_second
            with quickleft

            e "Sir, can you hear me? Are you alright?"

            v "Ugh, that thing, it- it... I'm in so much debt!"

            e "Stay with me. How did it capture you?"

            v "I CAN'T PAY RENT."

            e "Oh jeez."

            hide eris
            hide victim
            with quickleft

            $ key_guilty_villain = True
            jump part1_stage4
        
        "♢ Blue Brilliance! ♢":

            "Blue Brilliance is left as an exercise for the reader."

            jump part1_stage4

    return


label part1_stage4:

    show clover at left_second
    with quickleft

    if preferences.clover_swear:
        c "Thanks for stalling, y'all, the Glitter Cannon is fully charged. Time to fucking blow everything up!"
    else:
        c "Thanks for stalling, y'all, the Glitter Cannon is fully charged. Time to fucking blow everything up!"

    "Clover shakes as she struggles to contain the power of the fully charged beam. She aims it the best she can towards the monster and releases the blinding laser."

    show clover at left_first
    with quickleft
    with hpunch

    if preferences.clover_swear:
        c "TAKE THAT, BITCH! ARRRRGGGGHHHH!!!!!!!!!!"
    else:
        c "TAKE THAT! ARRRRGGGGHHHH!!!!!!!!!!"

    hide clover
    show adex at center
    with quickleft

    play sound charge volume 0.6
    call screen alpha_magic_p1

label .fadeout:

    hide screen alpha_magic_p1
    play sound impact volume 0.2
    call screen after_magic_p1

label .aftermath:
    
    hide screen after_magic_p1
    
    hide adex
    with dissolve

    "The monster instantly faints. He did not stand a chance."

    show amy at left_first
    with quickleft

    a "YOU DID IT! No one can deflect the Glitter Cannon!"

    show belle at left_second
    with quickleft

    b "That was perfect, Clover! You destroyed that thing!"

    if key_gofundme:
        b "And the stream loved it! We're getting so many donations!"

    show clover at right_second
    with quickright

    if preferences.clover_swear:
        c "FUCK YEAHHHHHHH!! GLITTER CANNOOONNN!"
    else:
        c "FRICK YEAHHHHHHH!! GLITTER CANNOOONNN!"

    show eris at right_first
    with quickright

    e "Sorry to break the mood, but I think we destroyed more than just the enemy. Like a lot more. And do you all hear that?"

    "Police sirens wail in the distance, approaching the smoking battleground."

    a "Hey, the police are here! Time to arrest a credit card monster!"

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

    a "Why did they throw US in jail?!"

    e "I can't believe this is happening. I'm glad we got the enemy, but when we get out of here we probably need to work on the accuracy of the Glitter Cannon."

    c "Hey, I'm working on it! It's not my problem that the Glitter Cannon is so amazingly amazing."

    c "My power is simply destroying things with godly amounts of glitter and cannon."

    a "At the end of the day we got the villain so let's just focus on the positive. Yayyyyyy!"

    if preferences.clover_swear:
        b "I can't think of any other people who I would rather be jailed with. I love you all. We girl boss pussy slayyyyyyyed today."
    else:
        b "I can't think of any other people who I would rather be jailed with. I love you all."

    "The door to the jail cell swings open and a woman walks in."

    l "I am the bailiff. You are all being summoned to the court today for your trial."

    $ choice2 = True

label .choices:

    menu:

        "♢ Go peacefully ♢":
            
            b "I think we should get going. We have nothing to worry about."

            e "Yeah. I sure hope you're right."

            a "Everything is sunshine and rainbows."

            jump part2_A2
        
        "♡ Summon a puppy ♡" if choice2:
            "Todo <3"
            $ choice2 = False
            jump .choices
        
        "♣ Start charging Glitter Cannon ♣":
            call charge_cannon from _call_charge_cannon
            jump part2_A2
        
        "♠ Blame Clover ♠" if key_blame_clover:
            jump bad_ending1

    "court"
    return


label part2_A2:

    show bg court
    play music audio.courtroom_bgm

    hide clover
    hide eris
    show judge at right
    with quickright

    play sound order

    j "As a direct result of your \"Glitter Cannon\", the 10 City Hotel and Casion suffered $2.5 million in damages."

    j "You are charged with vandalism."

    j "How do you plead?"

    hide amy
    hide belle
    with quickleft

    menu:

        "♢♠ Guilty ♠♢":
            jump part2_A3
        
        "♡♣ Not guilty ♣♡":
            call charge_cannon from _call_charge_cannon_1
            jump part2_B3


label part2_A3:

    "We plead guilty, BUT..."

    $ choice1 = True
    $ choice4 = True

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
        
        "♣ *Stick out your tongue* ♣" if choice4:

            show clover at left
            with quickleft

            c "MLEH!"

            j "Rude."

            hide clover
            with quickleft

            $ choice4 = False

            call charge_cannon from _call_charge_cannon_2
            jump .choices


label part2_A4:
    
    "Do you have anybody to vouch for you?"

    $ choice4 = True

label .choices:

    menu:

        "♡ The citizens in the hotel ♡" if key_calm_the_people:
            "Todo <3"
            jump part2_A5
        
        "♠ The monster's victim ♠" if key_speak_with_victim:

            show eris at left_first
            with quickleft

            e "We'd like to call in the monster's victim."
            
            show victim at left_second
            with quickleft

            v """It is true that the Cards of Justice saved me.

            I found myself in horrible amounts of debt and a destructive gambling addiction.

            The monster took advantage of me and tried to get me to open more credit lines so that I could gamble more and fall further into debt.

            If the Cards of Justice didn't slay the monster, I would be indebted to the monster forever."""

            hide victim
            with quickleft
            
            jump part2_A5
        
        "♢ Twitch chat ♢" if key_gofundme:
            "Todo <3"
            jump bad_ending2
        
        "♣ Your mom! ♣" if choice4:

            show clover at left
            with quickleft

            c "YOUR MOM!"

            j "Uncalled for."

            hide clover
            with quickleft

            $ choice4 = False

            call charge_cannon from _call_charge_cannon_3
            jump .choices


label part2_A5:

    j "Very well. We will let you off with some fines as a warning. Wait in the holding cell."

    hide victim
    with quickleft

    hide judge
    with quickleft

    scene bg jail
    play music jail

    show eris at left_first
    with quickleft

    show clover at left_second
    with quickleft

    show belle at right_first
    with quickright

    show amy at right_second
    with quickright

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

    show judge at right_first
    show adex at right_second
    with quickright

    j "Well, we have a witness here who says he witness your vandalism first-hand."

    m "That's right! Not only did these four blow up the building, but they attacked me!"

    j "What do you four have to say to defend yourselves?"

    menu:

        "♠ Call the victim to the stand ♠" if key_speak_with_victim:

            show eris at left_first
            with quickleft

            e "We would like to call Adex's victim to stand."

            hide adex
            show victim at right_second
            with quickright

            hide eris
            with quickleft

            jump part2_B4
        
        "♣ Try to enrage the monster ♣":
            
            show clover at left_first
            with quickleft

            c "Not only didn't stand a chance against the glitter cannon, you're really ugly to look at, why would anybody want to open a credit line with you?"

            show amy at left_second
            with quickleft

            a "You're so disgusting that not even my puppies can cheer me up. And who doesn't cheer up because of my adorable puppies?"

            play sound order

            j "ENOUGH! Settle down. We will not tolerate this behavior."

            hide clover
            hide amy
            with quickleft

            call charge_cannon from _call_charge_cannon_4
            jump bad_ending2
        
        "♢ Accuse the monster ♢":
            
            show clover at left_first
            with quickleft

            c "The city is all a mess because of you! You're the one who destroyed everything, definitely not my OP uncontrollable glitter cannon."

            show belle at left_second
            with quickleft

            b "Yeah! How dare you try to pin this on the Cards of Justice?!? We're the good ones, it's in our names. Cards. Of. JUSTICEEEEEEEEEEEE."

            hide clover
            hide belle
            with quickleft

            jump bad_ending2
        
        "♡ Appeal to ADEX's empathy ♡":
            
            show amy at left_first
            with quickleft

            a """Hey Adex, we know you're not a bad monster.
            You were just trying to help the citizens get out of debt but in a horrible, twisted way.
            We know that you will admit that you're guilty out of the goodness of your heart.
            After serving your time, you can pursue a better path to help people with your financial knowledge."""

            show belle at left_second
            with quickleft

            b "Please Adex, for the sake of keeping our group together, just admit your guilt."

            "Amy and Belle give Adex their biggest puppy eyes to convince him to feel bad for his actions."

            "It is not effective."

            m "You are all the dumbest group of magical girls I've ever met if you really think I'm going to fall for that one."

            hide amy
            hide belle
            with quickleft

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

            $ impulsive_clover = False
            call charge_cannon from _call_charge_cannon_5

            $ choice4 = False
            jump .choices


label part2_B5:

    v "No, I'm in debt."

    j "Ah. ADEX is bad."

    a "And with that, we have one thing left to say."

    menu:

        "♡♠♢ We did the right thing! ♢♠♡":
            jump good_ending1

        "♣ GLITTEERRRRR CANNOOOOOOONN!!! ♣" if cannon_charge >= 3:
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
            show belle at left_first
            with quickleft

            b """We can easily set up a GoFundMe!
            With the enormous Cards of Justice Twitch following, thanks to me streaming every moment of our epic boss fights, 
            we have accrued a loyal fan base willing to support our every wish and desire, including paying for the renewal of the city that we so faithfully serve."""

            show eris at left_second
            with quickleft

            e "That's great Belle! I think I underestimated the importance of your Twitch streaming, I think we should be even more invasive with the streaming next time!"

            jump neutral_ending1
        
        "♣ With a car wash ♣":
            "Todo <3"
            call charge_cannon from _call_charge_cannon_6
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

    play music battle

    show judge at right
    with quickright
    
    show clover at left
    with quickleft

    if preferences.clover_swear:
        c "I can't fuckin' TAKE this any more!"
    else:
        c "I can't TAKE this any more!"

    with hpunch
    c "GLITTER CANNOOOONN!!"

    hide clover
    show judge at center
    with quickleft

    play sound charge volume 0.6
    call screen alpha_magic_bad

label .fadeout:

    hide screen alpha_magic_bad
    play sound impact volume 0.2
    call screen after_magic_bad

label .aftermath:
    
    hide screen after_magic_bad

    hide judge
    with dissolve

    show clover at left_second
    with quickleft

    c "Take THAT!"

    show belle at right_second
    with quickright

    b "CLOVER!"

    b "What the hell?!"

    jump credits

    return


label neutral_ending1:

    play music jail

    "Neutral Ending 1 ♢: team pleads guilty, but some debt still has to be paid. Debt is repaid through gofundme"

    jump credits

    return


label neutral_ending2:

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
    stop music

    hide judge
    show adex at right
    with quickright
    
    show clover at left
    with quickleft

    c "That's it. We're doing this right."

    with hpunch
    c "GLITTERRRR"

    c "CANNOOOONN!!"

    hide clover
    show adex at center
    with quickleft

    play sound charge volume 0.6
    call screen alpha_magic_good

label .fadeout:

    hide screen alpha_magic_good
    play sound impact volume 0.2
    call screen after_magic_good

label .aftermath:
    
    hide screen after_magic_good

    hide adex
    with dissolve

    show clover at left_second
    with quickleft

    c "Take THAT!"

    show belle at right_second
    with quickright

    b "CLOVER! What are you doing?!"

    show judge at right
    show clover at left_first
    show belle at left_second
    with quickright

    "The judge bangs his gavel against the smoking ashes that used to be his desk."

    play sound order

    j "ORDER! Order in the court!"

    play music victory

    j "I now see the true evil intentions of this terrible monster."
    
    j "Your actions are destructive. Like, very destructive. BUT!"

    j "They may just be necessary."

    j "And for that reason, I declare you to be NOT GUILTY!"

    jump credits

    return


label good_ending3:

    # play music victory

    "Good Ending 3 ♠: team pleads guilty to receive a lesser sentence, they receive a warning, Eris learns to find fun in the silliness and recenters her focus on the sparkly- eyed idealism the group embodies, the group accepts that debt is a side effect of doing good"

    jump credits

    return


label credits:

    "Writers: Brighton Pauli, Zoie Tuinstra, KB Tran\nProgramming: KB Tran, Brighton Pauli\nArt: Lili Omilian, KB Tran"

    "Music: SC Klein, Michael Eaton"

    $ MainMenu(confirm=False)()
