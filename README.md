Google Music Manager - Python Daemon
====================================

[![latest release](https://img.shields.io/github/release/jaymoulin/google-music-manager.svg "latest release")](http://github.com/jaymoulin/google-music-manager/releases)
[![Bitcoin donation](https://github.com/jaymoulin/jaymoulin.github.io/raw/master/btc.png "Bitcoin donation")](https://m.freewallet.org/id/374ad82e/btc)
[![Litecoin donation](https://github.com/jaymoulin/jaymoulin.github.io/raw/master/ltc.png "Litecoin donation")](https://m.freewallet.org/id/374ad82e/ltc)
[![PayPal donation](https://github.com/jaymoulin/jaymoulin.github.io/raw/master/ppl.png "PayPal donation")](https://www.paypal.me/jaymoulin)
[![Beerpay donation](https://beerpay.io/jaymoulin/google-music-manager/badge.svg "Beerpay donation")](https://beerpay.io/jaymoulin/google-music-manager)


This program will replace former Google MusicManager to upload your music library to Google Music

This work is based upon [Simon Weber's Google Music API](https://github.com/simon-weber/gmusicapi).

Installation
------------

Avconv is needed to convert some of your files due to Google's MP3 constraint
also, this program needs `watchdog`, `gmusicapi`, `netifaces` and `bs4` Python libraries to work. 

```
apt-get install python3-pip libav-tools build-essential
pip3 install watchdog gmusicapi bs4 netifaces
```

Once installed, You have to authenticate to Google Music via the `auth.py` script 

```
# Usage ./auth.py [path_to_oauth_cred_file=~/oauth]
```

If first parameter is not defined, the script will try to store/load your oauth credentials through the `~/oauth` file.

Then follow prompted instructions.

You will be asked to go to a Google URL to allow the connection:

```
Visit the following url:
 https://accounts.google.com/o/oauth2/v2/auth?client_id=XXXXXXXXXXX.apps.googleusercontent.com&access_type=offline&scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fmusicmanager&response_type=code&redirect_uri=urn%3Aietf%3Awg%3Aoauth%3A2.0%3Aoob
Follow the prompts, then paste the auth code here and hit enter: 
```

Usage
-----

## Uploader

This program will scan a given directory for new elements to upload them to Google Music.
First, launch the daemon to watch a directory new inputs.

It will *NOT* upload already existing files, *ONLY* new files while the daemon is running. (Please contribute if you want this to change)

```
usage: uploader-daemon.py [-h] [--directory DIRECTORY] [--oauth OAUTH] [-r]
                          [--uploader_id UPLOADER_ID]

optional arguments:
  -h, --help            show this help message and exit
  --directory DIRECTORY, -d DIRECTORY
                        Music Folder to upload from (default: .)
  --oauth OAUTH, -a OAUTH
                        Path to oauth file (default: ~/oauth)
  -r, --remove          Remove files if present (default: False)
  --uploader_id UPLOADER_ID, -u UPLOADER_ID
                        Uploader identification (should be an uppercase MAC
                        address) (default: <current eth0 MAC address>)
```

## Downloader

This program will download all your uploaded musics from Google Music to a given directory.

```
usage: download.py [-h] [--directory DIRECTORY] [--oauth OAUTH]

optional arguments:
  -h, --help            show this help message and exit
  --directory DIRECTORY, -d DIRECTORY
                        Music Folder to download to (default: .)
  --oauth OAUTH, -a OAUTH
                        Path to oauth file (default: ~/oauth)
```

About
=====

Requirements
-----------

Google Music Uploader works with Python 3 or above.
It requires [Simon Weber's Google Music API](https://github.com/simon-weber/gmusicapi) and [Watchdog](https://pypi.python.org/pypi/watchdog).

Submitting bugs and feature requests
------------------------------------

Bugs and feature request are tracked on GitHub

Author
------

Jay MOULIN jaymoulin@gmail.com See also the list of contributors which participated in this program.

License
-------

Google Music Uploader is licensed under the MIT License
