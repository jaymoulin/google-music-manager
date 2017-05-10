#!/usr/bin/python3

# Usage ./uploader-daemon.py [music_folder=.] [path_to_oauth_cred_file=/root/oauth]

import sys
import time
import logging
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from gmusicapi import Musicmanager

class MusicToUpload(FileSystemEventHandler):
    def on_created(self,event):
        self.logger.info("Detected "+event.src_path)
        files = event.src_path
        if os.path.isdir(event.src_path) == True:
            files = [f for f in os.listdir(event.src_path) if os.path.isfile(os.path.join(event.src_path, f))]
        self.logger.info("Uploading...")
        self.api.upload(files, True)
        if self.willDelete == True:
            os.remove(event.src_path)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    logger.info("Init Daemon - Press Ctrl+C to quit")
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    oauth = sys.argv[2] if len(sys.argv) > 2 else '/root/oauth'
    willDelete = True if len(sys.argv) > 3 else False
    api = Musicmanager()
    event_handler = MusicToUpload()
    event_handler.api = api
    event_handler.willDelete = willDelete
    event_handler.logger = logger
    if api.login(oauth) != False:
        if willDelete == True:
            files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
            logger.info("Uploading...")
            api.upload(files, True)
            for f in files:
                logger.info("Deleting "+f)
                os.remove(f)
        observer = Observer()
        observer.schedule(event_handler, path, recursive=True)
        observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()
    else:
        print("Error with oauth credentials")
