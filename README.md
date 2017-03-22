Google Music Uploader - Python Daemon
=====================================

This program will replace former Google MusicManager to upload your music library to Google Music

This work is based upon [Simon Weber's Google Music API](https://github.com/simon-weber/gmusicapi).

Installation
------------

Avconv is needed to convert some of your files due to Google's MP3 constraint
also, this program needs `watchdog`, `gmusicapi` and `bs4` Python libraries to work. 

```
apt-get install python3-pip libav-tools build-essential
pip3 install watchdog gmusicapi bs4
```

Once installed, You have to authenticate to Google Music via the `auth.py` script 

```
# Usage ./auth.py [path_to_oauth_cred_file=/root/oauth]
```

If first parameter is not defined, the script will try to store/load your oauth credentials through the `/root/oauth` file.

It's suggested to use your own user to do so:
```
./auth.py ~/oauth
```
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
# Usage ./uploader-daemon.py [music_folder=.] [path_to_oauth_cred_file=/root/oauth]
```

Pass the first parameter to specify which directory to watch (recursively)
Pass the second parameter to specify the oauth file to use (created by `auth.py`)

## Downloader

This program will download all your uploaded musics from Google Music to a given directory.

```
# Usage ./download.py [music_folder=.] [path_to_oauth_cred_file=/root/oauth]
```

Pass the first parameter to specify which directory to download to
Pass the second parameter to specify the oauth file to use (created by `auth.py`)

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