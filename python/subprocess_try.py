import os
import subprocess
import time

if __name__ == '__main__':

    print(str(os.getpid()) + ": start hello")
    p = subprocess.Popen('exec python whilehello.py', shell=True)
    time.sleep(5)
    p.kill()
    p.wait()
    print(str(os.getpid()) + ": kill process") 
    # $ python subprocess_try.py 
    # 2926273: start hello
    # 2926274: hello
    # 2926274: hello
    # 2926274: hello
    # 2926274: hello
    # 2926274: hello
    # 2926273: kill process