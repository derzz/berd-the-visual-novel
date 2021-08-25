#All scenes
##Courthouse scene, not crazy
label courtcalm:
    scene bg court
    show crownberd:
        xzoom -1.0
        zoom 0.5
        xalign 0.3 yalign 0.55
    show lawyerberd:
        xalign 0.7 yalign 0.55
        zoom 0.5
    show judgeberd:
        zoom 0.5
        xalign 0.5 yalign 0.25
    return

label courtmove:
    scene bg court with fade
    show crownberd:
        xzoom -1.0
        zoom 0.5
        xalign 0.3 yalign 0.55
    show crownberd:
        linear 1.0 rotate 360
        linear 1.0 rotate 0
        repeat
    show lawyerberd:
        xalign 0.7 yalign 0.55
        zoom 0.5
    show lawyerberd:
        linear 1.0 yzoom -1.0
        linear 1.0 yzoom 1.0
        repeat
    show judgeberd:
        zoom 0.5
        xalign 0.5 yalign 0.25
    show judgeberd:
        linear 1.0 xzoom -1.0
        linear 1.0 xzoom 1.0
        repeat
    return

##Courthouse scene, all go crazy
label courtcrazy:
    scene bg court
    show crownberd:
        xzoom -1.0
        zoom 0.5
        xalign 0.3 yalign 0.55
    show crownberd:
        linear .1 rotate 360
        linear .1 rotate 0
        repeat
    show lawyerberd:
        xalign 0.7 yalign 0.55
        zoom 0.5
    show lawyerberd:
        linear .1 yzoom -1.0
        linear .1 yzoom 1.0
        repeat
    show judgeberd:
        zoom 0.5
        xalign 0.5 yalign 0.25
    show judgeberd:
        linear 0.1 xzoom -1.0
        linear .1 xzoom 1.0
        repeat
    return
#People Scenes
##Judge Scene
label judge:
    scene bg jbench
    show judgeberd:
        yalign 0.35 xalign 0.5
        zoom 1.6
    return

label defense:
    scene bg defense
    show lawyerberd:
        xzoom -1.0
        yalign .9 xalign 0.5
        zoom 2.0
    return
label crown:
    scene bg prosecution
    show crownberd:
        yalign 0.3 xalign 0.5
        zoom 2.0
    return
label witness:
    scene bg witness
    show terroristberd:
        yalign 1.2 xalign .5
        zoom 1.6
    return

label terroristB:
    scene bg witness
    show terroristberd off:
        yalign 1.2 xalign .5
        zoom 1.6
    return

label witnessF:
    scene bg witness
    show daberd:
        yalign 1.2 xalign .5
        zoom 1.6
    return
