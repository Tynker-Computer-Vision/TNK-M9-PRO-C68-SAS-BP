Detect the Goal
In this activity, you will learn to detect the goal when the basketball touches the basket.

<img src= "https://media.slid.es/uploads/1525749/images/10493775/SA3.gif" width = "480" height = "320">

Follow the given steps to complete this activity:

1. ### Detect the basket
* Open the main.py file.

* Import the math library.

    `import math`

* Draw circles using CENTER POINTS for goalpost and basketball.

    `cv2.circle(img,(c1,c2),2,(0,0,255),5)`

    `cv2.circle(img,(int(goalX),int(goalY)),2,(0,255,0),3)`

* Calculate the distance between the ball and basket.

    `dist = math.sqrt(((c1-goalX)**2) + (c2-goalY)**2)`

* Display the Goal message if the distance between the ball and the basket is less than or equal to `20`.

    `if(dist<=20):`

    `cv2.putText(img,"Goal",(300,90),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2)`


* Save and run the code to check the output.
