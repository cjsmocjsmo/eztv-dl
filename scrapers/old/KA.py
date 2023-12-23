#!/usr/bin/python3

import re
import requests
import logging
import scrapers.old.KAlib as ez

ANDOR = re.compile(r"andor")
ANDOR3 = "s02e01"
ANDOR2 = re.compile(ANDOR3)

LOWERDECKS = re.compile(r"star-trek-lower-decks")
LOWERDECKS3 = "s04e10"
LOWERDECKS2 = re.compile(LOWERDECKS3)

LOKI = re.compile("loki")
LOKI3 = "s02e06"
LOKI2 = re.compile(LOKI3)

DISCOVERY = re.compile(r"discovery")
DISCOVERY3 = "s05e01"
DISCOVERY2 = re.compile(DISCOVERY3)

MANDALORIAN  = re.compile(r"mandalorian")
MANDALORIAN3 = "s04e01"
MANDALORIAN2 = re.compile(MANDALORIAN3)

ORVILLE = re.compile(r"orville")
ORVILLE3 = "s04e01"
ORVILLE2 = re.compile(ORVILLE3)

FORALLMANKIND = re.compile(r"for-all-mankind")
FORALLMANKIND3 = "s04e01"
FORALLMANKIND2 = re.compile(FORALLMANKIND3)

BADBATCH = re.compile(r"bad-batch")
BADBATCH3 = "s03e01"
BADBATCH2 = re.compile(BADBATCH3)

WHEELOFTIME = re.compile(r"wheel-of-time")
WHEELOFTIME3 = "s03e01"
WHEELOFTIME2 = re.compile(WHEELOFTIME3)

FOUNDATION = re.compile(r'foundation')
FOUNDATION3 = "s03e01"
FOUNDATION2 = re.compile(FOUNDATION3)

STARWARSVISIONS = re.compile(r'star-wars-visions')
STARWARSVISIONS3 = "s02e01"
STARWARSVISIONS2 = re.compile(STARWARSVISIONS3)

STARTREKPRODIGY = re.compile(r"star-trek-prodigy")
STARTREKPRODIGY3 = "s02e01"
STARTREKPRODIGY2 = re.compile(STARTREKPRODIGY3)

BOOKOFBOBAFETT = re.compile(r"book-of-boba-fett")
BOOKOFBOBAFETT3 = "s02e01"
BOOKOFBOBAFETT2 = re.compile(BOOKOFBOBAFETT3)

CONTINENTAL = re.compile(r"continental")
CONTINENTAL3 = "s02e01"
CONTINENTAL2 = re.compile(CONTINENTAL3)

HALO = re.compile(r"halo")
HALO3 = "s02e01"
HALO2 = re.compile(HALO3)

STRANGENEWWORLDS = re.compile(r"strange-new-worlds")
STRANGENEWWORLDS3 = "s03e01"
STRANGENEWWORLDS2 = re.compile(STRANGENEWWORLDS3)

PREHISTORICPLANET = re.compile(r"prehistoric-planet")
PREHISTORICPLANET3 = "s03e01"
PREHISTORICPLANET2 = re.compile(PREHISTORICPLANET3)

OBIWANKENOBI = re.compile(r"obi-wan-kenobi")
OBIWANKENOBI3 = "s02e01"
OBIWANKENOBI2 = re.compile(OBIWANKENOBI3)

GROOT  = re.compile(r"groot")
GROOT3 = "s03e01"
GROOT2 = re.compile(GROOT3)

HOUSEOFTHEDRAGON  = re.compile(r"house-of-the-dragon")
HOUSEOFTHEDRAGON3 = "s02e01"
HOUSEOFTHEDRAGON2 = re.compile(HOUSEOFTHEDRAGON3)

LORDOFTHERINGSTHERINGSOFPOWER  = re.compile(r"the-lord-of-the-rings-the-rings-of-power")
LORDOFTHERINGSTHERINGSOFPOWER3 = "s02e01"
LORDOFTHERINGSTHERINGSOFPOWER2 = re.compile(LORDOFTHERINGSTHERINGSOFPOWER3)

SILO  = re.compile(r"silo")
SILO3 = "s02e01"
SILO2 = re.compile(SILO3)

AHSOKA  = re.compile(r"ahsoka")
AHSOKA3 = "s01e09"
AHSOKA2 = re.compile(AHSOKA3)

DROIDSTORY  = re.compile(r"a-droid-story")
DROIDSTORY3 = "s01e01"
DROIDSTORY2 = re.compile(DROIDSTORY3)

WAKANDA  = re.compile(r"wakanda")
WAKANDA3 = "s01e01"
WAKANDA2 = re.compile(WAKANDA3)

ACOLYTE  = re.compile(r"acolyte")
ACOLYTE3 = "s01e01"
ACOLYTE2 = re.compile(ACOLYTE3)

LANDO  = re.compile(r"lando")
LANDO3 = "s01e01"
LANDO2 = re.compile(LANDO3)

MONARCK = re.compile(r"monarck legacy of monsters")
MONARCK3 = "s01e01"
MONARCK2 = re.compile(MONARCK3)

logger = logging.getLogger(__name__)
# Set the log level
logger.setLevel(logging.DEBUG)
# Create a file handler
file_handler = logging.FileHandler('/home/pi/ScraperLogs/KA.log')
# Set the formatter for the file handler
file_handler.setFormatter(logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s'))
# Add the file handler to the logger
logger.addHandler(file_handler)

class CheckForNewEpisodes:
    def __init__(self):
        self.masterMagnet = []


    # def search_andor(self):
    #     r1 = requests.get('https://kickasstorrents.to/usearch/andor')
    #     r1_resp = r1.status_code
    #     r2 = requests.get('https://kickasstorrents.to/usearch/andor/2')
    #     r2_resp = r2.status_code
    #     p1_list = ez.search_for_new_episode(r1.text, ANDOR, ANDOR2)
    #     p2_list = ez.search_for_new_episode(r2.text, ANDOR, ANDOR2)
    #     res1 = len(p1_list[0]) + len(p2_list[0])
    #     res2 = len(p1_list[1]) + len(p2_list[1])
    #     print("Andor {} => \n1080p: {}\n 720p: {}\n status {}:{}".format(ANDOR3, res1, res2, r1_resp, r2_resp))
    #     logger.info("Andor {} => \n1080p: {}\n 720p: {}\n status {}:{}".format(ANDOR3, res1, res2, r1_resp, r2_resp))
    #     return res1 + res2


    def search_monarck(self):
        r1 = requests.get('https://kickasstorrents.to/usearch/monarck legacy of monsters')
        r1_resp = r1.status_code
        p1_list = ez.search_for_new_episode(r1.text, MONARCK, MONARCK2)
        print("Monarck {} => 1080p: {} 720p: {}".format(MONARCK3, p1_list[0], p1_list[1]))
        print(r1_resp)
        logger.info("Monarck {} => 1080p: {} 720p: {}".format(MONARCK3, p1_list[0], p1_list[1]))
        return p1_list[0] + p1_list[1]

    def search_lower_decks(self):
        r1 = requests.get('https://kickasstorrents.to/usearch/star trek lower decks')
        r2 = requests.get('https://kickasstorrents.to/usearch/star trek lower decks/2')
        p1_list = ez.search_for_new_episode(r1.text, LOWERDECKS,  LOWERDECKS2)
        p2_list = ez.search_for_new_episode(r2.text, LOWERDECKS,  LOWERDECKS2)
        res1 = len(p1_list[0]) + len(p2_list[0])
        res2 = len(p1_list[1]) + len(p2_list[1])
        print("Lower Decks {} => 1080p: {} 720p: {}\n".format(LOWERDECKS3, res1, res2))
        logger.info("Lower Decks {} => 1080p: {} 720p: {}\n".format(LOWERDECKS3, res1, res2))
        return res1 + res2

    def search_loki(self):
        r1 = requests.get('https://kickasstorrents.to/usearch/loki')
        r2 = requests.get('https://kickasstorrents.to/usearch/loki/2')
        p1_list = ez.search_for_new_episode(r1.text, LOKI,  LOKI2)
        p2_list = ez.search_for_new_episode(r2.text, LOKI,  LOKI2)
        res1 = len(p1_list[0]) + len(p2_list[0])
        res2 = len(p1_list[1]) + len(p2_list[1])
        print("Loki {} => 1080p: {} 720p: {}".format(LOKI3, res1, res2))
        logger.info("Loki {} => 1080p: {} 720p: {}".format(LOKI3, res1, res2))
        return res1 + res2

    def search_discovery(self):
        r1 = requests.get('https://kickasstorrents.to/usearch/discovery')
        r2 = requests.get('https://kickasstorrents.to/usearch/discovery/2')
        p1_list = ez.search_for_new_episode(r1.text, DISCOVERY, DISCOVERY2)
        p2_list = ez.search_for_new_episode(r2.text, DISCOVERY, DISCOVERY2)
        res1 = len(p1_list[0]) + len(p2_list[0])
        res2 = len(p1_list[1]) + len(p2_list[1])
        print("Discovery {} => 1080p: {} 720p: {}\n".format(DISCOVERY3, res1, res2))
        logger.info("Discovery {} => 1080p: {} 720p: {}\n".format(DISCOVERY3, res1, res2))
        return res1 + res2

    def search_mando(self):
        r1 = requests.get('https://kickasstorrents.to/usearch/mandalorian')
        r2 = requests.get('https://kickasstorrents.to/usearch/mandalorian/2')
        p1_list = ez.search_for_new_episode(r1.text, MANDALORIAN, MANDALORIAN2)
        p2_list = ez.search_for_new_episode(r2.text, MANDALORIAN, MANDALORIAN2)
        res1 = len(p1_list[0]) + len(p2_list[0])
        res2 = len(p1_list[1]) + len(p2_list[1])
        print("Mandalorian {} => 1080p: {} 720p: {}\n".format(MANDALORIAN3, res1, res2))
        logger.info("Mandalorian {} => 1080p: {} 720p: {}\n".format(MANDALORIAN3, res1, res2))
        return res1 + res2

    def search_orville(self):
        r1 = requests.get('https://kickasstorrents.to/usearch/orville')
        r2 = requests.get('https://kickasstorrents.to/usearch/orville/2')
        p1_list = ez.search_for_new_episode(r1.text, ORVILLE, ORVILLE2)
        p2_list = ez.search_for_new_episode(r2.text, ORVILLE, ORVILLE2)
        res1 = len(p1_list[0]) + len(p2_list[0])
        res2 = len(p1_list[1]) + len(p2_list[1])
        print("Orville {} => 1080p: {} 720p: {}\n".format(ORVILLE3, res1, res2))
        logger.info("Orville {} => 1080p: {} 720p: {}\n".format(ORVILLE3, res1, res2))
        return res1 + res2

    def search_for_all_man_kind(self):
        r1 = requests.get('https://kickasstorrents.to/usearch/for-all-mankind')
        r2 = requests.get('https://kickasstorrents.to/usearch/for-all-mankind/2')
        p1_list = ez.search_for_new_episode(r1.text, FORALLMANKIND, FORALLMANKIND2)
        p2_list = ez.search_for_new_episode(r2.text, FORALLMANKIND, FORALLMANKIND2)
        res1 = len(p1_list[0]) + len(p2_list[0])
        res2 = len(p1_list[1]) + len(p2_list[1])
        print("For All Mankind {} => 1080p: {} 720p: {}\n".format(FORALLMANKIND3, res1, res2))
        logger.info("For All Mankind {} => 1080p: {} 720p: {}\n".format(FORALLMANKIND3, res1, res2))
        return res1 + res2

    def search_bad_batch(self):
        r1 = requests.get('https://kickasstorrents.to/usearch/star-wars-bad-batch')
        r2 = requests.get('https://kickasstorrents.to/usearch/star-wars-bad-batch/2')
        p1_list = ez.search_for_new_episode(r1.text, BADBATCH, BADBATCH2)
        p2_list = ez.search_for_new_episode(r2.text, BADBATCH, BADBATCH2)
        res1 = len(p1_list[0]) + len(p2_list[0])
        res2 = len(p1_list[1]) + len(p2_list[1])
        print("Bad Batch {} => 1080p: {} 720p: {}\n".format(BADBATCH3, res1, res2))
        logger.info("Bad Batch {} => 1080p: {} 720p: {}\n".format(BADBATCH3, res1, res2))
        return res1 + res2

    def search_star_wars_visions(self):
        r1 = requests.get('https://kickasstorrents.to/usearch/star-wars-visions')
        r2 = requests.get('https://kickasstorrents.to/usearch/star-wars-visions/2')
        p1_list = ez.search_for_new_episode(r1.text, STARWARSVISIONS, STARWARSVISIONS2)
        p2_list = ez.search_for_new_episode(r2.text, STARWARSVISIONS, STARWARSVISIONS2)
        res1 = len(p1_list[0]) + len(p2_list[0])
        res2 = len(p1_list[1]) + len(p2_list[1])
        print("\nStar Wars Visions {} => 1080p: {} 720p: {}\n".format(STARWARSVISIONS3, res1, res2))
        logger.info("\nStar Wars Visions {} => 1080p: {} 720p: {}\n".format(STARWARSVISIONS3, res1, res2))
        return res1 + res2

    def search_wheeloftime(self):
        r1 = requests.get('https://kickasstorrents.to/usearch/wheel-of-time')
        r2 = requests.get('https://kickasstorrents.to/usearch/wheel-of-time/2')
        p1_list = ez.search_for_new_episode(r1.text, WHEELOFTIME, WHEELOFTIME2)
        p2_list = ez.search_for_new_episode(r2.text, WHEELOFTIME, WHEELOFTIME2)
        res1 = len(p1_list[0]) + len(p2_list[0])
        res2 = len(p1_list[1]) + len(p2_list[1])
        print("\nWheel Of Time {} => 1080p: {} 720p: {}\n".format(WHEELOFTIME3, res1, res2))
        logger.info("\nWheel Of Time {} => 1080p: {} 720p: {}\n".format(WHEELOFTIME3, res1, res2))
        return res1 + res2

    def search_foundation(self):
        r1 = requests.get('https://kickasstorrents.to/usearch/foundation')
        r2 = requests.get('https://kickasstorrents.to/usearch/foundation/2')
        p1_list = ez.search_for_new_episode(r1.text, FOUNDATION, FOUNDATION2)
        p2_list = ez.search_for_new_episode(r2.text, FOUNDATION, FOUNDATION2)
        res1 = len(p1_list[0]) + len(p2_list[0])
        res2 = len(p1_list[1]) + len(p2_list[1])
        print("\nFoundation {} => 1080p: {} 720p: {}\n".format(FOUNDATION3, res1, res2))
        logger.info("\nFoundation {} => 1080p: {} 720p: {}\n".format(FOUNDATION3, res1, res2))
        return res1 + res2

    def search_star_trek_prodigy(self):
        r1 = requests.get('https://kickasstorrents.to/usearch/star-trek-prodigy')
        r2 = requests.get('https://kickasstorrents.to/usearch/star-trek-prodigy/2')
        p1_list = ez.search_for_new_episode(r1.text, STARTREKPRODIGY, STARTREKPRODIGY2)
        p2_list = ez.search_for_new_episode(r2.text, STARTREKPRODIGY, STARTREKPRODIGY2)
        res1 = len(p1_list[0]) + len(p2_list[0])
        res2 = len(p1_list[1]) + len(p2_list[1])
        print("\nStar Trek Prodigy {} => 1080p: {} 720p: {}\n".format(STARTREKPRODIGY3, res1, res2))
        logger.info("\nStar Trek Prodigy {} => 1080p: {} 720p: {}\n".format(STARTREKPRODIGY3, res1, res2))
        return res1 + res2

    def search_book_of_boba_fett(self):
        r1 = requests.get('https://kickasstorrents.to/usearch/the-book-of-boba-fett')
        r2 = requests.get('https://kickasstorrents.to/usearch/the-book-of-boba-fett/2')
        p1_list = ez.search_for_new_episode(r1.text, BOOKOFBOBAFETT, BOOKOFBOBAFETT2)
        p2_list = ez.search_for_new_episode(r2.text, BOOKOFBOBAFETT, BOOKOFBOBAFETT2)
        res1 = len(p1_list[0]) + len(p2_list[0])
        res2 = len(p1_list[1]) + len(p2_list[1])
        print("\nThe Book Of Boba Fett {} => 1080p: {} 720p: {}\n".format(BOOKOFBOBAFETT3, res1, res2))
        logger.info("\nThe Book Of Boba Fett {} => 1080p: {} 720p: {}\n".format(BOOKOFBOBAFETT3, res1, res2))
        return res1 + res2

    def search_continental(self):
        r1 = requests.get('https://kickasstorrents.to/usearch/the-continental')
        r2 = requests.get('https://kickasstorrents.to/usearch/the-continental/2')
        p1_list = ez.search_for_new_episode(r1.text, CONTINENTAL, CONTINENTAL2)
        p2_list = ez.search_for_new_episode(r2.text, CONTINENTAL, CONTINENTAL2)
        res1 = len(p1_list[0]) + len(p2_list[0])
        res2 = len(p1_list[1]) + len(p2_list[1])
        print("\nThe Continental {} => 1080p: {} 720p: {}\n".format(CONTINENTAL3, res1, res2))
        logger.info("\nThe Continental {} => 1080p: {} 720p: {}\n".format(CONTINENTAL3, res1, res2))
        return res1 + res2

    def search_halo(self):
        r1 = requests.get('https://kickasstorrents.to/usearch/halo')
        r2 = requests.get('https://kickasstorrents.to/usearch/halo/2')
        p1_list = ez.search_for_new_episode(r1.text, HALO, HALO2)
        p2_list = ez.search_for_new_episode(r2.text, HALO, HALO2)
        res1 = len(p1_list[0]) + len(p2_list[0])
        res2 = len(p1_list[1]) + len(p2_list[1])
        print("\nHalo {} => 1080p: {} 720p: {}\n".format(HALO3, res1, res2))
        logger.info("\nHalo {} => 1080p: {} 720p: {}\n".format(HALO3, res1, res2))
        return res1 + res2

    def search_star_trek_strange_new_worlds(self):
        r1 = requests.get('https://kickasstorrents.to/usearch/star-trek-strange-new-worlds')
        r2 = requests.get('https://kickasstorrents.to/usearch/star-trek-strange-new-worlds/2')
        p1_list = ez.search_for_new_episode(r1.text, STRANGENEWWORLDS, STRANGENEWWORLDS2)
        p2_list = ez.search_for_new_episode(r2.text, STRANGENEWWORLDS, STRANGENEWWORLDS2)
        res1 = len(p1_list[0]) + len(p2_list[0])
        res2 = len(p1_list[1]) + len(p2_list[1])
        print("\nStar Trek Strange New Worlds {} => 1080p: {} 720p: {}\n".format(STRANGENEWWORLDS3, res1, res2))
        logger.info("\nStar Trek Strange New Worlds {} => 1080p: {} 720p: {}\n".format(STRANGENEWWORLDS3, res1, res2))
        return res1 + res2

    def search_prehistoric_planet(self):
        r1 = requests.get('https://kickasstorrents.to/usearch/prehistoric-planet')
        r2 = requests.get('https://kickasstorrents.to/usearch/prehistoric-planet/2')
        p1_list = ez.search_for_new_episode(r1.text, PREHISTORICPLANET, PREHISTORICPLANET2)
        p2_list = ez.search_for_new_episode(r2.text, PREHISTORICPLANET, PREHISTORICPLANET2)
        res1 = len(p1_list[0]) + len(p2_list[0])
        res2 = len(p1_list[1]) + len(p2_list[1])
        print("\nPrehistoric Planet {} => 1080p: {} 720p: {}\n".format(PREHISTORICPLANET3, res1, res2))
        logger.info("\nPrehistoric Planet {} => 1080p: {} 720p: {}\n".format(PREHISTORICPLANET3, res1, res2))
        return res1 + res2

    def search_obi_wan_kenobi(self):
        r1 = requests.get('https://kickasstorrents.to/usearch/kenobi')
        r2 = requests.get('https://kickasstorrents.to/usearch/kenobi/2')
        p1_list = ez.search_for_new_episode(r1.text, OBIWANKENOBI, OBIWANKENOBI2)
        p2_list = ez.search_for_new_episode(r2.text, OBIWANKENOBI, OBIWANKENOBI2)
        res1 = len(p1_list[0]) + len(p2_list[0])
        res2 = len(p1_list[1]) + len(p2_list[1])
        print("\nObi Wan Kenobi {} => 1080p: {} 720p: {}\n".format(OBIWANKENOBI3, res1, res2))
        logger.info("\nObi Wan Kenobi {} => 1080p: {} 720p: {}\n".format(OBIWANKENOBI3, res1, res2))
        return res1 + res2

    def search_house_of_the_dragon(self):
        r1 = requests.get('https://kickasstorrents.to/usearch/house-of-the-dragon')
        r2 = requests.get('https://kickasstorrents.to/usearch/house-of-the-dragon/2')
        p1_list = ez.search_for_new_episode(r1.text, HOUSEOFTHEDRAGON, HOUSEOFTHEDRAGON2)
        p2_list = ez.search_for_new_episode(r2.text, HOUSEOFTHEDRAGON, HOUSEOFTHEDRAGON2)
        res1 = len(p1_list[0]) + len(p2_list[0])
        res2 = len(p1_list[1]) + len(p2_list[1])
        print("\nHouse Of The Dragon {} => 1080p: {} 720p: {}\n".format(HOUSEOFTHEDRAGON3, res1, res2))
        logger.info("\nHouse Of The Dragon {} => 1080p: {} 720p: {}\n".format(HOUSEOFTHEDRAGON3, res1, res2))
        return res1 + res2

    def search_the_lord_of_the_rings_the_rings_of_power(self):
        r1 = requests.get('https://kickasstorrents.to/usearch/the-lord-of-the-rings-the-rings-of-power')
        r2 = requests.get('https://kickasstorrents.to/usearch/the-lord-of-the-rings-the-rings-of-power/2')
        p1_list = ez.search_for_new_episode(r1.text, LORDOFTHERINGSTHERINGSOFPOWER, LORDOFTHERINGSTHERINGSOFPOWER2)
        p2_list = ez.search_for_new_episode(r2.text, LORDOFTHERINGSTHERINGSOFPOWER, LORDOFTHERINGSTHERINGSOFPOWER2)
        res1 = len(p1_list[0]) + len(p2_list[0])
        res2 = len(p1_list[1]) + len(p2_list[1])
        print("\nThe Lord Of The Rings The Rings Of Power {} => 1080p: {} 720p: {}\n".format(LORDOFTHERINGSTHERINGSOFPOWER3, res1, res2))
        logger.info("\nThe Lord Of The Rings The Rings Of Power {} => 1080p: {} 720p: {}\n".format(LORDOFTHERINGSTHERINGSOFPOWER3, res1, res2))
        return res1 + res2

    def search_silo(self):
        r1 = requests.get('https://kickasstorrents.to/usearch/silo')
        r2 = requests.get('https://kickasstorrents.to/usearch/silo/2')
        p1_list = ez.search_for_new_episode(r1.text, SILO, SILO2)
        p2_list = ez.search_for_new_episode(r2.text, SILO, SILO2)
        res1 = len(p1_list[0]) + len(p2_list[0])
        res2 = len(p1_list[1]) + len(p2_list[1])
        print("\nSilo {} => 1080p: {} 720p: {}\n".format(SILO3, res1, res2))
        logger.info("\nSilo {} => 1080p: {} 720p: {}\n".format(SILO3, res1, res2))
        return res1 + res2

    def search_ahsoka(self):
        r1 = requests.get('https://kickasstorrents.to/usearch/ahsoka')
        r2 = requests.get('https://kickasstorrents.to/usearch/ahsoka/2')
        p1_list = ez.search_for_new_episode(r1.text, AHSOKA, AHSOKA2)
        p2_list = ez.search_for_new_episode(r2.text, AHSOKA, AHSOKA2)
        res1 = len(p1_list[0]) + len(p2_list[0])
        res2 = len(p1_list[1]) + len(p2_list[1])
        print("\nAhsoka {} => 1080p: {} 720p: {}\n".format(AHSOKA3, res1, res2))
        logger.info("\nAhsoka {} => 1080p: {} 720p: {}\n".format(AHSOKA3, res1, res2))
        return res1 + res2

    def search_acolyte(self):
        r1 = requests.get('https://kickasstorrents.to/usearch/star-wars-the-acolyte')
        r2 = requests.get('https://kickasstorrents.to/usearch/star-wars-the-acolyte/2')
        p1_list = ez.search_for_new_episode(r1.text, ACOLYTE, ACOLYTE2)
        p2_list = ez.search_for_new_episode(r2.text, ACOLYTE, ACOLYTE2)
        res1 = len(p1_list[0]) + len(p2_list[0])
        res2 = len(p1_list[1]) + len(p2_list[1])
        print("The Acolyte {} => 1080p: {} 720p: {}\n".format(ACOLYTE3, res1, res2))
        logger.info("The Acolyte {} => 1080p: {} 720p: {}\n".format(ACOLYTE3, res1, res2))
        return res1 + res2

    def search_lando(self):
        r1 = requests.get('https://kickasstorrents.to/usearch/star-wars-lando')
        r2 = requests.get('https://kickasstorrents.to/usearch/star-wars-lando/2')
        p1_list = ez.search_for_new_episode(r1.text, LANDO, LANDO2)
        p2_list = ez.search_for_new_episode(r2.text, LANDO, LANDO2)
        res1 = len(p1_list[0]) + len(p2_list[0])
        res2 = len(p1_list[1]) + len(p2_list[1])
        print("Lando {} => 1080p: {} 720p: {}\n".format(LANDO3, res1, res2))
        logger.info("Lando {} => 1080p: {} 720p: {}\n".format(LANDO3, res1, res2))
        return res1 + res2

    def search_droid_story(self):
        r1 = requests.get('https://kickasstorrents.to/usearch/star-wars-a-droid-story')
        r2 = requests.get('https://kickasstorrents.to/usearch/star-wars-a-droid-story/2')
        p1_list = ez.search_for_new_episode(r1.text, DROIDSTORY, DROIDSTORY2)
        p2_list = ez.search_for_new_episode(r2.text, DROIDSTORY, DROIDSTORY2)
        res1 = len(p1_list[0]) + len(p2_list[0])
        res2 = len(p1_list[1]) + len(p2_list[1])
        print("A Droid Story {} => 1080p: {} 720p: {}\n".format(DROIDSTORY3, res1, res2))
        logger.info("A Droid Story {} => 1080p: {} 720p: {}\n".format(DROIDSTORY3, res1, res2))
        return res1 + res2

    def search_groot(self):
        r1 = requests.get('https://kickasstorrents.to/usearch/i-am-groot')
        r2 = requests.get('https://kickasstorrents.to/usearch/i-am-groot/2')
        p1_list = ez.search_for_new_episode(r1.text, GROOT, GROOT2)
        p2_list = ez.search_for_new_episode(r2.text, GROOT, GROOT2)
        res1 = len(p1_list[0]) + len(p2_list[0])
        res2 = len(p1_list[1]) + len(p2_list[1])
        print("I Am Groot {} => 1080p: {} 720p: {}\n".format(GROOT3, res1, res2))
        logger.info("I Am Groot {} => 1080p: {} 720p: {}\n".format(GROOT3, res1, res2))
        return res1 + res2

    def search_marvel_wakanda(self):
        r1 = requests.get('https://kickasstorrents.to/usearch/wakanda')
        r2 = requests.get('https://kickasstorrents.to/usearch/wakanda/2')
        p1_list = ez.search_for_new_episode(r1.text, WAKANDA, WAKANDA2)
        p2_list = ez.search_for_new_episode(r2.text, WAKANDA, WAKANDA2)
        res1 = len(p1_list[0]) + len(p2_list[0])
        res2 = len(p1_list[1]) + len(p2_list[1])
        print("Wakanda {} => 1080p: {} 720p: {}\n".format(WAKANDA3, res1, res2))
        logger.info("Wakanda {} => 1080p: {} 720p: {}\n".format(WAKANDA3, res1, res2))
        return res1 + res2

    def main(self):
        v = self.search_andor()
        a = self.search_lower_decks()
        j = self.search_loki()
        b = self.search_discovery()
        c = self.search_mando()
        e = self.search_orville()
        h = self.search_for_all_man_kind()
        i = self.search_bad_batch()
        w = self.search_star_wars_visions()
        z = self.search_wheeloftime()
        y = self.search_foundation()
        t = self.search_star_trek_prodigy()
        n = self.search_book_of_boba_fett()
        xx = self.search_continental()
        t = self.search_halo()
        l = self.search_star_trek_strange_new_worlds()
        x = self.search_prehistoric_planet()
        q = self.search_obi_wan_kenobi()
        d = self.search_house_of_the_dragon()
        g = self.search_the_lord_of_the_rings_the_rings_of_power()
        k = self.search_silo()
        p = self.search_ahsoka()
        m = self.search_acolyte()
        o = self.search_lando()
        r = self.search_droid_story()
        s = self.search_groot()
        u = self.search_marvel_wakanda()
        sum1 = sum([a, b, c, d, e, g, h, i, j, k, l, m, n, o, p])
        sum2 = sum([q, u, r, s, t, v, w, x, y, z, xx])
        sum3 = sum1 + sum2
        print("Total Episodes: {}".format(sum3))

if __name__ == "__main__":
    foo = CheckForNewEpisodes()
    foo.main()

