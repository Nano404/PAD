#!/usr/bin/python3
import cgitb
cgitb.enable()
# Print necessary headers.
print("Content-Type: text/html")
print()
import cgitb
import os
read_logs = "cat /var/log/apache2/access.log"
log_result = os.system(read_logs)
print(os.system(read_logs))
