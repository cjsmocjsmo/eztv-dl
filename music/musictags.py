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

    # def track_check(self, atup):
    #     foo = atup[2].split("_-_")
    #     s1 = re.compile("[0-9]_[0-9][0-9]")
    #     s2 = re.compile("[0-9]-[0-9][0-9]")
    #     result = re.search(s1, foo[0])
    #     result2 = re.search(s2, foo[0])
    #     resultlist = []
    #     returnlist = []
    #     if result == None and result2 == None:
    #         foobar = "1_" + foo[0]
    #         resultlist.append(foobar)
    #         if foo[1]:
    #             resultlist.append(foo[1])
    #         try:
    #             if foo[2]:
    #                 resultlist.append(foo[2])
    #         except IndexError:
    #             pass

    #         try:
    #             if foo[3]:
    #                 resultlist.append(foo[3])
    #         except IndexError:
    #             pass

    #         try:
    #             if foo[4]:
    #                 resultlist.append(foo[4])
    #         except IndexError:
    #             pass

    #         result = ""
    #         for r in resultlist:
    #             result = result + "_-_" + r 

    #         newstringlist = []
            
    #         if atup[1]:
    #             newstringlist.append(atup[1])
    #         newstringlist.append(result[3:])
            
    #         if atup[3]:
    #             newstringlist.append(atup[3])
    #         try:
    #             if atup[4]:
    #                 newstringlist.append(atup[4])
    #         except IndexError:
    #             pass

    #         ns = ""
    #         fart = ""
    #         for newstring in newstringlist:
    #             ns = ns + "/" + newstring
    #             f = ns.replace("//", "/").replace("/.", ".")
    #             fart = f.replace("Ac_Dc", "AC_DC").replace("Tnt", "TNT").replace("Zz", "ZZ")
    #         try:
    #             os.rename(atup[0], fart)
    #         except FileNotFoundError:
    #             pass

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



# class WriteTags:
#     def write_tag(self, atup, fn):
#         audio = EasyID3(fn)
#         audio['title'] = atup[2]
#         audio['artist'] = atup[0]
#         audio['album'] = atup[1]
#         audio['tracknumber'] = atup[3] # empty
#         audio.save()

#     def write_tag_main(self):
#         WD = WalkDir()
#         alist = WD.find_mp3_files()
#         for mp33 in alist:
#             tagmeta = MP3Tags(mp33)
#             spart = tagmeta.Artist.split(" ")
#             spalb = tagmeta.Album.split(" ")
#             spsong = tagmeta.Song.split(" ")
#             ARTIST = ArtistTagFix().scan_and_fix_artist(spart)
#             ALBUM = AlbumTagFix().scan_and_fix_album(spalb)
#             SONG = SongTagFix().scan_and_fix_song(spsong)
#             TRACK = SplitTrack().SPTMain(tagmeta.Track)
#             ace = (ARTIST, ALBUM, SONG, TRACK)
#             self.write_tag(ace, mp33)
#             pprint(ace)







if __name__ == "__main__":
    WD = WalkDir()
    mp3_files = WD.find_mp3_files()
    for mp3 in mp3_files:
        meta = MP3Tags(mp3)
        print(meta.Artist)
        print(meta.Album)
        print(meta.Song)
    
