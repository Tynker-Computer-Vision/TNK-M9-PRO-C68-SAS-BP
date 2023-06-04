Change the Color of the Bounding Box
==========================================

In this activity, you will learn to change the color of the bounding box with respect to the distance between the ball and the goal.


<img src= "https://media.slid.es/uploads/1525749/images/10501309/aa1.gif" width = "480" height = "320">


Follow the given steps to complete this activity:

1. Set the color of the ball

* Declare a variable `ballBoxColor` and store the value `(255, 0, 255)` in it.

    `ballBoxColor = (255, 0, 255)`

* Access `ballBoxColor` as global variable inside the `drawBox()` function.

    `global ballBoxColor`

* Use `ballBoxColor` to color the rectangle. 

    `cv2.rectangle(img, (x, y), ((x+w), (y+h)), ballBoxColor, 3, 1)`

* Access `ballBoxColor` as global variable inside the `goalTrack()` function.

    `global ballBoxColor`
                      
* Set GBR value in ballBoxColor based on dist variable
    `ballBoxColor = (0, 20000/dist,dist)`                      

* Save and run the code to check the output.

