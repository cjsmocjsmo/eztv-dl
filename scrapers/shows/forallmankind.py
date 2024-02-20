import requests
import re
import os
import logging
import shows.search as search

class ForAllMankind:
    def __init__(self, args, cwd):
        self.args = args
        self.FORALLMANKIND = re.compile(r"for all mankind")
        self.FORALLMANKIND_SEA = "s05e01"
        self.FORALLMANKIND_SEA_REG = re.compile(self.FORALLMANKIND_SEA)
        self.FORALLMANKIND_EZ_1 = "https://eztv.re/search/for-all-mankind"
        self.FORALLMANKIND_KA_1 = "https://kickasstorrents.to/usearch/forallmankind"
        self.FORALLMANKIND_KA_2 = "https://kickasstorrents.to/usearch/forallmankind/2"
        self.FORALLMANKIND_1337x_1 = "https://www.1377x.to/search/forallmankind"
        self.FORALLMANKIND_1337x_2 = "https://www.1377x.to/search/forallmankind/2"

        self.FORALLMANKIND_logger = logging.getLogger(__name__)
        self.FORALLMANKIND_logger.setLevel(logging.DEBUG)
        self.file_handler = None
        addr1 = cwd + '/logs/forallmankind.log'
        if os.path.exists(addr1):
            self.file_handler = logging.FileHandler(addr1, mode='w')
            self.file_handler.setFormatter(logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s'))
            self.FORALLMANKIND_logger.addHandler(self.file_handler)

    def search_forallmankind_ez(self):
        try:
            r1 = requests.get(self.FORALLMANKIND_EZ_1)
            r1_resp = r1.status_code
            count = 0
            if r1_resp == 200:
                p1_list = search.Search().ez_search_for_new_episode(r1.text, self.FORALLMANKIND_SEA, self.FORALLMANKIND_SEA_REG)
                resp1080p = len(p1_list[0])
                resp720p = len(p1_list[1])
                count += resp1080p + resp720p
                print("\nEZ forallmankind {} => \n\tstatus: {}, \n\t1080p: {}\n\t720p: {}".format(self.FORALLMANKIND_SEA, r1_resp, resp1080p, resp720p))
                self.FORALLMANKIND_logger.info("\nEZ forallmankind {} => \n\tstatus: {}, \n\t1080p: {}\n\t720p: {}".format(self.FORALLMANKIND_SEA, r1_resp, resp1080p, resp720p))
            else:
                print("\nEZ forallmankind {} => status: {}".format(self.FORALLMANKIND_SEA, r1_resp))
                self.FORALLMANKIND_logger.info("\nEZ forallmankind {} => status: {}".format(self.FORALLMANKIND_SEA, r1_resp))
            return count
        except requests.exceptions.ConnectionError:
            print("forallmankind unable to connect to EZTV")
            self.FORALLMANKIND_logger.error("forallmankind unable to connect to EZTV")
            return 0
            
    def search_forallmankind_ka(self):
        try:
            r2 = requests.get(self.FORALLMANKIND_KA_1)
            r2_resp = r2.status_code
            r3 = requests.get(self.FORALLMANKIND_KA_2)
            r3_resp = r3.status_code
            count = 0
            if r2_resp == 200 and r3_resp == 200:
                p1_list = search.ka_search_for_new_episode(r2.text, self.FORALLMANKIND, self.FORALLMANKIND_SEA_REG)
                p2_list = search.ka_search_for_new_episode(r3.text, self.FORALLMANKIND, self.FORALLMANKIND_SEA_REG)
                res = (len(p1_list[0]), len(p1_list[1]))
                res1 = (len(p2_list[0]), len(p2_list[1]))
                count = res[0] + res[1] + res1[0] + res1[1]
                print("KA forallmankind {} => \n\tstatus: {}\n\t1080p: {}\n\t720p: {}".format(self.FORALLMANKIND_SEA, r3_resp, res1[0], res1[1]))
                self.FORALLMANKIND_logger.info("KA forallmankind {} => \n\tstatus: {}\n\t1080p: {}\n\t720p: {}".format(self.FORALLMANKIND_SEA, r3_resp, res1[0], res1[1]))
            else:
                print("KA forallmankind {} => status: {}".format(self.FORALLMANKIND_SEA, r3_resp))
                self.FORALLMANKIND_logger.info("KA forallmankind {} => status: {}".format(self.FORALLMANKIND_SEA, r3_resp))
            return count
        except requests.exceptions.ConnectionError as e:
            print(e)
            self.FORALLMANKIND_logger.error(e)
            return 0
            

    def search_forallmankind(self):
        if self.args.eztv:
            ez_count = self.search_forallmankind_ez()
            return ez_count
        elif self.args.kickass:
            ka_count = self.search_forallmankind_ka()
            return ka_count
        elif self.args.all:
            if self.args.eztv == True and self.args.kickass == True:
                print("Setting the -e and k flags are not allowed when using the --all flag")
            else:
                ez_count = self.search_forallmankind_ez()
                ka_count = self.search_forallmankind_ka()
                return ez_count + ka_count