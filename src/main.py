import markupsafe
import subprocess
import shutil
import os

os.mkdir("testdir")
shutil.copy("src/noxfile.py", "testdir")
subprocess.run(["uv", "venv", ".venv"], cwd="./testdir")
subprocess.run(["uv", "pip", "install", "markupsafe"], cwd="./testdir")
subprocess.run(["nox", "-f", "noxfile.py"], cwd="./testdir")
shutil.rmtree("testdir")

print(markupsafe.escape("Main hello, <world>!"))
