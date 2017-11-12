#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='googlemusicmanager',
    python_requires=">=3",
    version='0.6.0',
    packages=find_packages(),
    package_dir={'googlemusicmanager': 'lib'},
    author="Jay MOULIN",
    author_email="jaymoulin@gmail.com",
    description="This program will replace former Google MusicManager to upload your music library to Google Music",
    long_description=open('README.md').read(),
    install_requires=["watchdog", "gmusicapi", "bs4", "netifaces"],
    include_package_data=True,
    url='http://github.com/jaymoulin/google-music-manager',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Communications :: File Sharing",
        "Topic :: Artistic Software",
        "Topic :: Internet :: File Transfer Protocol (FTP)",
        "Topic :: Home Automation",
        "Topic :: Internet",
        "Topic :: Multimedia :: Sound/Audio",
    ],
    entry_points={
        'console_scripts': [
            'google-music-auth = googlemusicmanager.auth:main',
            'google-music-download = googlemusicmanager.download:main',
            'google-music-upload = googlemusicmanager.uploader_daemon:main',
        ],
    },
    license="MIT",
)
