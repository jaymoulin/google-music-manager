#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, time, logging, os, glob, netifaces, argparse

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from gmusicapi import Musicmanager

__all__ = ['upload']


class MusicToUpload(FileSystemEventHandler):
    def on_created(self, event):
        self.logger.info("Detected new files!")
        if os.path.isdir(self.path):
            files = [file for file in glob.glob(self.path + '/**/*', recursive=True)]
            for file_path in files:
                if os.path.isfile(file_path):
                    self.logger.info("Uploading : " + file_path)
                    uploaded, matched, not_uploaded = self.api.upload(file_path, True)
                    if (uploaded or matched) and self.willDelete:
                        os.remove(file_path)
        else:
            self.logger.info("Uploading : " + event.src_path)
            uploaded, matched, not_uploaded = self.api.upload(event.src_path, True)
            if self.willDelete and (uploaded or matched):
                os.remove(event.src_path)


def upload(directory='.', oauth='~/oauth', remove=False,
           uploader_id=netifaces.ifaddresses('eth0')[netifaces.AF_LINK][0]['addr'].upper()):
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    logger.info("Init Daemon - Press Ctrl+C to quit")

    api = Musicmanager()
    event_handler = MusicToUpload()
    event_handler.api = api
    event_handler.path = directory
    event_handler.willDelete = remove
    event_handler.logger = logger
    if not api.login(oauth, uploader_id):
        print("Error with oauth credentials")
        sys.exit(1)
    if remove:
        files = [file for file in glob.glob(directory + '/**/*', recursive=True)]
        for file_path in files:
            if os.path.isfile(file_path):
                logger.info("Uploading : " + file_path)
                uploaded, matched, not_uploaded = api.upload(file_path, True)
                if uploaded or matched:
                    os.remove(file_path)
    observer = Observer()
    observer.schedule(event_handler, directory, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--directory", '-d', default='.', help="Music Folder to upload from (default: .)")
    parser.add_argument("--oauth", '-a', default='~/oauth', help="Path to oauth file (default: ~/oauth)")
    parser.add_argument("-r", "--remove", action='store_true', help="Remove files if present (default: False)")
    parser.add_argument("--uploader_id", '-u',
                        default=netifaces.ifaddresses('eth0')[netifaces.AF_LINK][0]['addr'].upper(),
                        help="Uploader identification (should be an uppercase MAC address) (default: <current eth0 MAC address>)")
    args = parser.parse_args()
    upload(args.directory, args.oauth, args.remove, args.uploader_id)
