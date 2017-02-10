#!/usr/bin/python3

# Usage ./daemon.py [music_folder=.] [path_to_oauth_cred_file=/root/oauth]

import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from gmusicapi import Musicmanager

class MusicToUpload(FileSystemEventHandler):
    def on_created(self,event):
        self.logger.info("Uploading "+event.src_path)
        self.api.upload(event.src_path, True)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    logger.info("Init Daemon - Press Ctrl+C to quit")
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    oauth = sys.argv[2] if len(sys.argv) > 2 else '/root/oauth'
    api = Musicmanager()
    event_handler = MusicToUpload()
    event_handler.api = api
    event_handler.logger = logger
    if api.login(oauth) != False:
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