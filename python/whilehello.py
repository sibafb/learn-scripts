import os
import time
import subprocess

if __name__ == '__main__':
    while True:
        print(str(os.getpid()) + ": hello")
        time.sleep(1)
    print(str(os.getpid()) + "kill hello")