#!/usr/bin/python3
import re
import requests
import scrapers.old.tgtvlib as tg

CONTINENTAL       = re.compile(r"S01E03")
CONTINENTAL2      = re.compile(r"s01e03")

LOWERDECKS        = re.compile(r"S04E09")
LOWERDECKS2       = re.compile(r"s04e09")

class CheckForNewEpisoded:
    def __init__(self):
        self.MasterMagnet = []

    def search_continental(self):
        r = requests.get("https://torrentgalaxy.mx/torrents.php?search=continental#results")

        list_upper = tg.search_for_new_episode(r.text, CONTINENTAL)
        list_lower = tg.search_for_new_episode(r.text, CONTINENTAL2)
        count = len(list_upper) + len(list_lower)
        self.MasterMagnet.extend(list_upper)
        self.MasterMagnet.extend(list_lower)
        return count

    def search_lower_decks(self):
        r = requests.get("https://torrentgalaxy.mx/torrents.php?search=star+trek+lower+decks#results")

        list_upper = tg.search_for_new_episode(r.text, LOWERDECKS)
        list_lower = tg.search_for_new_episode(r.text, LOWERDECKS2)
        count = len(list_upper) + len(list_lower)
        self.MasterMagnet.extend(list_upper)
        self.MasterMagnet.extend(list_lower)
        return count

    def main(self):
        acount = self.search_continental()
        acount2 = self.search_lower_decks()
        print(acount + acount2)
        print(self.MasterMagnet)
        # print(acount)

if __name__ == "__main__":
    CheckForNewEpisoded().main()