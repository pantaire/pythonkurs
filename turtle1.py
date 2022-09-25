from turtle import *
counter = 0
smallcounter = 0

while counter < 6:
    #linienfarbe: rot, füllfarbe: pink
    color('red', 'pink')
    begin_fill()
    forward(100)
    right(60)
    circle(50)
    end_fill()
    while smallcounter < 6:
        if smallcounter % 2:
            color('violet','lightblue')
        else:
            color('lightblue','violet')
        begin_fill()
        circle(30)
        circle(1,60)
        smallcounter += 1
        end_fill()
    # reset smallcounter für die nächste Runde
    smallcounter = 0
    counter += 1
end_fill()
    
    