# File: chapter1.rpy

label chapter1:
    scene bg academy_exterior
    n "Chapter 1: Welcome to the Asylum"
    n "Welcome to Neo Scholars Academy, a place where the brightest minds come to hone their skills and change the world."
    
    play sound "audio/door_whoosh.mp3"
    
    menu:
        "Observe the arrivals":
            $ team_trust += 1
            jump observe_arrivals
        "Focus on the fumbling figure":
            $ anna_confidence += 1
            jump focus_anna

label observe_arrivals:
    n "One by one, the new recruits make their entrance, each in their own unique style."
    show ace confident at left
    n "Ace steps out of a sleek sports car, adjusting his designer sunglasses."
    hide ace
    show cipher focused at right
    n "Cipher slips through security unnoticed, vanishing into the building."
    hide cipher
    show maverick at center
    n "Maverick exits a chauffeur-driven limousine, waving enthusiastically."
    hide maverick
    show doc at left
    n "Doc is escorted by a professor, carrying a stack of books."
    hide doc
    show captain normal at center
    n "Captain arrives with a backpack and a friendly smile."
    hide captain
    jump anna_arrival

label focus_anna:
    show anna normal at center
    n "Amidst the sea of confident arrivals, one figure stands out - not for grace, but for sheer determination."
    
label anna_arrival:
    play sound "audio/thud.mp3"
    show anna embarrassed at center
    a "Oh no! Not again!"
    
    show captain normal at right
    c "Easy there! Looks like you could use some help."
    
    show anna embarrassed at left
    a "Thanks! I swear, this bag has a mind of its own."
    
    menu:
        "Apologize profusely":
            $ anna_confidence -= 1
            $ social_skill += 1
            a "I'm so sorry! I'm not usually this clumsy. Well, actually, that's a lie. I'm always this clumsy."
        "Crack a joke about the festival wristbands":
            $ anna_confidence += 1
            $ social_skill += 2
            a "Well, at least my festival wristband collection is getting some fresh air. They were feeling a bit claustrophobic in there."
    
    c "I'm Captain. Welcome to Neo Scholars, ...?"
    a "Anna. Anna Williams. Thanks for the save, Captain."

    scene bg induction_room
    play sound "audio/heels_clicking.mp3"
    
    show ms_thorne stern at center
    mt "Welcome, recruits. {i}Congratulations{/i} on making it this far."
    
    mt "The Neo Scholars program is designed to identify and cultivate the next generation of technological leaders. You will be pushed to your limits, mentally and physically. Only the best will survive."
    
    show ace confident at left
    ac "Sounds like boot camp for nerds."
    
    show ms_thorne stern at right
    mt "This is not a game, Mr. Mehta. We are preparing you to tackle real-world problems that could impact the very future of humanity."
    
    show cipher focused at left
    ci "Can we skip the inspirational speeches and get to the hacking already?"
    
    mt "Patience, Ms. Wang. Your skills will be tested in due time."
    
    show anna determined at center
    a "Ms. Thorne, will we be using cutting-edge AI algorithms? What about quantum computing?"
    
    mt "We'll get to specifics later, Ms. Williams. Now, focus."
    
    n "Ms. Thorne launches into a detailed presentation about the program's curriculum, showcasing high-pressure scenarios and intense training regimens."
    
    $ tech_skill += 1
    
    hide ms_thorne
    hide ace
    hide cipher
    
    show anna determined at left
    show captain normal at right
    
    c "So, Ms. Williams, excited for the challenges ahead?"
    a "Absolutely! I feel like I've been training for this my whole life!"
    
    $ anna_confidence += 1
    
    scene bg common_area
    
    show ace confident at left
    ac "This place is seriously lacking in entertainment."
    
    show cipher focused at right
    ci "Not exactly the high-tech haven I expected."
    
    show maverick at center
    m "Guys! Guys! I have a fantastic idea! It's gonna revolutionize the way we interact with technology!"
    
    show doc at left
    d "This furniture is ergonomically unsound. They should invest in adjustable lumbar support."
    
    hide ace
    hide cipher
    hide maverick
    hide doc
    
    show captain normal at right
    show anna normal at left
    
    c "Hey, you must be Anna. I'm Captain. Welcome aboard!"
    a "Thanks! It's... intense, right? Ms. Thorne seems a bit… well, intense."
    
    c "Don't worry, she grows on you… eventually. So, what are you looking forward to most about the program?"
    
    menu:
        "Express enthusiasm for the tech":
            $ tech_skill += 2
            $ anna_confidence += 1
            a "Oh, where do I even start? The AI algorithms, the quantum computing possibilities, the chance to work with cutting-edge tech... It's like every tech nerd's dream come true!"
        "Share concerns about fitting in":
            $ social_skill += 2
            $ team_trust += 1
            a "Honestly? I'm a bit worried. Everyone here seems so... polished. I'm just hoping I don't accidentally set the lab on fire or something."
    
    c "Alright, team. Let's break the ice with a game of charades. Any volunteers?"
    
    a "Oh, pick me! I'm amazing at charades!"
    
    $ social_skill += 1
    $ team_trust += 1
    
    n "As the first day winds down, curiosity gets the better of Anna."
    
    scene bg hallway_night
    
    menu:
        "Investigate the strange noise coming from the lab":
            $ tech_skill += 1
            $ anna_confidence += 1
            jump investigate_lab
        "Check out the locked door at the end of the hall":
            $ anna_confidence += 1
            $ team_trust -= 1
            jump check_locked_door
        "Return to the dorm room":
            $ anna_confidence -= 1
            jump return_to_dorm

label investigate_lab:
    show maverick at center
    show anna normal at left
    
    a "Maverick? What are you doing up so late?"
    m "Anna! I... uh... just had this brilliant idea and couldn't sleep. Want to see?"
    
    $ team_trust += 1
    
    jump end_of_chapter1

label check_locked_door:
    show anna normal at center
    n "Anna examines a keypad next to a locked door marked 'Restricted Area'."
    
    a "Hmm, I wonder what's behind here..."
    
    play sound "audio/footsteps.mp3"
    
    show cipher focused at right
    ci "Curiosity killed the cat, you know."
    
    show anna embarrassed at left
    a "Cipher! I was just... uh..."
    
    ci "Save it. We all have our secrets. Just be careful whose you stumble upon."
    
    jump end_of_chapter1

label return_to_dorm:
    show anna normal at center
    a "What a day. I can't wait to see what tomorrow brings."
    
    jump end_of_chapter1

label end_of_chapter1:
    n "And so ends the first day at Neo Scholars Academy. Little does Anna know, the real challenges are yet to come..."
    
    return