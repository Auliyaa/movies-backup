import urllib.parse
import urllib.request
import requests
from bs4 import BeautifulSoup
import os
import shutil

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}

def get_link(req: str):
    arg = urllib.parse.quote_plus(req)
    uri = f"https://yts.mx/browse-movies/{arg}/all/all/0/latest/0/all"

    response = requests.get(uri, headers=headers)

    soup = BeautifulSoup(response.text, 'html.parser')
    movie_links = soup.find_all('a', class_='browse-movie-link')
    href_values = [link['href'] for link in movie_links]

    response = requests.get(href_values[0], headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    torrent_links = soup.find_all('a')
    
    href_2160p_web = None
    href_2160p_bluray = None
    href_1080p_web = None
    href_1080p_bluray = None
    href_720p_web = None
    href_720p_bluray = None

    for link in torrent_links:
        title = link.get("title")
        href = link.get("href")
        if not title or not href:
            continue
        if "2160p" in title and not "bluray" in str(title).lower():
            href_2160p_web = href
        if "2160p" in title and "bluray" in str(title).lower():
            href_2160p_bluray = href
        if "1080p" in title and not "bluray" in str(title).lower():
            href_1080p_web = href
        if "1080p" in title and "bluray" in str(title).lower():
            href_1080p_bluray = href
        if "720p" in title and not "bluray" in str(title).lower():
            href_720p_web = href
        if "720p" in title and "bluray" in str(title).lower():
            href_720p_bluray = href

    if href_2160p_bluray:
        return "2160p.bluray",href_2160p_bluray
    if href_2160p_web:
        return "2160p.web",href_2160p_web
    if href_1080p_bluray:
        return "1080p.bluray",href_1080p_bluray
    if href_1080p_web:
        return "1080p.web",href_1080p_web
    if href_720p_bluray:
        return "720p.bluray",href_720p_bluray
    if href_720p_web:
        return "720p.web",href_720p_web
    return None,None


failed = []

def margoulin(title: str):
    try:
        quality,uri = get_link(title)
        if not uri:
            print(f"Failed: {title}: Not found")
            failed.append(title)
            return
        rsp = requests.get(uri, headers=headers)
        with open(f"./torrents/{title}.{quality}.torrent", "wb") as fd:
            fd.write(rsp.content)
        print(f"OK: {title}")
    except Exception as e:
        print(f"Failed: {title}: {e}")
        failed.append(title)


if (os.path.isdir("./torrents")):
    shutil.rmtree("./torrents")
if (os.path.isfile("./failed.txt")):
    os.remove("./failed.txt")
os.mkdir("./torrents")

margoulin_root = "Z:/Movies"
for item in os.listdir(margoulin_root):
    margoulin(item)

with open("./failed.txt", "w") as fd:
    for f in failed:
        fd.write(f)
        fd.write("\n")