# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


define e = Character("Da Berd", image = "daberd")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room


    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show daberd

    # Song: Thomas the tank engine ofc

    play music "audio/berd.mp3"

    # These display lines of dialogue.

    e "Hello there, I am daberd."

    e "Are you ready to start your quest to learn about the berds?"

    #Friendship points for secret ending
    $ friend = 0

    menu:
        "Yes":
            $ friend += 1
            jump intro1

        "No":
            jump intro_no

        "Where is lAwYeR berd":
            jump law

    label intro1:
        show daberd:
            yzoom -1.0
        e "Then we shall continue the journey of the berds and teach you more about how the berds are the coolest around."
        show daberd:
            yzoom -1.0
            xzoom -1.0
            linear 2.0 xalign 0.20
            linear 2.0 yalign 1.0
        e "But we must first know you! What is your name?(Don't include berd behind if you are thinking that, we will add the berd for you. also plz write in lowercase, only i get the uppercase :D)"
        python:
            name = renpy.input("What is your very kewl and pog name?")
            name.lower()
            name = name.strip() or "the unknown"
            name = name+" berd"
        define n = Character("[name]")

        show daberd:
            xzoom 1.0
            yzoom 1.0

        if name == "noodle berd":
            n "i am noodle berd"
            e "which one? i do enjoy myself some ramen :)"
            e "anyways..."
            jump intro2

        elif(name == 'pink berd'):
            n "i am pink berd!!! where are my explination marks?"
            e "of course, you do need the explination marks!!!"
            n "yes!!!"
            e "well here you go!!!"
            $ name = name + "!!!"
            n "yay!!!"
            e "anyways..."
            jump intro2

        elif(name == 'boomer berd'):
            e "wow, why are you a boomer"
            n ":("
            e "you can have some headphones then"
            "system" "headphones++"
            e "they do nothing btw"
            e "anyways..."
            jump intro2

        elif(name == 'big berd'):
            show daberd:
                zoom 5.0
                xalign 0.5 yalign 0.3

            stop music

            e "don't you dare take the og."

            jump done

        elif(name == 'chub berd'):
            e "chubchub!"
            e "i will need to change your name and my name accordingly!"
            $ name = "chubberd"
            $ e = "chubchub"
            e "i am now chubchub"
            e "you are chubberd, but i am chubchub!!"
            n "but that doesn't seem..."
            show daberd:
                zoom 4.0
                xalign 0.5 yalign 0.3
            e "SHUSH"
            show daberd:
                zoom 1.0
                xalign 0.20
                yalign 1.0
            e "anyways..."
            jump intro2

        elif(name == 'bean berd'):
            e "i sense biology and beans"
            n "ya, because that's my name??"
            e "also why are you in a pikachu hat?"
            n "why not?"
            e "fair enough."
            e "anyways..."
            jump intro2

        elif(name == 'pog berd'):
            e "why are you pog?"
            n "why are you pog?"
            e "wow how flattering!"
            e "let me just rename you real quickly"
            $ name = "pog berd >:D"
            e "there we go"
            n "wow, that is very pog"
            e "i know right"
            e "anyways..."
            jump intro2

        else:
            jump intro2

    label intro2:

        show daberd:
            xzoom -1.0
            linear 5.0 xalign 1.0
            xzoom 1.0
            linear 5.0 xalign 0.0
            repeat


        e "hello there [n], i see you see wizdom from daberd"
        e "anyways, we must talk about the beginning of the berdz"
        e "the berds are a nomadic tribe, and we started from the dawn of civilization"
        e "From the first stirrings of life beneath water... to the great beasts of the Stone Age... to man taking his first upright steps, we have come far."
        e "Then, we begun our greatest quest, from the early cradle of civilization on towards the stars."
        e "After that very kewl introduction, would you like to hear more about the berds?"

        menu:
            "Yes":
                $ friend += 1
                jump intro3

            "No":
                jump intro_no

    label intro3:
        show daberd:
            linear 2.0 xalign 0.50 yalign 0.50
        show daberd:
            linear 1.0 zoom 2.0
            linear 1.0 zoom 1.0
            repeat
        e "wow usually people get bored after i say that. pretty interesting"
        e "anyways, let's continue"
        show daberd:
            linear 1.0 xzoom -1.0 yzoom 1.0
            linear 1.0 xalign 0.75 yalign 1.0
            linear 1.0 zoom 1.0

        show daberd:
            xzoom -1.0
            linear 5.0 xalign 1.0
            xzoom 1.0
            linear 5.0 xalign 0.0
            repeat

        #History

        #Stone
        e "so the berds started with the big berd"
        e "why was he called the big berd, it was because he was"
        show daberd:
            xalign 0.4 yalign 0.2
            zoom 5.0
        e "{b}big{/b}"
        show daberd:
            zoom 1.0
            yalign 1.0
        show daberd:
            xzoom -1.0
            linear 5.0 xalign 1.0
            xzoom 1.0
            linear 5.0 xalign 0.0
            repeat
        e "with the help of the big berd, we travelled many miles picking up berds as we go"
        e "we created stones and wheel and yeetus deletus the enemies"

        #Classical
        e "after that, we have shown remarkable growth."
        e "we have left our bronze for iron and ruled with horse and berd."
        e "the sky above began to reveal its secrets, a collection of heaven that uplifts our hearts and guides us to foreign shores."
        e "we made boats that had a berd on it"
        e "we also befriended the horses with our berdness"
        e "and we also made the kazoo. in fact, that's our national insturment."
        e "do you want to continue listening about the great berd history?"

        menu:
            "Yes":
                $ friend += 1
                jump history2
            "No":
                e "oh that's sad. we had more secrets. let's just jump to the interesting portion:"
                jump ibserver
            "Now that I know your state secrets, i shall yeetus you":
                e "what"
                show daberd:
                    rotate 45
                stop music
                hide daberd with fade
                e "ahhhhhhhhhhhhh"

                #https://www.youtube.com/watch?v=da9PDzt53WA
                play music "death.mp3"
                "the creator" "oh, you weren't supposed to kill him."
                "the creator" "well since you did, I guess you win. so ya. here's bob because you shouldn't have killed daberd."
                show bob:
                    xalign 0.5 yalign 0.5
                "the creator" "ok bye."
                jump done

        label history2:
        #Medieval
        e "We have build great cities of stone and seen early empires rise and fall."
        e "Soon, we stood under the towering pinnacles of castles alongside out gallant knights."
        e "in fact, our knights were very courageous"
        e "did you konw that knight berd once saved princess berd"
        e "it was a very touching story"
        e "speaking of story, this was where the story of our people were written"
        e "just as the young apprentice learned to carry a sword"
        e "we also understood our place in this world"
        e "we were meant to be berds. berd."

        #Renassaince
        e "then we made muskets"
        e "did you know that musket berd is a very kewl berd, like big berd and knight berd"
        e "we also learned how to draw maps"
        e "and we sailed across the world"
        e "we also had scurvy berd who got scurvy"
        e "scurvy berd was not very happy"
        e "rip scurvy berd"

        #Industrial
        e "after the death of scurvy berd, we found coal"
        e "and of course, you know what that means..."
        e "NOT CHILD LABOR!!!"
        e "we were so modern, we instead used robot berd"
        e "because we were soooooooooooooooooooooooooo"
        e "kewl"

        e "anyways that is all the history of berd"
        e "and no, half of it is NOT copied off from civ"
        e "do you want to listen about the ib server"

        menu:
            "Yes":
                $ friend += 1
                jump ibserver
            "No":
                e "oh that's sad. TLDR: we just joined the server becaues why not"
                jump ending
            "Now that I know your state secrets, i shall yeetus you":
                e "what"
                show daberd:
                    linear 1.0 rotate 45
                stop music
                e "ahhhhhhhhhhhhh"
                hide daberd with fade
                #https://www.youtube.com/watch?v=da9PDzt53WA
                play music "death.mp3"
                "the creator" "oh, you weren't supposed to kill him."
                "the creator" "well since you did, I guess you win. so ya. here's bob because you shouldn't have killed daberd."
                show bob:
                    xalign 0.5 yalign 0.5
                "the creator" "ok bye."
                jump done

        label ibserver:
        #ib server thing
        e "so after our great journeys, we came to live in the server called ib. it was a fun server."
        e "oh apologies, the {b}server{/b} is fun, not ib"


        label ibChoice:
        e "would you like to hear more about ib?"
        menu:
            "yes":
                $ friend += 1
                e "ok grab some popcorn, you are about to hear death"
                jump ib
            "no":
                e "ok then, let's continue the story. it's good to hear you're not narcissitic."
                jump ending
            "give me the preview":
                e "ok so ib is torture. if you are narcissistic, you want to hear more about this."
                jump ibChoice


        label ib:
            e "so ib is not fun"
            e "in fact it's not very fun"
            e "there are horror stories left and right"
            e "and you have to pay for marks"
            e "for instance, let's bring in bob here to teach us about ib"
            e "remember, bob has ptsd from ib, so let's take it easy"
            define f = Character("bob", image = "bob")
            show bob:
                linear 1.0 xalign 0.0 yalign 1.0

            show daberd:
                linear 1.0 zoom 1.0
                linear 2.0 xalign 1.0 yalign 1.0
                xzoom 1.0

            e "hello there bob"
            show bob:
                linear 5.0 xalign 1.0
                yzoom -1.0 xzoom -1.0
                linear 5.0 yalign 0.0
                linear 5.0 xalign 0.0
                yzoom 1.0 xzoom 1.0
                linear 5.0 yalign 1.0
                repeat
            f "{b} iBibIBiBibibIbBiIbIbIbIbIbIbIbIBIbIbIBIbIb{/b}"

            e "well anyways, ask bob any questions that you have"

            menu:
                "What is it like being in ib?":
                    f "helphelphelphelphelphelphelphelp"

                "What are the teachers like?":
                    f "some are nice. but otherwise, there is one that i'm afraid to say because of persecution"
                    f ":("

                "Why are you moving around so weird?":
                    f "ibibibibibibibibibibibibibibibibibibibibibibibibibibibibibib"

            e "ok that's enough from bob, let's thank him for being him for being here today"
            hide bob

            e "that's enough about ib. let's move on to berds. so we just chilled in the server"
            jump ending




        label ending:
        e "and then more berds came. so yeah, that's the current history of the berds. any questions?"

        menu:
            "yes":
                $ friend += 1
                e "but i'm lazy so i won't answer any right now."
                #If friendship points equal to six
                if friend >= 6:
                    jump friend
                else:
                    e "k bye."
                    jump done

            "no":
                e "k bye then, this was a very nice talk."
                jump done

    label friend:
        e "wait, i can't believe you actually wanted to listen about the berds"
        e "well guess what"
        menu:
            "what":
                e "you get to see me do this kewl flip"
        window hide
        show daberd:
            linear 1.0 yalign 0.5
            linear 2.0 rotate 360
            linear 0.5 yalign 2.0
        pause 3.0
        e "that was kewl"
        e "ok goodbye fren"
        jump done

    label intro_no:
        e "That's sad. are you a berd terrorist then?"

        menu:

            "Yes":
                jump terrorist

            "No":
                jump nonterroist


    label terrorist:
        e "that's sad. well what else can we do. we'll see you soon i guess."
        jump done

    label nonterroist:
        e "hi en ming, how are you doing. life's pretty good right?"
        jump done

    # This ends the game.

    label done:
        return
