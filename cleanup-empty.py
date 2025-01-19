import os
import shutil

for entry in os.listdir(os.path.join("Y:","bittorrent")):
    p = os.path.join("Y:","bittorrent",entry)
    if os.path.isdir(p) and len(os.listdir(p)) == 0:
        print(entry)