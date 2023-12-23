#!/usr/bin/python3

import urllib.request
import gzip
import shutil
import datetime
import re
import glob
import os
import sqlite3

from pprint import pprint

class DownLoad:
    def __init__(self):
        self.prefix = '/home/pi/Documents/tgx'
        try:
            os.mkdir(self.prefix)
        except FileExistsError:
            pass


    def clean_download_dir(self):
        gzfiles = glob.glob(self.prefix + '*.gz')
        gzrm = [os.remove(gz) for gz in gzfiles]

        txtfiles = glob.glob(self.prefix + '*.txt')
        txrm = [os.remove(txt) for txt in txtfiles]

    def create_io_files(self):
        now = datetime.datetime.now()
        current_date = now.strftime("%Y-%m-%d %H:%M:%S")
        new_outfile = self.prefix + current_date + "-tgx24hdump.txt"
        new_infile = self.prefix + current_date + '_tgx.gz'
        return (new_infile, new_outfile)

    def download_file(self):
        io_files = self.create_io_files()
        new_infile = io_files[0]
        new_outfile = io_files[1]

        url = 'https://torrentgalaxy.mx/cache/tgx24hdump.txt.gz'
        urllib.request.urlretrieve(url, new_infile)
        # Open the gz file and extract its contents
        with gzip.open(new_infile, 'rb') as f_in:
            with open(new_outfile, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
        return new_outfile

class Utils:
    def read_the_file(self, afile):
        with open(afile, 'r') as f:
            line_list = [line for line in f]
        return line_list

    def filter_by_TV(self, line_list):
        tv_list = [line for line in line_list if re.search("TV", line) != None]
        return tv_list

    def filter_by_Movies(self, line_list):
        movie_list = [line for line in line_list if re.search("Movies", line) != None]
        return movie_list

    def filter_by_1080p(self, line_list):
        alist = [line for line in line_list if re.search("1080p", line) != None]
        return alist

    def filter_by_720p(self, line_list):
        alist = [line for line in line_list if re.search("720p", line) != None]
        return alist

    def filter_by_title(self, line_list, atitle):
        alist = [line for line in line_list if re.search(atitle, line) != None]
        return alist

    def process_entry(self, line_list, regex1, regex2, season1, season2):
        alist = []
        prelimlist = []
        masterlist = []
        for line in line_list:
            if re.search(regex1, line) != None:
                alist.append(line)
            if regex2 != None:
                if re.search(regex2, line) != None:
                    alist.append(line)
        list1080p = self.filter_by_1080p(alist)
        if len(list1080p) > 0:
            prelimlist.extend(list1080p)
        else:
            list720p = self.filter_by_720p(alist)
            prelimlist.extend(list720p)

        m1 = [line for line in prelimlist if re.search(season1, line) != None]
        m2 = [line for line in prelimlist if re.search(season2, line) != None]

        masterlist = m1 + m2

        return masterlist

    def process_title(self, title):
        twone = re.compile(r".2160p")
        twonel = re.compile(r".2160P")
        tenp = re.compile(r".1080p")
        tenpl = re.compile(r".1080P")
        sevp = re.compile(r".720p")
        sevpl = re.compile(r".720P")
        forp = re.compile(r".480p")
        forpl = re.compile(r".480P")
        ptv = re.compile(r".PTV")

        newtitle = ""
        year = ""
        if re.search(twone, title) != None:
            newtitle = re.split(twone, title)[0].replace(".", " ").replace("(", "").replace(")", "")
            year = newtitle[-4:]
            newtitle = newtitle[:-4].lower()
        elif re.search(twonel, title) != None:
            newtitle = re.split(twonel, title)[0].replace(".", " ").replace("(", "").replace(")", "")
            year = newtitle[-4:]
            newtitle = newtitle[:-4].lower()
        elif re.search(tenp, title) != None:
            newtitle = re.split(tenp, title)[0].replace(".", " ").replace("(", "").replace(")", "")
            year = newtitle[-4:]
            newtitle = newtitle[:-4].lower()
        elif re.search(tenpl, title) != None:
            newtitle = re.split(tenpl, title)[0].replace(".", " ").replace("(", "").replace(")", "")
            year = newtitle[-4:]
            newtitle = newtitle[:-4].lower()
        elif re.search(sevp, title) != None:
            newtitle = re.split(sevp, title)[0].replace(".", " ").replace("(", "").replace(")", "")
            year = newtitle[-4:]
            newtitle = newtitle[:-4].lower()
        elif re.search(sevpl, title) != None:
            newtitle = re.split(sevpl, title)[0].replace(".", " ").replace("(", "").replace(")", "")
            year = newtitle[-4:]
            newtitle = newtitle[:-4].lower()
        elif re.search(ptv, title) != None:
            newtitle = re.split(ptv, title)[0].replace(".", " ").replace("(", "").replace(")", "")
            year = newtitle[-4:]
            newtitle = newtitle[:-4].lower()
        elif re.search(forp, title) != None:
            newtitle = re.split(forp, title)[0].replace(".", " ").replace("(", "").replace(")", "")
            year = newtitle[-4:]
            newtitle = newtitle[:-4].lower()
        elif re.search(forpl, title) != None:
            newtitle = re.split(forpl, title)[0].replace(".", " ").replace("(", "").replace(")", "")
            year = newtitle[-4:]
            newtitle = newtitle[:-4].lower()
        else:
            pass
        return (newtitle, year)

    def create_mov_dict_list(self, mov_list_raw):
        movie_list = []
        for mov in mov_list_raw:
            crap = mov.split('|')
            title, year = self.process_title(crap[1])
            info = {
                "id": crap[0],
                "raw_title": crap[1],
                "title": title,
                "year": year,
                "addedon": datetime.date.today(),
                "catagory": crap[2].lower(),
                "link1": crap[3],
                "link2": crap[4],
            }
            movie_list.append(info)
        return movie_list

    def create_tv_dict_list(self, tv_list_raw):
        tv_list = []
        for tv in tv_list_raw:
            crap = tv.split('|')
            title, year = self.process_title(crap[1])
            info = {
                "id": crap[0],
                "raw_title": crap[1],
                "title": title,
                "year": year,
                "addedon": datetime.date.today(),
                "catagory": crap[2].lower(),
                "link1": crap[3],
                "link2": crap[4],
            }
            tv_list.append(info)
        return tv_list



class SQL:
    def create_tv_table(self, cursor, connection):
        query1 = """CREATE TABLE IF NOT EXISTS tv
                (id INTEGER PRIMARY KEY AUTOINCREMENT, catagory TEXT, myid TEXT NOT NULL UNIQUE, year TEXT, addedon TEXT, link1 TEXT, link2 TEXT, raw_title TEXT, title TEXT)"""
        cursor.execute(query1)
        connection.commit()

    def insert_tv(self, cursor, connection, tv_list):
        for tv in tv_list:
            try:
                sql_query = """INSERT INTO tv
                            (catagory, myid, year, addedon, link1, link2, raw_title, title)
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?)"""
                data_tup = (tv['catagory'], tv['id'], tv['year'], tv['addedon'], tv['link1'], tv['link2'], tv['raw_title'], tv['title'])
                cursor.execute(sql_query, data_tup)
                connection.commit()
            except sqlite3.IntegrityError:
                pass

    def create_movies_table(self, cursor, connection):
        query1 = """CREATE TABLE IF NOT EXISTS movies
                (id INTEGER PRIMARY KEY AUTOINCREMENT, catagory TEXT, myid TEXT NOT NULL UNIQUE, year TEXT, addedon TEXT, link1 TEXT, link2 TEXT, raw_title TEXT, title TEXT)"""
        cursor.execute(query1)
        connection.commit()

    def insert_movies(self, cursor, connection, mov_list):
        for mov in mov_list:
            try:
                sql_query = """INSERT INTO movies
                            (catagory, myid, year, addedon, link1, link2, raw_title, title)
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?)"""
                data_tup = (mov['catagory'], mov['id'], mov['year'], mov['addedon'], mov['link1'], mov['link2'], mov['raw_title'], mov['title'])
                cursor.execute(sql_query, data_tup)
                connection.commit()
            except sqlite3.IntegrityError:
                pass

    def tv_count(self, cursor):
        sql_query = """SELECT COUNT(*) FROM tv"""
        cursor.execute(sql_query)
        return cursor.fetchone()

    def movie_count(self, cursor):
        sql_query = """SELECT COUNT(*) FROM movies"""
        cursor.execute(sql_query)
        return cursor.fetchone()

# "Godzilla Minus One"

class TVSearch:
    def __init__(self):

        self.andor = re.compile(r'andor')
        self.ANDOR = re.compile(r"s02e01")

        self.lower_decks1 = re.compile(r'lower decks')
        self.lower_decks2 = re.compile(r'lower.decks')
        self.LOWERDECKS  = re.compile(r"s04e08")

        self.discovery = re.compile(r'discovery')
        self.DISCOVERY = re.compile(r"s05e01")

        self.mandalorian = re.compile(r"mandalorian")
        self.MANDALORIAN = re.compile(r"s04e01")

        self.orville = re.compile(r"orville")
        self.ORVILLE = re.compile(r"s04e01")

        self.for_all_mankind1 = re.compile(r"for all mankind")
        self.for_all_mankind2 = re.compile(r"for.all.mankind")
        self.FORALLMANKIND   = re.compile(r"s04e01")

        self.bad_batch1 = re.compile(r"bad batch")
        self.bad_batch2 = re.compile(r"bad.batch")
        self.BADBATCH   = re.compile(r"s03e01")

        self.wheel_of_time1 = re.compile(r"wheel of time")
        self.wheel_of_time2 = re.compile(r"wheel.of.time")
        self.WHEELOFTIME    = re.compile(r"s03e01")

        self.foundation = re.compile(r"foundation")
        self.FOUNDATION = re.compile(r's03e01')

        self.starwarsvisions1 = re.compile(r"star wars visions")
        self.starwarsvisions2 = re.compile(r"star.wars.visions")
        self.STARWARSVISIONS  = re.compile(r's02e05')

        self.startrekprodigy = re.compile(r"star trek prodigy")
        self.startrekprodigy2 = re.compile(r"star.trek.prodigy")
        self.STARTREKPRODIGY2 = re.compile(r"s02e01")

        self.bookofbobafett = re.compile(r"book of boba fett")
        self.bookofbobafett2 = re.compile(r"book.of.boba.fett")
        self.BOOKOFBOBAFETT2 = re.compile(r"s02e01")

        self.continental = re.compile(r"continental")
        self.CONTINENTAL = re.compile(r"s02e01")

        self.halo = re.compile(r"halo")
        self.HALO = re.compile(r"s02e01")

        self.strangenewworlds = re.compile(r"strange new worlds")
        self.strangenewworlds2 = re.compile(r"strange.new.worlds")
        self.STRANGENEWWORLDS = re.compile(r"s03e01")

        self.prehistoricplanet = re.compile(r"prehistoric planet")
        self.prehistoricplanet2 = re.compile(r"pre historic planet")
        self.prehistoricplanet3 = re.compile(r"prehistoric.planet")
        self.prehistoricplanet4 = re.compile(r"pre.historic.planet")
        self.PREHISTORICPLANET = re.compile(r"s03e01")

        self.obiwankenobi = re.compile(r"obi wan kenobi")
        self.obiwankenobi2 = re.compile(r"obi.wan.kenobi")
        self.OBIWANKENOBI = re.compile(r"s02e01")

        self.groot = re.compile(r"groot")
        self.GROOT = re.compile(r"s02e01")

        self.houseofthedragon = re.compile(r"house of the dragon")
        self.houseofthedragon2 = re.compile(r"house.of.the.dragon")
        self.HOUSEOFTHEDRAGON = re.compile(r"s02e01")

        self.lordoftherings = re.compile(r"lord of the rings the rings of power")
        self.lordoftherings2 = re.compile(r"lord.of.the.rings.the.rings.of.power")
        self.LORDOFTHERINGS = re.compile(r"s02e01")

        self.silo = re.compile(r"silo")
        self.SILO = re.compile(r"s02e01")

        self.ahsoka = re.compile(r"ahsoka")
        self.AHSOKA = re.compile(r"s02e01")

        self.droidstory = re.compile(r"droid story")
        self.droidstory2 = re.compile(r"droid.story")
        self.DROIDSTORY = re.compile(r"s02e01")

        self.wakanda = re.compile(r"wakanda")
        self.WAKANDA = re.compile(r"s02e01")

        self.acolyte = re.compile(r"acolyte")
        self.ACOLYTE = re.compile(r"s02e01")

        self.lando = re.compile(r"lando")
        self.LANDO = re.compile(r"s02e01")


    def andor_search(self, apath):
        resp = False
        resp2 = False
        if re.search(self.andor, apath['title']) != None:
            resp = True
        else:
            resp = False

        if resp:
            if re.search(self.ANDOR, apath['title']) != None:
                resp2 = True
            else:
                resp2 = False

        if resp == True and resp2 == True:
            return (apath['title'], apath['id'])
        else:
            return None

    def lower_decks_search(self, apath):
        resp = False
        resp2 = False
        if re.search(self.lower_decks1, apath['title']) != None:
            resp = True
        elif re.search(self.lower_decks2, apath['title']) != None:
            resp = True
        else:
            resp = False

        if resp:
            if re.search(self.LOWERDECKS, apath['title']) != None:
                resp2 = True
            else:
                resp2 = False

        if resp == True and resp2 == True:
            return (apath['title'], apath['id'])
        else:
            return None

    def discovery_search(self, apath):
        resp = False
        resp2 = False
        if re.search(self.discovery, apath['title']) != None:
            resp = True
        else:
            resp = False

        if resp:
            if re.search(self.DISCOVERY, apath['title']) != None:
                resp2 = True
            else:
                resp2 = False

        if resp == True and resp2 == True:
            return (apath['title'], apath['id'])
        else:
            return None

    def mandalorian_search(self, apath):
        resp = False
        resp2 = False
        if re.search(self.mandalorian, apath['title']) != None:
            resp = True
        else:
            resp = False

        if resp:
            if re.search(self.MANDALORIAN, apath['title']) != None:
                resp2 = True
            else:
                resp2 = False

        if resp == True and resp2 == True:
            return (apath['title'], apath['id'])
        else:
            return None

    def orville_search(self, apath):
        resp = False
        resp2 = False
        if re.search(self.orville, apath['title']) != None:
            resp = True
        else:
            resp = False

        if resp:
            if re.search(self.ORVILLE, apath['title']) != None:
                resp2 = True
            else:
                resp2 = False

        if resp == True and resp2 == True:
            return (apath['title'], apath['id'])
        else:
            return None

    def for_all_man_kind_search(self, apath):
        resp = False
        resp2 = False
        if re.search(self.for_all_mankind1, apath['title']) != None:
            resp = True
        elif re.search(self.for_all_mankind2, apath['title']) != None:
            resp = True
        else:
            resp = False

        if resp:
            if re.search(self.FORALLMANKIND, apath['title']) != None:
                resp2 = True
            else:
                resp2 = False

        if resp == True and resp2 == True:
            return (apath['title'], apath['id'])
        else:
            return None

    def bad_batch_search(self, apath):
        resp = False
        resp2 = False
        if re.search(self.bad_batch1, apath['title']) != None:
            resp = True
        elif re.search(self.bad_batch2, apath['title']) != None:
            resp = True
        else:
            resp = False

        if resp:
            if re.search(self.BADBATCH, apath['title']) != None:
                resp2 = True
            else:
                resp2 = False

        if resp == True and resp2 == True:
            return (apath['title'], apath['id'])
        else:
            return None

    def wheel_of_time_search(self, apath):
        resp = False
        resp2 = False
        if re.search(self.wheel_of_time1, apath['title']) != None:
            resp = True
        elif re.search(self.wheel_of_time2, apath['title']) != None:
            resp = True
        else:
            resp = False

        if resp:
            if re.search(self.WHEELOFTIME, apath['title']) != None:
                resp2 = True
            else:
                resp2 = False

        if resp == True and resp2 == True:
            return (apath['title'], apath['id'])
        else:
            return None

    def foundation_search(self, apath):
        resp = False
        resp2 = False
        if re.search(self.foundation, apath['title']) != None:
            resp = True
        else:
            resp = False

        if resp:
            if re.search(self.FOUNDATION, apath['title']) != None:
                resp2 = True
            else:
                resp2 = False

        if resp == True and resp2 == True:
            return (apath['title'], apath['id'])
        else:
            return None

    def starwarsvisions_search(self, apath):
        resp = False
        resp2 = False
        if re.search(self.starwarsvisions1, apath['title']) != None:
            resp = True
        elif re.search(self.starwarsvisions2, apath['title']) != None:
            resp = True
        else:
            resp = False

        if resp:
            if re.search(self.STARWARSVISIONS, apath['title']) != None:
                resp2 = True
            else:
                resp2 = False

        if resp == True and resp2 == True:
            return (apath['title'], apath['id'])
        else:
            return None

    def startrekprodigy_search(self, apath):
        resp = False
        resp2 = False
        if re.search(self.startrekprodigy, apath['title']) != None:
            resp = True
        elif re.search(self.startrekprodigy2, apath['title']) != None:
            resp = True
        else:
            resp = False

        if resp:
            if re.search(self.STARTREKPRODIGY2, apath['title']) != None:
                resp2 = True
            else:
                resp2 = False

        if resp == True and resp2 == True:
            return (apath['title'], apath['id'])
        else:
            return None

    def bookofbobafett_search(self, apath):
        resp = False
        resp2 = False
        if re.search(self.bookofbobafett, apath['title']) != None:
            resp = True
        elif re.search(self.bookofbobafett2, apath['title']) != None:
            resp = True
        else:
            resp = False

        if resp:
            if re.search(self.BOOKOFBOBAFETT2, apath['title']) != None:
                resp2 = True
            else:
                resp2 = False

        if resp == True and resp2 == True:
            return (apath['title'], apath['id'])
        else:
            return None

    def continental_search(self, apath):
        resp = False
        resp2 = False
        if re.search(self.continental, apath['title']) != None:
            resp = True
        else:
            resp = False

        if resp:
            if re.search(self.CONTINENTAL, apath['title']) != None:
                resp2 = True
            else:
                resp2 = False

        if resp == True and resp2 == True:
            return (apath['title'], apath['id'])
        else:
            return None

    def halo_search(self, apath):
        resp = False
        resp2 = False
        if re.search(self.halo, apath['title']) != None:
            resp = True
        else:
            resp = False

        if resp:
            if re.search(self.HALO, apath['title']) != None:
                resp2 = True
            else:
                resp2 = False

        if resp == True and resp2 == True:
            return (apath['title'], apath['id'])
        else:
            return None

    def strangenewworlds_search(self, apath):
        resp = False
        resp2 = False
        if re.search(self.strangenewworlds, apath['title']) != None:
            resp = True
        elif re.search(self.strangenewworlds2, apath['title']) != None:
            resp = True
        else:
            resp = False

        if resp:
            if re.search(self.STRANGENEWWORLDS, apath['title']) != None:
                resp2 = True
            else:
                resp2 = False

        if resp == True and resp2 == True:
            return (apath['title'], apath['id'])
        else:
            return None

    def prehistoricplanet_search(self, apath):
        resp = False
        resp2 = False
        if re.search(self.prehistoricplanet, apath['title']) != None:
            resp = True
        elif re.search(self.prehistoricplanet2, apath['title']) != None:
            resp = True
        elif re.search(self.prehistoricplanet3, apath['title']) != None:
            resp = True
        elif re.search(self.prehistoricplanet4, apath['title']) != None:
            resp = True
        else:
            resp = False

        if resp:
            if re.search(self.PREHISTORICPLANET, apath['title']) != None:
                resp2 = True
            else:
                resp2 = False

        if resp == True and resp2 == True:
            return (apath['title'], apath['id'])
        else:
            return None

    def obiwankenobi_search(self, apath):
        resp = False
        resp2 = False
        if re.search(self.obiwankenobi, apath['title']) != None:
            resp = True
        elif re.search(self.obiwankenobi2, apath['title']) != None:
            resp = True
        else:
            resp = False

        if resp:
            if re.search(self.OBIWANKENOBI, apath['title']) != None:
                resp2 = True
            else:
                resp2 = False

        if resp == True and resp2 == False:
            return (apath['title'], apath['id'])
        else:
            return None

    def groot_search(self, apath):
        resp = False
        resp2 = False
        if re.search(self.groot, apath['title']) != None:
            resp = True
        else:
            resp = False

        if resp:
            if re.search(self.GROOT, apath['title']) != None:
                resp2 = True
            else:
                resp2 = False

        if resp == True and resp2 == False:
            return (apath['title'], apath['id'])
        else:
            return None

    def houseofthedragon_search(self, apath):
        resp = False
        resp2 = False
        if re.search(self.houseofthedragon, apath['title']) != None:
            resp = True
        elif re.search(self.houseofthedragon2, apath['title']) != None:
            resp = True
        else:
            resp = False

        if resp:
            if re.search(self.HOUSEOFTHEDRAGON, apath['title']) != None:
                resp2 = True
            else:
                resp2 = False

        if resp == True and resp2 == False:
            return (apath['title'], apath['id'])
        else:
            return None

    def lordoftherings_search(self, apath):
        resp = False
        resp2 = False
        if re.search(self.lordoftherings, apath['title']) != None:
            resp = True
        elif re.search(self.lordoftherings2, apath['title']) != None:
            resp = True
        else:
            resp = False

        if resp:
            if re.search(self.LORDOFTHERINGS, apath['title']) != None:
                resp2 = True
            else:
                resp2 = False

        if resp == True and resp2 == False:
            return (apath['title'], apath['id'])
        else:
            return None

    def silo_search(self, apath):
        resp = False
        resp2 = False
        if re.search(self.silo, apath['title']) != None:
            resp = True
        else:
            resp = False

        if resp:
            if re.search(self.SILO, apath['title']) != None:
                resp2 = True
            else:
                resp2 = False

        if resp == True and resp2 == False:
            return (apath['title'], apath['id'])
        else:
            return None

    def ahsoka_search(self, apath):
        resp = False
        resp2 = False
        if re.search(self.ahsoka, apath['title']) != None:
            resp = True
        else:
            resp = False

        if resp:
            if re.search(self.AHSOKA, apath['title']) != None:
                resp2 = True
            else:
                resp2 = False

        if resp == True and resp2 == False:
            return (apath['title'], apath['id'])
        else:
            return None

    def droidstory_search(self, apath):
        resp = False
        resp2 = False
        if re.search(self.droidstory, apath['title']) != None:
            resp = True
        elif re.search(self.droidstory2, apath['title']) != None:
            resp = True
        else:
            resp = False

        if resp:
            if re.search(self.DROIDSTORY, apath['title']) != None:
                resp2 = True
            else:
                resp2 = False

        if resp == True and resp2 == False:
            return (apath['title'], apath['id'])
        else:
            return None

    def wakanda_search(self, apath):
        resp = False
        resp2 = False
        if re.search(self.wakanda, apath['title']) != None:
            resp = True
        else:
            resp = False

        if resp:
            if re.search(self.WAKANDA, apath['title']) != None:
                resp2 = True
            else:
                resp2 = False

        if resp == True and resp2 == False:
            return (apath['title'], apath['id'])
        else:
            return None

    def acolyte_search(self, apath):
        resp = False
        resp2 = False
        if re.search(self.acolyte, apath['title']) != None:
            resp = True
        else:
            resp = False

        if resp:
            if re.search(self.ACOLYTE, apath['title']) != None:
                resp2 = True
            else:
                resp2 = False

        if resp == True and resp2 == False:
            return (apath['title'], apath['id'])
        else:
            return None

    def lando_search(self, apath):
        resp = False
        resp2 = False
        if re.search(self.lando, apath['title']) != None:
            resp = True
        else:
            resp = False

        if resp:
            if re.search(self.LANDO, apath['title']) != None:
                resp2 = True
            else:
                resp2 = False

        if resp == True and resp2 == True:
            return (apath['title'], apath['id'])
        else:
            return None