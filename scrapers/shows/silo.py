import requests
import re
import shows.search as search

class Silo:
    def __init__(self, args, cwd):
        self.args = args
        self.silo = re.compile(r"silo")
        self.silo_SEA = "s02e11"
        self.silo_SEA_REG = re.compile(self.silo_SEA)
        self.silo_EZ_1 = "https://eztv.re/search/silo"
        self.silo_KA_1 = "https://kickasstorrents.to/usearch/silo"
        self.silo_KA_2 = "https://kickasstorrents.to/usearch/silo/2"
        self.silo_1337x_1 = "https://www.1377x.to/search/silo"
        self.silo_1337x_2 = "https://www.1377x.to/search/silo/2"

    def search_silo_ez(self):
        try:
            r1 = requests.get(self.silo_EZ_1)
            r1_resp = r1.status_code
            count = 0
            if r1_resp == 200:
                p1_list = search.Search().ez_search_for_new_episode(r1.text, self.silo_SEA, self.silo_SEA_REG)
                resp1080p = len(p1_list[0])
                resp720p = len(p1_list[1])
                count += resp1080p + resp720p
                print("\nEZ silo {} => \n\tstatus: {}, \n\t1080p: {}\n\t720p: {}".format(self.silo_SEA, r1_resp, resp1080p, resp720p))
            else:
                print("\nEZ silo {} => status: {}".format(self.silo_SEA, r1_resp))
            return count
        except requests.exceptions.ConnectionError:
            print("silo unable to connect to EZTV")
            return 0
            
    def search_silo_ka(self):
        try:
            r2 = requests.get(self.silo_KA_1)
            r2_resp = r2.status_code
            r3 = requests.get(self.silo_KA_2)
            r3_resp = r3.status_code
            count = 0
            if r2_resp == 200 and r3_resp == 200:
                p1_list = search.ka_search_for_new_episode(r2.text, self.silo, self.silo_SEA_REG)
                p2_list = search.ka_search_for_new_episode(r3.text, self.silo, self.silo_SEA_REG)
                res = (len(p1_list[0]), len(p1_list[1]))
                res1 = (len(p2_list[0]), len(p2_list[1]))
                count = res[0] + res[1] + res1[0] + res1[1]
                print("KA silo {} => \n\tstatus: {}\n\t1080p: {}\n\t720p: {}".format(self.silo_SEA, r3_resp, res1[0], res1[1]))
            else:
                print("KA silo {} => status: {}".format(self.silo_SEA, r3_resp))
            return count
        except requests.exceptions.ConnectionError as e:
            print(e)
            return 0
            

    def search_silo(self):
        if self.args.eztv:
            ez_count = self.search_silo_ez()
            return ez_count
        elif self.args.kickass:
            ka_count = self.search_silo_ka()
            return ka_count
        elif self.args.all:
            if self.args.eztv == True and self.args.kickass == True:
                print("Setting the -e and k flags are not allowed when using the --all flag")
            else:
                ez_count = self.search_silo_ez()
                ka_count = self.search_silo_ka()
                return ez_count + ka_count