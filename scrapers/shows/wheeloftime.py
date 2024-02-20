import requests
import re
import os
import logging
import shows.search as search

class WheelOfTime:
    def __init__(self, args, cwd):
        self.args = args
        self.WHEELOFTIME = re.compile(r"wheel of time")
        self.WHEELOFTIME_SEA = "s03e01"
        self.WHEELOFTIME_SEA_REG = re.compile(self.WHEELOFTIME_SEA)
        self.WHEELOFTIME_EZ_1 = "https://eztv.re/search/wheel-of-time"
        self.WHEELOFTIME_KA_1 = "https://kickasstorrents.to/usearch/wheeloftime"
        self.WHEELOFTIME_KA_2 = "https://kickasstorrents.to/usearch/wheeloftime/2"
        self.WHEELOFTIME_1337x_1 = "https://www.1377x.to/search/wheeloftime"
        self.WHEELOFTIME_1337x_2 = "https://www.1377x.to/search/wheeloftime/2"

        self.WHEELOFTIME_logger = logging.getLogger(__name__)
        self.WHEELOFTIME_logger.setLevel(logging.DEBUG)
        self.file_handler = None
        addr1 = cwd + '/logs/wheeloftime.log'
        if os.path.exists(addr1):
            self.file_handler = logging.FileHandler(addr1, mode='w')
            self.file_handler.setFormatter(logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s'))
            self.WHEELOFTIME_logger.addHandler(self.file_handler)
        else:
            # create addr1
            with open(addr1, 'w') as f:
                pass
            self.file_handler = logging.FileHandler(addr1, mode='w')
            self.file_handler.setFormatter(logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s'))
            self.WHEELOFTIME_logger.addHandler(self.file_handler)

    def search_wheeloftime_ez(self):
        try:
            r1 = requests.get(self.WHEELOFTIME_EZ_1)
            r1_resp = r1.status_code
            count = 0
            if r1_resp == 200:
                p1_list = search.Search().ez_search_for_new_episode(r1.text, self.WHEELOFTIME_SEA, self.WHEELOFTIME_SEA_REG)
                resp1080p = len(p1_list[0])
                resp720p = len(p1_list[1])
                count += resp1080p + resp720p
                print("\nEZ wheeloftime {} => \n\tstatus: {}, \n\t1080p: {}\n\t720p: {}".format(self.WHEELOFTIME_SEA, r1_resp, resp1080p, resp720p))
                self.WHEELOFTIME_logger.info("\nEZ wheeloftime {} => \n\tstatus: {}, \n\t1080p: {}\n\t720p: {}".format(self.WHEELOFTIME_SEA, r1_resp, resp1080p, resp720p))
            else:
                print("\nEZ wheeloftime {} => status: {}".format(self.WHEELOFTIME_SEA, r1_resp))
                self.WHEELOFTIME_logger.info("\nEZ wheeloftime {} => status: {}".format(self.WHEELOFTIME_SEA, r1_resp))
            return count
        except requests.exceptions.ConnectionError:
            print("wheeloftime unable to connect to EZTV")
            self.WHEELOFTIME_logger.error("wheeloftime unable to connect to EZTV")
            return 0
            
    def search_wheeloftime_ka(self):
        try:
            r2 = requests.get(self.WHEELOFTIME_KA_1)
            r2_resp = r2.status_code
            r3 = requests.get(self.WHEELOFTIME_KA_2)
            r3_resp = r3.status_code
            count = 0
            if r2_resp == 200 and r3_resp == 200:
                p1_list = search.ka_search_for_new_episode(r2.text, self.WHEELOFTIME, self.WHEELOFTIME_SEA_REG)
                p2_list = search.ka_search_for_new_episode(r3.text, self.WHEELOFTIME, self.WHEELOFTIME_SEA_REG)
                res = (len(p1_list[0]), len(p1_list[1]))
                res1 = (len(p2_list[0]), len(p2_list[1]))
                count = res[0] + res[1] + res1[0] + res1[1]
                print("KA wheeloftime {} => \n\tstatus: {}\n\t1080p: {}\n\t720p: {}".format(self.WHEELOFTIME_SEA, r3_resp, res1[0], res1[1]))
                self.WHEELOFTIME_logger.info("KA wheeloftime {} => \n\tstatus: {}\n\t1080p: {}\n\t720p: {}".format(self.WHEELOFTIME_SEA, r3_resp, res1[0], res1[1]))
            else:
                print("KA wheeloftime {} => status: {}".format(self.WHEELOFTIME_SEA, r3_resp))
                self.WHEELOFTIME_logger.info("KA wheeloftime {} => status: {}".format(self.WHEELOFTIME_SEA, r3_resp))
            return count
        except requests.exceptions.ConnectionError as e:
            print(e)
            self.WHEELOFTIME_logger.error(e)
            return 0
            

    def search_wheeloftime(self):
        if self.args.eztv:
            ez_count = self.search_wheeloftime_ez()
            return ez_count
        elif self.args.kickass:
            ka_count = self.search_wheeloftime_ka()
            return ka_count
        elif self.args.all:
            if self.args.eztv == True and self.args.kickass == True:
                print("Setting the -e and k flags are not allowed when using the --all flag")
            else:
                ez_count = self.search_wheeloftime_ez()
                ka_count = self.search_wheeloftime_ka()
                return ez_count + ka_count