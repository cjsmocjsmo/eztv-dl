#!/usr/bin/python3

import re
import os
import time
import requests
import xml.etree.ElementTree as ET
import sqlite3
# import TGZlib as tgzlib
# import sqlite3
import logging
import EZrsslib as ezlib

from pprint import pprint

logger = logging.getLogger(__name__)
# Set the log level
logger.setLevel(logging.DEBUG)
# Create a file handler
file_handler = None
if os.path.exists('/home/teresa/ScraperLogs/EZ.log'):
    file_handler = logging.FileHandler('/home/teresa/ScraperLogs/EZ.log', mode='w')
elif os.path.exists("/home/pi/ScraperLogs/EZ.log"):
    file_handler = logging.FileHandler('/home/pi/eztv-dl/scrapers/EZ_log.txt', mode='w')
# Set the formatter for the file handler
file_handler.setFormatter(logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s'))
# Add the file handler to the logger
logger.addHandler(file_handler)

class EZXML:

    def get_xml_file(self):
        logger.info("Starting EZXML.get_xml_file()")
        url = "https://eztv.re/ezrss.xml"
        outfilename = "/home/pi/eztv-dl/scrapers/eztv.xml"

        r = requests.get(url)
        r_resp = r.status_code

        if r_resp == 200:
            with open(outfilename, 'wb') as f:
                f.write(r.content)


        result_list = []
        tree = ET.parse(outfilename)
        root = tree.getroot()
        for child in root:
            result_list = []
            
            for itemc in child:
                # print(len(itemc))
                result = {}
                count = 0
                if len(itemc) > 0:
                    
                    for item in itemc:
                        # print(item.tag)
                        count += 1
                        # print(count)

                        if item.tag == 'guid':
                            id = ezlib.Utils().gen_md5_hash(item.text)
                            result['myid'] = id

                        if item.tag == 'title':
                            new_tit = ezlib.Utils().trim_title(item.text)
                            result['title'] = new_tit

                        if item.tag == "link":
                            result['link'] = item.text

                        if item.tag == 'category':
                            result['category'] = item.text

                        if item.tag == 'pubDate':
                            new_pubdate = ezlib.Utils().trim_pubdate(item.text)
                            result['pubdate'] = new_pubdate

                        if item.tag == '{http://xmlns.ezrss.it/0.1/}magnetURI':
                            result['magnetURI'] = item.text

                        if item.tag == '{http://xmlns.ezrss.it/0.1/}fileName':
                            result['filename'] = item.text
                            ext = os.path.splitext(item.text)[1]
                            result['ext'] = ext
                    
                    result_list.append(result)
                        
        return result_list



    def main(self):
        res = self.get_xml_file()
        connection = sqlite3.connect('/home/pi/eztv-dl/scrapers/EZ.db')
        cursor = connection.cursor()
        tv_table = ezlib.SQL().create_tv_table(cursor, connection)
        insert_tv = ezlib.SQL().insert_tv(cursor, connection, res)
        # pprint(res)
        # print(len(res))
        return len(res)


if __name__ == '__main__':
    start_time = time.time()
    voodoo = EZXML().main()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Total episodes found {}".format(voodoo))
    logger.info("Total episodes found {}".format(voodoo))
    print("Elapsed time: {}".format(elapsed_time))
    logger.info("Elapsed time: {}".format(elapsed_time))