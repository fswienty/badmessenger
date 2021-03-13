# badmessenger
A bad python messenger using google sheets

# What is this
This is a messenger connects to a google sheet and writes messages to it, together with a username chosen at startup and the current time. There are different rooms available (that you cannot change from within the program). I have no idea how to make the google drive api notify the program about changes to the sheet when someone else writes messange, so you'll have to manually pull messages from time to time. There's also the credentials to connect to the google sheet in this repo so there's nothing stopping you from taking these credentials and writing your own program thats completely screws over everything (pls don't).

# how2run
Run badmessenger.py to start or build an executable by running build.bat. Building requires pyinstaller. The build script is for windows, but should run fine on linux with some changes.
