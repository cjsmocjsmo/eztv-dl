import requests
import re
import os
import logging
import shows.search as search


class Discovery:
    def __init__(self, args, cwd):
        self.args = args
        self.DISCOVERY = re.compile(r"discovery")
        self.DISCOVERY_SEA = "s05e06"
        self.DISCOVERY_SEA_REG = re.compile(self.DISCOVERY_SEA)
        self.DISCOVERY_EZ_1 = "https://eztv.re/search/discovery"
        self.DISCOVERY_KA_1 = "https://kickasstorrents.to/usearch/discovery"
        self.DISCOVERY_KA_2 = "https://kickasstorrents.to/usearch/discovery/2"
        self.DISCOVERY_1337x_1 = "https://www.1377x.to/search/discovery"
        self.DISCOVERY_1337x_2 = "https://www.1377x.to/search/discovery/2"

        self.DISCOVERY_logger = logging.getLogger(__name__)
        self.DISCOVERY_logger.setLevel(logging.DEBUG)
        self.file_handler = None
        add1 = cwd + '/logs/discovery.log'
        if os.path.exists(add1):
            self.file_handler = logging.FileHandler(add1, mode='w')
            self.file_handler.setFormatter(logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s'))
            self.DISCOVERY_logger.addHandler(self.file_handler)
        else:
            # create add1
            with open(add1, 'w') as f:
                pass
            self.file_handler = logging.FileHandler(add1, mode='w')
            self.file_handler.setFormatter(logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s'))
            self.DISCOVERY_logger.addHandler(self.file_handler)

    def search_discovery_ez(self):
        self.DISCOVERY_logger.info("discovery searching for {}".format(self.DISCOVERY_SEA))
        try:
            r1 = requests.get(self.DISCOVERY_EZ_1)
            r1_resp = r1.status_code
            count = 0
            if r1_resp == 200:
                p1_list = search.Search().ez_search_for_new_episode(r1.text, self.DISCOVERY_SEA, self.DISCOVERY_SEA_REG)
                resp1080p = len(p1_list[0])
                resp720p = len(p1_list[1])
                count += resp1080p + resp720p
                print("\nEZ discovery {} => \n\tstatus: {}, \n\t1080p: {}\n\t720p: {}".format(self.DISCOVERY_SEA, r1_resp, resp1080p, resp720p))
                self.DISCOVERY_logger.info("\nEZ discovery {} => \n\tstatus: {}, \n\t1080p: {}\n\t720p: {}".format(self.DISCOVERY_SEA, r1_resp, resp1080p, resp720p))
            else:
                print("\nEZ discovery {} => status: {}".format(self.DISCOVERY_SEA, r1_resp))
                self.DISCOVERY_logger.info("\nEZ discovery {} => status: {}".format(self.DISCOVERY_SEA, r1_resp))
            return count
        except requests.exceptions.ConnectionError:
            print("discovery unable to connect to EZTV")
            self.DISCOVERY_logger.error("discovery unable to connect to EZTV")
            return 0

    def search_discovery_ka(self):
        try:
            r2 = requests.get(self.DISCOVERY_KA_1)
            r2_resp = r2.status_code
            print("discovery ka resp code: {}".format(r2_resp))
            self.DISCOVERY_logger.info("discovery ka resp code: {}".format(r2_resp))
            count = 0
            if r2_resp == 200:
                p2_list = search.Search().ka_search_for_new_episode(r2.text, self.DISCOVERY, self.DISCOVERY_SEA_REG)
                res1 = (len(p2_list[0]), len(p2_list[1]))
                count += res1[0] + res1[1]
                print("KA discovery {} => \n\tstatus: {}\n\t1080p: {}\n\t720p: {}".format(self.DISCOVERY_SEA, r2_resp, res1[0], res1[1]))
                self.DISCOVERY_logger.info("KA discovery {} => \n\tstatus: {}\n\t1080p: {}\n\t720p: {}".format(self.DISCOVERY_SEA, r2_resp, res1[0], res1[1]))
            else:
                print("KA discovery {} => status: {}".format(self.DISCOVERY_SEA, r2_resp))
                self.DISCOVERY_logger.info("KA discovery {} => status: {} connect with vpn".format(self.DISCOVERY_SEA, r2_resp))
            return count
        except requests.exceptions.ConnectionError as e:
            print(e)
            self.DISCOVERY_logger.error(e)
            return 0

    def search_discovery_1337x(self):
        try:
            r3 = requests.get(self.DISCOVERY_1337x_1)
            r3_resp = r3.status_code
            print("discovery 1337x resp code: {}".format(r3_resp))
            self.DISCOVERY_logger.info("discovery 1337x resp code: {}".format(r3_resp))
            count = 0
            if r3_resp == 200:
                p3_list = search.Search().x1337_search_for_new_episode(r3.text, self.DISCOVERY, self.DISCOVERY_SEA_REG)
            #     res2 = (len(p3_list[0]), len(p3_list[1]))
            #     count += res2[0] + res2[1]
            #     print("1337x discovery {} => \n\tstatus: {}\n\t1080p: {}\n\t720p: {}".format(self.DISCOVERY_SEA, r3_resp, res2[0], res2[1]))
            #     discovery_logger.info("1337x discovery {} => \n\tstatus: {}\n\t1080p: {}\n\t720p: {}".format(self.DISCOVERY_SEA, r3_resp, res2[0], res2[1]))
            # else:
            #     print("1337x discovery {} => status: {}".format(self.DISCOVERY_SEA, r3_resp))
            #     discovery_logger.info("1337x discovery {} => status: {}".format(self.DISCOVERY_SEA, r3_resp))
            return count
        except requests.exceptions.ConnectionError as e:
            print(e)
            self.DISCOVERY_logger.error(e)
            return 0

    def search_discovery(self):
        if self.args.eztv:
            ez_count = self.search_discovery_ez()
            return ez_count
        elif self.args.kickass:
            ka_count = self.search_discovery_ka()
            return ka_count
        elif self.args.x1337:
            x1337_count = self.search_discovery_1337x()
            return x1337_count
        elif self.args.all:
            ez_count = self.search_discovery_ez()
            ka_count = self.search_discovery_ka()
            x1337_count = self.search_discovery_1337x()
            return ez_count + ka_count + x1337_count
