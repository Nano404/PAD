import os
read_logs = "cat /var/log/apache2/access.log"
log_result = os.system(read_logs)
print(os.system(read_logs))
