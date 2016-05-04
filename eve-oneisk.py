#! python3

import os
import re
import sys
import glob
import time
import logging
import pyperclip
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Directory
dir = '/home/cgar/Documents/EVE/logs/Marketlogs/'

class MyHandler(FileSystemEventHandler):

    def on_modified(self, event):
        # Get the last imported file based on modified/creation date.
        newest = max(glob.iglob('/home/cgar/Documents/EVE/logs/Marketlogs/*'), key=os.path.getctime)

        # Open and read the latest file in read mode.
        content = open(newest, 'r')
        content_read = content.read()

        # Get the first value and substract one isk.
        regex = re.compile(r'\d+.\d+')
        result = regex.search(content_read)
        if result:
            value = result.group()
            value = float(value)
            value = value - .01

        pyperclip.copy(str(value))


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, dir)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
