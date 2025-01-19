import os
import re
import shutil

path_root = os.path.join("Y:","/bittorrent")

rx = "^([^(]+\\([0-9]+\\)).*"

for entry in os.listdir(path_root):
    entry_path = os.path.join(path_root,entry)
    if not os.path.isdir(entry_path): continue
    m = re.search(pattern=rx, string=entry)
    if not m: continue

    for file in os.listdir(entry_path):
        file_path = os.path.join(entry_path,file)
        if file_path.endswith(".jpg") or file_path.endswith(".txt"):
            print(f"DEL {file_path}")
            os.remove(file_path)
        if os.path.isdir(file_path) and file == "Subs":
            print(f"DEL {file_path}")
            shutil.rmtree(file_path)

    entry_path_mv = os.path.join(path_root,m.group(1))
    print(f"RENAME \"{entry_path}\" -> \"{entry_path_mv}\"")
    shutil.move(entry_path, entry_path_mv)