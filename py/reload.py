#!/usr/bin/python3
print("Content-type: text/html")
print()
import cgitb; cgitb.enable(display=1, logdir=None, context=5, format="html")
import os
#spreek voor zich reload de apache site
restart = "/etc/init.d/apache2 reload > /dev/null"
os.system(restart)
print("Apache reloading")