import os
import yts

yts.init_folders()

root_folder = os.path.join("Y:", "watch")
for item in os.listdir(root_folder):
    if not item.endswith(".qbt_rejected"): continue
    title = item.split(".")[0]
    print(title)
    if not yts.yts_download(title=title):
        print(f"Failed: {title}")