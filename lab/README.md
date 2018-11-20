# Producer Consumer Lab

    python3 demo.py

* **demo.py**: extracts frames from a video file, converts them to greyscale, and displays them in sequence
 * Each function executes within their own thread
 * Threads execute concurrently and process all frames of the video exactly once
 * Frames are communicated between threads using consumer/producer idioms, with queues bounded at ten frames
* **utils.py**: includes functions for extracting, converting, and displaying frames
 * **extract_frames**: function for extracting frames
 * **convert\_to_greyscale**: function for converting frames to greyscale
 * **display_frames**: function for displaying frames 
* **custom_queue.py**: includes a custom queue class to explicitly add synchronization (instead of using Python's Queue)
