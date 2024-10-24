import os
import re
import glob
from pprint import pprint


MOVS_FOLDER = "/home/teresa/Downloads/movs"
SAVE_DIR = "/home/teresa/Downloads/processed"
REMOVE_LIST = [
    "www.YTS.MX.jpg",
    "www.YTS.LT.jpg",
    "WWW.YIFY-TORRENTS.COM.jpg",
    "WWW.YTS.AG.jpg",
    "WWW.YTS.RE.jpg",
    "www.YTS.AM.jpg",
    "WWW.YTS.TO.jpg",
]

def remove_crap():
    for (paths, dirs, files) in os.walk(MOVS_FOLDER, followlinks=True):
        for filename in files:
            fnn = os.path.join(paths, filename)
            _, ext = os.path.splitext(fnn)
            _, fname = os.path.split(fnn)
            if fname in REMOVE_LIST:
                print("removing {}".format(fnn))
                try:
                    os.remove(fnn)
                except FileNotFoundError:
                    pass
            if ext == ".txt":
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

def rm_empty_dirs():
    for (paths, dirs, files) in os.walk(MOVS_FOLDER, followlinks=True):
        try:
            os.removedirs(paths)
        except OSError:
            print("No empty dirs to remove")
            pass

def get_dir_list():
    dlist = []
    for (paths, dirs, files) in os.walk(MOVS_FOLDER, followlinks=True):
        for filename in files:
            fnn = os.path.join(paths, filename)
            dir, _ = os.path.split(fnn)
            dlist.append(dir)
    dirlist = list(set(dlist))
    return dirlist

def remove_rename_dir(adirlist):
    foo = re.compile(r"\[")
    for dir in adirlist:
        baz = re.search(foo, dir)
        if baz != None:
            bs = baz.start() - 1
            # print(dir[:bs])
            os.renames(dir, dir[:bs])

def glob_for_jpg(adir):
    jpgglobpath = "/".join((adir, "*.jpg"))
    jpg_glob = glob.glob(jpgglobpath)
    if len(jpg_glob) < 1:
        print(jpgglobpath)
        return (None, None, None)
    try:
        jpg_olddir, jpg_oldfilename = os.path.split(jpg_glob[0])
        return (jpg_olddir, jpg_oldfilename, jpg_glob[0])
    except IndexError:
        print(adir)

def glob_for_mp4(adir):
    mp4globpath = "/".join((adir, "*.mp4"))
    mp4_glob = glob.glob(mp4globpath)
    if len(mp4_glob) < 1:
        print(mp4globpath)
        os._exit(1)
    try:
        mp4_olddir, mp4_oldfilename = os.path.split(mp4_glob[0])
        return (mp4_olddir, mp4_oldfilename, mp4_glob[0])
    except IndexError:
        print(adir)

def glob_dir_list(a_dir_list):
    globlist = []
    for dir in a_dir_list:
        _, jpg_oldfilename, jpg = glob_for_jpg(dir)
        _, mp4_oldfilename, mp4 = glob_for_mp4(dir)
        meta = {
            "mp4_fullpath": mp4,
            "jpg_fullpath": jpg,
            "savedir": SAVE_DIR,
            "jpg_oldfilename": jpg_oldfilename,
            "mp4_oldfilename": mp4_oldfilename,
        }
        pprint(meta)
        globlist.append(meta)
        
    return globlist

def split_at_1080p(agloblist):
    s1 = re.compile(r"\.IMAX\.1080p")
    s2 = re.compile(r"\.1080p")
    s3 = re.compile(r"\.720p")
    s4 = re.compile(r"\.2160p")
    for meta in agloblist:
        print(meta)
        search1 = re.search(s1, meta["mp4_oldfilename"])
        search2 = re.search(s2, meta["mp4_oldfilename"])
        search3 = re.search(s3, meta["mp4_oldfilename"])
        search4 = re.search(s4, meta["mp4_oldfilename"])
        splitindex_end = ""
        if search1:
            splitindex_end = search1.start()
        elif search2:
            splitindex_end = search2.start()
        elif search3:
            splitindex_end = search3.start()
        elif search4:
            splitindex_end = search4.start()
        fn = meta["mp4_oldfilename"][:splitindex_end]
        foofn = fn.replace("..", " ").replace("-", " ").replace(".", " ")
        foo = " ".join((foofn[:-5], "("))
        front =  "/".join((meta["savedir"], foo))

        newmp4path = front + foofn[-4:] + ").mp4"
        print("\n")
        print(meta["mp4_fullpath"])
        print(newmp4path)
        print("\n")
        os.renames(meta["mp4_fullpath"], newmp4path)
        if meta["jpg_fullpath"] != None:
            newjpgpath = front + foofn[-4:] + ").jpg"
            os.renames(meta["jpg_fullpath"], newjpgpath)

def run():
    remove_crap()
    rm_empty_dirs()
    dirlist = get_dir_list()
    # print(dirlist)
    remove_rename_dir(dirlist)
    dirlist2 = get_dir_list()
    # print(dirlist2)
    globlist = glob_dir_list(dirlist2)
    # print(globlist)
    split_at_1080p(globlist)

if __name__ == "__main__":
    run()