#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

__version__ = '0.7.1'

setup(
    name='google_music_manager_auth',
    python_requires=">=3",
    version=__version__,
    packages=find_packages(),
    author="Jay MOULIN",
    author_email="jaymoulin@gmail.com",
    description="Google MusicManager package to manage your music library to Google Music - Auth module",
    long_description=open('google_music_manager_auth/README.rst').read(),
    install_requires=["gmusicapi"],
    include_package_data=True,
    url='http://github.com/jaymoulin/google-music-manager/',
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
            'google-music-auth = google_music_manager_auth.auth:main',
        ],
    },
    license="MIT",
)
