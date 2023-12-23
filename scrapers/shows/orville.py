import requests
import re
import os
import logging
import shows.search as search

class Orville:
    def __init__(self, args, cwd):
        self.args = args
        self.ORVILLE = re.compile(r"orville")
        self.ORVILLE_SEA = "s04e01"
        self.ORVILLE_SEA_REG = re.compile(self.ORVILLE_SEA)
        self.ORVILLE_EZ_1 = "https://eztv.re/search/orville"
        self.ORVILLE_KA_1 = "https://kickasstorrents.to/usearch/orville"
        self.ORVILLE_KA_2 = "https://kickasstorrents.to/usearch/orville/2"
        self.ORVILLE_1337x_1 = "https://www.1377x.to/search/orville"
        self.ORVILLE_1337x_2 = "https://www.1377x.to/search/orville/2"

        self.orville_logger = logging.getLogger(__name__)
        self.orville_logger.setLevel(logging.DEBUG)
        self.file_handler = None
        addr1 = cwd + '/logs/orville.log'
        if os.path.exists(addr1):
            self.file_handler = logging.FileHandler(addr1, mode='w')
            self.file_handler.setFormatter(logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s'))
            self.orville_logger.addHandler(self.file_handler)

    def search_orville_ez(self):
        try:
            r1 = requests.get(self.ORVILLE_EZ_1)
            r1_resp = r1.status_code
            count = 0
            if r1_resp == 200:
                p1_list = search.Search().ez_search_for_new_episode(r1.text, self.ORVILLE, self.ORVILLE_SEA_REG)
                resp1080p = len(p1_list[0])
                resp720p = len(p1_list[1])
                count += resp1080p + resp720p
                print("\nEZ orville {} => \n\tstatus: {}, \n\t1080p: {}\n\t720p: {}".format(self.ORVILLE_SEA, r1_resp, resp1080p, resp720p))
                self.orville_logger.info("\nEZ orville {} => \n\tstatus: {}, \n\t1080p: {}\n\t720p: {}".format(self.ORVILLE_SEA, r1_resp, resp1080p, resp720p))
            else:
                print("\nEZ orville {} => status: {}".format(self.ORVILLE_SEA, r1_resp))
                self.orville_logger.info("\nEZ orville {} => status: {}".format(self.ORVILLE_SEA, r1_resp))
            return count
        except requests.exceptions.ConnectionError:
            print("orville unable to connect to EZTV")
            self.orville_logger.error("orville unable to connect to EZTV")
            return 0
            
    def search_orville_ka(self):
        try:
            r2 = requests.get(self.ORVILLE_KA_1)
            r2_resp = r2.status_code
            r3 = requests.get(self.ORVILLE_KA_2)
            r3_resp = r3.status_code
            count = 0
            if r2_resp == 200 and r3_resp == 200:
                p1_list = search.ka_search_for_new_episode(r2.text, self.ORVILLE, self.ORVILLE_SEA_REG)
                p2_list = search.ka_search_for_new_episode(r3.text, self.ORVILLE, self.ORVILLE_SEA_REG)
                res = (len(p1_list[0]), len(p1_list[1]))
                res1 = (len(p2_list[0]), len(p2_list[1]))
                count = res[0] + res[1] + res1[0] + res1[1]
                print("KA orville {} => \n\tstatus: {}\n\t1080p: {}\n\t720p: {}".format(self.ORVILLE_SEA, r3_resp, res1[0], res1[1]))
                self.orville_logger.info("KA orville {} => \n\tstatus: {}\n\t1080p: {}\n\t720p: {}".format(self.ORVILLE_SEA, r3_resp, res1[0], res1[1]))
            else:
                print("KA orville {} => status: {}".format(self.ORVILLE_SEA, r3_resp))
                self.orville_logger.info("KA orville {} => status: {}".format(self.ORVILLE_SEA, r3_resp))
            return count
        except requests.exceptions.ConnectionError as e:
            print(e)
            self.orville_logger.error(e)
            return 0
            

    def search_orville(self):
        if self.args.eztv:
            ez_count = self.search_orville_ez()
            return ez_count
        elif self.args.kickass:
            ka_count = self.search_orville_ka()
            return ka_count
        elif self.args.all:
            if self.args.eztv == True and self.args.kickass == True:
                print("Setting the -e and k flags are not allowed when using the --all flag")
            else:
                ez_count = self.search_orville_ez()
                ka_count = self.search_orville_ka()
                return ez_count + ka_count