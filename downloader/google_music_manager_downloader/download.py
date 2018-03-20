#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, time, logging, os.path, argparse, os
from gmusicapi import Musicmanager

__all__ = ['download']


def download(directory=".", oauth=os.environ['HOME'] + "/oauth"):
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    logger.info("Init Daemon - Press Ctrl+C to quit")
    api = Musicmanager()
    if not api.login(oauth):
        print("Error with oauth credentials")
        sys.exit(1)

    for song in api.get_uploaded_songs():
        folder_path = os.path.join(directory, song['album_artist'], song['album'])
        file_path = os.path.join(folder_path, '%d - %s.mp3' % (song['track_number'], song['title'].replace('/', '_')))
        file_path = file_path.encode('utf8')
        folder_path = folder_path.encode('utf8')
        if not os.path.exists(file_path):
            filename, audio = api.download_song(song['id'])
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            with open(file_path, 'wb') as f:
                f.write(audio)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--directory", '-d', default='.', help="Music Folder to download to (default: .)")
    parser.add_argument("--oauth", '-a', default=os.environ['HOME'] + '/oauth', help="Path to oauth file (default: ~/oauth)")
    args = parser.parse_args()
    download(args.directory, args.oauth)


if __name__ == "__main__":
    main()
