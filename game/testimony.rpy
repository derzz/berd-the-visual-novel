# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

default counter = 0
default pictureCount = 0

label testimony:
    call witness from _call_witness_9
    "WITNESS TESTIMONY"
    t "{b}1.{/b}So this guy right, he's walking on the road."
    t "{b}2.{/b}And he had a bomb!!!!!!!!"
    t "{b}3.{/b}I called the po po immediatitely"
    t "{b}4.{/b}And then they arrested him."
    t "{b}5.{/b}Which is very poggers."
    "END OF WITNESS TESTIMONY"
    if counter == 0:
        $ counter +=1
        jump afterTestimony

    else:
        jump cross

label afterTestimony:
    scene bg jbench
    show judgeberd:
        yalign 0.35 xalign 0.5
        zoom 1.6

    j "Wow, this guy is too poggers."
    j "He caught the guy before he endangered more berds lives!"
    j "orz"
    j "Anyways, Crown Berd, do we have some evidence that causes the client to be declared guilty"
    call crown from _call_crown_18
    c "Yes your berd."
    c "One of the first items we have is this bomb"
    show bomb:
        zoom 0.5
        xalign 1.0
        yalign .0
    c "It is not detonated"
    show bomb:
        linear 3.0 xalign 0.5 yalign 0.5 zoom 2.0
    "Added Bomb to court record"
    hide bomb
    c "We also have a lighter"
    show lighter:
        zoom 0.5
        xalign 1.0
        yalign .0
    c "It has the accused fingerprints."
    c "And someone's unknown fingerprints."
    c "We got no record of the known berds."
    c "Such as pink berd!!!, blue berd, bean berd, boomer berd, and pog berd >:D"
    c "{b}If we can compare the fingerprints to its owner, we can identify the person."
    c "And it was lit up according to expert analysis."
    show lighter:
        linear 3.0 xalign 0.7 yalign 0.4 zoom 1.2
    "Added lighter to court record"
    hide lighter
    c "Ok, finally, we have a cigarette."
    show cigarette:
        zoom 0.5
        xalign 1.0
        yalign .0
    c "It was likely that the accused wanted to smoke it before lighting the bomb."
    c "It also has the accused fingerprints."
    show cigarette:
        linear 3.0 xalign 0.7 yalign 0.4 zoom 1.2
    "Added cigarette to court record"
    hide cigarette
    c "That is all your berd."
    c "The accused fingerprints are all on all the items."
    c "Therefore, this berd is a berd terrorist and will be punished accordingly."
    call judge from _call_judge_25
    j "Thank you Crown Berd."
    j "Now, lawyer berd, it is time for your cross examination."
    j "Do you need an explanation?"

    label explain:
        menu:
            "yes":
                j "Ok so in this, you will find whether or not the witness has a contradiction."
                j "You will show it via evidence and find a contradiction."
                j "To do this, you click {i}present{/i} and choose the numbered statement to contradict."
                j "Then, you will click on the evidence that contradicts the statement."
                j "Be careful when choosing a statement and evidence, you cannot go back after you click the option."
                j "Before selecting, you also have the options to relook at the witness' statement and look at the court record where all the evidence is stored."
                j "Be sure to look at the court record, sometimes some interesting descriptions can come up."
                j "Do you still need an explanation?"
                jump explain
            "no":
                call defense from _call_defense_30
                l "No your berd, I understand."
                l "Let's start."
                "CROSS EXAMINATION"
                jump cross

    label testimonytwo:
        call witness from _call_witness_10
        "WITNESS TESTIMONY: WHAT DID THE TERRORIST LOOK LIKE?"
        #Maybe add animations here
        t "{b}1.{/b} Ok, so if I recall, the berd was walking on the road."
        t "{b}2.{/b} There was a cigarette on the ground."
        t "{b}3.{/b} And he was holding a pepper shaker."
        t "{b}4.{/b} As for his characteristics, uh, he was a white berd."
        t "{b}5.{/b} And, he looked pretty normal, nothing was on his face."
        t "END OF WITNESS TESTIMONY"
        if counter == 0:
            $ counter +=1
            jump afterTestimonyTwo
        else:
            jump crossTwo

    label afterTestimonyTwo:
        call judge from _call_judge_26
        j "Wow, that's very interesting."
        call crown from _call_crown_19
        c "As a note, the witness has not seen the picture. He is basing this of his own memories."
        call judge from _call_judge_27
        j "Very well, Lawyer Berd, please start with your cross examination."
        call defense from _call_defense_31
        l "Yes your berd."
        l "(Hm... Who's that other person?)"
        jump crossTwo
