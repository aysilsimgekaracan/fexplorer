import os
import subprocess

os.system("ls -l")

subprocess.call("cpu_util.sh")

subprocess.run('while true; do CPU_USAGE=$(top -b -n2 -p 1 | fgrep "Cpu(s)"); DATE=$(date "+%Y-%m-%d %H:%M:"); echo $DATE - $CPU_USAGE >> cpu_usage; echo Recorded; sleep 5s; done', shell=True)