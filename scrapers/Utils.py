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

class Acolyte:
    def __init__(self, args, cwd):
        self.args = args
        self.ACOLYTE = re.compile(r"acolyte")
        self.ACOLYTE_SEA = "s02e01"
        self.ACOLYTE_SEA_REG = re.compile(self.ACOLYTE_SEA)
        self.ACOLYTE_EZ_1 = "https://eztv.re/search/acolyte"

    def search_acolyte_ez(self):
        try:
            r1 = requests.get(self.ACOLYTE_EZ_1)
            r1_resp = r1.status_code
            count = 0
            if r1_resp == 200:
                p1_list = Search().ez_search_for_new_episode(r1.text, self.ACOLYTE_SEA, self.ACOLYTE_SEA_REG)
                resp1080p = len(p1_list[0])
                resp720p = len(p1_list[1])
                count += resp1080p + resp720p
                print("\nEZ acolyte {} => \n\tstatus: {}, \n\t1080p: {}\n\t720p: {}".format(self.ACOLYTE_SEA, r1_resp, resp1080p, resp720p))
            else:
                print("\nEZ acolyte {} => status: {}".format(self.ACOLYTE_SEA, r1_resp))
            return count
        except requests.exceptions.ConnectionError:
            print("acolyte unable to connect to EZTV")
            return 0

    def search_acolyte(self):
        if self.args.eztv:
            ez_count = self.search_acolyte_ez()
            return ez_count
        
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
        
class Andor:
    def __init__(self, args, cwd):
        self.args = args
        self.ANDOR = re.compile(r"andor")
        self.ANDOR_SEA = "s02e10"
        self.ANDOR_SEA_REG = re.compile(self.ANDOR_SEA)
        self.ANDOR_EZ_1 = "https://eztv.re/search/andor"

    def search_andor_ez(self):
        try:
            r1 = requests.get(self.ANDOR_EZ_1)
            r1_resp = r1.status_code
            count = 0
            if r1_resp == 200:
                p1_list = Search().ez_search_for_new_episode(r1.text, self.ANDOR_SEA, self.ANDOR_SEA_REG)
                resp1080p = len(p1_list[0])
                resp720p = len(p1_list[1])
                count += resp1080p + resp720p
                print("\nEZ Andor {} => \n\tstatus: {}, \n\t1080p: {}\n\t720p: {}".format(self.ANDOR_SEA, r1_resp, resp1080p, resp720p))
            else:
                print("\nEZ Andor {} => status: {}".format(self.ANDOR_SEA, r1_resp))
            return count
        except requests.exceptions.ConnectionError:
            print("Andor unable to connect to EZTV")
            return 0

    def search_andor(self):
        if self.args.eztv:
            ez_count = self.search_andor_ez()
            return ez_count
        
class BadBatch:
    def __init__(self, args, cwd):
        self.args = args
        self.BADBATCH = re.compile(r"bad batch")
        self.BADBATCH_SEA = "s04e01"
        self.BADBATCH_SEA_REG = re.compile(self.BADBATCH_SEA)
        self.BADBATCH_EZ_1 = "https://eztv.re/search/bad-batch"

    def search_badbatch_ez(self):
        try:
            r1 = requests.get(self.BADBATCH_EZ_1)
            r1_resp = r1.status_code
            count = 0
            if r1_resp == 200:
                p1_list = Search().ez_search_for_new_episode(r1.text, self.BADBATCH_SEA, self.BADBATCH_SEA_REG)
                resp1080p = len(p1_list[0])
                resp720p = len(p1_list[1])
                count += resp1080p + resp720p
                print("\nEZ badbatch {} => \n\tstatus: {}, \n\t1080p: {}\n\t720p: {}".format(self.BADBATCH_SEA, r1_resp, resp1080p, resp720p))
            else:
                print("\nEZ badbatch {} => status: {}".format(self.BADBATCH_SEA, r1_resp))
            return count
        except requests.exceptions.ConnectionError:
            print("badbatch unable to connect to EZTV")
            return 0

    def search_badbatch(self):
        if self.args.eztv:
            ez_count = self.search_badbatch_ez()
            return ez_count
        
class BookOfBobaFett:
    def __init__(self, args, cwd):
        self.args = args
        self.BOOKOFBOBAFETT = re.compile(r"book of boba fett")
        self.BOOKOFBOBAFETT_SEA = "s02e01"
        self.BOOKOFBOBAFETT_SEA_REG = re.compile(self.BOOKOFBOBAFETT_SEA)
        self.BOOKOFBOBAFETT_EZ_1 = "https://eztv.re/search/book-of-boba-fett"

    def search_bookofbobafett_ez(self):
        try:
            r1 = requests.get(self.BOOKOFBOBAFETT_EZ_1)
            r1_resp = r1.status_code
            count = 0
            if r1_resp == 200:
                p1_list = Search().ez_search_for_new_episode(r1.text, self.BOOKOFBOBAFETT_SEA, self.BOOKOFBOBAFETT_SEA_REG)
                resp1080p = len(p1_list[0])
                resp720p = len(p1_list[1])
                count += resp1080p + resp720p
                print("\nEZ bookofbobafett {} => \n\tstatus: {}, \n\t1080p: {}\n\t720p: {}".format(self.BOOKOFBOBAFETT_SEA, r1_resp, resp1080p, resp720p))
            else:
                print("\nEZ bookofbobafett {} => status: {}".format(self.BOOKOFBOBAFETT_SEA, r1_resp))
            return count
        except requests.exceptions.ConnectionError:
            print("bookofbobafett unable to connect to EZTV")
            return 0

    def search_bookofbobafett(self):
        if self.args.eztv:
            ez_count = self.search_bookofbobafett_ez()
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
        self.FOUNDATION_SEA = "s03e01"
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
        self.FUBAR_SEA = "s02e01"
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
        
class Halo:
    def __init__(self, args, cwd):
        self.args = args
        self.HALO = re.compile(r"halo")
        self.HALO_SEA = "s03e01"
        self.HALO_SEA_REG = re.compile(self.HALO_SEA)
        self.HALO_EZ_1 = "https://eztv.re/search/halo"

    def search_halo_ez(self):
        try:
            r1 = requests.get(self.HALO_EZ_1)
            r1_resp = r1.status_code
            count = 0
            if r1_resp == 200:
                p1_list = Search().ez_search_for_new_episode(r1.text, self.HALO_SEA, self.HALO_SEA_REG)
                resp1080p = len(p1_list[0])
                resp720p = len(p1_list[1])
                count += resp1080p + resp720p
                print("\nEZ halo {} => \n\tstatus: {}, \n\t1080p: {}\n\t720p: {}".format(self.HALO_SEA, r1_resp, resp1080p, resp720p))
                
            else:
                print("\nEZ halo {} => status: {}".format(self.HALO_SEA, r1_resp))
            return count
        except requests.exceptions.ConnectionError:
            print("halo unable to connect to EZTV")
            return 0

    def search_halo(self):
        if self.args.eztv:
            ez_count = self.search_halo_ez()
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
        self.PREHISTORICPLANET_SEA = "s03e01"
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

class StarTrekProdigy:
    def __init__(self, args, cwd):
        self.args = args
        self.STARTREKPRODIGY = re.compile(r"star trek prodigy")
        self.STARTREKPRODIGY_SEA = "s02e06"
        self.STARTREKPRODIGY_SEA_REG = re.compile(self.STARTREKPRODIGY_SEA)
        self.STARTREKPRODIGY_EZ_1 = "https://eztv.re/search/star-trek-prodigy"

    def search_startrekprodigy_ez(self):
        try:
            r1 = requests.get(self.STARTREKPRODIGY_EZ_1)
            r1_resp = r1.status_code
            count = 0
            if r1_resp == 200:
                p1_list = Search().ez_search_for_new_episode(r1.text, self.STARTREKPRODIGY_SEA, self.STARTREKPRODIGY_SEA_REG)
                resp1080p = len(p1_list[0])
                resp720p = len(p1_list[1])
                count += resp1080p + resp720p
                print("\nEZ startrekprodigy {} => \n\tstatus: {}, \n\t1080p: {}\n\t720p: {}".format(self.STARTREKPRODIGY_SEA, r1_resp, resp1080p, resp720p))
                
            else:
                print("\nEZ startrekprodigy {} => status: {}".format(self.STARTREKPRODIGY_SEA, r1_resp))
            return count
        except requests.exceptions.ConnectionError:
            print("startrekprodigy unable to connect to EZTV")
            return 0

    def search_startrekprodigy(self):
        if self.args.eztv:
            ez_count = self.search_startrekprodigy_ez()
            return ez_count

class StarWarsVisions:
    def __init__(self, args, cwd):
        self.args = args
        self.STARWARSVISIONS = re.compile(r"star wars visions")
        self.STARWARSVISIONS_SEA = "s03e01"
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
        self.STRANGENEWWORLDS_SEA = "s03e01"
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
        self.thelastofus_SEA = "s02e04"
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
        
class WheelOfTime:
    def __init__(self, args, cwd):
        self.args = args
        self.WHEELOFTIME = re.compile(r"wheel of time")
        self.WHEELOFTIME_SEA = "s03e09"
        self.WHEELOFTIME_SEA_REG = re.compile(self.WHEELOFTIME_SEA)
        self.WHEELOFTIME_EZ_1 = "https://eztv.re/search/wheel-of-time"

    def search_wheeloftime_ez(self):
        try:
            r1 = requests.get(self.WHEELOFTIME_EZ_1)
            r1_resp = r1.status_code
            count = 0
            if r1_resp == 200:
                p1_list = Search().ez_search_for_new_episode(r1.text, self.WHEELOFTIME_SEA, self.WHEELOFTIME_SEA_REG)
                resp1080p = len(p1_list[0])
                resp720p = len(p1_list[1])
                count += resp1080p + resp720p
                print("\nEZ wheeloftime {} => \n\tstatus: {}, \n\t1080p: {}\n\t720p: {}".format(self.WHEELOFTIME_SEA, r1_resp, resp1080p, resp720p))
                
            else:
                print("\nEZ wheeloftime {} => status: {}".format(self.WHEELOFTIME_SEA, r1_resp))
            return count
        except requests.exceptions.ConnectionError:
            print("wheeloftime unable to connect to EZTV")
            return 0

    def search_wheeloftime(self):
        if self.args.eztv:
            ez_count = self.search_wheeloftime_ez()
            return ez_count
        
class MobLand:
    def __init__(self, args, cwd):
        self.args = args
        self.MOBLAND = re.compile(r"mobland")
        self.MOBLAND_SEA = "s01e07"
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
        


        