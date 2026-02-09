# Grandma2-telnet-python

### update 09-02-2026:

Added the version for python3 which I have been using for 2 years already and renamed the old versions in python2 to *_python2.py

### main

This are 2 simple and terbile writen scripts to control your grandma2 lighting desk with Linux Show Player with telnet

You use maserver to connect to your light desk

./maserver.py ip port user password

you can then use maclient to send your grandma2 commands to maserver and so to your ligt desk.

./maclient.py "Go 1.1 Cue 1"

servertelnet.py is for testing

It is poorly writen but it works in linux show player

I suggest putting the scripts in your bin folder if you want it to work in linux show player

### Dependencies

For python 3 version(I don't use the python 2 version anymore your on you own with that one)

- telnetlib

As telnetlib is removed in python 3.13 you will need python standard telnetlib.
You can find it here https://github.com/youknowone/python-deadlib or install it with your package manager

- socket
- sys
- time

Probaly already installed on your system 


