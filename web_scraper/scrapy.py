#! /usr/bin/python3
import webbrowser,sys

webbrowser.open('http://google.com')
if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
    print(address)
