#!/usr/local/bin/python3

# Usage ./uploader-daemon.py [music_folder=.] [path_to_oauth_cred_file=/root/oauth] [remove_file=True|false]

import sys
import time
import logging
import os
import glob
import netifaces
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from gmusicapi import Musicmanager


class MusicToUpload(FileSystemEventHandler):
    def on_created(self, event):
        self.logger.info("Detected new files!")
        if os.path.isdir(self.path):
            files = [file for file in glob.glob(self.path + '/**/*', recursive=True)]
            for file_path in files:
                if os.path.isfile(file_path):
                    self.logger.info("Uploading : " + file_path)
                    self.api.upload(file_path, True)
                    if self.willDelete:
                        os.remove(file_path)
        else:
            self.logger.info("Uploading : " + event.src_path)
            self.api.upload(event.src_path, True)
            if self.willDelete:
                os.remove(event.src_path)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    logger.info("Init Daemon - Press Ctrl+C to quit")
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    oauth = sys.argv[2] if len(sys.argv) > 2 else '/root/oauth'
    willDelete = True if len(sys.argv) > 3 else False
    uploaderId = sys.argv[4] if len(sys.argv) > 4 else netifaces.ifaddresses('eth0')[netifaces.AF_LINK][0]['addr'].upper()
    api = Musicmanager()
    event_handler = MusicToUpload()
    event_handler.api = api
    event_handler.path = path
    event_handler.willDelete = willDelete
    event_handler.logger = logger
    if api.login(oauth, uploaderId):
        if willDelete:
            files = [file for file in glob.glob(path + '/**/*', recursive=True)]
            for file_path in files:
                if os.path.isfile(file_path):
                    logger.info("Uploading : " + file_path)
                    api.upload(file_path, True)
                    os.remove(file_path)
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
