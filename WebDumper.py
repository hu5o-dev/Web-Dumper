import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import threading
import time
import sys

def download_file(url, folder):
    local_filename = os.path.join(folder, os.path.basename(urlparse(url).path))
    response = requests.get(url, stream=True)
    with open(local_filename, 'wb') as file:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                file.write(chunk)
    return local_filename

def download_website(url, folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

    
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    html_file_path = os.path.join(folder, 'index.html')
    with open(html_file_path, 'wb') as file:
        file.write(response.content)

    
    assets = []
    for tag in soup.find_all(['link', 'script', 'img']):
        if tag.name == 'link' and tag.get('rel') == ['stylesheet']:
            href = tag.get('href')
            if href:
                asset_url = urljoin(url, href)
                assets.append(asset_url)
                download_file(asset_url, folder)
                tag['href'] = os.path.basename(asset_url)
        elif tag.name == 'script' and tag.get('src'):
            src = tag.get('src')
            asset_url = urljoin(url, src)
            assets.append(asset_url)
            download_file(asset_url, folder)
            tag['src'] = os.path.basename(asset_url)
        elif tag.name == 'img' and tag.get('src'):
            src = tag.get('src')
            asset_url = urljoin(url, src)
            assets.append(asset_url)
            download_file(asset_url, folder)
            tag['src'] = os.path.basename(asset_url)

    
    with open(html_file_path, 'w', encoding='utf-8') as file:
        file.write(str(soup))

def animate_download():
    """Display an animated 'Downloading...' message with dots."""
    dots = ['.', '..', '...']
    while True:
        for dot in dots:
            sys.stdout.write("\rDownloading" + dot)
            sys.stdout.flush()
            time.sleep(0.5)
            
            sys.stdout.write("\r" + " " * (len("Downloading" + dot)) + "\r")
            sys.stdout.flush()

def main():
    website_url = input("Enter the URL of the website to download: ")
    website_name = urlparse(website_url).hostname
    output_folder = f'{website_name}_download'

    
    animation_thread = threading.Thread(target=animate_download)
    animation_thread.daemon = True
    animation_thread.start()
    
    
    download_website(website_url, output_folder)
    
    
    sys.stdout.write("\rDownload complete!                \n")
    sys.stdout.flush()

if __name__ == "__main__":
    main()
