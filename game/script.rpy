label start:
    # Ask for the player's name
    define coco = Character("Coco", color="#FFD9AD")
    image bedroom_night = "bg room.png"
    image card = "time.png"
    image coco = im.Scale("coco.png", 1920, 1080)
    image chappy = im.Scale("coco happy.png", 1920, 1080)
    image cconfused = im.Scale("coco confused.png", 1920, 1080)
    image cocolockin = Movie(play="images/Cocolock.webm")

    # Initialize the score
    play music "Coco.mp3"
    $ score = 0
    scene coco with fade
    coco "Hoi!...ehm...what was your name again?"
    $ player_name = renpy.input("What's your name?")
    $ player_name = player_name.strip()
    if not player_name:
        $ player_name = "Peeb"

    # Check for special names and display a custom message
    if player_name.lower() == "maya":
        coco "Oh, Hoi Maya! Your hair was covering your beautiful face, so I didn’t recognize you!"
    elif player_name.lower() == "mymy":
        coco "Hoi Mymy! Finished with your littel fight with Kiki?"
    elif player_name.lower() == "coco":
        scene cconfused
        coco "Coco? Well, it's nice to meet myself."
    elif player_name.lower() == "vera":
        scene cconfused
        coco "Mrs. Persijn! I'm sorry for not recognizing you..."
    elif player_name.lower() == "soei":
        scene cconfused
        coco "Mom? What are you doing in school?"
    elif player_name.lower() == "terra":
        coco "Terra? I think I have heard of you before..."
    elif player_name.lower() == "patches":
        coco "I'm not a cleric."
    elif player_name.lower() == "gwyn":
        coco "plin plin plon..."   
    elif player_name.lower() == "solaire":
        coco "Praise the Sun!"
    elif player_name.lower() == "foenkie":
        jump pedo
    elif player_name.lower() == "peeb":
        coco "Sounds cute and majestic...I kinda hate the thought of Baby Mymy right now...I don't know why..."     
    else:
        coco "Oh, hoi [player_name]!"

    scene coco
    coco "Anyways, do you want to do my personality test?"
    menu:
        "Yes!":
            scene chappy
            coco "Yippe!"
        "No!":
            coco "Oh ok!"
            $ config.skipping = False  # Disable skipping
            scene chappy
            pause 9999
            return
    
    scene coco
    coco "Ok, let's start with the first question, ready?"
    coco "What's your favourite Colour?"
    # Question 1
    menu:
        "Red":
            $ score += 3
            scene chappy
            coco "Nice and comfy choice!"
        "Orange":
            $ score += 2
            scene chappy
            coco "Ah, the colour of enthusiasm!"
        "Yellow":
            $ score += 1
            scene chappy
            coco "Hey, that's my favourite!"

    scene coco
    coco "Let's move on to the second Question!"
    coco "What's your favourite Hobby?"
    # Question 2
    menu:
        "Exploring outdoors":
            $ score += 2
            coco "An Adventurer? Pretty cool!"
        "Reading or relaxing inside":
            $ score += 3
            coco "Interesting, not my think. Life is short, so I tend to enjoy the outside more!"
        "Spending time with friends":
            scene chappy
            coco "Right? It's so much fun!"
            $ score += 1

    # Question 3
    scene coco
    coco "What is, in your opinion, the best vacation spot?"
    menu:
        "A tropical beach":
            $ score += 3
            scene chappy
            coco "Sounds relaxing!"
        "A cultural city":
            $ score += 2
            coco "I've heard that Japan is a great place!"
        "A cozy cabin in the mountains":
            $ score += 1
            scene chappy
            coco "That would sound nice, just nature and you."

    # Question 4
    scene coco   
    coco "What is your favourite genre?"
    menu:
        "Action/Adventure":
            $ score += 2
            scene chappy
            coco "Not my think, but I can see the appeal!"
        "Drama/Romance":
            $ score += 3
            scene chappy
            coco "Oh lovely choice."
        "Comedy":
            $ score += 1
            scene chappy
            coco "I love comedy too! Adam Sandler Movies are my favourite."

    # Question 5
    scene coco
    coco "What's your favourite Animal??"
    menu:
        "Gazelle":
            $ score += 2
            scene chappy
            coco "Such beautiful creatures! Did you know they are the national animal of my home country?"
        "Cat":
            $ score += 3
            coco "Oh, I'm alergic to those...not a big fan."
        "Red Fox":
            $ score += 1
            scene chappy
            coco "That's an...interesting choice."
    scene chappy
    coco "Ok, that was all!"
    scene coco
    coco "Let me check my cheat sheet to see what you would be..."

    # Display personality result
    if score <= 7:
        $ result = f"{player_name}, you are a calm and introspective Person."
    elif score <= 12:
        $ result = f"{player_name}, you are a balanced and adaptable Person."
    else:
        $ result = f"{player_name}, you are a adventurous and energetic Person!"

    # Show the result
    coco "[result]"

    coco "Again, thanks for doing this and see you next time!"

    return

label pedo:
    stop music
    scene black
    play music "Coco is angry!.mp3"
    pause 1.35
    
    show cocolockin
    coco "I don't like people like you."

    
    return