# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 16:58:43 2019

@author: vchan
"""

# import libraries
import cv2
import face_recognition
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-o","--outpout", type=str,
                    help='Arrêter Le Wabna Svp ')
args = parser.parse_args()
# Get a reference to webcam 
video_capture = cv2.VideoCapture(0)

# Initialize variables
face_locations = []
count=0
while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_frame = frame[:, :, ::-1]

    # Find all the faces in the current frame of video
    face_locations = face_recognition.face_locations(rgb_frame)

    # Display the results
    for top, right, bottom, left in face_locations:
        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        count += 1
        # Save the captured image into the datasets folder
        cv2.imwrite(str(args.outpout)
+ "/data" + '.' + str(count) + ".jpg", frame)
    # Display the resulting image
    cv2.imshow('Video', frame)


    # Hit 'q' on the keyboard to quit!
    k = cv2.waitKey(100) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break
    #elif count >= 30: # Take 30 face sample and stop video
         #break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()
