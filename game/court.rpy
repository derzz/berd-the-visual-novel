


define e = Character("Da Berd", image = "daberd")
define l = Character("Lawyer Berd", image = "lawyerBerd")
define c = Character("Crown Berd", image = "crownberd")
define j = Character("Judge Berd", image = "judgeberd")
define t = Character("Kewl Berd")

label court:
    #Court Theme from Phoenix Wright Ace Attorney
    play music "audio/trial.mp3"
    call courtmove from _call_courtmove
    "COURTROOM NO. 4"
    call judge from _call_judge
    j "alright, order in the court."
    j "now i see that everyone here is very sad"
    j "because it's court you know"
    j "so i will make a joke"
    show judgeberd f with fade
    j "{b}baguette{/b}"
    show judgeberd with fade
    j "now that joke is over, we will move onto serious matters."

    call defense from _call_defense
    show lawyerberd:
        linear 1.0 yzoom -1.0
        linear 1.0 yzoom 1.0
        repeat
    j "here on the defence we have someone who is stupid but wins in the end"

    call crown from _call_crown
    show crownberd:
        linear 1.0 rotate 360
        linear 1.0 rotate 0
        repeat


    j "and here we have a prosecutor who wants to just win but ends up losing"
    j "and it's also because he's a massive hyprocrite and does some not legal things"
    call judge from _call_judge_1
    j "Now, let's get started. Crownberd, please present your case."
    call crown from _call_crown_1
    c "Yes your berd. Today we have a very serious case, we have someone accused of being a BERD TERRORIST"
    call courtcrazy from _call_courtcrazy
    "The courtroom goes wild at the fact that someone is a berd terrorist"
    call judge from _call_judge_2
    j "with that very suprising fact, lawyer berd, does your client plead guilty or not guilty"
    call defense from _call_defense_1
    l "not guilty your honor. in fact, i will prove that my client is not only innocent but also that someone else is the criminal"
    call crown from _call_crown_2
    c "wow, that is very poggers. even i can't do that. all i know is that we have a messed up court system where a person is {i}guilty until proven innocent{/i}"
    c "anyways, to ensure that lawyer berd's client is guilty, i will bring out a witness who is totally not the terrorist"
    call judge from _call_judge_3
    j "very well, bring in your witness"
    call witness from _call_witness
    t "hello there"
    call crown from _call_crown_3
    c "Hello there witness. Please state you name and occupation for the court."
    call witness from _call_witness_1
    t "of course, I am Kewl Berd and my job is just being kewl."
    show terroristberd:
        xzoom -1.0
    t "which is very kewl"
    t "like look at my glasses, they are very kewl."
    call judge from _call_judge_4
    j "wow, that is very kewl. no way this guy is the terrorist. anyways, can you please provide your testimony on why the defense's client is guilty of being a berd terrorist?"
    call witness from _call_witness_2
    t "yes of course."
    #Kurain Genealogy; Ace Attorney Meets Orchestra
    play music "audio/testify.mp3"
    jump testimony
