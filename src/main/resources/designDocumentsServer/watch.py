import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
# os.system("python createDesignDocs.py")
class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        # print("Got it!")
        os.system("python createDesignDocs.py")
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, path='markdowns/', recursive=False)
observer.start()
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
