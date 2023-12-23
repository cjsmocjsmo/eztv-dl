#!/usr/bin/env python3

from cmath import exp
import os
import re
import glob
from pprint import pprint
import shutil
from types import NoneType

class WalkDir:
    def __init__(self):
        self.folder = "/home/teresa/Downloads/movs"
        self.savedir = "/home/teresa/Downloads/processed"
        self.globlist = []
        self.dirlist = []
        self.to_rm_list = [
            "www.YTS.MX.jpg",
            "www.YTS.LT.jpg",
            "WWW.YIFY-TORRENTS.COM.jpg",
            "WWW.YTS.AG.jpg",
            "WWW.YTS.RE.jpg",
            "www.YTS.AM.jpg",
            "WWW.YTS.TO.jpg",
        ]

    def remove_crap(self):
        for (paths, dirs, files) in os.walk(self.folder, followlinks=True):
            for filename in files:
                fnn = os.path.join(paths, filename)
                _, ext = os.path.splitext(fnn)
                _, fname = os.path.split(fnn)
                if fname in self.to_rm_list:
                    print("removing {}".format(fnn))
                    try:
                        os.remove(fnn)
                    except FileNotFoundError:
                        pass
                elif ext == ".txt":
                    print("removing {}".format(fnn))
                    try:
                        os.remove(fnn)
                    except FileNotFoundError:
                        pass
                elif ext == ".srt":
                    print("removing {}".format(fnn))
                    try:
                        os.remove(fnn)
                    except FileNotFoundError:
                        pass
                else:
                    print("Nothing to remove")

    def get_dir_list(self):
        for (paths, dirs, files) in os.walk(self.folder, followlinks=True):
            for filename in files:
                fnn = os.path.join(paths, filename)
                dir, _ = os.path.split(fnn)
                self.dirlist.append(dir)

    def rm_empty_dirs(self):
        for (paths, dirs, files) in os.walk(self.folder, followlinks=True):
            try:
                os.removedirs(paths)
            except OSError:
                pass

    def Capitalize(self, string):
        character = string[0]
        if 97 <= ord(character) <= 122:
            shift = ord(character) - 32
            uppercase = chr(shift)
            return uppercase + string[1:]
        return string

    def glob_for_jpg(self, adir):
        jpgglobpath = "/".join((adir, "*.jpg"))
        jpg = glob.glob(jpgglobpath)
        if len(jpg) < 1:
            print(jpgglobpath)
            os._exit(1)
        try:
            jpg_olddir, jpg_oldfilename = os.path.split(jpg[0])
            return (jpg_olddir, jpg_oldfilename, jpg[0])
        except IndexError:
            print(adir)

    def glob_for_mp4(self, adir):
        mp4globpath = adir + "/*.mp4"
        mp4 = glob.glob(mp4globpath)
        mp4_olddir, mp4_oldfilename = os.path.split(mp4[0])
        return (mp4_olddir, mp4_oldfilename, mp4[0])


    def remove_crap_from_dirname(self):
        new_dir_list = list(set(self.dirlist))
        foo = re.compile(r"\[")
        for dir in new_dir_list:
            baz = re.search(foo, dir)
            if baz != None:
                bs = baz.start() -1
                print(dir[:bs])
                os.renames(dir, dir[:bs])

    def glob_dir_list(self):
        new_dir_list = list(set(self.dirlist))
        for dir in new_dir_list:
            _, jpg_oldfilename, jpg = self.glob_for_jpg(dir)
            mp4_olddir, mp4_oldfilename, mp4 = self.glob_for_mp4(dir)
            meta = {
                "mp4_fullpath": mp4,
                "jpg_fullpath": jpg,
                "savedir": self.savedir,
                "jpg_oldfilename": jpg_oldfilename,
                "mp4_oldfilename": mp4_oldfilename,
            }
            self.globlist.append(meta)
            print(self.globlist)

    # def rename_jpg(self, amp4, oldjpg):
        # mp4dir, _ = os.path.splitext(amp4)
        # newjpgname = ".".join((mp4dir, "jpg"))
        # try:
            # os.renames(oldjpg, newjpgname)
        # except FileNotFoundError:
            # print("\n\n filenotfounderror \n {} \n {} \n\n".format(
                # oldjpg, newjpgname))
            # pass
        # return newjpgname

    def split_at_1080p(self):
        s1 = re.compile(r".IMAX.1080p")
        s2 = re.compile(r".1080p")
        s3 = re.compile(r".720p")
        for meta in self.globlist:
            search1 = re.search(s1, meta["mp4_oldfilename"])
            search2 = re.search(s2, meta["mp4_oldfilename"])
            search3 = re.search(s3, meta["mp4_oldfilename"])
            splitindex_end = ""
            if search1:
                splitindex_end = search1.start()
            elif search2:
                splitindex_end = search2.start()
            elif search3:
                splitindex_end = search3.start()
            fn = meta["mp4_oldfilename"][:splitindex_end]
            foofn = fn.replace("..", " ").replace("-", " ").replace(".", " ")
            foo = " ".join((foofn[:-5], "("))
            front =  "/".join((meta["savedir"], foo))

            newmp4path = front + foofn[-4:] + ").mp4"
            newjpgpath = front + foofn[-4:] + ").jpg"
            print(newmp4path)
            print(newjpgpath)
            os.renames(meta["mp4_fullpath"], newmp4path)
            os.renames(meta["jpg_fullpath"], newjpgpath)



# class MoveFiles:
#     def __init__(self):
#         self.folder = "/home/teresa/Downloads/movs"
#         self.newfolder = "/home/teresa/Downloads/processed"
#         self.filelist = []

#     def find_files(self):
#         for (paths, dirs, files) in os.walk(self.folder, followlinks=True):
#             for filename in files:
#                 fnn = os.path.join(paths, filename)
#                 self.filelist.append(fnn)
#         return self.filelist

#     def move_files(self):
#         for fnn in self.filelist:
#             _, filename = os.path.split(fnn)
#             newaddr = os.path.join(self.newfolder, filename)
#             print("this is mov move \n {} \n {} \n\n".format(fnn, newaddr))
#             try:
#                 shutil.move(fnn, newaddr)
#             except OSError:
#                 print(fnn)

if __name__ == "__main__":
    WD = WalkDir()
    WD.remove_crap() #self.dirlist
    WD.rm_empty_dirs()
    WD.get_dir_list()


    WD.remove_crap_from_dirname()

    WD.get_dir_list()

    WD.glob_dir_list()
    WD.split_at_1080p()




