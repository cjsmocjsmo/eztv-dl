import requests
import re
import shows.search as search

class LowerDecks:
    def __init__(self, args, cwd):
        self.args = args
        self.LOWERDECKS = re.compile(r"lower decks")
        self.LOWERDECKS_SEA = "s05e09"
        self.LOWERDECKS_SEA_REG = re.compile(self.LOWERDECKS_SEA)
        self.LOWERDECKS_EZ_1 = "https://eztv.re/search/lower-decks"
        self.LOWERDECKS_KA_1 = "https://kickasstorrents.to/usearch/lowerdecks"
        self.LOWERDECKS_KA_2 = "https://kickasstorrents.to/usearch/lowerdecks/2"
        self.LOWERDECKS_1337x_1 = "https://www.1377x.to/search/lowerdecks"
        self.LOWERDECKS_1337x_2 = "https://www.1377x.to/search/lowerdecks/2"

    def search_lowerdecks_ez(self):
        try:
            r1 = requests.get(self.LOWERDECKS_EZ_1)
            r1_resp = r1.status_code
            count = 0
            if r1_resp == 200:
                p1_list = search.Search().ez_search_for_new_episode(r1.text, self.LOWERDECKS_SEA, self.LOWERDECKS_SEA_REG)
                resp1080p = len(p1_list[0])
                resp720p = len(p1_list[1])
                count += resp1080p + resp720p
                print("\nEZ LOWERDECKS {} => \n\tstatus: {}, \n\t1080p: {}\n\t720p: {}".format(self.LOWERDECKS_SEA, r1_resp, resp1080p, resp720p))
                
            else:
                print("\nEZ LOWERDECKS {} => status: {}".format(self.LOWERDECKS_SEA, r1_resp))
            return count
        except requests.exceptions.ConnectionError:
            print("LOWERDECKS unable to connect to EZTV")
            return 0

    def search_lowerdecks_ka(self):
        try:
            r2 = requests.get(self.LOWERDECKS_KA_1)
            r2_resp = r2.status_code
            count = 0
            if r2_resp == 200:
                p2_list = self.ka_search_for_new_episode(r2.text, self.LOWERDECKS, self.LOWERDECKS_SEA_REG)
                res1 = (len(p2_list[0]), len(p2_list[1]))
                count += res1[0] + res1[1]
                print("KA LOWERDECKS {} => \n\tstatus: {}\n\t1080p: {}\n\t720p: {}".format(self.LOWERDECKS_SEA, r2_resp, res1[0], res1[1]))
                
            else:
                print("KA LOWERDECKS {} => status: {}".format(self.LOWERDECKS_SEA, r2_resp))
            return count
        except requests.exceptions.ConnectionError as e:
            print(e)
            return 0

    def search_lowerdecks(self):
        if self.args.eztv:
            ez_count = self.search_lowerdecks_ez()
            return ez_count
        elif self.args.kickass:
            ka_count = self.search_lowerdecks_ka()
            return ka_count
        elif self.args.all:
            if self.args.eztv == True and self.args.kickass == True:
                print("Setting the -e and k flags are not allowed when using the --all flag")
            else:
                ez_count = self.search_lowerdecks_ez()
                ka_count = self.search_lowerdecks_ka()
                return ez_count + ka_count