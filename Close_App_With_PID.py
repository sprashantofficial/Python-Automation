import psutil
import os

for process in psutil.process_iter():
	if process.name() == "vlc.exe":
		os.system("taskkill /im " + str(process.pid))
