from gpiozero import LED
from gpiozero import Button
from time import sleep
from signal import pause
from random import choice

sequence2 = []

def output(button):
    print("Button Pressed", buttons.index(button))
    sequence2.append(buttons.index(button))
    


#leds = LEDBoard(5, 6, 13, 19, 26)
leds = [LED(26), LED(5), LED(27), LED(4)]
buttons = [Button(13), Button(6), Button(22), Button(17)]

sequence= []

for i in range(4):
    #choose 1 led
    #turn led on
    #sleep
    #turn led off
    x = choice(leds)
    x.on()
    sleep(0.5)
    x.off()
    sleep(0.25)
    
    sequence.append(leds.index(x))
    

    
for i in sequence:
    #wait for button press
    #buttons[i].wait_for_press()
    #if buttons[i].is_pressed:
        #print("correct")
    if buttons[0].is_pressed and buttons[0] ==buttons[i]:
        print("correct")
    elif buttons[1].is_pressed and buttons[1] ==buttons[i]:
        print("correct")
    elif buttons[2].is_pressed and buttons[2] ==buttons[i]:
        print("correct")
    elif buttons[3].is_pressed and buttons[3] ==buttons[i]:
        print("correct")
    elif buttons[0].is_pressed and buttons[0] !=buttons[i]:
        print("incorrect")
    elif buttons[1].is_pressed and buttons[1] !=buttons[i]:
        print("incorrect")
    elif buttons[2].is_pressed and buttons[2] !=buttons[i]:
        print("incorrect")
    elif buttons[3].is_pressed and buttons[3] !=buttons[i]:
        print("incorrect")
        
 
    sleep(0.25)
    #if correct, print win
    #else print u lose


#choose random led and turn it on