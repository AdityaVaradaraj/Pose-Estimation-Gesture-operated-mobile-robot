from socket import timeout
import numpy as np
import math

def robot_input(keypoints):
    if len(keypoints) > 2:
        center = keypoints[0][0] # Shoulder Line - Center
        shoulder = keypoints[0][1] # Shoulder Line - Shoulder
        elbow = keypoints[2][1] # Shoulder Line - Elbow

        if (elbow[1] < shoulder[1]):
            return 'f'
        elif (abs(elbow[1] - shoulder[1])<90):
            return 'b'
        else:
            return 's'
    
    else:
        print('No person in the frame')
