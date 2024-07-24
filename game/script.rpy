# File: script.rpy

# Define characters
define n = Character("Narrator")
define a = Character("Anna")
define c = Character("Captain")
define ac = Character("Ace")
define ci = Character("Cipher")
define m = Character("Maverick")
define d = Character("Doc")
define mt = Character("Ms. Thorne")
define sr = Character("Sergeant Reyes")
define ms = Character("Mr. Sato")

# Define global variables
default player_name = ""
default anna_confidence = 0
default team_trust = 0
default tech_skill = 0
default physical_skill = 0
default social_skill = 0

# Define images (you'll need to create these)
image bg academy_exterior = "images/academy_exterior.png"
image bg induction_room = "images/induction_room.png"
image bg common_area = "images/common_area.png"
image bg hallway_night = "images/hallway_night.png"
image bg coding_classroom = "images/coding_classroom.png"
image bg training_facility = "images/training_facility.png"
image bg vr_room = "images/vr_room.png"
image bg control_room = "images/control_room.png"
image bg conference_room = "images/conference_room.png"
# Add more background images as needed

# Character images
image anna normal = "images/anna_normal.png"
image anna embarrassed = "images/anna_embarrassed.png"
image anna determined = "images/anna_determined.png"
image anna frustrated = "images/anna_frustrated.png"
image anna triumphant = "images/anna_triumphant.png"

image captain normal = "images/captain_normal.png"
image ms_thorne stern = "images/ms_thorne_stern.png"
image ace confident = "images/ace_confident.png"
image cipher focused = "images/cipher_focused.png"
# Add more character images as needed

# The game starts here
label start:
    # Initialize the game
    $ player_name = renpy.input("What is your name?")
    $ player_name = player_name.strip()
    if player_name == "":
        $ player_name = "Anna"

    n "Welcome, [player_name], to Neo Scholars Academy."

    # Chapter 1
    call chapter1 from _call_chapter1

    # Chapter 2
    call chapter2 from _call_chapter2

    # Chapter 3
    call chapter3 from _call_chapter3

    # Chapter 4
    call chapter4 from _call_chapter4

    # Chapter 5
    call chapter5 from _call_chapter5

    # Epilogue
    call epilogue from _call_epilogue

    # End of the game
    n "Congratulations, [player_name]. You've completed your journey at Neo Scholars Academy."
    n "Your final stats:"
    n "Confidence: [anna_confidence]"
    n "Team Trust: [team_trust]"
    n "Tech Skill: [tech_skill]"
    n "Physical Skill: [physical_skill]"
    n "Social Skill: [social_skill]"

    "Thank you for playing!"

    return

# Include chapter files
include "chapter1.rpy"
include "chapter2.rpy"
include "chapter3.rpy"
include "chapter4.rpy"
include "chapter5.rpy"
include "epilogue.rpy"