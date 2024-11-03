#!/usr/bin/python3

import re
from bs4 import BeautifulSoup

class Search:
    def __init__(self):
        self.TEN_P = re.compile("1080p")
        self.SEV_P = re.compile("720p")

    def ez_search_for_new_episode(self, page, title, regex):
        list1080p = []
        list720p = []
        soup = BeautifulSoup(page, 'html.parser')
        count = 0
        for link in soup.findAll("a"):
            count += 1
            meta = (link.get("title"), link.get('href'))
            if meta[0] != None:
                ltitle = meta[0].lower()
                if re.search(regex, ltitle) != None:
                    if re.search(self.TEN_P, ltitle) != None:
                        list1080p.append(meta)
                    elif re.search(self.SEV_P, ltitle) != None:
                        list720p.append(meta)
                    else:
                        pass
        return (list1080p, list720p)

    def ka_search_for_new_episode(self, page, title, episode):
        linklist = []
        list1080p = []
        list720p = []
        soup = BeautifulSoup(page, 'html.parser')
        count = 0
        for link in soup.findAll("a"):
            count += 1
            meta = (link.get("title"), link.get('href'))
            print("this is meta0 {}".format(meta[0]))
            print("this is meta1 {}".format(meta[1]))

            if meta[0] != None:
                if re.search(title, meta[1]) != None:
                    if re.search(episode, meta[1]) != None:
                        if re.search(self.TEN_P, meta[1]) != None:
                            list1080p.append(meta[1])
                        elif re.search(self.SEV_P, meta[1]) != None:
                            list720p.append(meta[1])
                        else:
                            pass
        return (list1080p, list720p)

    def x1337_search_for_new_episode(self, page, title, episode):
        linklist = []
        list1080p = []
        list720p = []
        soup = BeautifulSoup(page, 'html.parser')
        count = 0
        for link in soup.findAll("a", recursive=True):
            count += 1
            meta = (link.get("title"), link.get('href'))
            print(link)
            print("this is meta0 {}".format(meta[0]))
            print("this is meta1 {}".format(meta[1]))

        #     if meta[0] != None:
        #         if re.search(title, meta[1]) != None:
        #             if re.search(episode, meta[1]) != None:
        #                 if re.search(self.TEN_P, meta[1]) != None:
        #                     list1080p.append(meta[1])
        #                 elif re.search(self.SEV_P, meta[1]) != None:
        #                     list720p.append(meta[1])
        #                 else:
        #                     pass
        # return (list1080p, list720p)

