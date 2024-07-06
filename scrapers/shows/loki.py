import requests
import re
import os
import logging
import shows.search as search

class Loki:
    def __init__(self, args, cwd):
        self.args = args
        self.LOKI = re.compile(r"loki")
        self.LOKI_SEA = "s03e01"
        self.LOKI_SEA_REG = re.compile(self.LOKI_SEA)
        self.LOKI_EZ_1 = "https://eztv.re/search/loki"
        self.LOKI_KA_1 = "https://kickasstorrents.to/usearch/loki"
        self.LOKI_KA_2 = "https://kickasstorrents.to/usearch/loki/2"
        self.LOKI_1337x_1 = "https://www.1377x.to/search/loki"
        self.LOKI_1337x_2 = "https://www.1377x.to/search/loki/2"

    def search_loki_ez(self):
        try:
            r1 = requests.get(self.LOKI_EZ_1)
            r1_resp = r1.status_code
            count = 0
            if r1_resp == 200:
                p1_list = search.Search().ez_search_for_new_episode(r1.text, self.LOKI, self.LOKI_SEA_REG)
                resp1080p = len(p1_list[0])
                resp720p = len(p1_list[1])
                count += resp1080p + resp720p
                print("\nEZ LOKI {} => \n\tstatus: {}, \n\t1080p: {}\n\t720p: {}".format(self.LOKI_SEA, r1_resp, resp1080p, resp720p))
                
            else:
                print("\nEZ LOKI {} => status: {}".format(self.LOKI_SEA, r1_resp))
            return count
        except requests.exceptions.ConnectionError:
            print("LOKI unable to connect to EZTV")
            return 0
            
    def search_loki_ka(self):
        try:
            r2 = requests.get(self.LOKI_KA_1)
            r2_resp = r2.status_code
            r3 = requests.get(self.LOKI_KA_2)
            r3_resp = r3.status_code
            count = 0
            if r2_resp == 200 and r3_resp == 200:
                p1_list = search.ka_search_for_new_episode(r2.text, self.LOKI, self.LOKI_SEA_REG)
                p2_list = search.ka_search_for_new_episode(r3.text, self.LOKI, self.LOKI_SEA_REG)
                res = (len(p1_list[0]), len(p1_list[1]))
                res1 = (len(p2_list[0]), len(p2_list[1]))
                count = res[0] + res[1] + res1[0] + res1[1]
                print("KA LOKI {} => \n\tstatus: {}\n\t1080p: {}\n\t720p: {}".format(self.LOKI_SEA, r3_resp, res1[0], res1[1]))
                
            else:
                print("KA LOKI {} => status: {}".format(self.LOKI_SEA, r3_resp))
            return count
        except requests.exceptions.ConnectionError as e:
            print(e)
            return 0
            

    def search_loki(self):
        if self.args.eztv:
            ez_count = self.search_loki_ez()
            return ez_count
        elif self.args.kickass:
            ka_count = self.search_loki_ka()
            return ka_count
        elif self.args.all:
            if self.args.eztv == True and self.args.kickass == True:
                print("Setting the -e and k flags are not allowed when using the --all flag")
            else:
                ez_count = self.search_loki_ez()
                ka_count = self.search_loki_ka()
                return ez_count + ka_count