import re
import os
import requests
import logging
from bs4 import BeautifulSoup
from pprint import pprint
# import EZlib as ez


ANDOR = re.compile(r"s01e04")
ANDOR2 = "s01e04"

LOWERDECKS = re.compile(r"s04e08")
LOWERDECKS2 = "s04e08"

LOKI = re.compile(r"s02e06")
LOKI2 = "s02e06"

DISCOVERY = re.compile(r"s05e01")
DISCOVERY2 = "s05e01"

MANDALORIAN  = re.compile(r"s04e01")

ORVILLE = re.compile(r"s04e01")

FORALLMANKIND = re.compile(r"s04e01")

BADBATCH = re.compile(r"s03e01")

WHEELOFTIME = re.compile(r"s03e01")

FOUNDATION2 = re.compile(r"s03e01")

STARWARSVISIONS2 = re.compile(r"s02e01")

STARTREKPRODIGY = re.compile(r"s02e01")

BOOKOFBOBAFETT = re.compile(r"s02e01")

CONTINENTAL = re.compile(r"s02e01")

HALO = re.compile(r"s02e01")

STRANGENEWWORLDS = re.compile(r"s03e01")

PREHISTORICPLANET = re.compile(r"s03e01")

OBIWANKENOBI = re.compile(r"s02e01")

GROOT  = re.compile(r"s03e01")

HOUSEOFTHEDRAGON  = re.compile(r"s02e01")

LORDOFTHERINGSTHERINGSOFPOWER  = re.compile(r"s02e01")

SILO  = re.compile(r"s02e01")

AHSOKA  = re.compile(r"s01e09")

DROIDSTORY  = re.compile(r"s01e01")

WAKANDA  = re.compile(r"s01e01")

ACOLYTE  = re.compile(r"s01e01")

LANDO  = re.compile(r"s01e01")

MONARCK = re.compile(r"s01e01")
MONARCK2 = "s01e01"

TEN = re.compile("1080p")
SEV = re.compile("720p")


logger = logging.getLogger(__name__)
# Set the log level
logger.setLevel(logging.DEBUG)
# Create a file handler
file_handler = None
if os.path.exists('/home/charliepi/ScraperLogs/EZ.log'):
    file_handler = logging.FileHandler('/home/charliepi/ScraperLogs/EZ.log', mode='w')
else:
    file_handler = logging.FileHandler('/home/pi/ScraperLogs/EZ.log', mode='w')
# Set the formatter for the file handler
file_handler.setFormatter(logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s'))
# Add the file handler to the logger
logger.addHandler(file_handler)

class EZCheckForNewEpisodes:
    def __init__(self):
        self.masterMaget = []

    def search_andor(self):
        r1 = requests.get('https://eztv.re/search/andor')
        r1_resp = r1.status_code
        if r1_resp == 200:
            p1_list = search_for_new_episode(r1.text, ANDOR)
            resp1080p = len(p1_list[0])
            resp720p = len(p1_list[1])
            print("\nAndor {} => \n\tstatus: {}, \n\t1080p: {}\n\t720p: {}".format(ANDOR2, r1_resp, resp1080p, resp720p))
            logger.info("\nAndor {} => \n\tstatus: {}, \n\t1080p: {}\n\t720p: {}".format(ANDOR2, r1_resp, resp1080p, resp720p))
        return resp1080p + resp720p

    def search_lowerdecks(self):
        r1 = requests.get('https://eztv.re/search/star-trek-lower-decks')
        r1_resp = r1.status_code
        if r1_resp == 200:
            p1_list = search_for_new_episode(r1.text, LOWERDECKS)
            resp1080p = len(p1_list[0])
            resp720p = len(p1_list[1])
            print("\nLOWERDECKS {} => \n\tstatus: {}, \n\t1080p: {}\n\t720p: {}".format(LOWERDECKS2, r1_resp, resp1080p, resp720p))
            logger.info("\nLOWERDECKS {} => \n\tstatus: {}, \n\t1080p: {}\n\t720p: {}".format(LOWERDECKS2, r1_resp, resp1080p, resp720p))
        return resp1080p + resp720p

    def search_loki(self):
        r1 = requests.get('https://eztv.re/search/loki')
        r1_resp = r1.status_code
        if r1_resp == 200:
            p1_list = search_for_new_episode(r1.text, LOKI)
            resp1080p = len(p1_list[0])
            resp720p = len(p1_list[1])
            print("\nLOKI {} => \n\tstatus: {}, \n\t1080p: {}\n\t720p: {}".format(LOKI2, r1_resp, resp1080p, resp720p))
            logger.info("\nLOKI {} => \n\tstatus: {}, \n\t1080p: {}\n\t720p: {}".format(LOKI2, r1_resp, resp1080p, resp720p))
        return resp1080p + resp720p

    def search_discovery(self):
        r1 = requests.get('https://eztv.re/search/star-trek-discovery')
        r1_resp = r1.status_code
        if r1_resp == 200:
            p1_list = search_for_new_episode(r1.text, DISCOVERY)
            resp1080p = len(p1_list[0])
            resp720p = len(p1_list[1])
            print("\nDISCOVERY {} => \n\tstatus: {}, \n\t1080p: {}\n\t720p: {}".format(DISCOVERY2, r1_resp, resp1080p, resp720p))
            logger.info("\nDISCOVERY {} => \n\tstatus: {}, \n\t1080p: {}\n\t720p: {}".format(DISCOVERY2, r1_resp, resp1080p, resp720p))
        return resp1080p + resp720p




    def search_monarck(self):
        r1 = requests.get('https://eztv.re/search/monarch-legacy-of-monsters')
        r1_resp = r1.status_code
        if r1_resp == 200:
            p1_list = search_for_new_episode(r1.text, MONARCK)
            resp1080p = len(p1_list[0])
            resp720p = len(p1_list[1])
            print("\nMONARCK {} => \n\tstatus: {}, \n\t1080p: {}\n\t720p: {}".format(MONARCK2, r1_resp, resp1080p, resp720p))
            logger.info("\nMONARCK {} => \n\tstatus: {}, \n\t1080p: {}\n\t720p: {}".format(MONARCK2, r1_resp, resp1080p, resp720p))
        return resp1080p + resp720p


    def main(self):
        andor = self.search_andor()
        lowerdecks = self.search_lowerdecks()
        loki = self.search_loki()
        discovery = self.search_discovery()
        monarck = self.search_monarck()

def search_for_new_episode(page, title):
    list1080p = []
    list720p = []
    soup = BeautifulSoup(page, 'html.parser')
    count = 0
    for link in soup.findAll("a"):
        count += 1
        meta = (link.get("title"), link.get('href'))
        if meta[0] != None:
            ltitle = meta[0].lower()
            if re.search(ANDOR, ltitle) != None:
                if re.search(TEN, meta[0]) != None:
                    list1080p.append(meta[0])
                elif re.search(SEV, meta[0]) != None:
                    list720p.append(meta[0])
                else:
                    pass
    return (list1080p, list720p)

if __name__ == "__main__":
    foo = EZCheckForNewEpisodes()
    foo.main()

