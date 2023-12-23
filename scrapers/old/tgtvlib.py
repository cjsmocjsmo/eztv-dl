#!/usr/bin/python3
import re
from bs4 import BeautifulSoup

ML = re.compile("magnet")
TEN = re.compile("1080p")
SEV = re.compile("720p")

def search_for_new_episode(page, EP):
    linklist = []
    list1080p = []
    list720p = []
    soup = BeautifulSoup(page, 'html.parser')
    for link in soup.findAll("a"):
        # print("this is href: {}".format(link.get('href')))
        meta = link.get("href")
        if meta != None:
            if re.search(ML, meta) != None:
                if re.search(EP, meta) != None:
                    if re.search(TEN, meta) != None:
                        list1080p.append(meta)
                    elif re.search(SEV, meta) != None:
                        list720p.append(meta)
    linklist.append(list1080p)
    linklist.append(list720p)
    return linklist