#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

__version__ = '0.7.3'

setup(
    name='google_music_manager_downloader',
    python_requires=">=3",
    version=__version__,
    packages=find_packages(),
    author="Jay MOULIN",
    author_email="jaymoulin@gmail.com",
    description="Google MusicManager package to manage your music library to Google Music - Download module",
    long_description=open('README.rst').read(),
    install_requires=["google_music_manager_auth"],
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
            'google-music-download = google_music_manager_downloader.download:main',
        ],
    },
    license="MIT",
)
