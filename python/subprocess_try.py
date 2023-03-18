import os
import subprocess
import time
import signal 

if __name__ == '__main__':

    print("PID: " + str(os.getpid()) + ": start hello")
    p = subprocess.Popen('exec python whilehello.py', shell=True)
    time.sleep(5)
    p.kill()
    p.wait()
    print("PID: " + str(os.getpid()) + ": kill process") 
    # $ python subprocess_try.py 
    # 2926273: start hello
    # 2926274: hello
    # 2926274: hello
    # 2926274: hello
    # 2926274: hello
    # 2926274: hello
    # 2926273: kill process

    # signal 非同期イベントにハンドラを設定する
    # https://docs.python.org/ja/3/library/signal.html
    print("PID: " + str(os.getpid()) + ": start hello")
    pr = subprocess.Popen('exec python whilehello.py', shell=True)
    time.sleep(5)

    pr.send_signal(signal.SIGINT)
    pr.wait()
    print("PID: " + str(os.getpid()) + ": kill process") 
    # 3424410: start hello
    # 3424434: hello
    # 3424434: hello
    # 3424434: hello
    # 3424434: hello
    # 3424434: hello
    # good bye.
    # 3424410: kill process