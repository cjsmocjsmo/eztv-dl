import hashlib
import re
import sqlite3

S1 = re.compile("1080p")
S2 = re.compile("720p")
S3 = re.compile("480p")
S4 = re.compile("xvid-afg")

class Utils:
    def gen_md5_hash(self, guid_text):
        guid_hash = hashlib.md5(guid_text.encode())
        return guid_hash.hexdigest()
    
    def trim_title(self, atitle):
        atitle = atitle.lower()
        if re.search(S1, atitle) != None:
            start = re.search(S1, atitle).start()
            split_start = start - 1
            new_title = atitle[:split_start]
            return new_title
        elif re.search(S2, atitle) != None:
            start = re.search(S2, atitle).start()
            split_start = start - 1
            new_title = atitle[:split_start]
            return new_title
        elif re.search(S3, atitle) != None:
            start = re.search(S3, atitle).start()
            split_start = start - 1
            new_title = atitle[:split_start]
            return new_title
        elif re.search(S4, atitle) != None:
            start = re.search(S4, atitle).start()
            split_start = start - 1
            new_title = atitle[:split_start]
            return new_title
        else:
            print(atitle)

    def trim_pubdate(self, pubdate):
        pubdate = pubdate.replace(",", "")
        pubdate_split = pubdate.split(" ")
        pub_len = len(pubdate_split)
        new_pubdate = pubdate_split[:pub_len - 2]
        new_pubdate = " ".join(new_pubdate)
        return new_pubdate


class SQL:
    def create_tv_table(self, cursor, connection):
        query1 = """CREATE TABLE IF NOT EXISTS tv
                (id INTEGER PRIMARY KEY AUTOINCREMENT, category TEXT, myid TEXT NOT NULL UNIQUE, title TEXT, link TEXT, pubdate TEXT, magnetURI TEXT, filename TEXT, ext TEXT)"""
        cursor.execute(query1)
        connection.commit()

    def insert_tv(self, cursor, connection, tv_list):
        for tv in tv_list:
            try:
                sql_query = """INSERT INTO tv
                            (category, myid, title, link, pubdate, magnetURI, filename, ext)
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?)"""
                data_tup = (tv['category'], tv['myid'], tv['title'], tv['link'], tv['pubdate'], tv['magnetURI'], tv['filename'], tv['ext'])
                cursor.execute(sql_query, data_tup)
                connection.commit()
            except sqlite3.IntegrityError:
                pass