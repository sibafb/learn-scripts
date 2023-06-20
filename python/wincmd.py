import platform
import subprocess

if platform.system() != "Windows":
    assert False

subprocess.run("cmd.exe /c echo hello", cwd="./")