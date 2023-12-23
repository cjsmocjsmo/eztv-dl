#!/usr/bin/env python3

import os
import re
from PIL import Image
import glob
import time
import music.musiclib as ML
from pprint import pprint
import music.musictags as MT


class Music:
    def __init__(self):
        # self.apath = "/home/teresa/Music"
        self.apath = "/media/charliepi/944D-6BF1/B"
        self.folder_fix_list = []
        self.front_cover_fix_list = []
        self.png_list = []
        self.special_chars_fix_list = []
        self.all_files_list = []
        self.metadata_list = []
        self.tuplist = []
        self.lessthanthree_list = []

        self.s1 = re.compile("_\(")
        self.s2 = re.compile("\)")
        self.result_AC_DC = []
        self.result_38_Special = []
        self.result_30_Seconds_To_Mars = []
        self.search1 = re.compile("Ac_Dc")
        self.search2 = re.compile("38_Special")
        self.search3 = re.compile("30_Seconds_To_Mars")

    def find_files(self):
        for (paths, dirs, files) in os.walk(self.apath, followlinks=True):
            for filename in files:
                fnn = os.path.join(paths, filename)
                dir, fn = os.path.split(fnn)
                if fn == "folder.jpg":
                    self.folder_fix_list.append(fnn)
                _, fn2 = os.path.splitext(fnn)
                if fn2 == ".jpg":
                    self.front_cover_fix_list.append(fnn)
                elif fn2 == ".png":
                    self.png_list.append(fnn)
                para_result = re.search(self.s1, fnn)
                if para_result:
                    specialchars = (fnn, para_result.start())
                    self.special_chars_fix_list.append(specialchars)

    def fix_folderjpg_filename(self):
        if len(self.folder_fix_list) < 1:
            pass
        else:
            for afolder in self.folder_fix_list:
                dir, afile = os.path.split(afolder)
                newfilename = dir + "/Folder.jpg"
                os.rename(afolder, newfilename)

    def remove_paras(self):
        if len(self.special_chars_fix_list) < 1:
            pass
        else:
            for atup in self.special_chars_fix_list:
                sp1 = atup[0][:atup[1]]
                newname = sp1 + ".mp3"
                os.rename(atup[0], newname)

    def find_changed_files(self):
        self.all_files_list = []
        for (paths, dirs, files) in os.walk(self.apath, followlinks=True):
            for filename in files:
                fnn = os.path.join(paths, filename)
                self.all_files_list.append(fnn)
                

    def check_folder_for_folderjpg(self):
        self.find_changed_files()
        dir_list = ML.get_dir_list(self.all_files_list)
        missing_pic_list = ML.glob_for_pics(dir_list)
        
        pprint(missing_pic_list)

    def get_file_metadata_from_list(self):
        for afile in self.all_files_list:
            basedir = afile[:18]
            thefile, ext = os.path.splitext(afile[19:])
            dir, filename = os.path.split(thefile)
            dir_split_list = dir.split("/")
            file_delimiter = "_-_"
            dir_delimiter = "/"
            file_split_list = filename.split(file_delimiter)
            count = len(file_split_list)

            if count > 1:
                if ext == ".mp3":
                    tags = MT.MP3Tags(afile)
                    meta = {
                        "full_filename": afile,
                        "basedir": basedir,
                        "dir": dir,
                        "dir_split_list": tuple(dir_split_list),
                        "filename": filename,
                        "filename_split_list": tuple(file_split_list),
                        "ext": ext,
                        "file_delem": file_delimiter,
                        "dir_delem": dir_delimiter,
                        "count": count,
                        "tags_artist": tags.Artist,
                        "tags_album": tags.Album,
                        "tags_song": tags.Song,
                    }
                    self.metadata_list.append(meta)
                    pprint(meta)
                else:
                    meta = {
                        "full_filename": afile,
                        "basedir": basedir,
                        "dir": dir,
                        "dir_split_list": tuple(dir_split_list),
                        "filename": filename,
                        "filename_split_list": tuple(file_split_list),
                        "ext": ext,
                        "file_delem": file_delimiter,
                        "dir_delem": dir_delimiter,
                        "count": count,
                        "tags_artist": None,
                        "tags_album": None,
                        "tags_song": None,
                    }
                    self.metadata_list.append(meta)
                    pprint(meta)
            else:
                pass
            # pprint(meta)
        return self.metadata_list

    def get_file_metadata_from_file(self, afile):
        basedir = afile[:18]
        thefile, ext = os.path.splitext(afile[19:])
        dir, filename = os.path.split(thefile)
        dir_split_list = dir.split("/")
        file_delimiter = "_-_"
        dir_delimiter = "/"
        file_split_list = filename.split(file_delimiter)
        count = len(file_split_list)
        if count > 1:
            if ext == ".mp3":
                meta = {
                    "full_filename": afile,
                    "basedir": basedir,
                    "dir": dir,
                    "dir_split_list": tuple(dir_split_list),
                    "filename": filename,
                    "filename_split_list": tuple(file_split_list),
                    "ext": ext,
                    "file_delem": file_delimiter,
                    "dir_delem": dir_delimiter,
                    "count": count,
                }
                return meta
            else:
                meta = {
                    "full_filename": afile,
                    "basedir": basedir,
                    "dir": dir,
                    "dir_split_list": tuple(dir_split_list),
                    "filename": filename,
                    "filename_split_list": tuple(file_split_list),
                    "ext": ext,
                    "file_delem": file_delimiter,
                    "dir_delem": dir_delimiter,
                    "count": count,
                    "tags_artist": None,
                    "tags_album": None,
                    "tags_song": None,
                }
                return meta

    def remove_extra_track_count(self):
        s1 = re.compile("[0-9]_[0-9][0-9]_-_[0-9][0-9]")
        for meta in self.metadata_list:
            if re.search(s1, meta["full_filename"]) != None:
                newfilename = meta["filename"][:2] + meta["filename"][7:]
                newfilename = newfilename.replace("'", "")
                newnewfilename = meta["basedir"] + "/" + \
                    meta['dir'] + "/" + newfilename + meta["ext"]
                # print(newnewfilename)
                # print(meta["full_filename"])
                os.rename(meta["full_filename"], newnewfilename)

    def check_filename_format(self):
        # s2 = re.compile("_[0-9][0-9][0-9][0-9]_-_[0-9][0-9][0-9][0-9]_-_")
        s2 = re.compile("_1983_-_1990_-_")
        s3 = re.compile("_-_Disc_1_-_")
        s4 = re.compile("_-_Disc_2_-_")
        s5 = re.compile("_-_Live_Album_-_")
        s6 = re.compile("_-_Studio_Album_-_")
        s7 = re.compile("_-_30th_Anniversary_Remaster_-_")
        for meta in self.metadata_list:
            if meta["count"] == 5:
                if re.search(s2, meta['full_filename']) != None:
                    zooname = meta['full_filename'].replace(
                        "_1983_-_1990_-_", "_1983_to_1990_-_")
                    try:
                        os.rename(meta['full_filename'], zooname)
                    except FileNotFoundError:
                        print(zooname)
                        # print(meta['full_filename'])
                elif re.search(s3, meta['full_filename']) != None:
                    bar = meta['full_filename'].replace("_-_Disc_1_-_", "_-_")
                    os.rename(meta['full_filename'], bar)
                elif re.search(s4, meta['full_filename']) != None:
                    baz = meta['full_filename'].replace("_-_Disc_2_-_", "_-_")
                    os.rename(meta['full_filename'], baz)
                elif re.search(s5, meta['full_filename']) != None:
                    boo = meta['full_filename'].replace(
                        "_-_Live_Album_-_", "_-_")
                    try:
                        os.rename(meta['full_filename'], boo)
                    except FileNotFoundError:
                        print(boo)
                        # print(meta['full_filename'])
                elif re.search(s6, meta['full_filename']) != None:
                    but = meta['full_filename'].replace(
                        "_-_Studio_Album_-_", "_-_")
                    os.rename(meta['full_filename'], but)
                elif re.search(s7, meta['full_filename']) != None:
                    bob = meta['full_filename'].replace(
                        "_-_30th_Anniversary_Remaster_-_", "_-_")
                    os.rename(meta['full_filename'], bob)
                else:
                    pass
                    # print(meta['full_filename'])
            if meta["count"] == 3:
                self.lessthanthree_list.append(meta)

    def process_lessthanthree_list(self):
        dlist = []
        for ameta in self.lessthanthree_list:
            foo = ameta['basedir'] + "/" + ameta['dir']
            dlist.append(foo)
        dlist = list(set(dlist))
        for d in dlist:
            globpath = d + "/*.mp3"
            mp3_glob = glob.glob(globpath)
            idx = 1
            for old_mp3 in mp3_glob:
                idx += 1
                idx2 = ""
                if idx < 10:
                    idx4 = str(idx)
                    idx2 = "0" + idx4
                else:
                    idx2 = str(idx)
                dir, filename = os.path.split(old_mp3)
                start = filename[:2]
                end = filename[2:]
                newfilename = dir + "/" + start + idx2 + "_-_" + end
                # print(old_mp3)
                # print(newfilename)
                os.rename(old_mp3, newfilename)

    def fix_glen_campbell(self):
        c1 = re.compile("Glen_Cambell")
        second_pass_list = []
        third_pass_list = []
        for meta in self.metadata_list:
            if re.search(c1, meta['full_filename']) != None:
                newdir = meta['dir'].replace("Glen_Cambell", "Glen_Campbell")
                newfilename = meta["filename"].replace(
                    "Glen_Cambell", "Glen_Campbell")
                newfullpath = meta['basedir'] + meta["dir_delem"] + \
                    newdir + meta["dir_delem"] + newfilename
                second_pass_list.append(newfullpath)
        for second in second_pass_list:
            second_pass = second.replace("Glen_Cambell", "Glen_Campbell")
            third_pass_list.append(second_pass)
        for third in third_pass_list:
            final = third.replace("Glen_Cambell", "Glen_Campbell")
            try:
                os.rename(meta['full_filename'], final)
            except FileNotFoundError:
                print(final)

    def remove_CD_stuff(self):
        cd = re.compile("CD[0-9]")
        cd2 = re.compile("Cd1")
        cd3 = re.compile("cd1")

        for meta in self.metadata_list:
            # if re.search(cd, meta["full_filename"]) != None:
            #     newdir = meta["dir"].replace("CD", "")
            #     newfilename = meta["filename"][1:]
            #     newpath = meta["basedir"] + meta["dir_delem"] + newdir + newfilename + meta["ext"]
            #     # os.rename(meta["full_filename"], newpath)
            #     print(newpath)
            if re.search(cd2, meta["full_filename"]) != None:
                # newdir = meta["dir"].replace("_Cd1", "")
                # newpath = meta["basedir"] + meta["dir_delem"] + newdir + meta["dir_delem"] + meta["filename"] + meta["ext"]
                # os.rename(meta["full_filename"], newpath)
                print(meta["full_filename"])
            

    def check_dir_artist_with_file_artist_name(self):
        sue_list = []
        for meta in self.metadata_list:
            if meta["dir_split_list"][0] == "country" or meta["dir_split_list"][0] == "pop":
                if meta["dir_split_list"][2] != meta["filename_split_list"][1]:
                    # sue = (meta["dir_split_list"][2], meta["filename_split_list"][1], meta)
                    sue = (meta["dir_split_list"][2],
                           meta["filename_split_list"][1], meta["full_filename"])

                    sue_list.append(sue)
            elif meta["dir_split_list"][1] != meta["dir_split_list"][1]:
                # sue2 = (meta["dir_split_list"][1], meta["dir_split_list"][1], meta)
                sue2 = (meta["dir_split_list"][1],
                        meta["dir_split_list"][1], meta["full_filename"])

                sue_list.append(sue2)
                # print(meta["dir_split_list"])
                # print(meta["filename_split_list"])
        sl = list(set(sue_list))
        print("printing sue list")
        pprint(sue_list)
        
    def check_for_uppercase(self):
        flist = []
        # plist = []
        # metalist = []
        for meta in self.metadata_list:
            # if meta['dir_split_list'][0] == "country":
            #     try:
            #         boo = (meta['dir_split_list'][3], meta["full_filename"])
            #         flist.append(boo)
            #     except IndexError:
            #         print(meta['dir_split_list'])

            # elif meta['dir_split_list'][0] == "pop":
            #     try:
            #         baz = (meta['dir_split_list'][3], meta["full_filename"])
            #         flist.append(baz)
            #     except IndexError:
            #         print(meta['dir_split_list'])
            # else:
            try:
                bee = (meta['dir_split_list'][2], meta["full_filename"])
                flist.append(bee)
            except IndexError:
                print(meta['dir_split_list'])

        upper_case_list = []
        for f in flist:
            if f[0].isupper():
                if f[0] == "XXX":
                    pass
                elif f[0] == "E=MC2":
                    pass
                elif f[0] == "T_R_O_U_B_L_E":
                    pass
                elif f[0] == "LMFAO":
                    pass
                else:
                    upper_case_list.append(f)
        # pprint(list(set(upper_case_list)))

        # mlist = []
        for upper in upper_case_list:
            meta = self.get_file_metadata_from_file(upper[1])
            zoo = meta["dir_split_list"][2]
            zookeeper = zoo.split(".")
            ace = ""
            for z in zookeeper:
                foo = z.capitalize()
                ace = ace + foo + "_"
            newzookeeper = meta["dir_split_list"][0] + meta["dir_delem"] + \
                meta["dir_split_list"][1] + meta['dir_delem'] + ace[:-1]
            newdir = meta['basedir'] + meta["dir_delem"] + newzookeeper
            old_dir, _ = os.path.split(meta['full_filename'])

            print(old_dir)
            print(newdir)
            try:
                os.rename(old_dir, newdir)
            except FileNotFoundError:
                pass
    
    def check_dir_filename_tag_match(self):
        c1 = 0
        c2 = 0
        c3 = 0
        for meta in self.metadata_list:
            dir_artist, dir_album = ML.get_dir_artist_album(meta)
            dir_artist = dir_artist.replace("_", " ")
            dir_album = dir_album.replace("_", " ")

            file_artist, file_album, file_song = ML.get_dir_artist_album_song(meta)
            file_artist = file_artist.replace("_", " ")
            file_album = file_album.replace("_", " ")
            file_song = file_song.replace("_", " ")
            tag = MT.MP3Tags(meta["full_filename"])
            tag_artist = tag.Artist
            tag_album = tag.Album
            tag_song = tag.Song
            
            if dir_artist != file_artist and file_artist != tag_artist:
                c1 += 1
                print("artist {}  |  {}  |  {}".format(dir_artist, file_artist, tag_artist))
            #     # print(meta["full_filename"])
            if dir_album != file_album and file_album != tag_album:
                c2 += 1
                print("album {}  |  {}  |  {}".format(dir_album, file_album, tag_album))
                # print(dir_album, file_album)
                # print(meta["full_filename"])
            if file_song != tag_song:
                c3 += 1
                print("songs {}  |  {}".format(file_song, tag_song))
            
        print(c1)
        print(c2)
        print(c3)
            

    def find_ACDC_38special_30seconds(self):
        for meta in self.metadata_list:
            if re.search(self.search1, meta["filename"]) != None:
                self.result_AC_DC.append(meta)
            elif re.search(self.search2, meta["filename"]) != None:
                self.result_38_Special.append(meta)
            elif re.search(self.search3, meta["filename"]) != None:
                self.result_30_Seconds_To_Mars.append(meta)

    def fix_AC_DC(self):
        for meta in self.result_AC_DC:
            if re.search(self.search1, meta["filename"]) != None:
                foo = meta['filename'].replace("Ac_Dc_-_Ac_Dc_Live", "AC_DC_-_AC_DC_Live")
                bar = foo.replace("Ac_Dc", "AC_DC")
                newpath = meta['basedir'] + meta["dir_delem"] + meta['dir'] + meta["dir_delem"] + bar + meta['ext']
                os.rename(meta["full_filename"], newpath)
    
    def fix_38special(self):
        dir_list = []
        for meta in self.result_38_Special:
            dir_list.append(meta['basedir'] + meta["dir_delem"] + meta['dir'])
        pdir_list = list(set(dir_list))

        for pdir in pdir_list:
            globpath = pdir + "/*.mp3"
            mp3glob = glob.glob(globpath)
            count = 0
            for mp3 in mp3glob:
                count += 1
                meta = self.get_file_metadata_from_file(mp3)
                striped_filename = meta['filename'][2:]
                if count < 10:
                    newfilename = "1_0" + str(count) + meta["file_delem"] + striped_filename
                else:
                    newfilename = "1_" + str(count) + meta["file_delem"] + striped_filename

                new_filename = meta['basedir'] + meta["dir_delem"] + meta['dir'] + meta["dir_delem"] + newfilename
                os.rename(meta["full_filename"], new_filename)

    def fix_30seconds(self):
        dir_list = []
        for meta in self.result_30_Seconds_To_Mars:
            dir_list.append(meta['basedir'] + meta["dir_delem"] + meta['dir'])
            print(meta["full_filename"])
        pdir_list = list(set(dir_list))
        pprint(pdir_list)

        for pdir in pdir_list:
            globpath = pdir + "/*.mp3"
            mp3glob = glob.glob(globpath)
            count = 0
            for mp3 in mp3glob:
                count += 1
                meta = self.get_file_metadata_from_file(mp3)
                striped_filename = meta['filename'][2:]
                if count < 10:
                    newfilename = "1_0" + str(count) + meta["file_delem"] + striped_filename
                else:
                    newfilename = "1_" + str(count) + meta["file_delem"] + striped_filename

                new_filename = meta['basedir'] + meta["dir_delem"] + meta['dir'] + meta["dir_delem"] + newfilename
                print(new_filename)
                os.rename(meta["full_filename"], new_filename)
    
    def fix_stuff(self):
        s1 = re.compile("The_Goo_Goo_Dolls")
        s2 = re.compile("Glen_Cambell_-_Glen_Cambell")
        s3 = re.compile("The_Nitty_Gritty_Dirt_Band")
        s4 = re.compile("Metallica")
        s5 = re.compile("The_Doobie_Brothers")
        s6 = re.compile("The_Scorpions")
        s7 = re.compile("The_Black_Crows")
        s8 = re.compile("Dance_Floor_Chemist")

        for meta in self.metadata_list:
            if re.search(s1, meta["full_filename"]) != None:
                newfilename = meta["full_filename"].replace("The_Goo_Goo_Dolls","Goo_Goo_Dolls")
                os.rename(meta["full_filename"], newfilename)
            if re.search(s2, meta["full_filename"]) != None:
                newfilename = meta["full_filename"].replace("Glen_Cambell_-_Glen_Cambell","Glen_Campbell_-_Glen_Campbell")
                os.rename(meta["full_filename"], newfilename)
            if re.search(s3, meta["full_filename"]) != None:
                newfilename = meta["full_filename"].replace("The_Nitty_Gritty_Dirt_Band","Nitty_Gritty_Dirt_Band")
                os.rename(meta["full_filename"], newfilename)


            if re.search(s4, meta["full_filename"]) != None:
                newfilename = meta["full_filename"].replace("Metallica","Mettallica")
                os.rename(meta["full_filename"], newfilename)
            if re.search(s5, meta["full_filename"]) != None:
                newfilename = meta["full_filename"].replace("_-_The_Doobie_Brothers_-_","_-_Doobie_Brothers_-_")
                os.rename(meta["full_filename"], newfilename)


            if re.search(s6, meta["full_filename"]) != None:
                newfilename = meta["full_filename"].replace("The_Scorpions","Scorpions")
                os.rename(meta["full_filename"], newfilename)
            if re.search(s7, meta["full_filename"]) != None:
                newfilename = meta["full_filename"].replace("The_Black_Crows","Black_Crows")
                os.rename(meta["full_filename"], newfilename)
            if re.search(s8, meta["full_filename"]) != None:
                newfilename = meta['filename_split_list'][0] + "_-_Dance_Floor_Chemist_-_" + meta['filename_split_list'][2] + meta["file_delem"] + meta['filename_split_list'][3] + meta["ext"]
                nfn = meta['basedir'] + meta['dir_delem'] + meta['dir'] + meta['dir_delem'] + newfilename
                os.rename(meta["full_filename"], nfn)

    def zztop_fix(self):
        for meta in self.metadata_list:
            newfilename = meta["full_filename"].replace("'", "")
            print(newfilename)
            os.rename(meta['full_filename'], newfilename)

    def fix_tearforfears(self):
        search = re.compile("The_Seeds_of_Love")
        for meta in self.metadata_list:
            if re.search(search, meta["full_filename"]) != None:
                newfilename = meta["full_filename"].replace("The_Seeds_of_Love", "The_Seeds_Of_Love")
                os.rename(meta["full_filename"], newfilename)

    def fix_beatles_one(self):
        search = re.compile("The_Beatles_1967_to_1970")
        for meta in self.metadata_list:
            if re.search(search, meta["full_filename"]) != None:
                newfilename = meta["full_filename"].replace("The_Beatles_1967_to_1970", "The_Beatles_1967_To_1970")
                os.rename(meta["full_filename"], newfilename)

    def fix_beatles_two(self):
        search = re.compile("With_the_Beatles")
        for meta in self.metadata_list:
            if re.search(search, meta["full_filename"]) != None:
                newfilename = meta["full_filename"].replace("With_the_Beatles", "With_The_Beatles")
                os.rename(meta["full_filename"], newfilename)

    def fix_beatles_three(self):
        search = re.compile("Anthology,_Vol._2")
        for meta in self.metadata_list:
            if re.search(search, meta["full_filename"]) != None:
                newfilename = meta["full_filename"].replace("Anthology,_Vol._2", "Anthology_Vol_2")
                os.rename(meta["full_filename"], newfilename)

    def fix_beatles_four(self):
        search = re.compile("The_Beatles_1962_to_1965")
        for meta in self.metadata_list:
            if re.search(search, meta["full_filename"]) != None:
                newfilename = meta["full_filename"].replace("The_Beatles_1962_to_1965", "The_Beatles_1962_To_1965")
                os.rename(meta["full_filename"], newfilename)

    def fix_beatles_five(self):
        search = re.compile("Anthology,_Vol._3")
        for meta in self.metadata_list:
            if re.search(search, meta["full_filename"]) != None:
                newfilename = meta["full_filename"].replace("Anthology,_Vol._3", "Anthology_Vol_3")
                os.rename(meta["full_filename"], newfilename)

    def fix_beatles_six(self):
        search = re.compile("Anthology,_Vol._1")
        for meta in self.metadata_list:
            if re.search(search, meta["full_filename"]) != None:
                newfilename = meta["full_filename"].replace("Anthology,_Vol._1", "Anthology_Vol_1")
                os.rename(meta["full_filename"], newfilename)

    def fix_beatles_7(self):
        search = re.compile("The_Beatles_Live_At_The_BBC")
        for meta in self.metadata_list:
            if re.search(search, meta["full_filename"]) != None:
                newfilename = meta["full_filename"].replace("The_Beatles_Live_At_The_BBC", "Live_At_The_BBC")
                os.rename(meta["full_filename"], newfilename)

    def fix_tk1(self):
        search = re.compile("Toby_Keiths_Classic_Christmas")
        for meta in self.metadata_list:
            if re.search(search, meta["full_filename"]) != None:
                newfilename = meta["full_filename"].replace("Toby_Keiths_Classic_Christmas", "Classic_Christmas")
                os.rename(meta["full_filename"], newfilename)

    def fix_thwho1(self):
        search = re.compile("Then_and_Now_1964-2004")
        for meta in self.metadata_list:
            if re.search(search, meta["full_filename"]) != None:
                newfilename = meta["full_filename"].replace("Then_and_Now_1964-2004", "Then_And_Now_1964_To_2004")
                os.rename(meta["full_filename"], newfilename)

    def fix_thwho2(self):
        search = re.compile("It's_Hard")
        for meta in self.metadata_list:
            if re.search(search, meta["full_filename"]) != None:
                newfilename = meta["full_filename"].replace("It's_Hard", "Its_Hard")
                os.rename(meta["full_filename"], newfilename)

    def fix_thwho3(self):
        search = re.compile("My_Generation-")
        for meta in self.metadata_list:
            if re.search(search, meta["full_filename"]) != None:
                newfilename = meta["full_filename"].replace("My_Generation-", "My_Generation")
                os.rename(meta["full_filename"], newfilename)

    def fix_TedN1(self):
        search = re.compile("If_You_Can't_Lick_'Em..__-_")
        for meta in self.metadata_list:
            if re.search(search, meta["full_filename"]) != None:
                newfilename = meta["full_filename"].replace("If_You_Can't_Lick_'Em..__-_", "If_You_Cant_Lick_Em_-_")
                os.rename(meta["full_filename"], newfilename)

    def fix_TDC(self):
        search = re.compile("Wave_of_Popular_Feeling")
        for meta in self.metadata_list:
            if re.search(search, meta["full_filename"]) != None:
                newfilename = meta["full_filename"].replace("Wave_of_Popular_Feeling", "Wave_Of_Popular_Feeling")
                os.rename(meta["full_filename"], newfilename)

    def fix_TT(self):
        search = re.compile("My_Honkey_Tonk_History")
        for meta in self.metadata_list:
            if re.search(search, meta["full_filename"]) != None:
                newfilename = meta["full_filename"].replace("My_Honkey_Tonk_History", "My_Honky_Tonk_History")
                os.rename(meta["full_filename"], newfilename)

    def fix_the_birds(self):
        search = re.compile("The_Notorious_Byrd_Brothers_\[Remastered\]")
        for meta in self.metadata_list:
            if re.search(search, meta["full_filename"]) != None:
                zoo = meta["full_filename"].split("_-_")
                newfilename = zoo[0] + meta["file_delem"] + zoo[1] + meta["file_delem"] + zoo[2][:-13] + meta["file_delem"] + zoo[3]
                # print(newfilename)
                os.rename(meta["full_filename"], newfilename)

    def fix_birds2(self):
        search = re.compile("Dr__Byrds_And_Mr__Hyde")
        for meta in self.metadata_list:
            if re.search(search, meta["full_filename"]) != None:
                newfilename = meta["full_filename"].replace("Dr__Byrds_And_Mr__Hyde", "Dr_Byrds_And_Mr_Hyde")
                os.rename(meta["full_filename"], newfilename)

    def fix_birds3(self):
        search = re.compile("Mr._Tambourine_Man")
        for meta in self.metadata_list:
            if re.search(search, meta["full_filename"]) != None:
                newfilename = meta["full_filename"].replace("Mr._Tambourine_Man", "Mr_Tambourine_Man")
                os.rename(meta["full_filename"], newfilename)

    def fix_srv(self):
        search = re.compile("The_Real_Deal__Greatest_Hits_Vol__2")
        for meta in self.metadata_list:
            if re.search(search, meta["full_filename"]) != None:
                newfilename = meta["full_filename"].replace("The_Real_Deal__Greatest_Hits_Vol__2", "The_Real_Deal_Greatest_Hits_Vol_2")
                os.rename(meta["full_filename"], newfilename)

    def fix_KP(self):
        search = re.compile("One_of_the_Boys")
        for meta in self.metadata_list:
            if re.search(search, meta["full_filename"]) != None:
                newfilename = meta["full_filename"].replace("One_of_the_Boys", "One_Of_The_Boys")
                os.rename(meta["full_filename"], newfilename)

    def fix_KennyC(self):
        search = re.compile("No_Shoes,_No_Shirt,_No_Problems")
        for meta in self.metadata_list:
            if re.search(search, meta["full_filename"]) != None:
                newfilename = meta["full_filename"].replace("No_Shoes,_No_Shirt,_No_Problems", "No_Shoes_No_Shirt_No_Problem")
                os.rename(meta["full_filename"], newfilename)

    def fix_BOC(self):
        search = re.compile("_yster_")
        for meta in self.metadata_list:
            if re.search(search, meta["full_filename"]) != None:
                newfilename = meta["full_filename"].replace("_yster_", "_Oyster_")
                os.rename(meta["full_filename"], newfilename)

    def fix_chicago(self):
        search = re.compile("Chicags_Greatest_Hits")
        for meta in self.metadata_list:
            if re.search(search, meta["full_filename"]) != None:
                newfilename = meta["full_filename"].replace("Chicags_Greatest_Hits", "Chicago_Greatest_Hits_1982_1989")
                os.rename(meta["full_filename"], newfilename)

    def last_fix(self):
        # search = re.compile("Get_Up!")
        for meta in self.metadata_list:
            print(meta["full_filename"])
            # zoo = meta["full_filename"].replace("\,", "").replace("\!", "").replace("__", "_")
            # boo = zoo.replace("\&", "And").replace("'", "").replace("Ii", "II").replace("Iii", "III")
            # print(boo)
            # # os.rename(meta["full_filename"], boo)
                





if __name__ == "__main__":
    starttime = time.time()
    M = Music()
    # files = M.find_files()
    # M.fix_folderjpg_filename()
    # M.remove_paras()
    # M.check_folder_for_folderjpg()
    
    # M.find_changed_files()
    # M.get_file_metadata_from_list()
    # M.remove_extra_track_count()
    
    # M.find_changed_files()
    # M.get_file_metadata_from_list()
    # M.check_filename_format()
    # M.process_lessthanthree_list()
    # M.find_changed_files()
    # M.get_file_metadata_from_list()
    # M.fix_glen_campbell()
    # M.find_changed_files()
    # M.get_file_metadata_from_list()
    # M.remove_CD_stuff()
    # M.find_changed_files()
    # M.get_file_metadata_from_list()
    # M.check_dir_artist_with_file_artist_name()
    # M.find_changed_files()
    # M.get_file_metadata_from_list()
    # M.find_ACDC_38special_30seconds()
    # M.fix_AC_DC()
    # M.fix_38special()
    # M.fix_30seconds()
    # M.check_for_uppercase()

    # M.zztop_fix()
    # M.fix_tearforfears()
    # M.fix_beatles_one()
    # M.fix_beatles_two()
    # M.fix_beatles_three()
    # M.fix_beatles_four()
    # M.fix_beatles_five()
    # M.fix_beatles_six() 
    # M.fix_beatles_7()
    # M.fix_tk1()
    # M.fix_thwho1()
    # M.fix_thwho2()
    # M.fix_thwho3()
    # M.fix_TedN1()
    # M.fix_TDC()
    # M.fix_TT()
    # M.fix_the_birds()
    # M.fix_birds2()
    # M.fix_birds2()
    # M.fix_birds3()
    # M.fix_srv()
    # M.fix_KP()
    # M.fix_KennyC()
    # M.fix_BOC()
    # M.fix_chicago()
    # M.last_fix()


    M.find_changed_files()
    M.get_file_metadata_from_list()

    M.check_dir_filename_tag_match()
    # M.fix_stuff()
    
    

    endtime = time.time()
    extime = endtime - starttime
    print(extime)
