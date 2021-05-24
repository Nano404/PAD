#!/usr/bin/python3
print("Content-Type: text/html")
print()
import cgitb; cgitb.enable(display=1, logdir=None, context=5, format="html")
import os
restart = "/etc/init.d/apache2 reload > /dev/null"
os.system(restart)
print("restart")