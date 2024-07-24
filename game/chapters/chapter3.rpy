# File: chapter3.rpy

label chapter3:
    scene bg common_area
    n "Chapter 3: Bonds Forged in Fire"

    show anna normal at center
    n "After weeks of intense training, the recruits gather for a much-needed movie night."

    a "So, what do you guys think? Hilarious, right?"

    show captain normal at right
    c "Not exactly my usual genre, but it's definitely... interesting."

    show maverick at left
    m "I could totally turn this movie into a groundbreaking app! Interactive humor delivery system, gamified plot twists..."

    hide maverick
    show doc at left
    d "The entertainment value seems inversely proportional to the intellectual merit."

    hide doc
    show cipher focused at left
    n "Cipher remains silent, but a faint smile plays on her lips as she watches."

    hide cipher
    show ace confident at left
    ac "Whatever. This is childish."

    hide ace

    menu:
        "Focus on a character's backstory":
            jump character_backstory
        "Engage in movie trivia challenge":
            jump movie_trivia

label character_backstory:
    menu:
        "Learn about Ace's past":
            jump ace_backstory
        "Discover Cipher's history":
            jump cipher_backstory
        "Explore Maverick's background":
            jump maverick_backstory
        "Understand Doc's journey":
            jump doc_backstory
        "Uncover Captain's story":
            jump captain_backstory

label ace_backstory:
    scene bg ace_room
    n "A young Ace sits alone in a dimly lit room, surrounded by glowing computer screens. Lines of code scroll rapidly as he types with lightning speed."
    n "A montage of empty lunchboxes and lonely birthday dinners reinforces his isolated childhood."
    $ team_trust += 1
    jump movie_night_end

label cipher_backstory:
    scene bg alleyway
    n "A grimy alleyway becomes the backdrop. A young Cipher, clad in tattered clothes, navigates the harsh environment with practiced ease."
    n "She hacks into a flickering terminal, a sly glint in her eyes."
    $ team_trust += 1
    jump movie_night_end

label maverick_backstory:
    scene bg lecture_hall
    n "A prestigious university lecture hall. Maverick, bored and restless, doodles elaborate inventions in his notebook while the professor drones on."
    n "Finally, he gathers his things and walks out, a determined expression on his face."
    $ team_trust += 1
    jump movie_night_end

label doc_backstory:
    scene bg library
    n "A library filled with towering bookshelves. A young Doc, nose buried in a weighty tome, ignores the friendly greetings of other students."
    n "Her expression is focused and intense."
    $ team_trust += 1
    jump movie_night_end

label captain_backstory:
    scene bg classroom
    n "A group project presentation. Captain stands nervously beside a group of confident classmates. He stumbles through his part, his ideas dismissed by his teammates."
    n "Despite the disappointment, a spark of determination flickers in his eyes."
    $ team_trust += 1
    jump movie_night_end

label movie_trivia:
    n "Anna initiates a movie trivia challenge, testing everyone's knowledge of the film they just watched."
    # Here you can implement a mini-game for movie trivia
    $ social_skill += 2
    $ team_trust += 2
    jump movie_night_end

label movie_night_end:
    scene bg hallway_night
    n "As the night winds down, Anna finds herself wandering the quiet halls of the academy."

    show captain normal at right
    c "Hey, Anna. Everything alright?"

    show anna normal at left
    a "Oh, Captain! Uh, yeah, just... reviewing some material."

    c "Come on, you can't fool me. Training got you down?"

    menu:
        "Share fears about the program":
            $ social_skill += 1
            $ team_trust += 1
            jump share_fears
        "Discuss future dreams":
            $ anna_confidence += 1
            jump discuss_dreams

label share_fears:
    a "It's not just that. Ms. Thorne... well, let's just say she doesn't exactly have high hopes for me."
    c "Don't listen to her. Ms. Thorne may be tough, but she doesn't see the whole picture."
    jump captain_encouragement

label discuss_dreams:
    a "I've always dreamed of creating technology that really helps people, you know? Not just gadgets, but real solutions to global problems."
    c "That's admirable, Anna. And with your unique perspective, I bet you'll come up with ideas none of us would think of."
    jump captain_encouragement

label captain_encouragement:
    c "You have something none of us do, Anna. Creativity. You see the world differently, and that's invaluable."
    $ anna_confidence += 2
    $ team_trust += 1

    scene bg vr_room
    n "Captain suggests exploring the virtual reality game lounge to take Anna's mind off her worries."

    menu:
        "Join the VR game":
            jump vr_game
        "Observe the others play":
            jump observe_vr

label vr_game:
    n "Anna dons the VR headset and joins her teammates in a virtual world filled with puzzles and challenges."
    # Implement a mini-game here for the VR experience
    $ tech_skill += 2
    $ team_trust += 2
    jump vr_end

label observe_vr:
    n "Anna watches her teammates navigate the virtual challenges, noting their problem-solving approaches."
    a "Interesting... Cipher always looks for the hidden path, while Ace goes for the most direct route..."
    $ tech_skill += 1
    $ social_skill += 1
    jump vr_end

label vr_end:
    scene bg kitchen
    n "As the night grows late, the team finds themselves gathering in the kitchen for a midnight snack."

    show anna normal at center
    a "Please let there be some leftover pizza..."

    play sound "audio/lights_on.mp3"
    n "Suddenly, the lights flick on"

    show ace confident at left
    show cipher focused at right
    ac "Williams? What are you doing here?"

    a "Uh... late-night study session?"

    menu:
        "Propose a snack cooking challenge":
            $ social_skill += 2
            $ team_trust += 2
            jump cooking_challenge
        "Suggest a quiet chat":
            $ social_skill += 1
            $ team_trust += 1
            jump quiet_chat

label cooking_challenge:
    n "The kitchen erupts into cheerful chaos as the recruits attempt to out-cook each other with creative midnight snacks."
    # Implement a mini-game here for the cooking challenge
    jump chapter3_end

label quiet_chat:
    n "The recruits gather around the kitchen table, sharing snacks and stories in the quiet of the night."
    c "You know, it's moments like these that really bring a team together."
    jump chapter3_end

label chapter3_end:
    n "As the recruits head back to their rooms, a new sense of camaraderie hangs in the air. Little do they know, their newfound bonds will soon be put to the ultimate test..."

    return  # This will end Chapter 3 and return to the main script