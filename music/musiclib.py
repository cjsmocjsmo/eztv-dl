#!/usr/bin/env python3
import os
import glob

def get_dir_artist_album(meta):
    dir_artist = meta['dir_split_list'][1].replace("_", " ")
    dir_album = meta['dir_split_list'][2].replace("_", " ")
    return (dir_artist, dir_album)       
            
def get_dir_artist_album_song(meta):
    fsplit = meta['filename'].split("_-_")
    file_artist = fsplit[1].replace("_", " ")
    file_album = fsplit[2].replace("_", " ")
    try:
        file_song = fsplit[3]
    except IndexError:
        # print(meta['full_filename'])
        file_song = "None"
    return (file_artist, file_album, file_song)
            
def get_dir_list(adirlist):
    dir_list = []
    for f in adirlist:
        dir, _ = os.path.split(f)
        dir_list.append(dir)
    dir_list = list(set(dir_list))
    return dir_list

def glob_for_pics(dir_list):
    missing_pic_list = []
    for dir in dir_list:
        globpath = dir + "/*.jpg"
        globpath2 = dir + "/*.png"
        result = glob.glob(globpath)
        result2 = glob.glob(globpath2)
        if len(result) == 0 and len(result2) == 0:
            missing_pic_list.append(dir)
    return (list(set(missing_pic_list)), len(missing_pic_list))