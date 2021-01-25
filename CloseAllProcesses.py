import psutil
import os

for process in psutil.process_iter():
    if 'python' not in process.name() and 'obs' not in process.name():
        print(process.name())
        os.system("taskkill /im " + str(process.pid))
