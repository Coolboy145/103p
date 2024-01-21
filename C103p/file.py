import sys
import time
import random

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# from_dir = "ENTER THE PATH OF DOWNLOAD FOLDER (USE " / ") in VSC"
# to_dir = "ENTER THE PATH OF DESTINATION FOLDER(USE " / ") in VSC"

from_dir = "c:/Users/barto/OneDrive/Desktop"
to_dir = "C:/Users/barto/OneDrive/Desktop/C103test"

dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}

# Event Hanlder Class

class FileMovementHandler(FileSystemEventHandler):

    def on_created(self, event):
        print(f"Hey,{event.scr_path} has been created!")
    
    def on_deleted(self, event):
        print(f"Ooops! Someone deleted {event.scr_path}!")

    def on_moved(self, event):
        print(f"Hey,{event.scr_path} has been moved or created!")

    def on_modified(self, event):
        print(f"Hey,{event.scr_path} has been modified!")


# Initialize Event Handler Class
event_handler = FileMovementHandler()


# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)


# Start the Observer
observer.start()

try:

  while True:
    time.sleep(2)
    print("running...")
except KeyboardInterrupt:
        print("stopped")
        observer.stop()

    