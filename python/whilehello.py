import os
import time
import subprocess

if __name__ == '__main__':
    try:
        while True:
            print("PID: " + str(os.getpid()) + ": hello")
            time.sleep(1)
        print("PID: " + str(os.getpid()) + "kill hello")
    except KeyboardInterrupt:
        print("PID: " + str(os.getpid()) + "good bye.")
        pass