Dotted Line Trajectory
======================  

In this activity, you will learn to change the tracking line from circle to dotted line.


<img src= "https://media.slid.es/uploads/1525749/images/10501308/aa2.gif" width = "480" height = "320">


Follow the given steps to complete this activity:

1. Draw the dotted line

* Open the `main.py` file.

* Remove the line to create a circle as trajectory.

    `cv2.circle(img,(xCords[i],yCords[i]),1,(0,0,255),2)`

* Check if i>0 and only then draw the line.

    `if (i > 0):`

* Draw line from `xCords[i], yCords[i]` to `(xChords[i-1], ychords[i-1])`.

    `cv2.line(img, (xCords[i], yCords[i]), (xCords[i-1],yCords[i-1]), (0, 0, 255), thickness=1)`


* Save and run the code to check the output.

