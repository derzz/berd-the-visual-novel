# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


define e = Character("Da Berd", image = "daberd")
define l = Character("Lawyer Berd", image = "lawyerBerd")
define c = Character("Crown Berd", image = "crownberd")
define j = Character("Judge Berd", image = "judgeberd")

# The game starts here.

label law:

    e "Ah, I see you want to see the law of berds"
    e "And you're just in luck! I will show you lawyer berd."
    show daberd:
        linear 1.0 xalign 0.0
        xzoom -1.0
    show lawyerberd at right
    l "Hello I am lawyer berd."
    e "Hello there lawyer berd, how are you"
    l "very good da berd. as you can see, i am ze lawyer berd"
    l "who faces against crown berd"
    l "wait, i hear him."
    show lawyerberd:
        linear 3.0 xalign 0.0
        xzoom -1.0
        linear 3.0 xalign 1.0
        xzoom 1.0
        repeat

    l "wHeRe ArE yOu crown berd????"
    l "I hEaR yOu!"
    show crownberd:
        xzoom -1.0
        xanchor 0.5
        yanchor 0.5
        rotate 25
        xalign -0.25
        yalign -0.1
    c "hello i am ze crown berd, a berd who wear a crown"
    show daberd:
        linear 1.0 xalign 0.7
        xzoom 1.0
    show lawyerberd:
        linear 1.0 xalign 1.0
        xzoom 1.0
    show crownberd:
        linear 1.0 rotate 0
        linear 1.0 xalign -0.1 yalign 2.0
    "the crown sparkles in the glory of crown berd"
    c "now what do you want from me lawyer berd who for some reason his defendants are always innoncent and i lose"
    c "because he CHEATS"
    l "how does one cheat in law"
    c "perjury?"
    l "fair enough. even though that's all of your witnesses in a nutshell."
    "the berds talk to each other, accusing each other of perjury for five minutes. and then..."
    show judgeberd:
        xzoom -1.0
        rotate 25
        xalign -0.25
        yalign -0.1
    show crownberd:
        xzoom 1.0
        linear 2.0 rotate 25
    show lawyerberd:
        xzoom 1.0
        yalign 0.8
        xalign 0.9
        xanchor 0.5
        yanchor 0.5
        linear 2.0 rotate 25
    show daberd:
        xzoom 1.0
        yalign 0.8
        xanchor 0.5
        yanchor 0.5
        linear 2.0 rotate 25
    j "WHERE ARE YOU GUYS"
    j "WE HAVE A TRIAL STARTING NOW"
    j "HURRY UP WITH YOUR LOVE TALK"
    show judgeberd:
        linear 5.0 xalign -2.0
    show daberd:
        linear 2.0 rotate 0
    show crownberd:
        linear 2.0 rotate 0
        xzoom -1.0
        xalign 0.0
    show lawyerberd:
        linear 2.0 rotate 0
    c "you heard your berd"
    hide judgeberd
    c "we must go"
    l "yes indeed"
    #Show crown and lawyer berd running out and daberd talking to user to follow them
    show crownberd xzoom -1.0
    show crownberd:
        linear 2.0 xalign -5.0 yzoom -1.0
    show lawyerberd:
        linear 2.0 xalign -5.0 yalign 0.0 rotate 360
    "crown berd and lawyer berd run out into the distance"
    hide crownberd
    hide lawyerberd
    e "it looks like it's going to be a very exciting court case, do you want to go see it?"
    menu:
        "Yes":
            e "poggers, let's go"
            jump court
        "Who needs law when you can go into anarchy.":
            e "Oh, that's sad"
            e "Welp, that's very sad that you don't want to see some berd law"
            e "Well, there's nothing else to do..."
            e "... except to talk about the history of berds!!"
            jump intro1
