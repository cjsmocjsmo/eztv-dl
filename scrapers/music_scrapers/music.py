import gzip
import shutil
import urllib.request
import os
import datetime
import glob
from pprint import pprint


class DownLoad:
    def __init__(self):
        self.prefix = '/home/teresa/Documents/tgx/'
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
        # Open the gz file and extract its contents
        with gzip.open(new_infile, 'rb') as f_in:
            with open(new_outfile, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
        return new_outfile

    def parse_file(self):
        dlist = []
        open_file = self.download_file()
        with open(open_file, 'r') as f:
            lines = f.readlines()
            for line in lines:
                data = line.split("|")
                if data[2] == "Music":
                    print(data[1])
                    user_choice = input("Enter 0 to save, 1 to delete: ")
                    if user_choice == '0':
                        # Save logic here
                        dlist.append(data)
                    elif user_choice == '1':
                        # Delete logic here
                        pass
                    else:
                        print("Invalid choice. Please enter 0 or 1.")
        pprint(dlist)

if __name__ == "__main__":
    dl = DownLoad()
    dl.clean_download_dir()
    dlfile = dl.download_file()
    dl.parse_file()