#!/usr/bin/python3

# Usage ./auth.py [path_to_oauth_cred_file=/root/oauth]

import sys
from gmusicapi import Musicmanager

if __name__ == "__main__":
    api = Musicmanager()
    api.login(sys.argv[1]) if len(sys.argv) > 1 else '/root/oauth')