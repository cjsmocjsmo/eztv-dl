import os
import time
import requests
import logging
import argparse
from pprint import pprint
import shows.search as ez


import shows.acolyte as ACOLYTE
import shows.ahsoka as AHSOKA
import shows.andor as ANDOR
import shows.badbatch as BADBATCH
import shows.bookofbobafett as BOOKOFBOBAFETT
import shows.continental as CONTINENTAL
import shows.discovery as DISCOVERY
import shows.forallmankind as FORALLMANKIND
import shows.foundation as FOUNDATION
import shows.fubar as FUBAR
import shows.halo as HALO
import shows.houseofthedragon as HOUSEOFTHEDRAGON
import shows.lando as LANDO
import shows.loki as LOKI
import shows.lowerdecks as LOWERDECKS
import shows.mandilorian as MANDILORIAN
import shows.monarchlegacyofmonsters as MONARCHLEGACYOFMONSTER
import shows.obiwankenobi as OBIWANKENOBI
import shows.orville as ORVILLE
import shows.prehistoricplanet as PREHISTORICPLANET
import shows.rebelmoon as REBELMOON
import shows.silo as SILO
import shows.startrekprodigy as STARTREKPRODIGY
import shows.starwarsvisions as STARWARSVISIONS
import shows.strangenewworlds as STRANGENEWWORLDS
import shows.wheeloftime as WHEELOFTIME



# cwd = os.getcwd()
# print(cwd)

logger = logging.getLogger(__name__)
# Set the log level
logger.setLevel(logging.DEBUG)
# Create a file handler
file_handler = None
if os.path.exists('/home/teresa/ScraperLogs/scraper.log'):
    file_handler = logging.FileHandler('/home/teresa/ScraperLogs/scraper.log', mode='w')
elif os.path.exists("/home/charliepi/ScraperLogs/scraper.log"):
    file_handler = logging.FileHandler('/home/charliepi/ScraperLogs/scraper.log', mode='w')
elif os.path.exists("/home/pi/ScraperLogs/scraper.log"):
    file_handler = logging.FileHandler('/home/pi/ScraperLogs/scraper.log', mode='w')
# Set the formatter for the file handler
file_handler.setFormatter(logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s'))
# Add the file handler to the logger
logger.addHandler(file_handler)

class CheckForNewEpisodes:
    def __init__(self):
        self.masterMaget = []

    def main(self, args, cwd):
        start = time.time()

        acolyte = ACOLYTE.Acolyte(args, cwd).search_acolyte()
        time.sleep(10)

        ahsoka = AHSOKA.Ahsoka(args, cwd).search_ahsoka()
        time.sleep(10)

        andor = ANDOR.Andor(args, cwd).search_andor()
        time.sleep(10)

        badbatch = BADBATCH.BadBatch(args, cwd).search_badbatch()
        time.sleep(10)

        bookofbobafett = BOOKOFBOBAFETT.BookOfBobaFett(args, cwd).search_bookofbobafett()
        time.sleep(10)

        continental = CONTINENTAL.Continental(args, cwd).search_continental()
        time.sleep(10)

        discovery = DISCOVERY.Discovery(args, cwd).search_discovery()
        time.sleep(10)

        fubar = FUBAR.Fubar(args, cwd).search_fubar()
        time.sleep(10)

        forallmankind = FORALLMANKIND.ForAllMankind(args, cwd).search_forallmankind()
        time.sleep(10)

        foundation = FOUNDATION.Foundation(args, cwd).search_foundation()
        time.sleep(10)

        # groot = self.search_groot(args)
        # time.sleep(10)

        halo = HALO.Halo(args, cwd).search_halo()
        time.sleep(10)

        houseofthedragon = HOUSEOFTHEDRAGON.HouseOfTheDragon(args, cwd).search_houseofthedragon()
        time.sleep(10)

        lando = LANDO.Lando(args, cwd).search_lando()
        time.sleep(10)

        loki = LOKI.Loki(args, cwd).search_loki()
        time.sleep(10)

        # lordoftherings = self.search_lord_of_the_rings()
        # time.sleep(10)

        lowerdecks = LOWERDECKS.LowerDecks(args, cwd).search_lowerdecks_ez()
        time.sleep(10)

        mandalorian = MANDILORIAN.Mandilorian(args, cwd).search_mandilorian()
        time.sleep(10)

        monarch = MONARCHLEGACYOFMONSTER.MonarchLegacyOfMonsters(args, cwd).search_monarchlegacyofmonsters()
        time.sleep(10)

        obiwankenobi = OBIWANKENOBI.ObiWanKenobi(args, cwd).search_obiwankenobi()
        time.sleep(10)

        orville = ORVILLE.Orville(args, cwd).search_orville()
        time.sleep(10)

        prehistoricplanet = PREHISTORICPLANET.PrehistoricPlanet(args, cwd).search_prehistoricplanet()
        time.sleep(10)

        rebelmoon = REBELMOON.RebelMoon(args, cwd).search_rebelmoon()
        time.sleep(10)

        silo = SILO.Silo(args, cwd).search_silo()
        time.sleep(10)

        startrekprodigy = STARTREKPRODIGY.StarTrekProdigy(args, cwd).search_startrekprodigy()
        time.sleep(10)

        starwarsvisions = STARWARSVISIONS.StarWarsVisions(args, cwd).search_starwarsvisions()
        time.sleep(10)

        strangenewworlds = STRANGENEWWORLDS.StrangeNewWorlds(args, cwd).search_strangenewworlds()
        time.sleep(10)

        wheeloftime = WHEELOFTIME.WheelOfTime(args, cwd).search_wheeloftime()
        time.sleep(10)
       
        epi_total = [
            andor, lowerdecks, loki, discovery, mandalorian, 
            orville, forallmankind, badbatch, wheeloftime, 
            foundation, starwarsvisions, startrekprodigy, 
            bookofbobafett, continental, halo, strangenewworlds,
            prehistoricplanet, obiwankenobi, houseofthedragon,
            silo, ahsoka, acolyte, lando, monarch,
        ]
        end = time.time()
        ttime = (end - start) / 60
        ttime_str = str(ttime)
        total_time = ttime_str[:4]

        # print("Total episodes found: {}".format(sum(epi_total)))
        print("Total time taken: {} min".format(total_time))



if __name__ == "__main__":
    cwd = os.getcwd()
    print(cwd)

    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--eztv", action="store_true", help="Scan EzTV for episodes")
    parser.add_argument("-k", "--kickass", action="store_true", help="Scan Kickass for episodes")
    parser.add_argument("-x", "--x1337", action="store_true", help="Scan for 1337x episodes")
    parser.add_argument("-a", "--all", action="store_true", help="Scan all sites for episodes")
    args = parser.parse_args()

    # andor = andor.Andor(args, logger).search_andor()

    foo = CheckForNewEpisodes()
    foo.main(args, cwd)

