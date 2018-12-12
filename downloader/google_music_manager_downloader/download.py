#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import logging
import netifaces
import argparse
import os
from gmusicapi import Musicmanager

__DEFAULT_IFACE__ = netifaces.gateways()['default'][netifaces.AF_INET][1]
__DEFAULT_MAC__ = netifaces.ifaddresses(__DEFAULT_IFACE__)[netifaces.AF_LINK][0]['addr'].upper()


def download(
    directory: str = ".",
    oauth: str = os.environ['HOME'] + "/oauth",
    device_id: str = __DEFAULT_MAC__
) -> None:
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    logger.info("Init Daemon - Press Ctrl+C to quit")
    api = Musicmanager()
    if not api.login(oauth, device_id):
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
    parser.add_argument(
        "--oauth",
        '-a',
        default=os.environ['HOME'] + '/oauth',
        help="Path to oauth file (default: ~/oauth)"
    )
    parser.add_argument(
        "--device_id",
        '-i',
        default=__DEFAULT_MAC__,
        help="Uploader identification (should be an uppercase MAC address) (default: <current eth0 MAC address>)"
    )
    args = parser.parse_args()
    download(args.directory, oauth=args.oauth, device_id=args.device_id)


if __name__ == "__main__":
    main()
