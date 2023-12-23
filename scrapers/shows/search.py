#!/usr/bin/python3

import re
from bs4 import BeautifulSoup

STARWARSVISIONS = re.compile(r"star wars visions")
STARWARSVISIONS1 = re.compile(r"star.wars.visions")
STARWARSVISIONS_SEA = "s03e01"
STARWARSVISIONS_SEA_REG = re.compile(STARWARSVISIONS_SEA)
STARWARSVISIONS_EZ_1 = "https://eztv.re/search/star-wars-visions"
STARWARSVISIONS_KA_1 = "https://kickasstorrents.to/usearch/star wars visions"
STARWARSVISIONS_KA_2 = "https://kickasstorrents.to/usearch/star wars visions/2"



STRANGENEWWORLDS = re.compile(r"strange new worlds")
STRANGENEWWORLDS1 = re.compile(r"strange.new.worlds")
STRANGENEWWORLDS_SEA = "s03e01"
STRANGENEWWORLDS_SEA_REG = re.compile(STRANGENEWWORLDS_SEA)
STRANGENEWWORLDS_EZ_1 = "https://eztv.re/search/strange-new-worlds"
STRANGENEWWORLDS_KA_1 = "https://kickasstorrents.to/usearch/strange new worlds"
STRANGENEWWORLDS_KA_2 = "https://kickasstorrents.to/usearch/strange new worlds/2"



GROOT  = re.compile(r"groot")
GROOT_SEA = "s03e01"
GROOT_SEA_REG = re.compile(GROOT_SEA)
GROOT_EZ_1 = "https://eztv.re/search/groot"
GROOT_KA_1 = "https://kickasstorrents.to/usearch/groot"
GROOT_KA_2 = "https://kickasstorrents.to/usearch/groot/2"



LORDOFTHERINGS  = re.compile(r"lord of the rings the rings of power")
LORDOFTHERINGS1  = re.compile(r"lord.of.the.rings.the.rings.of.power")
LORDOFTHERINGS_SEA = "s02e01"
LORDOFTHERINGS_SEA_REG = re.compile(LORDOFTHERINGS_SEA)
LORDOFTHERINGS_EZ_1 = "https://eztv.re/search/lord-of-the-rings-the-rings-of-power"
LORDOFTHERINGS_KA_1 = "https://kickasstorrents.to/usearch/lord of the rings the rings of power"
LORDOFTHERINGS_KA_2 = "https://kickasstorrents.to/usearch/lord of the rings the rings of power/2"



DROIDSTORY  = re.compile(r"droid story")
DROIDSTORY1  = re.compile(r"droid.story")
DROIDSTORY_SEA = "s01e01"
DROIDSTORY_SEA_REG = re.compile(DROIDSTORY_SEA)
DROIDSTORY_EZ_1 = "https://eztv.re/search/droid-story"
DROIDSTORY_KA_1 = "https://kickasstorrents.to/usearch/droid story"
DROIDSTORY_KA_2 = "https://kickasstorrents.to/usearch/droid story/2"

WAKANDA  = re.compile(r"wakanda")
WAKANDA_SEA = "s02e01"
WAKANDA_SEA_REG = re.compile(WAKANDA_SEA)
WAKANDA_EZ_1 = "https://eztv.re/search/wakanda"
WAKANDA_KA_1 = "https://kickasstorrents.to/usearch/wakanda"
WAKANDA_KA_2 = "https://kickasstorrents.to/usearch/wakanda/2"



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

