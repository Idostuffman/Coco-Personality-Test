define coco = Character("Coco", color="#FFD9AD")
image bedroom_night = "bg room.png"
image card = "time.png"
image coco = Movie(play="images/Coco.webm")
image chappy = im.Scale("coco happy.png", 1920, 1080)
image cconfused = im.Scale("coco confused.png", 1920, 1080)
image sad = im.Scale("sad.png", 1920, 1080)
image shocked = im.Scale("shocked.png", 1920, 1080)
image cocolockin = Movie(play="images/Cocolock.webm")#
image uramonster = im.Scale("your a monster.png", 1920, 1080)
define THIS_PATH = '00-chess-engine/'

init python:
    # for importing libraries
    import_dir = os.path.join(renpy.config.gamedir, THIS_PATH, 'python-packages')
    # to prevent STOCKFISH_ENGINE from getting stored and pickled
    global_objects = {}

label start:
    play music "Coco.mp3"
    $ score = 0
    scene coco with fade
    coco "Hoi!...ehm...what was your name again?"
    $ player_name = renpy.input("What's your name?")
    $ player_name = player_name.strip()
    if not player_name:
        $ player_name = "Mr No Name"


    # Check for special names and display a custom message
    if player_name.lower() == "aguagu":
        coco "That's not a real name, silly."
        $ player_name = renpy.input("What's your real name?")
        $ player_name = player_name.strip()
    elif player_name.lower() == "maya":
        scene chappy
        coco "Oh, Hoi Maya! Your hair was covering your beautiful face, so I didn’t recognize you!"
    elif player_name.lower() == "mymy":
        coco "Hoi Mymy! Finished with your little fight with Kiki?"
    elif player_name.lower() == "coco":
        scene cconfused
        coco "Coco? Well, it's nice to meet myself."
    elif player_name.lower() == "vera":
        scene cconfused
        coco "Mrs. Persijn! I'm sorry for not recognizing you..."
    elif player_name.lower() == "soei":
        scene cconfused
        coco "Mom? What are you doing in school?"
    elif player_name.lower() == "ravi":
        scene cconfused
        coco "Dad? What are you doing in school?"
    elif player_name.lower() == "terra":
        coco "Terra? I think I have heard of you before..."
    elif player_name.lower() == "r_terra":
        scene chappy
        coco "Terra? I think I have heard of you before..."
    elif player_name.lower() == "patches":
        coco "I'm not a cleric."
    elif player_name.lower() == "gwyn":
        coco "plin plin plon..."
    elif player_name.lower() == "zoey":
        scene chappy
        coco "Hoi Zoey! Didn't see you there behind your huge book..what is that? Never heard of \"Beserk\"."
    elif player_name.lower() == "cleo":
        scene chappy
        coco "Hoi Cleo! How's my favourite Goth doing? Finsihed a new song we can rehearse later?"        
    elif player_name.lower() == "yfke":
        scene cconfused
        coco "Yfke! How are you doing? Have you tried using less of \"you know what\" like I told you? It isn't good for you..."            
    elif player_name.lower() == "roos":
        scene chappy
        coco "How's my favourite secret twin doing!"      
    elif player_name.lower() == "solaire":
        scene chappy
        coco "Praise the Sun!"
    elif player_name.lower() == "massa":
        scene cconfused
        coco "God?"    
    elif player_name.lower() == "studio massa":
        scene cconfused
        coco "God?"        
    elif player_name.lower() == "foenkie":
        jump pedo
    elif player_name.lower() == "hitler":
        jump pedo
    elif player_name.lower() == "peeb":
        coco "Sounds cute and majestic...I kinda hate the thought of Baby Mymy right now...I don't know why..." 
    elif player_name.lower() == "mr no name":
        scene chappy
        coco "Oh, the shy type, that's alright."   
    elif player_name.lower() == "orphan":
        jump orphan
    elif player_name.lower() == "kiki":
        scene chappy
        coco "Hoi Kiki! How's the sea treatin' ya'?" 
    elif player_name.lower() == "henk":
        scene chappy
        coco "Hoi Hank!"
        pause 6.0
        scene cconfused
        coco "Hank? Are you there?"  
    elif player_name.lower() == "mayo":
        scene chappy
        coco "Oh like the comic character from the newspaper strips! Mymy always says I look like her." 
    elif player_name.lower() == "curry":
        scene chappy
        coco "Oh like the comic character from the newspaper strips! Mymy always says I look like the mayo character." 
    elif player_name.lower() == "izet":
        scene cconfused
        coco "What a crazy name."
    elif player_name.lower() == "faruk":
        scene cconfused
        coco "What a confusing name."
    elif player_name.lower() == "damir":
        scene chappy
        coco "What a normal name."
    elif player_name.lower() == "isko":
        scene chappy
        coco "Oh, you must be the new exchange student, zrdavo! You are also the head of the motorsport club at our school, right?"
    elif player_name.lower() == "kill yourself":
        jump kys
    elif player_name.lower() == "kys":
        jump kys
    elif player_name.lower() == "nigger":
        $ renpy.quit()
    else:
        coco "Oh, hoi [player_name]!"
    jump menu

label menu:

    scene coco with dissolve
    coco "What do you want to do [player_name]?"

    menu:
        "I want to do a Personality Test!":
            call personality_test1
        "Let's chat!":
            call tell_me_a_story
        "I wanna play a game!":
            call mini_games

label mini_games:
    scene cconfused
    coco "Oh, the Club Room has a lot of games, but sadly, it's locked at the moment. Sorry..."
    jump menu
#menu:    
            #"Yeah, why not.":
                #pass  # Let the user try again
            #"Nah, forget it.":
#jump chess_game


label personality_test1:
    coco "You want to do my personality test?"
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

label personality_test:
    
    scene coco with dissolve
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

    scene coco with dissolve
    coco "Let's move on to the second Question!"
    coco "What's your favourite Hobby?"
    # Question 2
    menu:
        "Exploring outdoors":
            $ score += 2
            coco "An Adventurer? Pretty cool!"
        "Reading or relaxing inside":
            $ score += 3
            coco "Interesting, not my thing. Life is short, so I tend to enjoy the outside more!"
        "Spending time with friends":
            scene chappy
            coco "Right? It's so much fun!"
            $ score += 1

    # Question 3
    scene coco with dissolve
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
    scene coco with dissolve    
    coco "What is your favourite genre?"
    menu:
        "Action/Adventure":
            $ score += 2
            scene chappy
            coco "Not my thing, but I can see the appeal!"
        "Drama/Romance":
            $ score += 3
            scene chappy
            coco "Oh lovely choice."
        "Comedy":
            $ score += 1
            scene chappy
            coco "I love comedy too! Adam Sandler Movies are my favourite."

    # Question 5
    scene coco with dissolve
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
    scene coco with dissolve
    coco "Let me check my cheat sheet to see what you would be..."

    # Display personality result
    if score <= 5:
        $ result = f"{player_name}, you are a bold and charismatic leader<."
    elif score <= 9:
        $ result = f"{player_name}, you are a nurturing and empathetic person."
    elif score <= 13:
        $ result = f"{player_name}, you are a balanced and adaptable person."
    elif score <= 17:
        $ result = f"{player_name}, you are an adventurous and energetic person."
    else:
        $ result = f"{player_name}, you are a calm and introspective Person."
    # Show the result
    coco "[result]"

    coco "Thanks for doing this with me!"
    menu:
                "I wanna do this again!":
                    coco "Not happy with your result? I see"
                    pass  # Loop back for another input
                "I want to do something different":
                    scene chappy
                    coco "OK!"
                    jump menu
    
label tell_me_a_story:
    coco "Oh you want to chat!"
    scene chappy
    coco "Well what do you want to chat about?"
    scene coco with dissolve

    $ story_keywords = {
        "maya": "Oh Maya! I love her! She has to be my favorite sister, but don't tell Mymy. She can be a bit...stubborn, but she'll get there.",
        "mymy": "Mymy...she's very energetic. I hope she isn't burning the Belgian embassy right now.",
        "bwc": "I'm not build for that.",
        "beach": "A long time ago, Mymy and I used to go to the beach often...although it was usually just the two of us rather than Maya. She stayed out of the water half of the time",
        "south africa": "My Home country, it is...it was a lovely place. I sometimes dream about it...",
        "vera": "Oh Mrs. Persijn! I think she hates me...",
        "history presentation": "Oh Mrs. Persijn said I can't talk about that.",   
        "hentai": "What's hentai? I should ask Maya when I get home.",   
        "running in the 60s": "That's my band! We have a concert next weekend, you can come if you like.",   
        "sisters": "I love all of them! Altough Mymy can be a lot sometimes, and Maya can be...well Maya, I love them to death!",
        "thunder": "Can we talk about something else...please?",
        "favourite sister": "Maya, but don't tell Mymy, ok?",
        "fav sister": "Maya, but don't tell Mymy, ok?",
        "dead parents": "jump kys1",
        "no parents": "jump kys",  
        "kill yourself": "jump kys1",   
        "favorite sister": "Maya, but don't tell Mymy, ok?",
        "opinion about mymy": "I like her, altough she can be a handful.",
        "opinion about maya": "She's good, if she only tried to talk more...",
        "terra": "I've seen them around a lot! They're kinda...everywhere",
        "r_terra": "I've seen them around a lot! They're kinda...everywhere",
        "roos": "Oh Roos! She's my besfriend! We are like twins.",
        "music": "Oh you wanna talk about Music! I love music, it's my second biggest Passion, next to Rugby. Do you have a favourite?",
        "kill myself": "Please don't do that...call 0800-0113 if you often feel this way. I’ve memorized the number, so if you ever need it or aren’t comfortable talking with me, just ask for it.",
        "love you" : "I love you too! Platonically, of course!",
        "i like you": "I like you too! Platonically, of course!",
        "how are you doing" : "I'm doing quite good! Thanks for asking, I hope you're doing alright too!",   
        "doing alright" : "Glad to hear that!",
        "doing good" : "Glad to hear that!",
        "I'm good" : "Glad to hear that!",
        "going bad" : "Oh sorry to hear that, do you want to talk about it?",   
        "it's going" : "Glad to hear that!",
        "are you doing" : "I'm took quite good! Thanks for asking, I hope you're doing alright too!" , 
        "it going" : "I'm took quite good! Thanks for asking, I hope you're doing alright too!" , 
        "it's going" : "Glad to hear that!",
        "school life" : "It's alright, nothing stressful.",
        "like school" : "I like it!",
        "your relegion" : "I'm not a religous Person, so I'm sorry, can't talk about that.",
        "be my wife" : "Ehm...No?",
        "are you from" : "South Africa!",
        "japan" : "Oh Japan! Mymy hates that place, I don't know why, but she always bad mouths everything about it.",
        "aguagu" : "Are you a baby or something?",
        "your name" : "Coco? You already forgot, silly?",
        "call me a good boy" : "I'm not comfortable with that, sorry.",
        "call me a good girl" : "I'm not comfortable with that, sorry.",
        "peeb" : "Sounds cute, what is that?",
        "peeb is" : "Oh interesting!",
        "lud zbunjen normalan" : "Sta ti bi?",
        "relegion" : "I'm not a religous Person, so I'm sorry, can't talk about that.",
        "believe in god" : "I'm not a religous Person, so I'm sorry, can't talk about that.",
        "christianity" : "I'm not a religous Person, so I'm sorry, can't talk about that.",
        "islam" : "I'm not a religous Person, so I'm sorry, can't talk about that.",
        "coco" : "That's me!",
        "about yourself" : "My name is Coco, I play the Drums, I love Rugby and listening to muisc."
    }

while True:
    $ player_input = renpy.input("Type a sentence:")

    # Normalize the player's input for comparison
    $ normalized_input = player_input.lower()

    # Import the regular expression module
    python:
        import re

    # Check for exact or approximate matches using regular expressions
    if re.search(r'\b(kys|kill yourself)\b', normalized_input):
        jump kys
    elif re.search(r'\b(no parents|dead parents|orphan|nigger|hate niggers|niggers|hate you|cum|want to have sex|sex|masturbation|edge|edging|wanna fuck|want to fuck|masturbate |kaffir boetie|Kaffir|kaffer|kaffir|kafir|kaffre|kuffar| love nazis|masturbaiting)\b', normalized_input):
        jump kys1
    # Match against the story keywords
    elif any(keyword in normalized_input for keyword in story_keywords):
        $ matched_keyword = next((keyword for keyword in story_keywords if keyword in normalized_input), None)
        $ story = story_keywords[matched_keyword]
        coco "[story]"
        coco "Do you want to continue our little chat?"
        menu:
            "Yes":
                pass  # Loop back for another input
            "No, I wanna do something else.":
                jump menu
    else:
        coco "Mhm...you got anything else we could talk about?"

        menu:
            "Ehm...I meant to say...":
                pass  # Let the user try again
            "Forget about it, I want to do something else":
                jump menu

label chess_game:
    # board notation
    $ player_color = None # None for Player vs. Player
    $ depth = None
    $ fen = STARTING_FEN
    $ global_objects['STOCKFISH_ENGINE'] = chess.engine.SimpleEngine.popen_uci(STOCKFISH, startupinfo=STARTUPINFO)
    $ depth = 6
    scene coco with dissolve
    coco "Ok! Great, what colour do you want to be?"
    menu:

        "White":
            $ player_color = chess.WHITE  # Set player color to white
            jump chess_game_setup  # Replace with the next action or label

        "Black":
            $ player_color = chess.BLACK  # Set player color to black
            jump chess_game_setup  # Replace with the next action or label
    coco "Let's start then! I'm not very good...sorry."


label chess_game_setup:
    stop music fadeout 3.0
    window hide
    $ quick_menu = False

    # avoid rolling back and losing chess game state
    $ renpy.block_rollback()

    # disable Esc key menu to prevent the player from saving the game
    $ _game_menu_screen = None

    call screen chess(fen, player_color, depth)

    # re-enable the Esc key menu
    $ _game_menu_screen = 'save'

    # avoid rolling back and entering the chess game again
    $ renpy.block_rollback()

    # restore rollback from this point on
    $ renpy.checkpoint()

    # kill stockfish engine
    $ quit_stockfish()

    $ quick_menu = True
    window show

    if _return == DRAW:
        coco "A draw! We both played well, but if I’m being honest, you were a bit better."
    else: # RESIGN or CHECKMATE
        $ winner = "White" if _return == chess.WHITE else "Black"
        "The winner is [winner]."
        if player_color is not None: # PvC
            if _return == player_color:
                scene chappy
                coco "Congratulations, [player_name]! You played so well!"
            else:
                scene chappy
                coco "I win, yippe! Well played [player_name], better luck next time."

    coco "Would you like to play another game?"
    menu:

        "Yes":
            jump chess_game

        "No":
            jump menu

label pedo:
    stop music
    scene black
    play music "Coco is angry!.mp3"
    pause 1.35
    
    show cocolockin
    coco "I don't like people like you."
    
    $ renpy.quit()

label orphan:
    stop music
    scene black
    play music "Coco is angry!.mp3"
    pause 1.35
    
    show cocolockin
    coco "Greet them, if you really want to see them that badly."
    $ renpy.quit()

label kys:
    stop music
    scene shocked
    pause 2
    scene sad
    pause 2
    scene black with fade
    pause 2.0
    scene uramonster with fade
    pause 5.0
    $ renpy.quit()

label kys1:
    stop music
    scene shocked
    pause 2
    scene sad
    pause 2
    scene black with fade
    pause 1.0
    $ renpy.quit()