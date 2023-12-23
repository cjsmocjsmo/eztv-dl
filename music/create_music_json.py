#!/usr/bin/env python3


import os
import json
import glob
import time
import hashlib

from PIL import Image
from mutagen import File
from mutagen.mp3 import MP3

from pprint import pprint
import musictags as MT

class Artist:
    def __init__(self):
        self.apath = "/media/charliepi/FOO/music"
        self.basedir = "/media/charliepi/FOO/music"


        # self.apath = "/home/pipi/Music"
        # self.basedir = "/home/pipi/Music"

        # self.apath = "/media/teresa/00C3-A200/A"
        # self.basedir = "/media/teresa/00C3-A200"
        
    def artist_check(self, alist):
        count = 0
        for meta in alist:
            if meta['Ext'] == ".mp3":
                da = meta['Dir_artist'].replace("_", " ")
                fa = meta['File_artist'].replace("_", " ")
                ta = meta['Tags_artist']
                if da == fa and fa == ta:
                    pass
                else:
                    count += 1
                    print(da, fa, ta)
                    print(meta['Full_Filename'])
        print(count)

    def album_check(self, alist):
        count = 0
        for meta in alist:
            if meta['Ext'] == ".mp3":
                da = meta['Dir_album'].replace("_", " ")
                fa = meta['File_album'].replace("_", " ")
                ta = meta['Tags_album']
                if da == fa and fa == ta:
                    pass
                else:
                    count += 1
                    print(da, fa, ta)
                    print(meta['Full_Filename'])
        print(count)

    def song_check(self, alist):
        count = 0
        for meta in alist:
            if meta['Ext'] == ".mp3":
                ds = meta['File_song'].replace("_", " ")
                fs = meta['Tags_song'].replace("_", " ")
                
                if ds == fs:
                    pass
                else:
                    count += 1
                    print(ds, fs)
                    print(meta['Full_Filename'])
        print(count)

    # def glob_for_pics(self, dir_list):
    #     missing_pic_list = []
    #     for dir in dir_list:
    #         globpath = dir + "/*.jpg"
    #         globpath2 = dir + "/*.png"
    #         result = glob.glob(globpath)
    #         result2 = glob.glob(globpath2)
    #         if len(result) == 0 and len(result2) == 0:
    #             missing_pic_list.append(dir)
    #     return (list(set(missing_pic_list)), len(missing_pic_list))


class MusicFiles:
    def __init__(self):

        self.apath = "/media/charliepi/FOO/music"
        self.BaseDir = "/media/charliepi/FOO/music"
        self.metaDir = "/media/charliepi/FOO/metadata/"


        # self.apath = "/home/teresa/Music/"
        # self.BaseDir = "/home/teresa/Music"

        # self.apath = "/home/pipi/Music"
        # self.BaseDir = "/home/pipi/Music"
        # self.metaDir = "/home/pipi/metadata/"

        self.Dirlist = []

    def clean_metaDir(self):
        for (paths, Dirs, files) in os.walk(self.metaDir, followlinks=True):
            for Filename in files:
                fnn = os.path.join(paths, Filename)
                _, ext = os.path.splitext(fnn)
                if ext == ".json":
                    os.remove(fnn)

    def glob_for_pics(self):
        missing_pic_list = []
        dlist = list(set(self.Dirlist))
        for Dir in dlist:
            globpath = Dir + "/*.jpg"
            globpath2 = Dir + "/*.png"
            globpath3 = Dir + "/*.mp3"
            result = glob.glob(globpath)
            result2 = glob.glob(globpath2)
            result3 = glob.glob(globpath3)
            if len(result) < 1:
                print(globpath)
    #         else:
                # print(len(result3))
                # oldfile = result3[0]
        #         newfile = Dir + "/Folder.jpg"
        #         if len(result) == 0 and len(result2) == 0:
        #             print(oldfile)
        #             print(newfile)
        #             try:
        #                 audio = File(oldfile)
        #                 artwork = audio.tags[u'APIC:'].data
        #                 with open(newfile, 'wb') as img:
        #                     img.write(artwork)
        #             except (KeyError, TypeError, AttributeError):
        #                 missing_pic_list.append(Dir)
        # return (list(set(missing_pic_list)), len(missing_pic_list))

    def check_for_jpg(self, afile):
        Dir, _ = os.path.split(afile)
        jpgpath = "".join((Dir, "/Folder.jpg"))
        if os.path.exists(jpgpath):
            return True
        else:
            return False

    def img_size(self, afile):
        with Image.open(afile) as img_s:
            width, height = img_s.size
            return (width, height)

    def calc_md5(self, afile):
        md5 = hashlib.md5(afile.encode('utf-8')).hexdigest()
        print(md5)
        return md5
        
    def play_length(self, afile):
        audio = MP3(afile)
        audio_info = audio.info
        length_in_secs = int(audio_info.length)
        length_in_mills = length_in_secs * 1000
        return length_in_mills


    def metadata_from_file(self, afile):
        # print(afile)
        meta = {}
        meta['BaseDir'] = self.BaseDir
        meta['Full_Filename'] = afile

        meta['File_Size'] = os.path.getsize(afile)

        thefile, ext = os.path.splitext(afile)
        meta["Ext"] = ext

        fullDir, Filename = os.path.split(thefile)
        _, Dir = fullDir.split(self.BaseDir)
        meta['Dir'] = Dir
        meta["Filename"] = Filename

        dsplitlist = Dir.split("/")[1:]
        
        meta['Dir_Split_List'] = dsplitlist
        
        meta['Dir_catagory'] = dsplitlist[0]
        meta['Dir_artist'] = dsplitlist[1]
        meta['Dir_album'] = dsplitlist[2]
        

        
        meta['Dir_delem'] = "/"
        if ext != ".mp3":
            meta['File_delem'] = "None"
            width, height = self.img_size(afile)
            meta['Jpg_width'] = width
            meta['Jpg_height'] = height
            meta['File_id'] = self.calc_md5(afile)
            return meta
        else:
            meta['File_delem'] = "_-_"
            File_split_list = Filename.split("_-_")
            meta['File_split_list'] = File_split_list
            meta['Track'] = File_split_list[0]
            meta['File_artist'] = File_split_list[1]
            meta['File_album'] = File_split_list[2]
            meta['File_song'] = File_split_list[3]
            meta['File_id'] = self.calc_md5(afile)
            tags = MT.MP3Tags(afile)
            meta['Tags_artist'] = tags.Artist
            meta['Tags_album'] = tags.Album
            meta['Tags_song'] = tags.Song
            meta['Artist_first'] = tags.Artist[:1]
            meta['Album_first'] = tags.Album[:1]
            meta['Song_first'] = tags.Song[:1]
            boo = self.check_for_jpg(afile)
            meta['Jpg_exists'] = boo
            meta['Play_length'] = self.play_length(afile)
        
        # pprint(meta)
        return meta

    def write_to_file(self, meta, acount):
        if meta['Ext'] == ".mp3":
            newfile = self.metaDir + meta["Filename"] + ".json"
            with open(newfile, "w") as nf:
                data = json.dumps(meta, indent = 4)
                nf.write(data)
            print("\n")
            print(newfile)
            print("\n")
        else:
            newfile = self.metaDir + meta["Filename"] + ".json"
            with open(newfile, "w") as nf:
                data = json.dumps(meta, indent = 4)
                nf.write(data)
            print("\n")
            print(newfile)
            print("\n")

    def find(self):
        all_files_list = []
        count = 0
        for (paths, Dirs, files) in os.walk(self.apath, followlinks=True):
            for Filename in files:
                fnn = os.path.join(paths, Filename)
                Dir, _ = os.path.split(fnn)
                _, ext = os.path.splitext(fnn)
                if ext == ".sh":
                    pass
                else:
                    self.Dirlist.append(Dir)

                    meta = self.metadata_from_file(fnn)
                    count += 1
                    self.write_to_file(meta, count)

                    all_files_list.append(meta)
                    # pprint(meta)
        return all_files_list

if __name__ == "__main__":
    starttime = time.time()
    MF = MusicFiles()
    MF.clean_metaDir()
    ART = Artist()
    
    musicfiles = MF.find()
    print("\n\n STARTING ARTIST \n\n")
    ART.artist_check(musicfiles)
    
    print("\n\n STARTING ALBUM \n\n")
    ART.album_check(musicfiles)
    
    print("\n\n STARTING SONG \n\n")
    ART.song_check(musicfiles)

    # print("\n\n STARTING GLOB FOR PIC \n\n")

    # miss_pic_list = MF.glob_for_pics()
    


    
