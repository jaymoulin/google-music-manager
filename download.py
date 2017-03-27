#!/usr/bin/python3

# Usage ./download.py [music_folder=.] [path_to_oauth_cred_file=/root/oauth]

import sys
import time
import logging
import os.path
from gmusicapi import Musicmanager

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    logger.info("Init Daemon - Press Ctrl+C to quit")
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    oauth = sys.argv[2] if len(sys.argv) > 2 else '/root/oauth'
    api = Musicmanager()
    if api.login(oauth) != False:
        for song in api.get_uploaded_songs():
            folder_path = os.path.join(path, song['album_artist'], song['album'])
            file_path = os.path.join(folder_path, '%d - %s.mp3' % (song['track_number'], song['title'].replace('/', '_')))
            file_path = file_path.encode('utf8')
            folder_path = folder_path.encode('utf8')
            if os.path.exists(file_path) == False:
                filename, audio = api.download_song(song['id'])
                if os.path.exists(folder_path) == False:
                    os.makedirs(folder_path)
                with open(file_path, 'wb') as f:
                    f.write(audio)
    else:
        print("Error with oauth credentials")
