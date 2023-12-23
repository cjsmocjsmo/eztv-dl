import requests
import re
import os
import logging
import shows.search as search

class RebelMoon:
    def __init__(self, args, cwd):
        self.args = args
        self.REBELMOON = re.compile(r"rebel moon")
        self.REBELMOON_SEA = "s01e01"
        self.REBELMOON_SEA_REG = re.compile(self.REBELMOON_SEA)
        self.REBELMOON_EZ_1 = "https://eztv.re/search/rebel-moon"
        self.REBELMOON_KA_1 = "https://kickasstorrents.to/usearch/rebelmoon"
        self.REBELMOON_KA_2 = "https://kickasstorrents.to/usearch/rebelmoon/2"
        self.REBELMOON_1337x_1 = "https://www.1377x.to/search/rebelmoon"
        self.REBELMOON_1337x_2 = "https://www.1377x.to/search/rebelmoon/2"

        self.REBELMOON_logger = logging.getLogger(__name__)
        self.REBELMOON_logger.setLevel(logging.DEBUG)
        self.file_handler = None
        addr1 = cwd + '/logs/rebelmoon.log'
        if os.path.exists(addr1):
            self.file_handler = logging.FileHandler(addr1, mode='w')
            self.file_handler.setFormatter(logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s'))
            self.REBELMOON_logger.addHandler(self.file_handler)

    def search_rebelmoon_ez(self):
        try:
            r1 = requests.get(self.REBELMOON_EZ_1)
            r1_resp = r1.status_code
            count = 0
            if r1_resp == 200:
                p1_list = search.Search().ez_search_for_new_episode(r1.text, self.REBELMOON_SEA, self.REBELMOON_SEA_REG)
                resp1080p = len(p1_list[0])
                resp720p = len(p1_list[1])
                count += resp1080p + resp720p
                print("\nEZ rebelmoon {} => \n\tstatus: {}, \n\t1080p: {}\n\t720p: {}".format(self.REBELMOON_SEA, r1_resp, resp1080p, resp720p))
                self.REBELMOON_logger.info("\nEZ rebelmoon {} => \n\tstatus: {}, \n\t1080p: {}\n\t720p: {}".format(self.REBELMOON_SEA, r1_resp, resp1080p, resp720p))
            else:
                print("\nEZ rebelmoon {} => status: {}".format(self.REBELMOON_SEA, r1_resp))
                self.REBELMOON_logger.info("\nEZ rebelmoon {} => status: {}".format(self.REBELMOON_SEA, r1_resp))
            return count
        except requests.exceptions.ConnectionError:
            print("rebelmoon unable to connect to EZTV")
            self.REBELMOON_logger.error("rebelmoon unable to connect to EZTV")
            return 0
            
    def search_rebelmoon_ka(self):
        try:
            r2 = requests.get(self.REBELMOON_KA_1)
            r2_resp = r2.status_code
            r3 = requests.get(self.REBELMOON_KA_2)
            r3_resp = r3.status_code
            count = 0
            if r2_resp == 200 and r3_resp == 200:
                p1_list = search.ka_search_for_new_episode(r2.text, self.REBELMOON, self.REBELMOON_SEA_REG)
                p2_list = search.ka_search_for_new_episode(r3.text, self.REBELMOON, self.REBELMOON_SEA_REG)
                res = (len(p1_list[0]), len(p1_list[1]))
                res1 = (len(p2_list[0]), len(p2_list[1]))
                count = res[0] + res[1] + res1[0] + res1[1]
                print("KA rebelmoon {} => \n\tstatus: {}\n\t1080p: {}\n\t720p: {}".format(self.REBELMOON_SEA, r3_resp, res1[0], res1[1]))
                self.REBELMOON_logger.info("KA rebelmoon {} => \n\tstatus: {}\n\t1080p: {}\n\t720p: {}".format(self.REBELMOON_SEA, r3_resp, res1[0], res1[1]))
            else:
                print("KA rebelmoon {} => status: {}".format(self.REBELMOON_SEA, r3_resp))
                self.REBELMOON_logger.info("KA rebelmoon {} => status: {}".format(self.REBELMOON_SEA, r3_resp))
            return count
        except requests.exceptions.ConnectionError as e:
            print(e)
            self.REBELMOON_logger.error(e)
            return 0
            

    def search_rebelmoon(self):
        if self.args.eztv:
            ez_count = self.search_rebelmoon_ez()
            return ez_count
        elif self.args.kickass:
            ka_count = self.search_rebelmoon_ka()
            return ka_count
        elif self.args.all:
            if self.args.eztv == True and self.args.kickass == True:
                print("Setting the -e and k flags are not allowed when using the --all flag")
            else:
                ez_count = self.search_rebelmoon_ez()
                ka_count = self.search_rebelmoon_ka()
                return ez_count + ka_count