import cv2
from pynput.keyboard import Controller

keyboard = Controller()
cap = cv2.VideoCapture(0)  # Or 1 if any external webcam or mobile cam is used
#### List of trackers ####
# tracker = cv2.TrackerMOSSE_create()
# tracker = cv2.TrackerCSRT_create()  
# tracker = cv2.TrackerBoosting_create()
# tracker = cv2.TrackerMIL_create()
# tracker = cv2.TrackerGOTURN_create()
# tracker = cv2.TrackerKCF_create()
# tracker = cv2.TrackerTLD_create() 
tracker = cv2.TrackerMedianFlow_create()  # (g)

count = 0
# The code for selection of ROI(bounding box)
reg, img = cap.read()  # reading the image, reg returns true or false whether the frame is redenred or not, img return the frame
img = cv2.flip(img, 1)  # flipping the image horizontally
bbox = cv2.selectROI("Tracking", img, None)  # getting the coordinates of the selected box
tracker.init(img, bbox) 

init_points = bbox 
ix, iy, iw, ih = int(init_points[0]), int(init_points[1]), int(init_points[2]), int(init_points[3])
center_x = ix + int(iw/2)  # getting the center of the bbox
center_y = iy + int(ih/2)  # getting the center of the bbox
tracking_circle_radius = 28  # radius of circle used for tracking


# The function is used for checking the direction of motion
def get_direction(tracker_dot_x, tracker_dot_y):
    global count
    if tracker_dot_x < center_x + tracking_circle_radius and tracker_dot_x > center_x - tracking_circle_radius and tracker_dot_y < center_y + tracking_circle_radius//2 and tracker_dot_y > center_y - tracking_circle_radius//2:
        count = 0
    if count < 1:
        if tracker_dot_y > (center_y + tracking_circle_radius//2):
            keyboard.press('s')
            keyboard.release('s')
            print('Movement : down')
            count+=1

        if tracker_dot_y < (center_y - tracking_circle_radius//2):
            keyboard.press('w')
            keyboard.release('w')
            print('Movement : up')
            count+=1
        
        if tracker_dot_x > (center_x + tracking_circle_radius):
            keyboard.press('d')
            keyboard.release('d')
            print('Movement : right')
            count+=1
        
        if tracker_dot_x < (center_x - tracking_circle_radius):
            keyboard.press('a')
            keyboard.release('a')
            print('Movement : left')
            count+=1


while True:
    timer = cv2.getTickCount()
    ret, img = cap.read()

    img = cv2.flip(img, 1)
    detection_circle_radius = 6
    x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])  # returns the live coordinates
    tracker_dot_x = x + w//2  # getting the live center coordinates
    tracker_dot_y = y + h//2  # getting the live center coordinates
    cv2.circle(img, (tracker_dot_x, tracker_dot_y), detection_circle_radius, (255, 0, 0), 2)  # The tracker circle
    cv2.circle(img, (center_x, center_y), tracking_circle_radius, (255, 255, 0), 2)  # The bounding circle
    get_direction(tracker_dot_x, tracker_dot_y)
    success, bbox = tracker.update(img)
    
    fps = str(int(cv2.getTickFrequency() / (cv2.getTickCount() - timer)))  # This returns the fps(frame per second)
    cv2.putText(img, fps, (20, 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    cv2.imshow('img', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
