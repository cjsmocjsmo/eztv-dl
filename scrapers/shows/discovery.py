import requests
import re
import shows.search as search


class Discovery:
    def __init__(self, args, cwd):
        self.args = args
        self.DISCOVERY = re.compile(r"discovery")
        self.DISCOVERY_SEA = "s05e11"
        self.DISCOVERY_SEA_REG = re.compile(self.DISCOVERY_SEA)
        self.DISCOVERY_EZ_1 = "https://eztv.re/search/discovery"
        self.DISCOVERY_KA_1 = "https://kickasstorrents.to/usearch/discovery"
        self.DISCOVERY_KA_2 = "https://kickasstorrents.to/usearch/discovery/2"
        self.DISCOVERY_1337x_1 = "https://www.1377x.to/search/discovery"
        self.DISCOVERY_1337x_2 = "https://www.1377x.to/search/discovery/2"

    def search_discovery_ez(self):
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
                
            else:
                print("\nEZ discovery {} => status: {}".format(self.DISCOVERY_SEA, r1_resp))
            return count
        except requests.exceptions.ConnectionError:
            print("discovery unable to connect to EZTV")
            return 0

    def search_discovery_ka(self):
        try:
            r2 = requests.get(self.DISCOVERY_KA_1)
            r2_resp = r2.status_code
            print("discovery ka resp code: {}".format(r2_resp))
            count = 0
            if r2_resp == 200:
                p2_list = search.Search().ka_search_for_new_episode(r2.text, self.DISCOVERY, self.DISCOVERY_SEA_REG)
                res1 = (len(p2_list[0]), len(p2_list[1]))
                count += res1[0] + res1[1]
                print("KA discovery {} => \n\tstatus: {}\n\t1080p: {}\n\t720p: {}".format(self.DISCOVERY_SEA, r2_resp, res1[0], res1[1]))
                
            else:
                print("KA discovery {} => status: {}".format(self.DISCOVERY_SEA, r2_resp))
            return count
        except requests.exceptions.ConnectionError as e:
            print(e)
            return 0

    def search_discovery_1337x(self):
        try:
            r3 = requests.get(self.DISCOVERY_1337x_1)
            r3_resp = r3.status_code
            print("discovery 1337x resp code: {}".format(r3_resp))
            count = 0
            if r3_resp == 200:
                p3_list = search.Search().x1337_search_for_new_episode(r3.text, self.DISCOVERY, self.DISCOVERY_SEA_REG)
            return count
        except requests.exceptions.ConnectionError as e:
            print(e)
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
