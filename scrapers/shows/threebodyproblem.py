import requests
import re
import os
import logging
import shows.search as search

class ThreeBodyProblem:
    def __init__(self, args, cwd):
        self.args = args
        self.threebodyproblem = re.compile(r"threebodyproblem")
        self.threebodyproblem_SEA = "s02e01"
        self.threebodyproblem_SEA_REG = re.compile(self.threebodyproblem_SEA)
        self.threebodyproblem_EZ_1 = "https://eztv.re/search/3-body-problem"
        self.threebodyproblem_KA_1 = "https://kickasstorrents.to/usearch/3-body-problem"
        self.threebodyproblem_KA_2 = "https://kickasstorrents.to/usearch/3-body-problem/2"
        self.threebodyproblem_1337x_1 = "https://www.1377x.to/search/3-body-problem"
        self.threebodyproblem_1337x_2 = "https://www.1377x.to/search/3-body-problem/2"

        self.threebodyproblem_logger = logging.getLogger(__name__)
        self.threebodyproblem_logger.setLevel(logging.DEBUG)
        self.file_handler = None
        addr1 = cwd + '/logs/threebodyproblem.log'
        if os.path.exists(addr1):
            self.file_handler = logging.FileHandler(addr1, mode='w')
            self.file_handler.setFormatter(logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s'))
            self.threebodyproblem_logger.addHandler(self.file_handler)
        else:
            # create addr1
            with open(addr1, 'w') as f:
                pass
            self.file_handler = logging.FileHandler(addr1, mode='w')
            self.file_handler.setFormatter(logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s'))
            self.threebodyproblem_logger.addHandler(self.file_handler)

    def search_threebodyproblem_ez(self):
        try:
            r1 = requests.get(self.threebodyproblem_EZ_1)
            r1_resp = r1.status_code
            count = 0
            if r1_resp == 200:
                p1_list = search.Search().ez_search_for_new_episode(r1.text, self.threebodyproblem_SEA, self.threebodyproblem_SEA_REG)
                resp1080p = len(p1_list[0])
                resp720p = len(p1_list[1])
                count += resp1080p + resp720p
                print("\nEZ threebodyproblem {} => \n\tstatus: {}, \n\t1080p: {}\n\t720p: {}".format(self.threebodyproblem_SEA, r1_resp, resp1080p, resp720p))
                self.threebodyproblem_logger.info("\nEZ threebodyproblem {} => \n\tstatus: {}, \n\t1080p: {}\n\t720p: {}".format(self.threebodyproblem_SEA, r1_resp, resp1080p, resp720p))
            else:
                print("\nEZ threebodyproblem {} => status: {}".format(self.threebodyproblem_SEA, r1_resp))
                self.threebodyproblem_logger.info("\nEZ threebodyproblem {} => status: {}".format(self.threebodyproblem_SEA, r1_resp))
            return count
        except requests.exceptions.ConnectionError:
            print("threebodyproblem unable to connect to EZTV")
            self.threebodyproblem_logger.error("threebodyproblem unable to connect to EZTV")
            return 0
            
    def search_threebodyproblem_ka(self):
        try:
            r2 = requests.get(self.threebodyproblem_KA_1)
            r2_resp = r2.status_code
            r3 = requests.get(self.threebodyproblem_KA_2)
            r3_resp = r3.status_code
            count = 0
            if r2_resp == 200 and r3_resp == 200:
                p1_list = search.ka_search_for_new_episode(r2.text, self.threebodyproblem, self.threebodyproblem_SEA_REG)
                p2_list = search.ka_search_for_new_episode(r3.text, self.threebodyproblem, self.threebodyproblem_SEA_REG)
                res = (len(p1_list[0]), len(p1_list[1]))
                res1 = (len(p2_list[0]), len(p2_list[1]))
                count = res[0] + res[1] + res1[0] + res1[1]
                print("KA threebodyproblem {} => \n\tstatus: {}\n\t1080p: {}\n\t720p: {}".format(self.threebodyproblem_SEA, r3_resp, res1[0], res1[1]))
                self.threebodyproblem_logger.info("KA threebodyproblem {} => \n\tstatus: {}\n\t1080p: {}\n\t720p: {}".format(self.threebodyproblem_SEA, r3_resp, res1[0], res1[1]))
            else:
                print("KA threebodyproblem {} => status: {}".format(self.threebodyproblem_SEA, r3_resp))
                self.threebodyproblem_logger.info("KA threebodyproblem {} => status: {}".format(self.threebodyproblem_SEA, r3_resp))
            return count
        except requests.exceptions.ConnectionError as e:
            print(e)
            self.threebodyproblem_logger.error(e)
            return 0
            

    def search_threebodyproblem(self):
        if self.args.eztv:
            ez_count = self.search_threebodyproblem_ez()
            return ez_count
        elif self.args.kickass:
            ka_count = self.search_threebodyproblem_ka()
            return ka_count
        elif self.args.all:
            if self.args.eztv == True and self.args.kickass == True:
                print("Setting the -e and k flags are not allowed when using the --all flag")
            else:
                ez_count = self.search_threebodyproblem_ez()
                ka_count = self.search_threebodyproblem_ka()
                return ez_count + ka_count