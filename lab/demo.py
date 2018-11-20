#!/usr/bin/env python3

# demo.py: extract frames from a video file, converts them to greyscale, and displays them in sequence

from threading import Thread

import utils
from custom_queue import CustomQueue

filename = "clip.mp4"  # filename of video to load
buff_size = 10  # bound queues to 10 frames

extract_grey_queue = CustomQueue(buff_size)  # queue for extract and greyscale threads
grey_display_queue = CustomQueue(buff_size)  # queue for greyscale and display threads

# threads for each function
extract_thread = Thread(target=utils.extract_frames, args=(filename, extract_grey_queue))
greyscale_thread = Thread(target=utils.convert_to_greyscale, args=(extract_grey_queue, grey_display_queue))
display_thread = Thread(target=utils.display_frames, args=(grey_display_queue,))

# producer-consumer: extract_thread --produce--> extract_grey_queue --consume--> greyscale_thread
# producer-consumer: greyscale_thread --produce--> grey_display_queue --consume--> display_thread

extract_thread.start()
greyscale_thread.start()
display_thread.start()
