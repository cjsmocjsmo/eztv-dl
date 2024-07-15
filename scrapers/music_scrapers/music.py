import gzip
import shutil
import urllib.request
import os
import datetime
import glob
import re
from pprint import pprint

class DownLoad:
    def __init__(self):
        self.prefix = '/home/charliepi/Documents/tgx/'
        self.downloads = '/home/charliepi/Documents/tgx/Downloads.txt'
        try:
            os.mkdir(self.prefix)
        except FileExistsError:
            pass
        self.s1 = re.compile(r"Various Artists")
        self.s2 = re.compile(r"COUNTRY")

    def clean_download_dir(self):
        gzfiles = glob.glob(self.prefix + '*.gz')
        gzrm = [os.remove(gz) for gz in gzfiles]
        txtfiles = glob.glob(self.prefix + '*.txt')
        txrm = [os.remove(txt) for txt in txtfiles]

    def create_io_files(self):
        now = datetime.datetime.now()
        current_date = now.strftime("%Y-%m-%d %H:%M:%S")
        new_outfile = self.prefix + current_date + "_tgx24hdump.txt"
        new_infile = self.prefix + current_date + '_tgx.gz'
        return (new_infile, new_outfile)
    
    def download_file(self):
        io_files = self.create_io_files()
        new_infile = io_files[0]
        new_outfile = io_files[1]
        new_outfile = new_outfile.replace(" ", "_")
        url = 'https://torrentgalaxy.mx/cache/tgx24hdump.txt.gz'
        urllib.request.urlretrieve(url, new_infile)
        with gzip.open(new_infile, 'rb') as f_in:
            with open(new_outfile, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
        return new_outfile

    def parse_file(self):
        dlist = []
        open_file = self.download_file()
        with open(open_file, 'r', encoding='utf-8', errors='replace') as f:
            lines = f.readlines()
            for line in lines:
                data = line.split("|")
                if data[2] == "Music":
                    if re.search(self.s1, data[1]):
                        dlist.append(data[4])
                    if re.search(self.s2, data[1]):
                        dlist.append(data[4])
                    print(data)
        pprint(dlist)
        with open(self.downloads, 'a') as download_file:
            for item in dlist:
                download_file.write(item + "\n")  # Add a newline character for each item

if __name__ == "__main__":
    dl = DownLoad()
    dl.clean_download_dir()
    dlfile = dl.download_file()
    dl.parse_file()