# Movement Games
Ever wondered about playing Subway Surfers with your body movements! I have made a program to synchronize basic body movements with movements in games like Subway Surfers, Temple Run, and any other games like these.
I have made the program in python using `OpenCV`(for video and movement detection) and `pynput`(for keyboard actions). 
## Prerequisites:
Follow the following instructions to run the code on your local machine.

### OpenCV:
Install this package using:

`pip install opencv-contrib-python`

In case the code shows any error try installing:

`pip install opencv-python`
### pynput:
Install this package using:

`pip install pynput`

### Installing the Game:
You can download the game from anywhere. There are a lot of options present but some of them might not work. I have used [Bluestacks](https://www.bluestacks.com/?utm_source=cdn3&utm_medium=waf) to run Subway Surfers.

### Using mobile camera as webcam(Optional)
Laptop cameras generally do not have good quality. So I have used [Droid Cam](https://droidcam.en.softonic.com/) to use my mobile camera as a webcam to get a better frame rate and accuracy. If you are doing this then make sure to change the argument of the `cv2.VideoCapture(0)` to `1` in line number 5.
# Running the Code:
After running the code, a window will open. Make a box-like structure keeping its midpoint on the part of the body to be detected(in my case: tip of nose). 

![Screenshot (187)](https://user-images.githubusercontent.com/67066785/107855213-0628c280-6e47-11eb-92a3-411a185257fc.png)

Press Enter and a small circle will appear around that part. Now if you move out of the circumference of the tracking circle, the terminal shows where are you moving. Now start playing the game and move as you want the player to move. HAPPY PLAY!
# Setting parameters:
You can always set some parameters according to your convenience:

>Tracking Circle(outer circle): `tracking_circle_radius` in line number 27

>Detection Circle(inner circle): `detection_circle_radius` in line number 66

>There are 8 trackers available. `MedianFlow` works best for me as it provides good accuracy as well as efficiency but you can try all of them which works best for you.  
## Points to Note:
>You can run the code on any IDE but my VSCode was giving some issue so I recommend using PyCharm.

>Try to keep the camera away from the light as reflection hampers the tracking.

>Try to avoid unnecessary movement as the detection circle might displace from its desired position.

>The program is not very efficient. It may take you time to get acquainted.
