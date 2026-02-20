import os
import time
import logging
import argparse
import Utils as SHOWS

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

        ahsoka = SHOWS.Ahsoka(args, cwd).search_ahsoka()
        logger.info("Ahsoka: {}".format(ahsoka))
        time.sleep(5)

        fallout = SHOWS.Fallout(args, cwd).search_fallout()
        logger.info("Fallout: {}".format(fallout))
        time.sleep(5)

        forallmankind = SHOWS.ForAllMankind(args, cwd).search_forallmankind()
        logger.info("ForAllMankind: {}".format(forallmankind))
        time.sleep(5)

        foundation = SHOWS.Foundation(args, cwd).search_foundation()
        logger.info("Foundation: {}".format(foundation))
        time.sleep(5)

        fubar = SHOWS.Fubar(args, cwd).search_fubar()
        logger.info("Fubar: {}".format(fubar))
        time.sleep(5)

        houseofthedragon = SHOWS.HouseOfTheDragon(args, cwd).search_houseofthedragon()
        logger.info("HouseOfTheDragon: {}".format(houseofthedragon))
        time.sleep(5)

        mandalorian = SHOWS.Mandilorian(args, cwd).search_mandilorian()
        logger.info("Mandilorian: {}".format(mandalorian))
        time.sleep(5)

        monarch = SHOWS.MonarchLegacyOfMonsters(args, cwd).search_monarchlegacyofmonsters()
        logger.info("MonarchLegacyOfMonsters: {}".format(monarch))
        time.sleep(5)

        obiwankenobi = SHOWS.ObiWanKenobi(args, cwd).search_obiwankenobi()
        logger.info("ObiWanKenobi: {}".format(obiwankenobi))
        time.sleep(5)

        orville = SHOWS.Orville(args, cwd).search_orville()
        logger.info("Orville: {}".format(orville))
        time.sleep(5)

        prehistoricplanet = SHOWS.PrehistoricPlanet(args, cwd).search_prehistoricplanet()
        logger.info("PrehistoricPlanet: {}".format(prehistoricplanet))
        time.sleep(5)

        silo = SHOWS.Silo(args, cwd).search_silo()
        logger.info("Silo: {}".format(silo))
        time.sleep(5)

        starwarsvisions = SHOWS.StarWarsVisions(args, cwd).search_starwarsvisions()
        logger.info("StarWarsVisions: {}".format(starwarsvisions))
        time.sleep(5)

        strangenewworlds = SHOWS.StrangeNewWorlds(args, cwd).search_strangenewworlds()
        logger.info("StrangeNewWorlds: {}".format(strangenewworlds))
        time.sleep(5)

        shogun = SHOWS.Shogun(args, cwd).search_shogun()
        logger.info("Shogun: {}".format(shogun))
        time.sleep(5)

        thelastofus = SHOWS.TheLastOfUs(args, cwd).search_thelastofus()
        logger.info("TheLastOfUs: {}".format(thelastofus))
        time.sleep(5)

        skeletoncrew = SHOWS.SkeletonCrew(args, cwd).search_skeletoncrew()
        logger.info("SkeletonCrew: {}".format(skeletoncrew))
        time.sleep(5)

        mobland = SHOWS.MobLand(args, cwd).search_mobland()
        logger.info("MobLand: {}".format(mobland))
        time.sleep(5)

        ironheart = SHOWS.IronHeart(args, cwd).search_ironheart()
        logger.info("IronHeart: {}".format(ironheart))

        wednesday = SHOWS.Wednesday(args, cwd).search_wednesday()
        logger.info("Wednesday: {}".format(wednesday))
        time.sleep(5)

        ncis = SHOWS.NCIS(args, cwd).search_ncis()
        logger.info("NCIS: {}".format(ncis))
        time.sleep(5)

        ncissydney = SHOWS.NCISSydney(args, cwd).search_ncissydney()
        logger.info("NCISSydney: {}".format(ncissydney))
        time.sleep(5)

        ncisorigins = SHOWS.NCISOrigins(args, cwd).search_ncisorigins()
        logger.info("NCISOrigins: {}".format(ncisorigins))
        time.sleep(5)

        toni_and_ziva = SHOWS.TonyAndZiva(args, cwd).search_tonyandziva()
        logger.info("TonyAndZiva: {}".format(toni_and_ziva))
        time.sleep(5)

        dmv = SHOWS.DMV(args, cwd).search_dmv()
        logger.info("DMV: {}".format(dmv))
        time.sleep(5)

        percyjacksonandtheolympians = SHOWS.PercyJacksonAndTheOlympians(args, cwd).search_percyjacksonandtheolympians()
        logger.info("PercyJacksonAndTheOlympians: {}".format(percyjacksonandtheolympians))
        time.sleep(5)

        starfleetacademy = SHOWS.StarfleetAcademy(args, cwd).search_starfleetacademy()
        logger.info("StarfleetAcademy: {}".format(starfleetacademy))
        time.sleep(5)

        wonderman = SHOWS.WonderMan(args, cwd).search_wonderman()
        logger.info("WonderMan: {}".format(wonderman))
        time.sleep(5)

        darkwinds = SHOWS.DarkWinds(args, cwd).search_darkwinds()
        logger.info("DarkWinds: {}".format(darkwinds))
        time.sleep(5)

        

        epi_total = [
            ahsoka,
            darkwinds, dmv,
            fallout, forallmankind, foundation, fubar,
            houseofthedragon,
            ironheart,
            mobland, mandalorian, monarch,
            ncis, ncisorigins, ncissydney,
            obiwankenobi, orville, 
            percyjacksonandtheolympians, prehistoricplanet,
            shogun, silo, starfleetacademy, starwarsvisions, strangenewworlds, skeletoncrew,
            thelastofus, toni_and_ziva,
            wednesday, wonderman,
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
    args = parser.parse_args()

    foo = CheckForNewEpisodes()
    foo.main(args, cwd)

