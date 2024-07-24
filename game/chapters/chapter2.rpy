# File: chapter2.rpy

label chapter2:
    scene bg coding_classroom
    play sound "audio/keyboard_typing.mp3" loop

    n "Chapter 2: Trials and Tribulations"

    show ms_thorne stern at center
    mt "Today's challenge: decrypt a high-level encryption code. First one to crack it wins bragging rights."

    hide ms_thorne

    menu:
        "Focus on Ace's approach":
            $ tech_skill += 1
            jump ace_coding
        "Focus on Cipher's method":
            $ tech_skill += 1
            jump cipher_coding
        "Observe Maverick's technique":
            $ tech_skill += 1
            jump maverick_coding
        "Watch Doc's analysis":
            $ tech_skill += 1
            jump doc_coding
        "Check on Anna's progress":
            $ anna_confidence += 1
            jump anna_coding

label ace_coding:
    show ace confident at center
    n "Ace attacks the problem head-on, his fingers a blur as he types line after line of code."
    ac "Child's play. Watch and learn, rookies."
    jump coding_challenge_end

label cipher_coding:
    show cipher focused at center
    n "Cipher's approach is more methodical, her eyes darting across the screen as she searches for patterns and weaknesses."
    ci "Interesting... This encryption has a fatal flaw."
    jump coding_challenge_end

label maverick_coding:
    show maverick at center
    m "Hmm, maybe a brute-force attack wouldn't work here. There has to be a more elegant solution..."
    jump coding_challenge_end

label doc_coding:
    show doc at center
    n "Doc's analytical mind is in overdrive, breaking down the problem into its component parts."
    d "If we apply the Fibonacci sequence to the key distribution..."
    jump coding_challenge_end

label anna_coding:
    show anna frustrated at center
    a "Why isn't this working? There has to be another way..."
    
    show ms_thorne stern at right
    mt "Still struggling, Ms. Williams? I'm afraid coding might be a bit beyond your skillset."
    
    show anna determined at center
    a "Almost there! I just need to find the right approach..."

    $ tech_skill += 2

label coding_challenge_end:
    play sound "audio/buzzer.mp3"
    show ace confident at left
    ac "Done! Beat that, rookies!"
    
    show ms_thorne stern at right
    mt "Impressive work, Mr. Mehta. The rest of you could learn from his efficiency."

    scene bg training_facility
    play sound "audio/whistle_blow.mp3"

    show sr at center
    sr "Move it, maggots! You call this running? This is a global crisis simulation, not a stroll in the park!"

    hide sr

    menu:
        "Push through the pain":
            $ physical_skill += 2
            $ anna_confidence += 1
            jump push_through
        "Take a strategic approach":
            $ physical_skill += 1
            $ tech_skill += 1
            jump strategic_approach

label push_through:
    show anna determined at center
    n "You grit your teeth and push your body to its limits."
    a "I... won't... give... up!"
    jump obstacle_course

label strategic_approach:
    show anna normal at center
    n "You decide to analyze the course and find the most efficient path."
    a "If I time this right, I can use the momentum from the rope swing to clear the wall..."
    jump obstacle_course

label obstacle_course:
    play sound "audio/fall_thud.mp3"
    show anna embarrassed at center
    n "Despite your efforts, you trip and fall face-first into the sand."
    
    show sr at right
    sr "Ms. Williams, having trouble with basic physical exertion? Perhaps you should consider a career in... scrapbooking?"
    
    show ms_thorne stern at left
    mt "Pathetic. Looks like we have dead weight on our hands."
    
    show anna determined at center
    a "I may not be the fastest or strongest, but I won't give up!"

    $ anna_confidence += 1
    $ physical_skill += 1

    # Here you would implement the quick-time event for completing the course
    call screen obstacle_course_minigame
    $ obstacle_success = _return

    if obstacle_success:
        $ physical_skill += 2
        n "With a burst of determination, you manage to complete the course, surprising everyone including yourself."
    else:
        $ anna_confidence -= 1
        n "Despite your best efforts, you struggle to complete the course. But you refuse to give up."

    scene bg vr_room
    show ms_thorne stern at center
    mt "This is a social engineering challenge. Your objective: infiltrate a high-security facility and retrieve classified data. Use your skills, not brute force."

    hide ms_thorne

    menu:
        "Observe Ace's hacking attempt":
            $ tech_skill += 1
            jump ace_hacking
        "Watch Cipher's stealthy approach":
            $ social_skill += 1
            jump cipher_stealth
        "See Maverick's creative solution":
            $ tech_skill += 1
            jump maverick_solution
        "Follow Doc's analytical method":
            $ tech_skill += 1
            jump doc_analysis
        "Try Anna's unconventional tactic":
            $ social_skill += 2
            $ anna_confidence += 1
            jump anna_tactic

label ace_hacking:
    show ace confident at center
    ac "Firewall? More like paper wall. I'm in."
    jump social_engineering_end

label cipher_stealth:
    show cipher focused at center
    ci "They'll never know I was here."
    jump social_engineering_end

label maverick_solution:
    show maverick at center
    m "Who needs hacking when you have the power of social media influencers?"
    jump social_engineering_end

label doc_analysis:
    show doc at center
    d "By analyzing the guard rotation patterns, I've identified a 2.5-minute window of opportunity."
    jump social_engineering_end

label anna_tactic:
    show anna normal at center
    a "Hey there! Beautiful day for a... uh... high-security facility infiltration, right?"
    
    n "Guard: You alright there, kid?"
    
    menu:
        "Attempt a joke":
            $ social_skill += 1
            a "Just trying to lighten the mood! You know, high-stakes missions and all..."
        "Try flattery":
            $ social_skill += 1
            a "I just couldn't help but notice how well you maintain security here. It's impressive!"
        "Feign confusion":
            $ social_skill += 1
            a "Oh gosh, is this not the tour group meeting spot? I'm so lost!"
    
    n "Guard: Look, I don't know what you're up to, but your enthusiasm is... refreshing. Just promise me you won't break anything, okay?"
    
    show anna surprised at center
    a "You... you're letting me through?"
    
    n "Guard: Sure, kid. Go get 'em, tiger."

    $ anna_confidence += 2

label social_engineering_end:
    scene bg control_room
    show ms_thorne stern at center
    mt "Now that you've gained access, your next task is to locate and extract the classified data."

    # Here you would implement the hacking simulation mini-game
    call screen hacking_simulation
    $ hacking_success = _return

    if hacking_success:
        $ tech_skill += 2
        n "You successfully navigate the virtual system and extract the classified data."
    else:
        $ tech_skill += 1
        n "You struggle with the system but manage to extract some of the data before being detected."

    show cipher focused at left
    show anna normal at right
    ci "What in the world are you doing, Williams?"
    a "Oh, you know, just taking the scenic route through the firewall."

    $ tech_skill += 1
    $ team_trust += 1

    scene bg conference_room
    show captain normal at center
    c "Alright team, let's break down what we learned today."

    menu:
        "Discuss the coding challenge":
            $ tech_skill += 1
            jump discuss_coding
        "Analyze the physical training":
            $ physical_skill += 1
            jump analyze_training
        "Review the social engineering exercise":
            $ social_skill += 1
            jump review_social
        "Examine the hacking simulation":
            $ tech_skill += 1
            jump examine_hacking

label discuss_coding:
    c "The encryption challenge really tested our problem-solving skills."
    jump debrief_end

label analyze_training:
    c "That obstacle course was no joke. It's clear we need to work on our physical conditioning."
    jump debrief_end

label review_social:
    c "The social engineering exercise showed that sometimes, the direct approach isn't always best."
    jump debrief_end

label examine_hacking:
    c "That final hacking simulation combined everything we've learned so far."
    jump debrief_end

label debrief_end:
    show ms_thorne stern at right
    mt "While some of you showed promise, others... have a long way to go. Remember, in the real world, failure isn't an option."
    
    show anna normal at left
    a "Neither is compassion, apparently."
    
    show captain normal at center
    c "Hey, don't let her get to you. Your out-of-the-box thinking could be our secret weapon."

    $ team_trust += 1
    $ anna_confidence += 1

    n "As the team files out, Anna can't help but feel a mix of determination and uncertainty. The challenges are tough, but she's not about to give up now..."

    return  # This will end Chapter 2 and return to the main script

screen obstacle_course_minigame:
    frame:
        xalign 0.5
        yalign 0.5
        vbox:
            text "Obstacle Course Challenge" size 40
            text "Quick! Choose the right path!" size 20
            hbox:
                textbutton "Left" action Return(True)
                textbutton "Right" action Return(False)
                textbutton "Center" action Return(True)
    # This is a simplified representation. You'd want to create a more complex and engaging mini-game.

screen hacking_simulation:
    frame:
        xalign 0.5
        yalign 0.5
        vbox:
            text "Hacking Simulation" size 40
            text "Navigate the system and extract the data" size 20
            hbox:
                textbutton "Brute Force" action Return(False)
                textbutton "Exploit Vulnerability" action Return(True)
                textbutton "Social Engineering" action Return(False)
    # This is a simplified representation. You'd want to create a more complex and engaging mini-game.