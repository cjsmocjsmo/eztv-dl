import requests
import re
import os
import logging
import shows.search as search

class StrangeNewWorlds:
    def __init__(self, args, cwd):
        self.args = args
        self.STRANGENEWWORLDS = re.compile(r"strange new worlds")
        self.STRANGENEWWORLDS_SEA = "s03e01"
        self.STRANGENEWWORLDS_SEA_REG = re.compile(self.STRANGENEWWORLDS_SEA)
        self.STRANGENEWWORLDS_EZ_1 = "https://eztv.re/search/strange-new-worlds"
        self.STRANGENEWWORLDS_KA_1 = "https://kickasstorrents.to/usearch/strangenewworlds"
        self.STRANGENEWWORLDS_KA_2 = "https://kickasstorrents.to/usearch/strangenewworlds/2"
        self.STRANGENEWWORLDS_1337x_1 = "https://www.1377x.to/search/strangenewworlds"
        self.STRANGENEWWORLDS_1337x_2 = "https://www.1377x.to/search/strangenewworlds/2"

        self.STRANGENEWWORLDS_logger = logging.getLogger(__name__)
        self.STRANGENEWWORLDS_logger.setLevel(logging.DEBUG)
        self.file_handler = None
        addr1 = cwd + '/logs/strangenewworlds.log'
        if os.path.exists(addr1):
            self.file_handler = logging.FileHandler(addr1, mode='w')
            self.file_handler.setFormatter(logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s'))
            self.STRANGENEWWORLDS_logger.addHandler(self.file_handler)
        else:
            # create addr1
            with open(addr1, 'w') as f:
                pass
            self.file_handler = logging.FileHandler(addr1, mode='w')
            self.file_handler.setFormatter(logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s'))
            self.STRANGENEWWORLDS_logger.addHandler(self.file_handler)

    def search_strangenewworlds_ez(self):
        try:
            r1 = requests.get(self.STRANGENEWWORLDS_EZ_1)
            r1_resp = r1.status_code
            count = 0
            if r1_resp == 200:
                p1_list = search.Search().ez_search_for_new_episode(r1.text, self.STRANGENEWWORLDS_SEA, self.STRANGENEWWORLDS_SEA_REG)
                resp1080p = len(p1_list[0])
                resp720p = len(p1_list[1])
                count += resp1080p + resp720p
                print("\nEZ strangenewworlds {} => \n\tstatus: {}, \n\t1080p: {}\n\t720p: {}".format(self.STRANGENEWWORLDS_SEA, r1_resp, resp1080p, resp720p))
                self.STRANGENEWWORLDS_logger.info("\nEZ strangenewworlds {} => \n\tstatus: {}, \n\t1080p: {}\n\t720p: {}".format(self.STRANGENEWWORLDS_SEA, r1_resp, resp1080p, resp720p))
            else:
                print("\nEZ strangenewworlds {} => status: {}".format(self.STRANGENEWWORLDS_SEA, r1_resp))
                self.STRANGENEWWORLDS_logger.info("\nEZ strangenewworlds {} => status: {}".format(self.STRANGENEWWORLDS_SEA, r1_resp))
            return count
        except requests.exceptions.ConnectionError:
            print("strangenewworlds unable to connect to EZTV")
            self.STRANGENEWWORLDS_logger.error("strangenewworlds unable to connect to EZTV")
            return 0
            
    def search_strangenewworlds_ka(self):
        try:
            r2 = requests.get(self.STRANGENEWWORLDS_KA_1)
            r2_resp = r2.status_code
            r3 = requests.get(self.STRANGENEWWORLDS_KA_2)
            r3_resp = r3.status_code
            count = 0
            if r2_resp == 200 and r3_resp == 200:
                p1_list = search.ka_search_for_new_episode(r2.text, self.STRANGENEWWORLDS, self.STRANGENEWWORLDS_SEA_REG)
                p2_list = search.ka_search_for_new_episode(r3.text, self.STRANGENEWWORLDS, self.STRANGENEWWORLDS_SEA_REG)
                res = (len(p1_list[0]), len(p1_list[1]))
                res1 = (len(p2_list[0]), len(p2_list[1]))
                count = res[0] + res[1] + res1[0] + res1[1]
                print("KA strangenewworlds {} => \n\tstatus: {}\n\t1080p: {}\n\t720p: {}".format(self.STRANGENEWWORLDS_SEA, r3_resp, res1[0], res1[1]))
                self.STRANGENEWWORLDS_logger.info("KA strangenewworlds {} => \n\tstatus: {}\n\t1080p: {}\n\t720p: {}".format(self.STRANGENEWWORLDS_SEA, r3_resp, res1[0], res1[1]))
            else:
                print("KA strangenewworlds {} => status: {}".format(self.STRANGENEWWORLDS_SEA, r3_resp))
                self.STRANGENEWWORLDS_logger.info("KA strangenewworlds {} => status: {}".format(self.STRANGENEWWORLDS_SEA, r3_resp))
            return count
        except requests.exceptions.ConnectionError as e:
            print(e)
            self.STRANGENEWWORLDS_logger.error(e)
            return 0
            

    def search_strangenewworlds(self):
        if self.args.eztv:
            ez_count = self.search_strangenewworlds_ez()
            return ez_count
        elif self.args.kickass:
            ka_count = self.search_strangenewworlds_ka()
            return ka_count
        elif self.args.all:
            if self.args.eztv == True and self.args.kickass == True:
                print("Setting the -e and k flags are not allowed when using the --all flag")
            else:
                ez_count = self.search_strangenewworlds_ez()
                ka_count = self.search_strangenewworlds_ka()
                return ez_count + ka_count