#!/usr/bin/python3
# Print necessary headers.
print("Content-Type: text/html")
print()
import cgitb
import cgi
import os
cgitb.enable()
ip = cgi.escape(os.environ["REMOTE_ADDR"])