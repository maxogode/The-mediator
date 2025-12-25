
init:
    define y = Character("Yuki", color="#4903fc")
    define h = Character("Hatsune", color="#34c9eb")
    default counter = 0

transform center_move:
    xalign 0.5
    yalign 1.0

transform left_move:
    xalign 0.3
    yalign 1.0

transform right_move:
    xalign 0.7
    yalign 1.0

transform getCloserLeft:
    xalign 0.42
    yalign 1.0

transform getCloserRight:
    xalign 0.58
    yalign 1.0


label start:

    $ player_name = renpy.input("Before we begin the game, please input your name.")
    $ player_name = player_name.strip()

    if player_name == "":
        $ player_name = "Player"

    $ p = Character(player_name, color="#fc03a9")
    $ counter = 0

    play music "menu.mp3"
    
    scene bg entrance

    p "It's friday morning, and I've just arrived to school."

    p "To be honest, I'm completely burnt out."

    p "I just want the day to be over so I can go home and binge some Tv Shows."

    p "Suddenly, I hear two girls arguing near the Entrance."

    show yuki angry at left_move:
        zoom 1.5
    with dissolve

    y "Just admit you were wrong and apologise!"

    show hatsune angry at right_move:
        zoom 1.5
    with dissolve

    h "Don't you think you're overreacting a little, Yuki?"

    p "The purple haired Girl, who seems to have a hot temper, is Yuki."

    y "Overreacting? Do you even understand what you did?"

    show yuki sad 

    y "How could you say that, Hatsune?"

    p "The blue haired girls name is apparently Hatsune."

    p "She seems calmer and more composed, but I can still feel the aggravation in her voice."

    h "Whatever... it's not like I-"

    show hatsune sad
    h "Nevermind, theres people around."

    show yuki blush

    y "What?"

    p "Suddenly, both of the girls look at me."

    p "What did I get myself into?!"

    show hatsune angry

    h "I'm off to class, talk to me when you've calmed down a little."

    hide hatsune with dissolve

    show yuki angry at center_move with move

    y "Hey, you! what do you think you are doing?."

    menu:
        "Say Nothing":
            jump quiet
        "Apologise":
            $ counter += 1
            jump sorry


label quiet:

    p "..."
    
    y "Hello? Did you lose your hearing"

    jump postChoice1


label sorry:

    p "I'm sorry, I didn't mean to-"

    show yuki blush

    y "Well in any case..."

    jump postChoice1


label postChoice1:

    show yuki angry

    y "Mind your buisness!"

    hide yuki with dissolve

    p "Jeez, what is with these two?!"

    p "Confused, I choose not to question it and head to class."

    stop music fadeout 1.0

    scene bg hallway with fade

    play sound "crowd.mp3"

    p "I still can't stop thinking about Hatsune and Yuki..."

    p "What were they even arguing about..."

    p "Suddenly, I bump into someone."

    with hpunch

    show hatsune sad at center_move:
        zoom 1.5
    with dissolve

    stop sound fadeout 0.5

    play music "hatsune_song.mp3"

    h "Oh, it's you again!"

    h "You're [player_name], right?"

    p "Hi... Hatsune."

    h "Sorry about what you saw earlier."

    p "Don't sweat it. Are you okay though?"

    show hatsune default

    h "Mostly, yeah."

    h "It's just petty drama between girls."

    h "Long story short, Yuki's boyfriend came onto me."

    p "Oh! that's-"

    h "Crazy, I know."

    h "But what's crazier is that she thinks the opposite happened."

    h "No matter what I try to tell her, she doesn't seem to believe me..."

    show hatsune excited

    h "Pretty immature of her right?"

    menu:
        "She's crazy":
            jump crazy
        
        "Be empathetic":
            $ counter += 1
            jump empathy


label crazy:

    p "Yeah, shes a complete psycho."
    
    h "Right?! I still have to talk to her during break though, unlucky me."

    jump postChoice2


label empathy:

    p "No!"

    show hatsune sad

    p "Hatsune looks at me with shock."

    p "Yes, she might seem a little immature..."

    p "...But that's only because she's emotional and doesn't know how to deal with her feelings!"

    p "You should be more understanding and let her calm down before you judge her!"

    show hatsune happy

    h "I guess I never thought of that..."

    h "You're right."

    h "Thanks for the pep talk."

    jump postChoice2


label postChoice2:

    h "Until next time, [player_name]"

    hide hatsune with dissolve

    stop music

    play sound "school_bell.mp3"

    p "The bell rings, and I rush to class"

    scene bg classroom with fade

    p "The teacher assigned us in pairs, and I got put with Yuki"

    play music "yuki_song.mp3"
    
    show yuki blush at center_move:
        zoom 1.5
    with dissolve

    y "It's like I can't escape you [player_name], can I?"

    p "I could say the same thing..."

    y "I'm assuming she told you what happened."

    p "Yes... she did."

    show yuki angry

    y "So?"

    p "So what?"

    y "Thoughts?"

    menu:
        "Be honest":
            $ counter += 1
            jump honesty

        "Be avoidant":
            jump avoidant


label honesty:

    p "Yuki, you shouldn't always trust the ones you love?"

    show yuki sad

    y "Huh?"

    p "Your boyfriend is at fault."

    p "While I understand your anger, it's not right to take out your frustrations out on hatsune."

    show yuki default

    y "Thanks for being honest with me..."

    jump postChoice3


label avoidant:

    p "She shouldn't have done that."

    p "Who does she think she is anyway?!"

    show yuki excited

    y "Right?! I'm glad you understand."

    y "Thanks!"

    jump postChoice3


label postChoice3:

    play music "menu.mp3"

    y "Now Let's get to the schoolwork."

    hide yuki with dissolve

    p "The class ends, and I go outside to get some fresh air fresh air."

    scene bg entrance with fade

    p "There, I once again encounter Yuki and Hatsune."

    if counter == 3:

        show yuki default at left_move:
            zoom 1.5
        with dissolve

        show hatsune default at right_move:
            zoom 1.5
        with dissolve

        y "I'm sorry I didn't believe your side of the story."

        h "I'm sorry for being inconsiderate."

        show yuki excited at getCloserLeft

        show hatsune excited at getCloserRight

        with move


        p "The two of them hug."

        p "Thank god I said the right things at the right time"

    else:

        show yuki angry at left_move:
            zoom 1.5
        with dissolve

    
        show hatsune angry at right_move:
            zoom 1.5
        with dissolve

        y "If you ever speak to me again, I will kill you!"

        h "Whatever, you were an annoying friend anyway!"

        hide yuki 

        hide hatsune 

        with dissolve

        p "I sigh"

        p "Could I have helped more if I said the right thing?"

    return