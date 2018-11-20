# utils.py: functions (adapted from Pruitt, David) to extract, convert, and display frames

import cv2
import numpy as np


# extract frames from file into output buffer
def extract_frames(file_name, output_buffer):
    frame_count = 0
    vidcap = cv2.VideoCapture(file_name)  # capture video
    while True:
        read, image = vidcap.read()  # grab frame
        if not read:  # break at end of video
            break
        print("Reading frame", frame_count)
        frame_count += 1
        read, jpg_encoded = cv2.imencode('.jpg', image)  # encode image
        output_buffer.put(jpg_encoded)  # add frame to buffer
    output_buffer.put(None)  # enqueue "end of file"
    print("Frame extraction complete")


# convert frames from color to greyscale, from input buffer into output buffer
def convert_to_greyscale(input_buffer, output_buffer):
    frame_count = 0
    while True:
        jpg_encoded = input_buffer.get()
        if jpg_encoded is None:  # break on "end of file"
            break
        jpg_encoded = np.asarray(bytearray(jpg_encoded), dtype=np.uint8)  # convert frame to a numpy array
        image = cv2.imdecode(jpg_encoded, cv2.IMREAD_UNCHANGED)  # decode image
        print("Converting frame", frame_count)
        frame_count += 1
        image_grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # convert image to greyscale
        success, jpg_encoded = cv2.imencode('.jpg', image_grey)  # encode image
        output_buffer.put(jpg_encoded)  # add frame to buffer
    output_buffer.put(None)  # enqueue "end of file"
    print("Greyscale conversion complete")


# display frames from input buffer
def display_frames(input_buffer):
    frame_count = 0
    while True:
        jpg_encoded = input_buffer.get()
        if jpg_encoded is None:  # break on "end of file"
            break
        jpg_encoded = np.asarray(bytearray(jpg_encoded), dtype=np.uint8)  # convert frame to a numpy array
        image = cv2.imdecode(jpg_encoded, cv2.IMREAD_UNCHANGED)  # decode image
        print("Displaying frame", frame_count)
        frame_count += 1
        cv2.imshow("Video", image)  # display image in a window called "Video"
        if cv2.waitKey(42) and 0xFF == ord("q"):  # wait 42 ms
            break
    print("Finished displaying all frames")
    cv2.destroyAllWindows()  # cleanup the windows
