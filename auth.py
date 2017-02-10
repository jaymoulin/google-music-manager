#!/usr/bin/python3

# Usage ./auth.py [path_to_oauth_cred_file=/root/oauth]

import sys
from gmusicapi import Musicmanager

if __name__ == "__main__":
    path=sys.argv[1] if len(sys.argv) > 1 else '/root/oauth'
    api = Musicmanager()
    if api.perform_oauth(path) == True:
        print("Logged successfully")
