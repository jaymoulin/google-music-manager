#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Usage ./auth.py [path_to_oauth_cred_file=~/oauth]

import sys
from gmusicapi import Musicmanager

__all__ = ['auth']


def auth(auth_file='~/oauth'):
    api = Musicmanager()
    if api.perform_oauth(auth_file):
        print("Logged successfully")


def main():
    auth(sys.argv[1] if len(sys.argv) > 1 else '~/oauth')


if __name__ == "__main__":
    main()
