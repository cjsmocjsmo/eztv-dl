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
import shows.forallmankind as FORALLMANKIND
import shows.foundation as FOUNDATION
import shows.fubar as FUBAR
import shows.halo as HALO
import shows.houseofthedragon as HOUSEOFTHEDRAGON
import shows.lowerdecks as LOWERDECKS
import shows.mandilorian as MANDILORIAN
import shows.monarchlegacyofmonsters as MONARCHLEGACYOFMONSTER
import shows.obiwankenobi as OBIWANKENOBI
import shows.orville as ORVILLE
import shows.prehistoricplanet as PREHISTORICPLANET
import shows.silo as SILO
import shows.startrekprodigy as STARTREKPRODIGY
import shows.starwarsvisions as STARWARSVISIONS
import shows.strangenewworlds as STRANGENEWWORLDS
import shows.wheeloftime as WHEELOFTIME
import shows.shogun as SHOGUN
import shows.fallout as FALLOUT
import shows.thelastofus as THELASTOFUS

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler = None
if os.path.exists('/home/teresa/ScraperLogs/scraper.log'):
    file_handler = logging.FileHandler('/home/teresa/ScraperLogs/scraper.log', mode='w')
elif os.path.exists("/home/charliepi/ScraperLogs/scraper.log"):
    file_handler = logging.FileHandler('/home/charliepi/ScraperLogs/scraper.log', mode='w')
elif os.path.exists("/home/pi/ScraperLogs/scraper.log"):
    file_handler = logging.FileHandler('/home/pi/ScraperLogs/scraper.log', mode='w')
elif os.path.exists("/home/pipi/ScraperLogs/scraper.log"):
    file_handler = logging.FileHandler('/home/pipi/ScraperLogs/scraper.log', mode='w')
file_handler.setFormatter(logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s'))
logger.addHandler(file_handler)

class CheckForNewEpisodes:
    def __init__(self):
        self.masterMaget = []

    def main(self, args, cwd):
        start = time.time()
        
        acolyte = ACOLYTE.Acolyte(args, cwd).search_acolyte()
        logger.info("Acolyte: {}".format(acolyte))
        time.sleep(5)

        ahsoka = AHSOKA.Ahsoka(args, cwd).search_ahsoka()
        logger.info("Ahsoka: {}".format(ahsoka))
        time.sleep(5)

        andor = ANDOR.Andor(args, cwd).search_andor()
        logger.info("Andor: {}".format(andor))
        time.sleep(5)

        badbatch = BADBATCH.BadBatch(args, cwd).search_badbatch()
        logger.info("BadBatch: {}".format(badbatch))
        time.sleep(5)

        bookofbobafett = BOOKOFBOBAFETT.BookOfBobaFett(args, cwd).search_bookofbobafett()
        logger.info("BookOfBobaFett: {}".format(bookofbobafett))
        time.sleep(5)

        continental = CONTINENTAL.Continental(args, cwd).search_continental()
        logger.info("Continental: {}".format(continental))
        time.sleep(5)

        fallout = FALLOUT.Fallout(args, cwd).search_fallout()
        logger.info("Fallout: {}".format(fallout))
        time.sleep(5)

        forallmankind = FORALLMANKIND.ForAllMankind(args, cwd).search_forallmankind()
        logger.info("ForAllMankind: {}".format(forallmankind))
        time.sleep(5)

        foundation = FOUNDATION.Foundation(args, cwd).search_foundation()
        logger.info("Foundation: {}".format(foundation))
        time.sleep(5)

        fubar = FUBAR.Fubar(args, cwd).search_fubar()
        logger.info("Fubar: {}".format(fubar))
        time.sleep(5)

        halo = HALO.Halo(args, cwd).search_halo()
        logger.info("Halo: {}".format(halo))
        time.sleep(5)

        houseofthedragon = HOUSEOFTHEDRAGON.HouseOfTheDragon(args, cwd).search_houseofthedragon()
        logger.info("HouseOfTheDragon: {}".format(houseofthedragon))
        time.sleep(5)

        lowerdecks = LOWERDECKS.LowerDecks(args, cwd).search_lowerdecks_ez()
        logger.info("LowerDecks: {}".format(lowerdecks))
        time.sleep(5)

        mandalorian = MANDILORIAN.Mandilorian(args, cwd).search_mandilorian()
        logger.info("Mandilorian: {}".format(mandalorian))
        time.sleep(5)

        monarch = MONARCHLEGACYOFMONSTER.MonarchLegacyOfMonsters(args, cwd).search_monarchlegacyofmonsters()
        logger.info("MonarchLegacyOfMonsters: {}".format(monarch))
        time.sleep(5)

        obiwankenobi = OBIWANKENOBI.ObiWanKenobi(args, cwd).search_obiwankenobi()
        logger.info("ObiWanKenobi: {}".format(obiwankenobi))
        time.sleep(5)

        orville = ORVILLE.Orville(args, cwd).search_orville()
        logger.info("Orville: {}".format(orville))
        time.sleep(5)

        prehistoricplanet = PREHISTORICPLANET.PrehistoricPlanet(args, cwd).search_prehistoricplanet()
        logger.info("PrehistoricPlanet: {}".format(prehistoricplanet))
        time.sleep(5)

        silo = SILO.Silo(args, cwd).search_silo()
        logger.info("Silo: {}".format(silo))
        time.sleep(5)

        startrekprodigy = STARTREKPRODIGY.StarTrekProdigy(args, cwd).search_startrekprodigy()
        logger.info("StarTrekProdigy: {}".format(startrekprodigy))
        time.sleep(5)

        starwarsvisions = STARWARSVISIONS.StarWarsVisions(args, cwd).search_starwarsvisions()
        logger.info("StarWarsVisions: {}".format(starwarsvisions))
        time.sleep(5)

        strangenewworlds = STRANGENEWWORLDS.StrangeNewWorlds(args, cwd).search_strangenewworlds()
        logger.info("StrangeNewWorlds: {}".format(strangenewworlds))
        time.sleep(5)

        shogun = SHOGUN.Shogun(args, cwd).search_shogun()
        logger.info("Shogun: {}".format(shogun))
        time.sleep(5)

        thelastofus = THELASTOFUS.TheLastOfUs(args, cwd).search_thelastofus()
        logger.info("TheLastOfUs: {}".format(thelastofus))
        time.sleep(5)

        wheeloftime = WHEELOFTIME.WheelOfTime(args, cwd).search_wheeloftime()
        logger.info("WheelOfTime: {}".format(wheeloftime))
        time.sleep(5)

        epi_total = [
            acolyte, ahsoka, andor, 
            badbatch, bookofbobafett, 
            continental, 
            fallout, forallmankind, foundation, fubar, 
            halo, houseofthedragon, 
            lowerdecks, 
            mandalorian, monarch, 
            obiwankenobi, orville, 
            prehistoricplanet, 
            shogun, silo, startrekprodigy,  starwarsvisions, strangenewworlds,  
            thelastofus,
            wheeloftime, 
        ]
        end = time.time()
        ttime = (end - start) / 60
        ttime_str = str(ttime)
        total_time = ttime_str[:4]

        print("Total episodes found: {}".format(sum(epi_total)))
        logger.info("Total episodes found: {}".format(sum(epi_total)))
        print("Total time taken: {} min".format(total_time))
        logger.info("Total time taken: {} min".format(total_time))



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

