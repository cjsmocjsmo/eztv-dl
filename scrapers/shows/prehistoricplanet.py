import requests
import re
import os
import logging
import shows.search as search

class PrehistoricPlanet:
    def __init__(self, args, cwd):
        self.args = args
        self.PREHISTORICPLANET = re.compile(r"prehistoric planet")
        self.PREHISTORICPLANET_SEA = "s03e01"
        self.PREHISTORICPLANET_SEA_REG = re.compile(self.PREHISTORICPLANET_SEA)
        self.PREHISTORICPLANET_EZ_1 = "https://eztv.re/search/prehistoric-planet"
        self.PREHISTORICPLANET_KA_1 = "https://kickasstorrents.to/usearch/prehistoricplanet"
        self.PREHISTORICPLANET_KA_2 = "https://kickasstorrents.to/usearch/prehistoricplanet/2"
        self.PREHISTORICPLANET_1337x_1 = "https://www.1377x.to/search/prehistoricplanet"
        self.PREHISTORICPLANET_1337x_2 = "https://www.1377x.to/search/prehistoricplanet/2"

        self.PREHISTORICPLANET_logger = logging.getLogger(__name__)
        self.PREHISTORICPLANET_logger.setLevel(logging.DEBUG)
        self.file_handler = None
        addr1 = cwd + '/logs/prehistoricplanet.log'
        if os.path.exists(addr1):
            self.file_handler = logging.FileHandler(addr1, mode='w')
            self.file_handler.setFormatter(logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s'))
            self.PREHISTORICPLANET_logger.addHandler(self.file_handler)
        else:
            # create addr1
            with open(addr1, 'w') as f:
                pass
            self.file_handler = logging.FileHandler(addr1, mode='w')
            self.file_handler.setFormatter(logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s'))
            self.PREHISTORICPLANET_logger.addHandler(self.file_handler)

    def search_prehistoricplanet_ez(self):
        try:
            r1 = requests.get(self.PREHISTORICPLANET_EZ_1)
            r1_resp = r1.status_code
            count = 0
            if r1_resp == 200:
                p1_list = search.Search().ez_search_for_new_episode(r1.text, self.PREHISTORICPLANET, self.PREHISTORICPLANET_SEA_REG)
                resp1080p = len(p1_list[0])
                resp720p = len(p1_list[1])
                count += resp1080p + resp720p
                print("\nEZ prehistoricplanet {} => \n\tstatus: {}, \n\t1080p: {}\n\t720p: {}".format(self.PREHISTORICPLANET_SEA, r1_resp, resp1080p, resp720p))
                self.PREHISTORICPLANET_logger.info("\nEZ prehistoricplanet {} => \n\tstatus: {}, \n\t1080p: {}\n\t720p: {}".format(self.PREHISTORICPLANET_SEA, r1_resp, resp1080p, resp720p))
            else:
                print("\nEZ prehistoricplanet {} => status: {}".format(self.PREHISTORICPLANET_SEA, r1_resp))
                self.PREHISTORICPLANET_logger.info("\nEZ prehistoricplanet {} => status: {}".format(self.PREHISTORICPLANET_SEA, r1_resp))
            return count
        except requests.exceptions.ConnectionError:
            print("prehistoricplanet unable to connect to EZTV")
            self.PREHISTORICPLANET_logger.error("prehistoricplanet unable to connect to EZTV")
            return 0
            
    def search_prehistoricplanet_ka(self):
        try:
            r2 = requests.get(self.PREHISTORICPLANET_KA_1)
            r2_resp = r2.status_code
            r3 = requests.get(self.PREHISTORICPLANET_KA_2)
            r3_resp = r3.status_code
            count = 0
            if r2_resp == 200 and r3_resp == 200:
                p1_list = search.ka_search_for_new_episode(r2.text, self.PREHISTORICPLANET, self.PREHISTORICPLANET_SEA_REG)
                p2_list = search.ka_search_for_new_episode(r3.text, self.PREHISTORICPLANET, self.PREHISTORICPLANET_SEA_REG)
                res = (len(p1_list[0]), len(p1_list[1]))
                res1 = (len(p2_list[0]), len(p2_list[1]))
                count = res[0] + res[1] + res1[0] + res1[1]
                print("KA prehistoricplanet {} => \n\tstatus: {}\n\t1080p: {}\n\t720p: {}".format(self.PREHISTORICPLANET_SEA, r3_resp, res1[0], res1[1]))
                self.PREHISTORICPLANET_logger.info("KA prehistoricplanet {} => \n\tstatus: {}\n\t1080p: {}\n\t720p: {}".format(self.PREHISTORICPLANET_SEA, r3_resp, res1[0], res1[1]))
            else:
                print("KA prehistoricplanet {} => status: {}".format(self.PREHISTORICPLANET_SEA, r3_resp))
                self.PREHISTORICPLANET_logger.info("KA prehistoricplanet {} => status: {}".format(self.PREHISTORICPLANET_SEA, r3_resp))
            return count
        except requests.exceptions.ConnectionError as e:
            print(e)
            self.PREHISTORICPLANET_logger.error(e)
            return 0
            

    def search_prehistoricplanet(self):
        if self.args.eztv:
            ez_count = self.search_prehistoricplanet_ez()
            return ez_count
        elif self.args.kickass:
            ka_count = self.search_prehistoricplanet_ka()
            return ka_count
        elif self.args.all:
            if self.args.eztv == True and self.args.kickass == True:
                print("Setting the -e and k flags are not allowed when using the --all flag")
            else:
                ez_count = self.search_prehistoricplanet_ez()
                ka_count = self.search_prehistoricplanet_ka()
                return ez_count + ka_count