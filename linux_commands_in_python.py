# import os


# cmd_1 = "ls -la"

# os.system(cmd_1)

import subprocess

proc = subprocess.Popen(["cat", "/etc/services"], stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()
print(out)