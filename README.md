# CIS2020_Final_Project
Final Project
Resources
Tutorial

"Simon Says"
-

The original intent with this project was to create a functioning game of Simon where the player must memorize the pattern in which certain lights would come on, gradually increasing the difficulty by adding one more light flash to the puzzle. However, after some development, the game instead turned into being a more rudimentary version where all 4 lights will flash (one right after the other) and the player must then press each corresponding button after the full sequence is complete. As you'll see, however, this didn't quite go to plan either.

Materials
-

To recreate this project, you will need the following:
  * Raspberry Pi
  * Breadboard
  * Resistors
  * Buttons
  * LEDs

Step 1: Set up Pi
-

Set up your Pi and breadboard like in the screenshots posted.


Step 2: Testing
-

During this step, the most import thing that we're looking at here is making sure that all of our physcal elements are working - that way we'll know in later steps that the code is faulty instead of the machine. 

You can use simple commands to manually check whether or not each button is working.
```python
from gpiozero import Button

button = Button(2) #"2" is a placeholder here. Your button number should correspond to it's GPIO pin.

while True:
    if button.is_pressed:
        print("Button is pressed")
    else:
        print("Button is not pressed")
```
After this, simply test each LED lighting up due to a button press.

Step 3: Label leds and buttons
-

This step will be crucial for our next step! 
```
leds = [LED(26), LED(5), LED(27), LED(4)]
buttons = [Button(13), Button(6), Button(22), Button(17)]
```

Step 4: Create sequences
-

Next, you will use a sequence to determine a random sequence in which the lights will flash.

```
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
```
Step 5: Second Sequence
-

Next, you must create a second sequence for your buttons. We will use this to "link up" which LED corresponds to which button.

```
sequence2 = []

def output(button):
    print("Button Pressed", buttons.index(button))
    sequence2.append(buttons.index(button))
```

Step 6: ???
-

After that, we tried implementing an elseif statement to make sure that the program would know if the player pressed the right button for the right LED. However, we ran into the issue where the button would instead simply wait until the correct button was pressed and would not react to the players putting in an incorrect pattern.

```
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
```


This is about as far as we got, thank you for checking out this project!
