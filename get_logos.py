import urllib.request
import re

def get_logo(url):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        html = urllib.request.urlopen(req).read().decode('utf-8', errors='ignore')
        imgs = re.findall(r'<img[^>]+src=["\'](.*?)["\']', html, re.I)
        for src in imgs:
            if 'logo' in src.lower() or 'emblem' in src.lower() or 'gerb' in src.lower():
                if not src.startswith('http'):
                    src = url.rstrip('/') + '/' + src.lstrip('/')
                print(f"Found logo at {url}: {src}")
                return
        print(f"No explicit logo found at {url}. Top images: {imgs[:3]}")
    except Exception as e:
        print(f"Error {url}: {e}")

get_logo('http://school68.com.ua/')
get_logo('https://www.nvk-ok.org.ua/')
get_logo('http://school70inkr.dnepredu.com/')
