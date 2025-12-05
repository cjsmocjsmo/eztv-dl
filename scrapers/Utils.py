import requests
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
                        # print(meta)
                        list1080p.append(meta)
                    elif re.search(self.SEV_P, ltitle) != None:
                        list720p.append(meta)
                    else:
                        pass
        return (list1080p, list720p)

class Ahsoka:
    def __init__(self, args, cwd):
        self.args = args
        self.AHSOKA = re.compile(r"ahsoka")
        self.AHSOKA_SEA = "s02e01"
        self.AHSOKA_SEA_REG = re.compile(self.AHSOKA_SEA)
        self.AHSOKA_EZ_1 = "https://eztv.re/search/ahsoka"

    def search_ahsoka_ez(self):
        try:
            r1 = requests.get(self.AHSOKA_EZ_1)
            r1_resp = r1.status_code
            count = 0
            if r1_resp == 200:
                p1_list = Search().ez_search_for_new_episode(r1.text, self.AHSOKA_SEA, self.AHSOKA_SEA_REG)
                resp1080p = len(p1_list[0])
                resp720p = len(p1_list[1])
                count += resp1080p + resp720p
                print("\nEZ ahsoka {} => \n\tstatus: {}, \n\t1080p: {}\n\t720p: {}".format(self.AHSOKA_SEA, r1_resp, resp1080p, resp720p))
            else:
                print("\nEZ ahsoka {} => status: {}".format(self.AHSOKA_SEA, r1_resp))
            return count
        except requests.exceptions.ConnectionError:
            print("ahsoka unable to connect to EZTV")
            return 0

    def search_ahsoka(self):
        if self.args.eztv:
            ez_count = self.search_ahsoka_ez()
            return ez_count
        
class Fallout:
    def __init__(self, args, cwd):
        self.args = args
        self.fallout = re.compile(r"fallout")
        self.fallout_SEA = "s02e01"
        self.fallout_SEA_REG = re.compile(self.fallout_SEA)
        self.fallout_EZ_1 = "https://eztv.re/search/fallout"

    def search_fallout_ez(self):
        try:
            r1 = requests.get(self.fallout_EZ_1)
            r1_resp = r1.status_code
            count = 0
            if r1_resp == 200:
                p1_list = Search().ez_search_for_new_episode(r1.text, self.fallout_SEA, self.fallout_SEA_REG)
                resp1080p = len(p1_list[0])
                resp720p = len(p1_list[1])
                count += resp1080p + resp720p
                print("\nEZ fallout {} => \n\tstatus: {}, \n\t1080p: {}\n\t720p: {}".format(self.fallout_SEA, r1_resp, resp1080p, resp720p))
                
            else:
                print("\nEZ fallout {} => status: {}".format(self.fallout_SEA, r1_resp))
            return count
        except requests.exceptions.ConnectionError:
            print("fallout unable to connect to EZTV")
            return 0

    def search_fallout(self):
        if self.args.eztv:
            ez_count = self.search_fallout_ez()
            return ez_count
        
class ForAllMankind:
    def __init__(self, args, cwd):
        self.args = args
        self.FORALLMANKIND = re.compile(r"for all mankind")
        self.FORALLMANKIND_SEA = "s05e01"
        self.FORALLMANKIND_SEA_REG = re.compile(self.FORALLMANKIND_SEA)
        self.FORALLMANKIND_EZ_1 = "https://eztv.re/search/for-all-mankind"

    def search_forallmankind_ez(self):
        try:
            r1 = requests.get(self.FORALLMANKIND_EZ_1)
            r1_resp = r1.status_code
            count = 0
            if r1_resp == 200:
                p1_list = Search().ez_search_for_new_episode(r1.text, self.FORALLMANKIND_SEA, self.FORALLMANKIND_SEA_REG)
                resp1080p = len(p1_list[0])
                resp720p = len(p1_list[1])
                count += resp1080p + resp720p
                print("\nEZ forallmankind {} => \n\tstatus: {}, \n\t1080p: {}\n\t720p: {}".format(self.FORALLMANKIND_SEA, r1_resp, resp1080p, resp720p))
                
            else:
                print("\nEZ forallmankind {} => status: {}".format(self.FORALLMANKIND_SEA, r1_resp))
            return count
        except requests.exceptions.ConnectionError:
            print("forallmankind unable to connect to EZTV")
            return 0

    def search_forallmankind(self):
        if self.args.eztv:
            ez_count = self.search_forallmankind_ez()
            return ez_count
        
class Foundation:
    def __init__(self, args, cwd):
        self.args = args
        self.FOUNDATION = re.compile(r"foundation")
        self.FOUNDATION_SEA = "s04e01"
        self.FOUNDATION_SEA_REG = re.compile(self.FOUNDATION_SEA)
        self.FOUNDATION_EZ_1 = "https://eztv.re/search/foundation"

    def search_foundation_ez(self):
        try:
            r1 = requests.get(self.FOUNDATION_EZ_1)
            r1_resp = r1.status_code
            count = 0
            if r1_resp == 200:
                p1_list = Search().ez_search_for_new_episode(r1.text, self.FOUNDATION_SEA, self.FOUNDATION_SEA_REG)
                resp1080p = len(p1_list[0])
                resp720p = len(p1_list[1])
                count += resp1080p + resp720p
                print("\nEZ foundation {} => \n\tstatus: {}, \n\t1080p: {}\n\t720p: {}".format(self.FOUNDATION_SEA, r1_resp, resp1080p, resp720p))
                
            else:
                print("\nEZ foundation {} => status: {}".format(self.FOUNDATION_SEA, r1_resp))
            return count
        except requests.exceptions.ConnectionError:
            print("foundation unable to connect to EZTV")
            return 0

    def search_foundation(self):
        if self.args.eztv:
            ez_count = self.search_foundation_ez()
            return ez_count
        
class Fubar:
    def __init__(self, args, cwd):
        self.args = args
        self.FUBAR = re.compile(r"fubar")
        self.FUBAR_SEA = "s03e01"
        self.FUBAR_SEA_REG = re.compile(self.FUBAR_SEA)
        self.FUBAR_EZ_1 = "https://eztv.re/search/fubar"

    def search_fubar_ez(self):
        try:
            r1 = requests.get(self.FUBAR_EZ_1)
            r1_resp = r1.status_code
            count = 0
            if r1_resp == 200:
                p1_list = Search().ez_search_for_new_episode(r1.text, self.FUBAR_SEA, self.FUBAR_SEA_REG)
                resp1080p = len(p1_list[0])
                resp720p = len(p1_list[1])
                count += resp1080p + resp720p
                print("\nEZ fubar {} => \n\tstatus: {}, \n\t1080p: {}\n\t720p: {}".format(self.FUBAR_SEA, r1_resp, resp1080p, resp720p))
                
            else:
                print("\nEZ fubar {} => status: {}".format(self.FUBAR_SEA, r1_resp))
            return count
        except requests.exceptions.ConnectionError:
            print("fubar unable to connect to EZTV")
            return 0

    def search_fubar(self):
        if self.args.eztv:
            ez_count = self.search_fubar_ez()
            return ez_count

class HouseOfTheDragon:
    def __init__(self, args, cwd):
        self.args = args
        self.HOUSEOFTHEDRAGON = re.compile(r"house of the dragon")
        self.HOUSEOFTHEDRAGON_SEA = "s03e01"
        self.HOUSEOFTHEDRAGON_SEA_REG = re.compile(self.HOUSEOFTHEDRAGON_SEA)
        self.HOUSEOFTHEDRAGON_EZ_1 = "https://eztv.re/search/house-of-the-dragon"

    def search_houseofthedragon_ez(self):
        try:
            r1 = requests.get(self.HOUSEOFTHEDRAGON_EZ_1)
            r1_resp = r1.status_code
            count = 0
            if r1_resp == 200:
                p1_list = Search().ez_search_for_new_episode(r1.text, self.HOUSEOFTHEDRAGON_SEA, self.HOUSEOFTHEDRAGON_SEA_REG)
                resp1080p = len(p1_list[0])
                resp720p = len(p1_list[1])
                count += resp1080p + resp720p
                print("\nEZ houseofthedragon {} => \n\tstatus: {}, \n\t1080p: {}\n\t720p: {}".format(self.HOUSEOFTHEDRAGON_SEA, r1_resp, resp1080p, resp720p))
                
            else:
                print("\nEZ houseofthedragon {} => status: {}".format(self.HOUSEOFTHEDRAGON_SEA, r1_resp))
            return count
        except requests.exceptions.ConnectionError:
            print("houseofthedragon unable to connect to EZTV")
            return 0

    def search_houseofthedragon(self):
        if self.args.eztv:
            ez_count = self.search_houseofthedragon_ez()
            return ez_count

class Mandilorian:
    def __init__(self, args, cwd):
        self.args = args
        self.MANDILORIAN_= re.compile(r"mandilorian")
        self.MANDILORIAN_SEA = "s04e01"
        self.MANDILORIAN_SEA_REG = re.compile(self.MANDILORIAN_SEA)
        self.MANDILORIAN_EZ_1 = "https://eztv.re/search/mandilorian"

    def search_mandilorian_ez(self):
        try:
            r1 = requests.get(self.MANDILORIAN_EZ_1)
            r1_resp = r1.status_code
            count = 0
            if r1_resp == 200:
                p1_list = Search().ez_search_for_new_episode(r1.text, self.MANDILORIAN_SEA, self.MANDILORIAN_SEA_REG)
                resp1080p = len(p1_list[0])
                resp720p = len(p1_list[1])
                count += resp1080p + resp720p
                print("\nEZ mandilorian {} => \n\tstatus: {}, \n\t1080p: {}\n\t720p: {}".format(self.MANDILORIAN_SEA, r1_resp, resp1080p, resp720p))
                
            else:
                print("\nEZ mandilorian {} => status: {}".format(self.MANDILORIAN_SEA, r1_resp))
            return count
        except requests.exceptions.ConnectionError:
            print("mandilorian unable to connect to EZTV")
            return 0

    def search_mandilorian(self):
        if self.args.eztv:
            ez_count = self.search_mandilorian_ez()
            return ez_count

class MonarchLegacyOfMonsters:
    def __init__(self, args, cwd):
        self.args = args
        self.MONARCHLEGACYOFMONSTERS = re.compile(r"monarch legacy of monsters")
        self.MONARCHLEGACYOFMONSTERS_SEA = "s02e01"
        self.MONARCHLEGACYOFMONSTERS_SEA_REG = re.compile(self.MONARCHLEGACYOFMONSTERS_SEA)
        self.MONARCHLEGACYOFMONSTERS_EZ_1 = "https://eztv.re/search/monarch-legacy-of-monsters"

    def search_monarchlegacyofmonsters_ez(self):
        try:
            r1 = requests.get(self.MONARCHLEGACYOFMONSTERS_EZ_1)
            r1_resp = r1.status_code
            count = 0
            if r1_resp == 200:
                p1_list = Search().ez_search_for_new_episode(r1.text, self.MONARCHLEGACYOFMONSTERS_SEA, self.MONARCHLEGACYOFMONSTERS_SEA_REG)
                resp1080p = len(p1_list[0])
                resp720p = len(p1_list[1])
                count += resp1080p + resp720p
                print("\nEZ monarchlegacyofmonsters {} => \n\tstatus: {}, \n\t1080p: {}\n\t720p: {}".format(self.MONARCHLEGACYOFMONSTERS_SEA, r1_resp, resp1080p, resp720p))

            else:
                print("\nEZ monarchlegacyofmonsters {} => status: {}".format(self.MONARCHLEGACYOFMONSTERS_SEA, r1_resp))

            return count
        except requests.exceptions.ConnectionError:
            print("monarchlegacyofmonsters unable to connect to EZTV")
            return 0

    def search_monarchlegacyofmonsters(self):
        if self.args.eztv:
            ez_count = self.search_monarchlegacyofmonsters_ez()
            return ez_count
        
class ObiWanKenobi:
    def __init__(self, args, cwd):
        self.args = args
        self.OBIWANKENOBI = re.compile(r"obi wan kenobi")
        self.OBIWANKENOBI_SEA = "s02e01"
        self.OBIWANKENOBI_SEA_REG = re.compile(self.OBIWANKENOBI_SEA)
        self.OBIWANKENOBI_EZ_1 = "https://eztv.re/search/obi-wan-kenobi"

    def search_obiwankenobi_ez(self):
        try:
            r1 = requests.get(self.OBIWANKENOBI_EZ_1)
            r1_resp = r1.status_code
            count = 0
            if r1_resp == 200:
                p1_list = Search().ez_search_for_new_episode(r1.text, self.OBIWANKENOBI_SEA, self.OBIWANKENOBI_SEA_REG)
                resp1080p = len(p1_list[0])
                resp720p = len(p1_list[1])
                count += resp1080p + resp720p
                print("\nEZ obiwankenobi {} => \n\tstatus: {}, \n\t1080p: {}\n\t720p: {}".format(self.OBIWANKENOBI_SEA, r1_resp, resp1080p, resp720p))
                
            else:
                print("\nEZ obiwankenobi {} => status: {}".format(self.OBIWANKENOBI_SEA, r1_resp))
            return count
        except requests.exceptions.ConnectionError:
            print("obiwankenobi unable to connect to EZTV")
            return 0

    def search_obiwankenobi(self):
        if self.args.eztv:
            ez_count = self.search_obiwankenobi_ez()
            return ez_count

class Orville:
    def __init__(self, args, cwd):
        self.args = args
        self.ORVILLE = re.compile(r"orville")
        self.ORVILLE_SEA = "s04e01"
        self.ORVILLE_SEA_REG = re.compile(self.ORVILLE_SEA)
        self.ORVILLE_EZ_1 = "https://eztv.re/search/orville"

    def search_orville_ez(self):
        try:
            r1 = requests.get(self.ORVILLE_EZ_1)
            r1_resp = r1.status_code
            count = 0
            if r1_resp == 200:
                p1_list = Search().ez_search_for_new_episode(r1.text, self.ORVILLE, self.ORVILLE_SEA_REG)
                resp1080p = len(p1_list[0])
                resp720p = len(p1_list[1])
                count += resp1080p + resp720p
                print("\nEZ orville {} => \n\tstatus: {}, \n\t1080p: {}\n\t720p: {}".format(self.ORVILLE_SEA, r1_resp, resp1080p, resp720p))
                
            else:
                print("\nEZ orville {} => status: {}".format(self.ORVILLE_SEA, r1_resp))
            return count
        except requests.exceptions.ConnectionError:
            print("orville unable to connect to EZTV")
            return 0

    def search_orville(self):
        if self.args.eztv:
            ez_count = self.search_orville_ez()
            return ez_count

class PrehistoricPlanet:
    def __init__(self, args, cwd):
        self.args = args
        self.PREHISTORICPLANET = re.compile(r"prehistoric planet")
        self.PREHISTORICPLANET_SEA = "s04e01"
        self.PREHISTORICPLANET_SEA_REG = re.compile(self.PREHISTORICPLANET_SEA)
        self.PREHISTORICPLANET_EZ_1 = "https://eztv.re/search/prehistoric-planet"

    def search_prehistoricplanet_ez(self):
        try:
            r1 = requests.get(self.PREHISTORICPLANET_EZ_1)
            r1_resp = r1.status_code
            count = 0
            if r1_resp == 200:
                p1_list = Search().ez_search_for_new_episode(r1.text, self.PREHISTORICPLANET, self.PREHISTORICPLANET_SEA_REG)
                resp1080p = len(p1_list[0])
                resp720p = len(p1_list[1])
                count += resp1080p + resp720p
                print("\nEZ prehistoricplanet {} => \n\tstatus: {}, \n\t1080p: {}\n\t720p: {}".format(self.PREHISTORICPLANET_SEA, r1_resp, resp1080p, resp720p))
                
            else:
                print("\nEZ prehistoricplanet {} => status: {}".format(self.PREHISTORICPLANET_SEA, r1_resp))
            return count
        except requests.exceptions.ConnectionError:
            print("prehistoricplanet unable to connect to EZTV")
            return 0

    def search_prehistoricplanet(self):
        if self.args.eztv:
            ez_count = self.search_prehistoricplanet_ez()
            return ez_count
        
class Shogun:
    def __init__(self, args, cwd):
        self.args = args
        self.shogun = re.compile(r"shogun")
        self.shogun_SEA = "s02e01"
        self.shogun_SEA_REG = re.compile(self.shogun_SEA)
        self.shogun_EZ_1 = "https://eztv.re/search/shogun-2024"

    def search_shogun_ez(self):
        try:
            r1 = requests.get(self.shogun_EZ_1)
            r1_resp = r1.status_code
            count = 0
            if r1_resp == 200:
                p1_list = Search().ez_search_for_new_episode(r1.text, self.shogun_SEA, self.shogun_SEA_REG)
                resp1080p = len(p1_list[0])
                resp720p = len(p1_list[1])
                count += resp1080p + resp720p
                print("\nEZ shogun {} => \n\tstatus: {}, \n\t1080p: {}\n\t720p: {}".format(self.shogun_SEA, r1_resp, resp1080p, resp720p))
            else:    
                print("\nEZ shogun {} => status: {}".format(self.shogun_SEA, r1_resp))
            return count
        except requests.exceptions.ConnectionError:
            print("shogun unable to connect to EZTV")
            return 0

    def search_shogun(self):
        if self.args.eztv:
            ez_count = self.search_shogun_ez()
            return ez_count

class Silo:
    def __init__(self, args, cwd):
        self.args = args
        self.silo = re.compile(r"silo")
        self.silo_SEA = "s03e01"
        self.silo_SEA_REG = re.compile(self.silo_SEA)
        self.silo_EZ_1 = "https://eztv.re/search/silo"

    def search_silo_ez(self):
        try:
            r1 = requests.get(self.silo_EZ_1)
            r1_resp = r1.status_code
            count = 0
            if r1_resp == 200:
                p1_list = Search().ez_search_for_new_episode(r1.text, self.silo_SEA, self.silo_SEA_REG)
                resp1080p = len(p1_list[0])
                resp720p = len(p1_list[1])
                count += resp1080p + resp720p
                print("\nEZ silo {} => \n\tstatus: {}, \n\t1080p: {}\n\t720p: {}".format(self.silo_SEA, r1_resp, resp1080p, resp720p))
            else:
                print("\nEZ silo {} => status: {}".format(self.silo_SEA, r1_resp))
            return count
        except requests.exceptions.ConnectionError:
            print("silo unable to connect to EZTV")
            return 0

    def search_silo(self):
        if self.args.eztv:
            ez_count = self.search_silo_ez()
            return ez_count

class SkeletonCrew:
    def __init__(self, args, cwd):
        self.args = args
        self.skeletoncrew = re.compile(r"skeletoncrew")
        self.skeletoncrew_SEA = "s02e01"
        self.skeletoncrew_SEA_REG = re.compile(self.skeletoncrew_SEA)
        self.skeletoncrew_EZ_1 = "https://eztv.re/search/skeleton-crew"

    def search_skeletoncrew_ez(self):
        try:
            r1 = requests.get(self.skeletoncrew_EZ_1)
            r1_resp = r1.status_code
            count = 0
            if r1_resp == 200:
                p1_list = Search().ez_search_for_new_episode(r1.text, self.skeletoncrew_SEA, self.skeletoncrew_SEA_REG)
                resp1080p = len(p1_list[0])
                resp720p = len(p1_list[1])
                count += resp1080p + resp720p
                print("\nEZ skeletoncrew {} => \n\tstatus: {}, \n\t1080p: {}\n\t720p: {}".format(self.skeletoncrew_SEA, r1_resp, resp1080p, resp720p))
            else:
                print("\nEZ skeletoncrew {} => status: {}".format(self.skeletoncrew_SEA, r1_resp))
            return count
        except requests.exceptions.ConnectionError:
            print("skeletoncrew unable to connect to EZTV")
            return 0

    def search_skeletoncrew(self):
        if self.args.eztv:
            ez_count = self.search_skeletoncrew_ez()
            return ez_count

class StarWarsVisions:
    def __init__(self, args, cwd):
        self.args = args
        self.STARWARSVISIONS = re.compile(r"star wars visions")
        self.STARWARSVISIONS_SEA = "s04e01"
        self.STARWARSVISIONS_SEA_REG = re.compile(self.STARWARSVISIONS_SEA)
        self.STARWARSVISIONS_EZ_1 = "https://eztv.re/search/star-wars-visions"

    def search_starwarsvisions_ez(self):
        try:
            r1 = requests.get(self.STARWARSVISIONS_EZ_1)
            r1_resp = r1.status_code
            count = 0
            if r1_resp == 200:
                p1_list = Search().ez_search_for_new_episode(r1.text, self.STARWARSVISIONS_SEA, self.STARWARSVISIONS_SEA_REG)
                resp1080p = len(p1_list[0])
                resp720p = len(p1_list[1])
                count += resp1080p + resp720p
                print("\nEZ starwarsvisions {} => \n\tstatus: {}, \n\t1080p: {}\n\t720p: {}".format(self.STARWARSVISIONS_SEA, r1_resp, resp1080p, resp720p))
                
            else:
                print("\nEZ starwarsvisions {} => status: {}".format(self.STARWARSVISIONS_SEA, r1_resp))
            return count
        except requests.exceptions.ConnectionError:
            print("starwarsvisions unable to connect to EZTV")
            return 0

    def search_starwarsvisions(self):
        if self.args.eztv:
            ez_count = self.search_starwarsvisions_ez()
            return ez_count

class StrangeNewWorlds:
    def __init__(self, args, cwd):
        self.args = args
        self.STRANGENEWWORLDS = re.compile(r"strange new worlds")
        self.STRANGENEWWORLDS_SEA = "s04e01"
        self.STRANGENEWWORLDS_SEA_REG = re.compile(self.STRANGENEWWORLDS_SEA)
        self.STRANGENEWWORLDS_EZ_1 = "https://eztv.re/search/strange-new-worlds"

    def search_strangenewworlds_ez(self):
        try:
            r1 = requests.get(self.STRANGENEWWORLDS_EZ_1)
            r1_resp = r1.status_code
            count = 0
            if r1_resp == 200:
                p1_list = Search().ez_search_for_new_episode(r1.text, self.STRANGENEWWORLDS_SEA, self.STRANGENEWWORLDS_SEA_REG)
                resp1080p = len(p1_list[0])
                resp720p = len(p1_list[1])
                count += resp1080p + resp720p
                print("\nEZ strangenewworlds {} => \n\tstatus: {}, \n\t1080p: {}\n\t720p: {}".format(self.STRANGENEWWORLDS_SEA, r1_resp, resp1080p, resp720p))
                
            else:
                print("\nEZ strangenewworlds {} => status: {}".format(self.STRANGENEWWORLDS_SEA, r1_resp))
            return count
        except requests.exceptions.ConnectionError:
            print("strangenewworlds unable to connect to EZTV")
            return 0

    def search_strangenewworlds(self):
        if self.args.eztv:
            ez_count = self.search_strangenewworlds_ez()
            return ez_count
        
class TheLastOfUs:
    def __init__(self, args, cwd):
        self.args = args
        self.thelastofus = re.compile(r"thelastofus")
        self.thelastofus_SEA = "s03e01"
        self.thelastofus_SEA_REG = re.compile(self.thelastofus_SEA)
        self.thelastofus_EZ_1 = "https://eztv.re/search/the-last-of-us"

    def search_thelastofus_ez(self):
        try:
            r1 = requests.get(self.thelastofus_EZ_1)
            r1_resp = r1.status_code
            count = 0
            if r1_resp == 200:
                p1_list = Search().ez_search_for_new_episode(r1.text, self.thelastofus_SEA, self.thelastofus_SEA_REG)
                resp1080p = len(p1_list[0])
                resp720p = len(p1_list[1])
                count += resp1080p + resp720p
                print("\nEZ thelastofus {} => \n\tstatus: {}, \n\t1080p: {}\n\t720p: {}".format(self.thelastofus_SEA, r1_resp, resp1080p, resp720p))
                
            else:
                print("\nEZ thelastofus {} => status: {}".format(self.thelastofus_SEA, r1_resp))
            return count
        except requests.exceptions.ConnectionError:
            print("thelastofus unable to connect to EZTV")
            return 0

    def search_thelastofus(self):
        if self.args.eztv:
            ez_count = self.search_thelastofus_ez()
            return ez_count
        
class MobLand:
    def __init__(self, args, cwd):
        self.args = args
        self.MOBLAND = re.compile(r"mobland")
        self.MOBLAND_SEA = "s02e01"
        self.MOBLAND_SEA_REG = re.compile(self.MOBLAND_SEA)
        self.MOBLAND_EZ_1 = "https://eztv.re/search/mobland"

    def search_mobland_ez(self):
        try:
            r1 = requests.get(self.MOBLAND_EZ_1)
            r1_resp = r1.status_code
            count = 0
            if r1_resp == 200:
                p1_list = Search().ez_search_for_new_episode(r1.text, self.MOBLAND_SEA, self.MOBLAND_SEA_REG)
                resp1080p = len(p1_list[0])
                resp720p = len(p1_list[1])
                count += resp1080p + resp720p
                print("\nEZ mobland {} => \n\tstatus: {}, \n\t1080p: {}\n\t720p: {}".format(self.MOBLAND_SEA, r1_resp, resp1080p, resp720p))
                
            else:
                print("\nEZ mobland {} => status: {}".format(self.MOBLAND_SEA, r1_resp))
            return count
        except requests.exceptions.ConnectionError:
            print("mobland unable to connect to EZTV")
            return 0

    def search_mobland(self):
        if self.args.eztv:
            ez_count = self.search_mobland_ez()
            return ez_count
        
class IronHeart:
    def __init__(self, args, cwd):
        self.args = args
        self.IRONHEART = re.compile(r"iron heart")
        self.IRONHEART_SEA = "s02e01"
        self.IRONHEART_SEA_REG = re.compile(self.IRONHEART_SEA)
        self.IRONHEART_EZ_1 = "https://eztv.re/search/ironheart"

    def search_ironheart_ez(self):
        try:
            r1 = requests.get(self.IRONHEART_EZ_1)
            r1_resp = r1.status_code
            count = 0
            if r1_resp == 200:
                p1_list = Search().ez_search_for_new_episode(r1.text, self.IRONHEART_SEA, self.IRONHEART_SEA_REG)
                resp1080p = len(p1_list[0])
                resp720p = len(p1_list[1])
                count += resp1080p + resp720p
                print("\nEZ ironheart {} => \n\tstatus: {}, \n\t1080p: {}\n\t720p: {}".format(self.IRONHEART_SEA, r1_resp, resp1080p, resp720p))
                
            else:
                print("\nEZ ironheart {} => status: {}".format(self.IRONHEART_SEA, r1_resp))
            return count
        except requests.exceptions.ConnectionError:
            print("ironheart unable to connect to EZTV")
            return 0

    def search_ironheart(self):
        if self.args.eztv:
            ez_count = self.search_ironheart_ez()
            return ez_count

class Wednesday:
    def __init__(self, args, cwd):
        self.args = args
        self.WEDNESDAY = re.compile(r"wednesday")
        self.WEDNESDAY_SEA = "s03e01"
        self.WEDNESDAY_SEA_REG = re.compile(self.WEDNESDAY_SEA)
        self.WEDNESDAY_EZ_1 = "https://eztv.re/search/wednesday"

    def search_wednesday_ez(self):
        try:
            r1 = requests.get(self.WEDNESDAY_EZ_1)
            r1_resp = r1.status_code
            count = 0
            if r1_resp == 200:
                p1_list = Search().ez_search_for_new_episode(r1.text, self.WEDNESDAY_SEA, self.WEDNESDAY_SEA_REG)
                resp1080p = len(p1_list[0])
                resp720p = len(p1_list[1])
                count += resp1080p + resp720p
                print("\nEZ wednesday {} => \n\tstatus: {}, \n\t1080p: {}\n\t720p: {}".format(self.WEDNESDAY_SEA, r1_resp, resp1080p, resp720p))

            else:
                print("\nEZ wednesday {} => status: {}".format(self.WEDNESDAY_SEA, r1_resp))
            return count
        except requests.exceptions.ConnectionError:
            print("wednesday unable to connect to EZTV")
            return 0

    def search_wednesday(self):
        if self.args.eztv:
            ez_count = self.search_wednesday_ez()
            return ez_count

class NCIS:
    def __init__(self, args, cwd):
        self.args = args
        self.NCIS = re.compile(r"ncis")
        self.NCIS_SEA = "s23e08"
        self.NCIS_SEA_REG = re.compile(self.NCIS_SEA)
        self.NCIS_EZ_1 = "https://eztv.re/search/ncis"

    def search_ncis_ez(self):
        try:
            r1 = requests.get(self.NCIS_EZ_1)
            r1_resp = r1.status_code
            count = 0
            if r1_resp == 200:
                p1_list = Search().ez_search_for_new_episode(r1.text, self.NCIS_SEA, self.NCIS_SEA_REG)
                resp1080p = len(p1_list[0])
                resp720p = len(p1_list[1])
                count += resp1080p + resp720p
                print("\nEZ ncis {} => \n\tstatus: {}, \n\t1080p: {}\n\t720p: {}".format(self.NCIS_SEA, r1_resp, resp1080p, resp720p))

            else:
                print("\nEZ ncis {} => status: {}".format(self.NCIS_SEA, r1_resp))
            return count
        except requests.exceptions.ConnectionError:
            print("ncis unable to connect to EZTV")
            return 0

    def search_ncis(self):
        if self.args.eztv:
            ez_count = self.search_ncis_ez()
            return ez_count

class NCISSydney:
    def __init__(self, args, cwd):
        self.args = args
        self.NCISSYDNEY = re.compile(r"NCIS-Sydney")
        self.NCISSYDNEY_SEA = "s03e08"
        self.NCISSYDNEY_SEA_REG = re.compile(self.NCISSYDNEY_SEA)
        self.NCISSYDNEY_EZ_1 = "https://eztv.re/search/ncis-sydney"

    def search_ncissydney_ez(self):
        try:
            r1 = requests.get(self.NCISSYDNEY_EZ_1)
            r1_resp = r1.status_code
            count = 0
            if r1_resp == 200:
                p1_list = Search().ez_search_for_new_episode(r1.text, self.NCISSYDNEY_SEA, self.NCISSYDNEY_SEA_REG)
                resp1080p = len(p1_list[0])
                resp720p = len(p1_list[1])
                count += resp1080p + resp720p
                print("\nEZ NCIS-Sydney {} => \n\tstatus: {}, \n\t1080p: {}\n\t720p: {}".format(self.NCISSYDNEY_SEA, r1_resp, resp1080p, resp720p))

            else:
                print("\nEZ NCIS-Sydney {} => status: {}".format(self.NCISSYDNEY_SEA, r1_resp))
            return count
        except requests.exceptions.ConnectionError:
            print("NCIS-Sydney unable to connect to EZTV")
            return 0

    def search_ncissydney(self):
        if self.args.eztv:
            ez_count = self.search_ncissydney_ez()
            return ez_count

class NCISOrigins:
    def __init__(self, args, cwd):
        self.args = args
        self.NCISORIGINS = re.compile(r"NCIS-Origins")
        self.NCISORIGINS_SEA = "s02e08"
        self.NCISORIGINS_SEA_REG = re.compile(self.NCISORIGINS_SEA)
        self.NCISORIGINS_EZ_1 = "https://eztv.re/search/ncis-origins"

    def search_ncisorigins_ez(self):
        try:
            r1 = requests.get(self.NCISORIGINS_EZ_1)
            r1_resp = r1.status_code
            count = 0
            if r1_resp == 200:
                p1_list = Search().ez_search_for_new_episode(r1.text, self.NCISORIGINS_SEA, self.NCISORIGINS_SEA_REG)
                resp1080p = len(p1_list[0])
                resp720p = len(p1_list[1])
                count += resp1080p + resp720p
                print("\nEZ NCIS-Origins {} => \n\tstatus: {}, \n\t1080p: {}\n\t720p: {}".format(self.NCISORIGINS_SEA, r1_resp, resp1080p, resp720p))

            else:
                print("\nEZ NCIS-Origins {} => status: {}".format(self.NCISORIGINS_SEA, r1_resp))
            return count
        except requests.exceptions.ConnectionError:
            print("NCIS-Origins unable to connect to EZTV")
            return 0

    def search_ncisorigins(self):
        if self.args.eztv:
            ez_count = self.search_ncisorigins_ez()
            return ez_count

class TonyAndZiva:
    def __init__(self, args, cwd):
        self.args = args
        self.TONIANDZIVA = re.compile(r"NCIS-Tony-and-Ziva")
        self.TONIANDZIVA_SEA = "s02e01"
        self.TONIANDZIVA_SEA_REG = re.compile(self.TONIANDZIVA_SEA)
        self.TONIANDZIVA_EZ_1 = "https://eztv.re/search/ncis-tony-and-ziva"

    def search_tonyandziva_ez(self):
        try:
            r1 = requests.get(self.TONIANDZIVA_EZ_1)
            r1_resp = r1.status_code
            count = 0
            if r1_resp == 200:
                p1_list = Search().ez_search_for_new_episode(r1.text, self.TONIANDZIVA_SEA, self.TONIANDZIVA_SEA_REG)
                resp1080p = len(p1_list[0])
                resp720p = len(p1_list[1])
                count += resp1080p + resp720p
                print("\nEZ NCIS-Tony-and-Ziva {} => \n\tstatus: {}, \n\t1080p: {}\n\t720p: {}".format(self.TONIANDZIVA_SEA, r1_resp, resp1080p, resp720p))

            else:
                print("\nEZ NCIS-Tony-and-Ziva {} => status: {}".format(self.TONIANDZIVA_SEA, r1_resp))
            return count
        except requests.exceptions.ConnectionError:
            print("NCIS-Tony-and-Ziva unable to connect to EZTV")
            return 0

    def search_tonyandziva(self):
        if self.args.eztv:
            ez_count = self.search_tonyandziva_ez()
            return ez_count

class DMV:
    def __init__(self, args, cwd):
        self.args = args
        self.DMV = re.compile(r"DMV")
        self.DMV_SEA = "s01e09"
        self.DMV_SEA_REG = re.compile(self.DMV_SEA)
        self.DMV_EZ_1 = "https://eztv.re/search/dmv"

    def search_dmv_ez(self):
        try:
            r1 = requests.get(self.DMV_EZ_1)
            r1_resp = r1.status_code
            count = 0
            if r1_resp == 200:
                p1_list = Search().ez_search_for_new_episode(r1.text, self.DMV_SEA, self.DMV_SEA_REG)
                resp1080p = len(p1_list[0])
                resp720p = len(p1_list[1])
                count += resp1080p + resp720p
                print("\nEZ DMV {} => \n\tstatus: {}, \n\t1080p: {}\n\t720p: {}".format(self.DMV_SEA, r1_resp, resp1080p, resp720p))

            else:
                print("\nEZ DMV {} => status: {}".format(self.DMV_SEA, r1_resp))
            return count
        except requests.exceptions.ConnectionError:
            print("DMV unable to connect to EZTV")
            return 0

    def search_dmv(self):
        if self.args.eztv:
            ez_count = self.search_dmv_ez()
            return ez_count
