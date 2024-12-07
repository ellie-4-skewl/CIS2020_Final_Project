# CIS2020_Final_Project
Final Project
Resources
Tutorial

"Simon Says"

The original intent with this project was to create a functioning game of Simon where the player must memorize the pattern in which certain lights would come on, gradually increasing the difficulty by adding one more light flash to the puzzle. However, after some development, the game instead turned into being a more rudimentary version where all 4 lights will flash (one right after the other) and the player must then press each corresponding button after the full sequence is complete. As you'll see, however, this didn't quite go to plan either.

Materials

To recreate this project, you will need the following:
  * Raspberry Pi
  * Breadboard
  * Resistors
  * Buttons
  * LEDs

Step 1: Set up Pi



Step 2: Testing

During this step, the most import thing that we're looking at here is making sure that all of our physcal elements are working - that way we'll know in later steps that the code is faulty instead of the machine. 

You can use simple commands to manually check whether or not each 
```python
from gpiozero import Button

button = Button(2) #"2" is a placeholder here. Your button number should correspond to it's GPIO pin.

while True:
    if button.is_pressed:
        print("Button is pressed")
    else:
        print("Button is not pressed")
```

Step 3:

Step 4:
