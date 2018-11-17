#!/usr/bin/env python3

from threading import Thread
from queue import Queue
import utils

filename = "clip.mp4"  # filename of video to load
buff_size = 10  # bound queues to 10 frames

extract_grey_queue = Queue(buff_size)  # queue for extract and greyscale threads
grey_display_queue = Queue(buff_size)  # queue for greyscale and display threads

# threads for each function
extract_thread = Thread(target=utils.extract_frames, args=(filename, extract_grey_queue))
greyscale_thread = Thread(target=utils.convert_to_greyscale, args=(extract_grey_queue, grey_display_queue))
display_thread = Thread(target=utils.display_frames, args=(grey_display_queue,))

extract_thread.start()
greyscale_thread.start()
display_thread.start()
