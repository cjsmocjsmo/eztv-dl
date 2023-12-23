#!/usr/bin/env python3

import os
import re
# from typing import Final
import typing
import mutagen
from mutagen import File
from pprint import pprint
from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3

class WalkDir:
    def __init__(self):
        self.folder = "/media/pipi/FOO/music"
        # self.folder = "/media/charliepi/944D-6BF1/newMusic/"
        self.mp3list = []

    def find_mp3_files(self):
        for (paths, dirs, files) in os.walk(self.folder, followlinks=True):
            for filename in files:
                fnn = os.path.join(paths, filename)
                _, ext = os.path.splitext(fnn)
                if ext == ".mp3":
                    self.mp3list.append(fnn)
        return self.mp3list

class SplitPath:
    def __init__(self) -> None:
        pass

    def gen_path_tupal(self, astring):
        dstring, ext = os.path.splitext(astring)
        dir, filename = os.path.split(dstring)
        return astring, dir, filename, ext

    def gen_path_tupal_list(self, alist):
        path_tupal_list = []
        for a in alist:
            pt = self.gen_path_tupal(a)
            path_tupal_list.append(pt)
        return path_tupal_list

    def cd1_check_and_rename(self, apt):
        if apt[1][-3:] == "CD1":
            newname = apt[1][:-3] + apt[2] + apt[3]
            os.rename(apt[0], newname)
            try:
                os.remove(apt[0])
            except FileNotFoundError:
                pass
            print(newname)

    def cd2_check_and_rename(self, apt):
        if apt[1][-3:] == "CD2":
            newname = apt[1][:-3] + apt[2] + apt[3]
            os.rename(apt[0], newname)
            try:
                os.remove(apt[0])
            except FileNotFoundError:
                pass
            print(newname)

    def cd3_check_and_rename(self, apt):
        if apt[1][-3:] == "CD3":
            newname = apt[1][:-3] + apt[2] + apt[3]
            print(newname)
            os.rename(apt[0], newname)
            try:
                os.remove(apt[0])
            except FileNotFoundError:
                pass

    def cd4_check_and_rename(self, apt):
        if apt[1][-3:] == "CD4":
            newname = apt[1][:-3] + apt[2] + apt[3]
            print(newname)
            os.rename(apt[0], newname)
            try:
                os.remove(apt[0])
            except FileNotFoundError:
                pass

    def cd5_check_and_rename(self, apt):
        if apt[1][-3:] == "CD5":
            newname = apt[1][:-3] + apt[2] + apt[3]
            print(newname)
            os.rename(apt[0], newname)
            try:
                os.remove(apt[0])
            except FileNotFoundError:
                pass

    def cd6_check_and_rename(self, apt):
        if apt[1][-3:] == "CD6":
            newname = apt[1][:-3] + apt[2] + apt[3]
            print(newname)
            os.rename(apt[0], newname)
            try:
                os.remove(apt[0])
            except FileNotFoundError:
                pass

    def cd7_check_and_rename(self, apt):
        if apt[1][-3:] == "CD7":
            newname = apt[1][:-3] + apt[2] + apt[3]
            print(newname)
            os.rename(apt[0], newname)
            try:
                os.remove(apt[0])
            except FileNotFoundError:
                pass

    def cd8_check_and_rename(self, apt):
        if apt[1][-3:] == "CD8":
            newname = apt[1][:-3] + apt[2] + apt[3]
            print(newname)
            os.rename(apt[0], newname)
            try:
                os.remove(apt[0])
            except FileNotFoundError:
                pass

    def cd9_check_and_rename(self, apt):
        if apt[1][-3:] == "CD9":
            newname = apt[1][:-3] + apt[2] + apt[3]
            print(newname)
            os.rename(apt[0], newname)
            try:
                os.remove(apt[0])
            except FileNotFoundError:
                pass

    def track_check(self, atup):
        foo = atup[2].split("_-_")
        s1 = re.compile("[0-9]_[0-9][0-9]")
        s2 = re.compile("[0-9]-[0-9][0-9]")
        result = re.search(s1, foo[0])
        result2 = re.search(s2, foo[0])
        resultlist = []
        returnlist = []
        if result == None and result2 == None:
            foobar = "1_" + foo[0]
            resultlist.append(foobar)
            if foo[1]:
                resultlist.append(foo[1])
            try:
                if foo[2]:
                    resultlist.append(foo[2])
            except IndexError:
                pass

            try:
                if foo[3]:
                    resultlist.append(foo[3])
            except IndexError:
                pass

            try:
                if foo[4]:
                    resultlist.append(foo[4])
            except IndexError:
                pass

            result = ""
            for r in resultlist:
                result = result + "_-_" + r 

            newstringlist = []
            
            if atup[1]:
                newstringlist.append(atup[1])
            newstringlist.append(result[3:])
            
            if atup[3]:
                newstringlist.append(atup[3])
            try:
                if atup[4]:
                    newstringlist.append(atup[4])
            except IndexError:
                pass

            ns = ""
            fart = ""
            for newstring in newstringlist:
                ns = ns + "/" + newstring
                f = ns.replace("//", "/").replace("/.", ".")
                fart = f.replace("Ac_Dc", "AC_DC").replace("Tnt", "TNT").replace("Zz", "ZZ")
            try:
                os.rename(atup[0], fart)
            except FileNotFoundError:
                pass

class RemoveUnwanted:
    def remove_crap(self):
        WD = WalkDir()
        mp3_files3 = WD.find_mp3_files()
        for mp3 in mp3_files3:
            se1 = re.compile("1_1_1_1_1_")
            search1 = re.search(se1, mp3)
            if search1 != None:
                newname = mp3.replace("1_1_1_1_1_", "").replace("1_1_1_1_", "")
                print(newname)
                print(mp3)
                try:
                    os.rename(mp3, newname)
                except FileNotFoundError:
                    pass

class MP3Tags:
	Track = None
	Artist = None
	Album = None
	Song = None
	
	def __init__(self, fn):
		self.fn = fn

		try:
			self.audio = File(self.fn)
		except (KeyError, mutagen.mp3.HeaderNotFoundError, AttributeError):
			print(self.fn)
			pass

		try:
			type(self).Track = self.audio['TRCK'].text[0]
		except (KeyError, AttributeError):
			type(self).Track = '50'
	
		try:
			type(self).Artist = self.audio["TPE1"].text[0]
		except (KeyError, AttributeError): 
			type(self).Artist = 'Fuck Artist'
			print(''.join(("KeyError: No TPE1 tag... ", self.fn)))
	
		try:
			type(self).Album = self.audio["TALB"].text[0]
		except (KeyError, AttributeError): 
			type(self).Album = 'Fuck Album'
			print(''.join(("KeyError No TALB tag ... ", self.fn)))
			
		try:
			type(self).Song = self.audio['TIT2'].text[0]
		except (KeyError, AttributeError): 
			type(self).Song = 'Fuck Song'
			print(''.join(("KeyError: No TIT2 tag... ", self.fn)))

class ArtistTagFix:
    def scan_and_fix_artist(self, astr):
        # pattern = re.compile(r'^[A-Z0-9]*(?![a-z])')
        pattern = re.compile(r'^[A-Z0-9]')
        newlist = []
        for a in astr:
            # print(a)
            if re.search(pattern, a) == None:
                z = a.replace("'", "").replace("(", "").replace(")", "").replace("/", " ").replace("&", "And").replace(",", "")
                x = z.replace("!", "").replace("+ ", "").replace("?", "").replace("_", " ").replace("Zz", "ZZ").replace(":", " ")
                y = x.replace(";", "").replace("=", "")
                b = y.capitalize()
                newlist.append(b)
            else:
                z = a.replace("'", "").replace("(", "").replace(")", "").replace("/", " ").replace("&", "And").replace(",", "")
                x = z.replace("!", "").replace("+ ", "").replace("?", "").replace("_", " ").replace("Zz", "ZZ").replace(":", " ")
                y = x.replace(";", "").replace("=", "")
                newlist.append(y)
        newstr = ""
        for b in newlist:
            newstr = newstr + " " + b
        return newstr[1:]
    
class AlbumTagFix:
    def scan_and_fix_album(self, astr):
        pattern = re.compile(r'^[A-Z0-9]')
        newlist = []
        for a in astr:
            # print(a)
            if re.search(pattern, a) == None:
                z = a.replace("'", "").replace("(", "").replace(")", "").replace("/", " ").replace("&", "And").replace(",", "")
                x = z.replace("!", "").replace("+ ", "").replace("?", "").replace("_", " ").replace("Zz", "ZZ").replace(":", " ")
                y = x.replace(";", "").replace("=", "")
                b = y.capitalize()
                newlist.append(b)
            else:
                z = a.replace("'", "").replace("(", "").replace(")", "").replace("/", " ").replace("&", "And").replace(",", "")
                x = z.replace("!", "").replace("+ ", "").replace("?", "").replace("_", " ").replace("Zz", "ZZ").replace(":", " ")
                y = x.replace(";", "").replace("=", "")
                newlist.append(y)
        newstr = ""
        for b in newlist:
            newstr = newstr + " " + b
        return newstr[1:]

class SongTagFix:
    def scan_and_fix_song(self, astr):
        if "Bonus" in astr:
            astr.remove("Bonus")
        if "bonus" in astr:
            astr.remove("bonus")
        if "Track" in astr:
            astr.remove("Track")
        if "[live]" in astr:
            astr.remove("[live]")
        if "[non-lp" in astr:
            astr.remove(" [non-lp")
        if "Version]" in astr:
            astr.remove("Version]") 
        if "[Remastered]" in astr:
            astr.remove("[Remastered]")
        if "[remastered]" in astr:
            astr.remove("[remastered]")
        if "LED.ZEPPELIN.BOX.SET." in astr:
            astr.remove("LED.ZEPPELIN.BOX.SET.")
        if "[live][#]" in astr:
            astr.remove("[live][#]")
        
        pattern = re.compile(r'^[A-Z0-9]')
        newlist = []
        for a in astr:
            # print(a)
            if re.search(pattern, a) == None:
                z = a.replace("'", "").replace("(", "").replace(")", "").replace("/", " ").replace("&", "And").replace(",", "")
                x = z.replace("!", "").replace("+ ", "").replace("?", "").replace("_", " ").replace("Zz", "ZZ").replace(":", " ")
                y = x.replace(";", "").replace("=", "")
                b = y.capitalize()
                newlist.append(b)
            else:
                z = a.replace("'", "").replace("(", "").replace(")", "").replace("/", " ").replace("&", "And").replace(",", "")
                x = z.replace("!", "").replace("+ ", "").replace("?", "").replace("_", " ").replace("Zz", "ZZ").replace(":", " ")
                y = x.replace(";", "").replace("=", "")
                newlist.append(y)
        newstr = ""
        for b in newlist:
            newstr = newstr + " " + b
        foo = newstr.replace(" [featuring Sons Of Sylvia]", "")
        bar = foo[1:]
        return bar

class WriteTags:
    def write_tag(self, atup, fn):
        audio = EasyID3(fn)
        audio['title'] = atup[2]
        audio['artist'] = atup[0]
        audio['album'] = atup[1]
        audio['tracknumber'] = atup[3] # empty
        audio.save()

    def write_tag_main(self):
        WD = WalkDir()
        alist = WD.find_mp3_files()
        for mp33 in alist:
            tagmeta = MP3Tags(mp33)
            spart = tagmeta.Artist.split(" ")
            spalb = tagmeta.Album.split(" ")
            spsong = tagmeta.Song.split(" ")
            ARTIST = ArtistTagFix().scan_and_fix_artist(spart)
            ALBUM = AlbumTagFix().scan_and_fix_album(spalb)
            SONG = SongTagFix().scan_and_fix_song(spsong)
            TRACK = SplitTrack().SPTMain(tagmeta.Track)
            ace = (ARTIST, ALBUM, SONG, TRACK)
            self.write_tag(ace, mp33)
            pprint(ace)

class SplitTrack:
    def scan_length(self, astr):
        astringlist = []
        for a in astr:
            astringlist.append(a)
        length = len(astringlist)
        return length

    def trk_split(self, bstr):
        bspl = bstr.split("/")
        return bspl[0]

    def trk_fix(self, atrk):
        if len(atrk) == 1:
            newtrk = "0" + atrk
            return newtrk
        else:
            return atrk
        
    def SPTMain(self, astring):
        sp_len = self.scan_length(astring)
        if sp_len == 1:
            newstr = "0" + astring
            return newstr
        elif sp_len == 2:
            return astring
        elif sp_len > 2:
            trk = self.trk_split(astring)
            return self.trk_fix(trk)

class MatchTagFilename:
    def change_file_names(self):
        WD = WalkDir()
        mp3_files = WD.find_mp3_files()
        SP = SplitPath()
        pathTupal = SP.gen_path_tupal_list(mp3_files)
        for p in pathTupal:
            meta = MP3Tags(p[0])
            foo = p[2].split("_-_")
            if len(foo) == 3:
                newstr = meta.Album.replace(" ", "_")
                _, ext = os.path.splitext(p[0])
                
                new_addr = p[1] + "/" + foo[0] + "_-_" + foo[1] + "_-_" +  newstr + "_-_" + foo[2] + ext
                os.rename(p[0], new_addr)
                print(p[0])
                print(new_addr)

class FinalFix:
    def last_fix(self):
        WD = WalkDir()
        mp3_files = WD.find_mp3_files()


        foo = []
        s = re.compile("[A-Z0-9]")
        for mp3 in mp3_files:
            tags = MP3Tags(mp3)
            if re.search(s, tags.Song[:1]) != None:
                pass 
            else:
                z = tags.Song[1:]
                aa = z.split(" ")
                if "" in aa:
                    aa.remove("")
                dick = []
                for a in aa:
                    ac = a.capitalize()
                    dick.append(ac)
                pussy = " ".join(dick)

                audio = EasyID3(mp3)
                audio["title"] = pussy
                audio.save()
                print(pussy)
                print(dick)

if __name__ == "__main__":
    WD = WalkDir()
    mp3_files = WD.find_mp3_files()
    for mp3 in mp3_files:
        meta = MP3Tags(mp3)
        print(meta.Artist)
        print(meta.Album)
        print(meta.Song)
    # SP = SplitPath()
    # pathTupal = SP.gen_path_tupal_list(mp3_files)
    # # print("gen_path_tup complete")
    # pprint(pathTupal)
    # for p in pathTupal:
    #     SP.cd1_check_and_rename(p)
    #     SP.cd2_check_and_rename(p)
    #     SP.cd3_check_and_rename(p)
    #     SP.cd4_check_and_rename(p)
    #     SP.cd5_check_and_rename(p)
    #     SP.cd6_check_and_rename(p)
    #     SP.cd7_check_and_rename(p)
    #     SP.cd8_check_and_rename(p)
    #     SP.cd9_check_and_rename(p)

    # print("cd2_check_and_rename complete")
    # mp3_files2 = WD.find_mp3_files()
    # pathTupal2 = SP.gen_path_tupal_list(mp3_files2)
    # for pp in pathTupal2:
    #     SP.track_check(pp)
    # print("tracks complete")

    # RU = RemoveUnwanted().remove_crap()
    
    # WT = WriteTags().write_tag_main()

    # MTF = MatchTagFilename().change_file_names()
    # FF = FinalFix().last_fix()

