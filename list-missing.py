import os

for entry in os.listdir("D:/dev/NAS/Movies and Shows/torrents"):
    title = entry.split(".")[0]
    if not os.path.exists(os.path.join("Z:","Movies",title)):
        print(title)
