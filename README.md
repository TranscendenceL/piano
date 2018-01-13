# windmill interface description 
A2A3 for sound senser
A6A7 for LED
56789 by default for motor
10 11 for bozzer
# Protocal
## music notes
1:do 
2:re
......
7:si
11:high do
12:high re
......
17:high si
21:low do
22:low re
......
27:low si
## dance action
41:open the fan
42:close the fan
43:open LED
44:close LED
45:vary the color of LED
46:stop 45
## some variables added
100:medium light of the LED
255:maximum light of the LED
0:minimum light of the LED
# test case
## sound senser
sdss.xml
function: print the rate of sound
## LED
led.xml
function: show the light turn on or not
## motor
mtr.xml
function: run the windmill
## bozzer
bzr.xml
function: play the sound
