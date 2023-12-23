import requests
import re
import os
import logging
import shows.search as search

class Ahsoka:
    def __init__(self, args, cwd):
        self.args = args
        self.AHSOKA = re.compile(r"ahsoka")
        self.AHSOKA_SEA = "s03e01"
        self.AHSOKA_SEA_REG = re.compile(self.AHSOKA_SEA)
        self.AHSOKA_EZ_1 = "https://eztv.re/search/ahsoka"
        self.AHSOKA_KA_1 = "https://kickasstorrents.to/usearch/ahsoka"
        self.AHSOKA_KA_2 = "https://kickasstorrents.to/usearch/ahsoka/2"
        self.AHSOKA_1337x_1 = "https://www.1377x.to/search/ahsoka"
        self.AHSOKA_1337x_2 = "https://www.1377x.to/search/ahsoka/2"

        self.AHSOKA_logger = logging.getLogger(__name__)
        self.AHSOKA_logger.setLevel(logging.DEBUG)
        self.file_handler = None
        addr1 = cwd + '/logs/ahsoka.log'
        if os.path.exists(addr1):
            self.file_handler = logging.FileHandler(addr1, mode='w')
            self.file_handler.setFormatter(logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s'))
            self.AHSOKA_logger.addHandler(self.file_handler)

    def search_ahsoka_ez(self):
        try:
            r1 = requests.get(self.AHSOKA_EZ_1)
            r1_resp = r1.status_code
            count = 0
            if r1_resp == 200:
                p1_list = search.Search().ez_search_for_new_episode(r1.text, self.AHSOKA_SEA, self.AHSOKA_SEA_REG)
                resp1080p = len(p1_list[0])
                resp720p = len(p1_list[1])
                count += resp1080p + resp720p
                print("\nEZ ahsoka {} => \n\tstatus: {}, \n\t1080p: {}\n\t720p: {}".format(self.AHSOKA_SEA, r1_resp, resp1080p, resp720p))
                self.AHSOKA_logger.info("\nEZ ahsoka {} => \n\tstatus: {}, \n\t1080p: {}\n\t720p: {}".format(self.AHSOKA_SEA, r1_resp, resp1080p, resp720p))
            else:
                print("\nEZ ahsoka {} => status: {}".format(self.AHSOKA_SEA, r1_resp))
                self.AHSOKA_logger.info("\nEZ ahsoka {} => status: {}".format(self.AHSOKA_SEA, r1_resp))
            return count
        except requests.exceptions.ConnectionError:
            print("ahsoka unable to connect to EZTV")
            self.AHSOKA_logger.error("ahsoka unable to connect to EZTV")
            return 0
            
    def search_ahsoka_ka(self):
        try:
            r2 = requests.get(self.AHSOKA_KA_1)
            r2_resp = r2.status_code
            r3 = requests.get(self.AHSOKA_KA_2)
            r3_resp = r3.status_code
            count = 0
            if r2_resp == 200 and r3_resp == 200:
                p1_list = search.ka_search_for_new_episode(r2.text, self.AHSOKA, self.AHSOKA_SEA_REG)
                p2_list = search.ka_search_for_new_episode(r3.text, self.AHSOKA, self.AHSOKA_SEA_REG)
                res = (len(p1_list[0]), len(p1_list[1]))
                res1 = (len(p2_list[0]), len(p2_list[1]))
                count = res[0] + res[1] + res1[0] + res1[1]
                print("KA ahsoka {} => \n\tstatus: {}\n\t1080p: {}\n\t720p: {}".format(self.AHSOKA_SEA, r3_resp, res1[0], res1[1]))
                self.AHSOKA_logger.info("KA ahsoka {} => \n\tstatus: {}\n\t1080p: {}\n\t720p: {}".format(self.AHSOKA_SEA, r3_resp, res1[0], res1[1]))
            else:
                print("KA ahsoka {} => status: {}".format(self.AHSOKA_SEA, r3_resp))
                self.AHSOKA_logger.info("KA ahsoka {} => status: {}".format(self.AHSOKA_SEA, r3_resp))
            return count
        except requests.exceptions.ConnectionError as e:
            print(e)
            self.AHSOKA_logger.error(e)
            return 0
            

    def search_ahsoka(self):
        if self.args.eztv:
            ez_count = self.search_ahsoka_ez()
            return ez_count
        elif self.args.kickass:
            ka_count = self.search_ahsoka_ka()
            return ka_count
        elif self.args.all:
            if self.args.eztv == True and self.args.kickass == True:
                print("Setting the -e and k flags are not allowed when using the --all flag")
            else:
                ez_count = self.search_ahsoka_ez()
                ka_count = self.search_ahsoka_ka()
                return ez_count + ka_count