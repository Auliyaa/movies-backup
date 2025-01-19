import yts
import os
import shutil

yts.init_folders()

failed = []
data_root = "Z:/Movies"

for item in os.listdir(data_root):
    if not yts.yts_download(item):
        failed.append(item)

for item in os.listdir("Z:/TV Shows"):
    failed.append(item)

with open("./failed.txt", "w") as fd:
    for f in failed:
        fd.write(f)
        fd.write("\n")