#!/usr/bin/python3

import os
import glob
import logging

class CleanDropbox:
    def __init__(self):
        self.picpath = "/home/teresa/Dropbox/Apps/BarPiCam/*.jpg"
        self.logfile = "/home/teresa/Desktop/DropBoxLogs.txt"

    def setup_logging(self):
        if not os.path.exists(self.logfile):
            with open(self.logfile, "w") as newfile:
                newfile.write("LOG FILE CREATED \n")

        logging.basicConfig(
            filename =self.logfile,
            level = logging.DEBUG,
            format = '%(levelname)s:%(asctime)s:%(message)s',
        )

    def glob_dir(self, picpath):
        logging.debug("globbing dir")
        return glob.glob(picpath)

    def remove_pics(self, piclist):
        logging.debug("removing files")
        [os.remove(pic) for pic in piclist]
        

    def main(self):
        self.setup_logging()
        pics = self.glob_dir(self.picpath)
        print(pics)
        pic_count = len(pics)
        self.remove_pics(pics)
        logging.debug("removed {} files".format(pic_count))

if __name__ == "__main__":
    cdb = CleanDropbox()
    cdb.main()