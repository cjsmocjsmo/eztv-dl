#!/usr/bin/python3

import os
import subprocess

class GetVidSize:
    def __init__(self):
        self.folder = "/media/pipi/FOO"
        self.oversized = []

    def find_files(self):
        for (paths, dirs, files) in os.walk(self.folder, followlinks=True):
            for filename in files:
                fnn = os.path.join(paths, filename)
                _, ext = os.path.splitext(fnn)
                if ext == ".mkv":
                    size = os.stat(fnn).st_size
                    print(size)
                    if size > 1073741824:
                        tup = (fnn, size)
                        
                        self.oversized.append(tup)

    def resize_vid(self, fn):
        filename, ext = os.path.splitext(fn)
        outfile = filename + ".mp4"
        cmd = "ffmpeg -i '{}' '{}'".format(fn, outfile)
        subprocess.Popen(cmd)

    def main(self):
        self.find_files()
        for f in self.oversized:
            self.resize_vid(f[0])
            print(f)

if __name__ == "__main__":
    foo = GetVidSize()
    foo.main()
    
