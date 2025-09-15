define player_name = "Player"
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
    import random

init python:
    # for importing libraries
    import_dir = os.path.join(renpy.config.gamedir, THIS_PATH, 'python-packages')
    # to prevent STOCKFISH_ENGINE from getting stored and pickled
    global_objects = {}

label start:
    $ poems = [
        {
            "intro": ["This one is about love.", "It's a classic!"], 
            "text": ["Roses are red,", "Violets are blue,", "Sugar is sweet,", "And so are you."]
        },
        {
            "intro": ["This one's good! I don't know who wrote it, sadly...", "I found this in front of my door after band practice, crumpled on the ground. Who would throw away such a beautiful piece of poetry?"], 
            "text": ["Is there a land where joy runs free,\nWhere I can find peace and my destiny,\nA place where my dreams can come alive,\nWhere happiness helps my soul survive?", "Whenever I’m left alone in the night,\nWhen birds and flowers lose their light,\nI dream of a sky where the Sun won’t fade,\nIts golden rays in glory displayed."]
        },
        {
            "intro": ["This one is from Zoey, she loves her silly love songs.", "Cleo rejected it, but I quite liked it!"], 
            "text": ["I was still studying, he was working late,\nAt night I read the works of Shakespeare’s fate.\nSometimes he'd wonder at my strange rhymes,\nBut he never let me worry, no matter the times.", "He had stronger arms than I could claim,\nHe had stronger arms than I could tame.\nHe always let me take control,\nHe let me win his soul."]
        },
        {
            "intro": ["This one was made by Cleo!", "She kind of wants to push our sound in a new direction."], 
            "text": ["Pay attention to the last thing,\nKeep me within you, let it cling.\nI feel like I'm wandering through terraces of mind,\nSomething in me is divided, hard to find.", "I love you, I love your dreams to guess,\nAnd I don't know why it causes you distress.\nDon't worry about it, let it be,\nDon't worry about it, set your mind free."]
        },
    ]     
    # Shuffle the list to randomize the order
    $ random.shuffle(poems)   

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
    elif player_name.lower() == "hefty":
        scene chappy
        coco "Hoi Hefty! Hoe gaat het met je?"        
    elif player_name.lower() == "ilse":
        scene chappy
        coco "Hi Ilse, how are you doing? By the way, Maya birthday is coming up soon, can you help me bake a cake for her?"
    elif player_name.lower() == "kill yourself":
        jump kys
    elif player_name.lower() == "kys":
        jump kys
    elif player_name.lower() == "nigger":
        $ renpy.quit()
    elif player_name.lower() == "nigga":
        $ renpy.quit()
    elif player_name.lower() == "cum":
        $ renpy.quit()
    elif player_name.lower() == "sex":
        $ renpy.quit()
    elif player_name.lower() == "masturbation":
        $ renpy.quit()
    elif player_name.lower() == "edge":
        $ renpy.quit()
    elif player_name.lower() == "edging":
        $ renpy.quit()
    elif player_name.lower() == "fuck":
        $ renpy.quit()
    elif player_name.lower() == "masturbate":
        $ renpy.quit()
    elif player_name.lower() == "kaffir boetie":
        $ renpy.quit()
    elif player_name.lower() == "kaffir":
        $ renpy.quit()
    elif player_name.lower() == "kaffer":
        $ renpy.quit()
    elif player_name.lower() == "kafir":
        $ renpy.quit()
    elif player_name.lower() == "kaffre":
        $ renpy.quit()
    elif player_name.lower() == "kuffar":
        $ renpy.quit()
    elif player_name.lower() == "nazis":
        $ renpy.quit()
    elif player_name.lower() == "faggot":
        $ renpy.quit()
    elif player_name.lower() == "fag":
        $ renpy.quit()
    elif player_name.lower() == "tranny":
        $ renpy.quit()
    elif player_name.lower() == "shemale":
        $ renpy.quit()
    elif player_name.lower() == "rape":
        $ renpy.quit()
    elif player_name.lower() == "raping":
        $ renpy.quit()
    elif player_name.lower() == "rapist":
        $ renpy.quit()
    elif player_name.lower() == "kill yourself":
        jump kys
    elif player_name.lower() == "kys":
        jump kys
    elif player_name.lower() == "gas the jews":
        $ renpy.quit()
    elif player_name.lower() == "hitler did nothing wrong":
        $ renpy.quit()
    elif player_name.lower() == "nazi":
        $ renpy.quit()
    elif player_name.lower() == "white power":
        $ renpy.quit()
    elif player_name.lower() == "heil hitler":
        $ renpy.quit()
    elif player_name.lower() == "pedophile":
        $ renpy.quit()
    elif player_name.lower() == "child porn":
        $ renpy.quit()
    elif player_name.lower() == "cp":
        $ renpy.quit()
    elif player_name.lower() == "incest":
        $ renpy.quit()
    elif player_name.lower() == "bestiality":
        $ renpy.quit()
    elif player_name.lower() == "zoophilia":
        $ renpy.quit()
    elif player_name.lower() == "genocide":
        $ renpy.quit()
    elif player_name.lower() == "ethnic cleansing":
        $ renpy.quit()
    elif player_name.lower() == "bomb":
        $ renpy.quit()
    elif player_name.lower() == "terrorist":
        $ renpy.quit()
    elif player_name.lower() == "jihad":
        $ renpy.quit()
    elif player_name.lower() == "muslim ban":
        $ renpy.quit()
    elif player_name.lower() == "sharia law":
        $ renpy.quit()
    elif player_name.lower() == "infidel":
        $ renpy.quit()
    elif player_name.lower() == "chink":
        $ renpy.quit()
    elif player_name.lower() == "gook":
        $ renpy.quit()
    elif player_name.lower() == "fuck you":
        jump kys1
    elif player_name.lower() == "die":
        jump kys
    elif player_name.lower() == "sand nigger":
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
        "Can you read me something?":
            if poems:
                coco "Of course! Let me get my poem folder real quick!"
                # Get the next poem and remove it from the list
                $ current_poem = poems.pop(0)
                
                # Coco says the intro lines
                python:
                    for line in current_poem["intro"]:
                        renpy.say(coco, line)
                
                # Coco reads the poem line by line
                python:
                    for line in current_poem["text"]:
                        renpy.say(coco, line)
                jump menu
            else:
                coco "I don't have any more poems, sorry."
                jump menu
label mini_games:
    scene cconfused
    coco "Oh, the Club Room has a lot of games! But I do not have any here sadly."
    #menu:    
    #    "Yeah, why not.":
    #       pass  # Let the user try again
    #    "Nah, forget it.":
    jump menu

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
            $ renpy.quit()
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
        "Action":
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
        "hobby": "I love playing the drums! It's my way of expressing myself.",
        "hobbies": "I love playing the drums! It's my way of expressing myself.",
        "favorite color": "Yellow! It's so bright and cheerful, don't you think?",
        "do you play any": "I play the drums! It's very fun!",
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
        "my favourite band" : "Oh nice! I'll check them out.",
        "my favourite bands" : "Oh nice! I'll check them out.",
        "doing good" : "Glad to hear that!",
        "I'm ok" : "Glad to hear that!",
        "I'm fine" : "Glad to hear that!",
        "I'm alright" : "Glad to hear that!",
        "I'm doing" : "Glad to hear that!",
        "I'm good" : "Glad to hear that!",
        "going bad" : "Oh sorry to hear that, do you want to talk about it?",   
        "going good" : "Glad to hear that!",
        "going alright" : "Glad to hear that!",
        "going fine" : "Glad to hear that!",
        "going ok" : "Glad to hear that!",
        "how's it going" : "Glad to hear that!",
        "how is it going" : "Glad to hear that!",
        "how are you" : "I'm doing quite good! Thanks for asking, I hope you're doing alright too!" ,
        "how are you doing" : "I'm doing quite good! Thanks for asking, I hope you're doing alright too!" ,
        "it's going" : "Glad to hear that!",
        "are you doing" : "I'm doing quite good! Thanks for asking, I hope you're doing alright too!" , 
        "it going" : "I'm doing quite good! Thanks for asking, I hope you're doing alright too!" , 
        "it's going" : "Glad to hear that!",
        "school life" : "It's alright, nothing stressful.",
        "like school" : "I like it!",
        "your religion" : "I'm not a religous Person, so I'm sorry, can't talk about that.",
        "be my wife" : "Ehm...No?",
        "are you from" : "South Africa!",
        "japan" : "Oh Japan! Mymy hates that place, I don't know why, but she always bad mouths everything about it.",
        "aguagu" : "Are you a baby or something?",
        "your name" : "Coco? You already forgot, silly?",
        "call me a good boy" : "I'm not comfortable with that, sorry.",
        "call me a good girl" : "I'm not comfortable with that, sorry.",
        "peeb" : "Sounds cute, what is that?",
        "peebs" : "Sounds cute, what is that?",
        "peebs is" : "Oh interesting!",
        "peeb is" : "Oh interesting!",
        "peebs are" : "Oh interesting!",
        "peeb are" : "Oh interesting!",
        "peeb is a" : "Oh interesting!",
        "peebs are a" : "Oh interesting!",
        "peeb is the" : "Oh interesting!",
        "peebs are the" : "Oh interesting!",
        "lud zbunjen normalan" : "Sta ti bi?",
        "religion" : "I'm not a religous Person, so I'm sorry, can't talk about that.",
        "believe in god" : "I'm not a religous Person, so I'm sorry, can't talk about that.",
        "christianity" : "I'm not a religous Person, so I'm sorry, can't talk about that.",
        "islam" : "I'm not a religous Person, so I'm sorry, can't talk about that.",
        "coco" : "That's me!",
        "what's your name" : "Coco! Nice to meet you!",
        "your name" : "Coco! Nice to meet you!",
        "what's my name" : "How did you forget that silly?",
        "whats my name" : "How did you forget that silly?",   
        "my name" : "How did you forget that silly?",     
        "who are you" : "I'm Coco! Nice to meet you!",
        "who is coco" : "That's me!",
        "who is mymy" : "That's my sister! She's a bit chaotic, but I love her.",
        "who is maya" : "That's my sister! She's a bit shy, but I love her.",
        "about yourself" : "My name is Coco, I play the Drums, I love Rugby and listening to music.",
        "rugby": "Oh, Rugby! My biggest passion! I love the adrenaline, the strategy, the teamwork... it's everything to me!",  
        "drums": "Drumming is like my heartbeat, you know? I can't imagine a day without playing.",  
        "favourite food": "Oh, that's a tough one... but if I had to choose, probably bobotie. Have you ever tried it?",  
        "video games": "I like them! Though I don’t play that often. Maya is way more into them than I am.",  
        "dreams": "I sometimes dream of South Africa... of running through the fields, feeling free.",  
        "fears": "Thunder... I really don't like it. Can we change the subject?",  
        "birthday": "Oh, trying to plan something special for me? Well, it's a secret!",  
        "funny story": "Once, Mymy dared me to eat a spoonful of cinnamon... I regret that.",  
        "favorite color": "Yellow! It's so bright and cheerful, don't you think?",
        "favorite animal": "I love gazelles! They're so graceful and elegant.",  
        "cats or dogs": "Dogs, definitely! They're always so happy and energetic! I'm not that fond of cats...",  
        "childhood": "It was...complicated. But let's not dwell on that.",  
        "superpower": "If I could have any power? Probably super speed! I'd be unstoppable on the rugby field.",   
        "biggest regret": "There are things I wish I could change, but dwelling on the past won't fix them.",  
        "future": "I don't know what the future holds, but I'll keep running forward.",  
        "secrets": "If I told you, they wouldn’t be secrets anymore, would they?",  
        "best memory": "Probably the times Maya, Mymy and me played together as children. We laughed so much back then.",  
        "worst memory": "Can we not talk about that?",  
        "mymy opinion": "She's wild, chaotic, and sometimes a headache, but I wouldn't trade her for the world.",  
        "maya opinion": "Maya's very lovely, I just wish she'd talk more.",  
        "joke": "Okay, okay, I've got one! Why did the drummer break up with their metronome? ...Because it was too controlling!",  
        "favorite season": "Spring! Everything is blooming and alive, just like me!",
        "favorite hobby": "I love playing the drums! It's my way of expressing myself.",
        "favorite sport": "Rugby! The thrill, the teamwork... it's everything to me!",
        "favorite book": "I love reading! But I don't have a favorite book, I just read whatever I can get my hands on.",
        "favorite anime": "I don't really watch anime, but I know Maya loves it! I think she likes \"Bukunu Senpei\"? Or something like that.",
        "music taste": "I love all kinds of music, but rock has my heart!",  
        "favorite band": "I love so many! But I guess I have a soft spot for a lot of 70s Prog Bands, their music is timeless!",
        "favorite song": "I love \"21st Century Schizoid Man\" by King Crimson! It's a classic! But I also love some local Bands here.",
        "favorite instrument": "The drums, of course! But I respect all instruments...except maybe the recorder.",
        "maya hates me": "I don’t think she hates you! Maya just...has a funny way of showing affection sometimes.",
        "mymy hates me": "Mymy? Hate someone? I doubt it! She’s just a bit...overwhelming at times.",
        "favorite movie": "I love Adam Sandler movies! The comedy, Sandler himself... it’s like a rollercoaster ride!",
        "coffee or tea": "Tee, hands down. Coffee is fine, but tea kinda keeps me alive!",  
        "favorite place": "There was this hill over looking a field back home... I used to sit there for hours, just watching the world.",
        "bobotie": "Oh, bobotie! My absolute favorite food! It’s like a warm hug from home—spiced, sweet, and just perfect.",
        "springbok": "Springboks! Majestic creatures, fast and strong. Plus, they’re great at rugby. Coincidence? I think not.",
        "rugby world cup": "Oh, the Rugby World Cup! It’s like a festival of strength and strategy. I love watching the games!",
        "epke": "Epke? Don't know them sorry.",
        "adoptive parents": "Soei and Ravi... They’re great, really. I don’t always know what to say to them, but they try and I love them for that.",
        "new parents": "I guess that’s what Soei and Ravi are now. It’s... different, but not bad. I love them.",
        "parents": "If you mean my birth parents... let’s not talk about that, okay?",
        "soei": "Soei is patient. Which is good, considering we’re not the easiest bunch to handle.",
        "ravi": "Ravi’s cool! He tries to understand us, even if we’re a bit much sometimes.",
        "noga": "Oh... that. I didn’t mean to take it from Maya, I swear! It's just...whatever...sorry.",
        "eiko": "Who’s that? Should I know them?",
        "eiko is mymy's": "jump no",  
        "eiko is mymys": "jump no",                 
        "anime": "I think anime is fun! Maya really likes it, but Mymy...not so much. She always complains about it.",
        "manga": "I think manga is fun! Maya really likes it, but Mymy...not so much. She always complains about it.",
        "books": "I love reading! I read a lot of biology and adventure books, but I also like some classics.",
        "book": "I love reading! I read a lot of biology and adventure books, but I also like some classics.",
        "mymy sister": "Mymy has a sisters. She says it like that, for some reason. It’s cute.",
        "miku": "Oh, Hatsune Miku! Maya loves her! I don’t really get it, but hey, if it makes her happy.",
        "hatsune miku": "Oh, Hatsune Miku! Maya loves her! I don’t really get it, but hey, if it makes her happy.",
        "miku hatsune": "Oh, Hatsune Miku! Maya loves her! I don’t really get it, but hey, if it makes her happy.",
        "cleo": "Cleo’s great! She’s the serious one, which, honestly, we need.",
        "zoey": "Zoey’s cool. A little quiet, but when she talks, it’s usually something smart.",
        "kiki": "Kiki? I like her, she's very adventourous! But her and Mymy can be a bit...much together.",
        "yfke": "Yfke! She's interesting...I like her, but I sometimes worry too much about her...she does some stuff that makes me a bit worried.",
        "ilse": "Ilse is very nice, she likes to bake a lot of cakes. I'll askk her to bake one for Maya's birthday.",
        "roos": "Roos is my best friend! We are like twins. She's very chill.",
        "henk": "Henk? I think I know him. He’s... something.",
        "lesotho": "Oh, I’ve been there once or twice! It’s beautiful, the mountains especially.",
        "south african": "Oh, I’m South African! Born and raised in the beautiful countryside.",
        "africa": "Oh, I’m South African! Born and raised in the beautiful countryside.",
        "african": "Oh, I’m South African! Born and raised in the beautiful countryside.",
        "afrikaan": "Oh, I’m South African! Born and raised in the beautiful countryside.",
        "afrikaans": "Oh, I’m South African! Born and raised in the beautiful countryside.",
        "brainrot": "ts pmo icl idc sybau",
        "brain rot": "ts pmo icl idc sybau",
        "your band": "Running in the 60s! We play a mix of folk, eurobeat and whatever else we feel like.",
        "running in the 60s": "That's my band! We have a concert next weekend, you can come if you like.",
        "your band name": "Running in the 60s! We play a mix of folk, eurobeat and whatever else we feel like.",
    }

while True:
    $ player_input = renpy.input("Type a sentence:")

    # Normalize the player's input for comparison
    $ normalized_input = player_input.lower()

    # Import the regular expression module
    python:
        import re

    # Check for exact or approximate matches using regular expressions
    if re.search(r'\b(kys|kill yourself)\b', normalized_input, re.IGNORECASE):
        jump kys
    elif re.search(r'\b(no parents|dead parents|orphan|nigger|hate niggers|niggers|hate you|cum|want to have sex|sex|masturbation|edge|edging|wanna fuck|want to fuck|masturbate|kaffir boetie|kaffir|kaffer|kafir|kaffre|kuffar|love nazis|masturbating|faggot|fag|tranny|rape|raping|rapist|kill yourself|kys|suicide|gas the jews|hitler did nothing wrong|nazi|white power|heil hitler|pedo|pedophile|child porn|cp|incest|bestiality|zoophilia|genocide|ethnic cleansing|jihad|sharia law|infidel|chink|gook|spic|wetback|beaner|cuck|fuck you|die|moon cricket|porch monkey|jungle bunny|sand nigger|raghead|camel jockey)\b', normalized_input, re.IGNORECASE):
        jump kys1
    elif re.search(r'\b(eiko is|eiko is mymys)\b', normalized_input, re.IGNORECASE):
        jump no    
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
    $ depth = 4
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
        scene chappy
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

label no:
    scene shocked
    coco "What? Mymy has a sister? I need to ask her about that...{p=0.8}{nw} "
    stop music
    scene black
    pause 2.0
    "No one is supposed to know about that..."
    $ renpy.quit()