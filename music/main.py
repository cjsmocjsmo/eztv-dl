import glob
import os
import re
import subprocess
import yaml
from PIL import Image
from mutagen.easyid3 import EasyID3

# Load the configuration file
with open('/media/pipi/HD/eztv-dl/music/config.yaml', 'r') as config_file:
    config = yaml.safe_load(config_file)

class ConvertPngFiles:
    def __init__(self, config):
        self.config = config

    def new_filename(self, filename):
        return filename.replace('.png', '.jpg')

    def convert_png_file(self, png_list):
        for png in png_list:
            jpg = self.new_filename(png)
            im = Image.open(png)
            rgb_im = im.convert('RGB')
            rgb_im.save(jpg)
            os.remove(png)
            # print(f'Converted {png} to {jpg}')

    def convert_png_files(self):
        path = self.config['base_directory']
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.endswith(self.config['file_extensions'][3]):
                    self.convert_png_file(file)

class ConvertFlacToMp3:
    def __init__(self, config):
        self.config = config

    def new_filename(self, filename):
        return filename.replace('.flac', '.mp3')

    def convert_flac_file(self, flac):
        mp3 = self.new_filename(flac)
        try:
            subprocess.run(['ffmpeg', '-i', flac, mp3], check=True)
            print(f'Converted {flac} to {mp3}')
        except subprocess.CalledProcessError as e:
            print(f'Error converting {flac}: {e}')
            

    def convert_flac_files(self):
        path = self.config['base_directory']
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.endswith(self.config['file_extensions'][1]):
                    path = os.path.join(root, file)
                    self.convert_flac_file(path)
                    os.removes(path)

class RemoveSpecialCharacters:
    def __init__(self, config):
        self.config = config

    def remove_parenthases(self, apath):
        par1 = re.compile("\(")
        par2 = re.compile("\)")

        if par1.search(apath) != None and par2.search(apath) != None:
            new_name = re.sub(r'\(.*?\)', '', apath)
            # print(f'Removed Parentheses from {apath}')
            # print(f'New Name: {new_name}')
            return new_name
        else:
            return apath

    def remove_special_characters(self):
        for root, dirs, files in os.walk(self.config['base_directory']):
            for file in files:
                new_name = file.replace("&", "And").replace("+", "And").replace("'", "")
                new_name = new_name.replace("’", "").replace("!", "").replace("?", "")
                new_name = new_name.replace(":", "").replace(";", "").replace("’", "").replace("“", "")
                no_par_name = self.remove_parenthases(new_name)
                no_par_name = no_par_name.replace("  ", " ")
                
                old_path = os.path.join(root, file)
                new_path = os.path.join(root, no_par_name)
                if old_path is not new_path:
                    os.renames(old_path, new_path)
                    # print(f'Renamed {old_path} to {new_path}')

class ArtistTagCheck:
    def __init__(self, config):
        self.config = config

    def tag_info(self, file):
        try:
            audio = EasyID3(file)
            artist = audio.get('artist', ['Unknown'])[0]
            return artist
        except Exception as e:
            print(f'Error reading artist tag for {file}: {e}')

    def remove_spe_char(self, artist):
        new_artist = artist.replace("&", "And").replace("+", "And").replace("'", "").replace(",", "")
        new_artist = new_artist.replace("’", "").replace("!", "").replace("?", "")
        new_artist = new_artist.replace(":", "").replace(";", "").replace("’", "").replace("“", "")
        return new_artist
    
    def remove_parenthases(self, apath):
        par1 = re.compile("\(")
        par2 = re.compile("\)")

        if par1.search(apath) != None and par2.search(apath) != None:
            new_name = re.sub(r'\(.*?\)', '', apath)
            # print(f'Removed Parentheses from {apath}')
            # print(f'New Name: {new_name}')
            return new_name
        else:
            return apath

    def write_artist_tag(self, file, artist):
        try:
            audio = EasyID3(file)
            audio['artist'] = artist
            audio.save()
            print(f'Wrote artist tag for {file}')
        except Exception as e:
            print(f'Error writing artist tag for {file}: {e}')

    def check_artist_tag(self):
        for root, dirs, files in os.walk(self.config['base_directory']):
            for file in files:
                if file.endswith('.mp3'):
                    file_path = os.path.join(root, file)
                    artist = self.tag_info(file_path)
                    new_artist = self.remove_spe_char(artist)
                    new_artist = self.remove_parenthases(new_artist)
                    
                    if artist is not new_artist:
                        self.write_artist_tag(file_path, new_artist)
                    
class AlbumTagCheck:
    def __init__(self, config):
        self.config = config

    def tag_info(self, file):
        try:
            audio = EasyID3(file)
            album = audio.get('album', ['Unknown'])[0]
            return album
        except Exception as e:
            print(f'Error reading album tag for {file}: {e}')

    def remove_spe_char(self, album):
        new_album = album.replace("&", "And").replace("+", "And").replace("'", "").replace(",", "")
        new_album = new_album.replace("’", "").replace("!", "").replace("?", "")
        new_album = new_album.replace(":", "").replace(";", "").replace("’", "").replace("“", "")
        return new_album
    
    def remove_parenthases(self, apath):
        par1 = re.compile("\(")
        par2 = re.compile("\)")

        if par1.search(apath) != None and par2.search(apath) != None:
            new_name = re.sub(r'\(.*?\)', '', apath)
            # print(f'Removed Parentheses from {apath}')
            # print(f'New Name: {new_name}')
            return new_name
        else:
            return apath

    def write_album_tag(self, file, album):
        try:
            audio = EasyID3(file)
            audio['album'] = album
            audio.save()
            print(f'Wrote album tag for {file}')
        except Exception as e:
            print(f'Error writing album tag for {file}: {e}')

    def check_album_tag(self):
        for root, dirs, files in os.walk(self.config['base_directory']):
            for file in files:
                if file.endswith('.mp3'):
                    file_path = os.path.join(root, file)
                    album = self.tag_info(file_path)
                    new_album = self.remove_spe_char(album)
                    new_album = self.remove_parenthases(new_album)
                    
                    if album is not new_album:
                        self.write_album_tag(file_path, new_album)

class TitleTagCheck:
    def __init__(self, config):
        self.config = config

    def tag_info(self, file):
        try:
            audio = EasyID3(file)
            title = audio.get('title', ['Unknown'])[0]
            return title
        except Exception as e:
            print(f'Error reading title tag for {file}: {e}')

    def remove_spe_char(self, title):
        new_title = title.replace("&", "And").replace("+", "And").replace("'", "").replace(",", "")
        new_title = new_title.replace("’", "").replace("!", "").replace("?", "")
        new_title = new_title.replace(":", "").replace(";", "").replace("’", "").replace("“", "")
        return new_title
    
    def remove_parenthases(self, apath):
        par1 = re.compile("\(")
        par2 = re.compile("\)")

        if par1.search(apath) != None and par2.search(apath) != None:
            new_name = re.sub(r'\(.*?\)', '', apath)
            # print(f'Removed Parentheses from {apath}')
            # print(f'New Name: {new_name}')
            return new_name
        else:
            return apath
        
    def write_title_tag(self, file, title):
        try:
            audio = EasyID3(file)
            audio['title'] = title
            audio.save()
            print(f'Wrote title tag for {file}')
        except Exception as e:
            print(f'Error writing title tag for {file}: {e}')

    def check_title_tag(self):
        for root, dirs, files in os.walk(self.config['base_directory']):
            for file in files:
                if file.endswith('.mp3'):
                    file_path = os.path.join(root, file)
                    title = self.tag_info(file_path)
                    new_title = self.remove_spe_char(title)
                    new_title = self.remove_parenthases(new_title)
                    
                    if title is not new_title:
                        self.write_title_tag(file_path, new_title)

class TrackNumberTagCheck:
    def __init__(self, config):
        self.config = config

    def tag_info(self, file):
        try:
            audio = EasyID3(file)
            track_number = audio.get('tracknumber', ['Unknown'])[0]
            return track_number
        except TypeError as e:
            print(f'Error reading track number tag for {file}: {e}')

    def track_tag_check(self):
        results = []
        for root, dirs, files in os.walk(self.config['base_directory']):
            for file in files:
                if file.endswith('.mp3'):
                    
                    fn = os.path.join(root, file)
                    
                    track_number = self.tag_info(fn)
                    # print(f'Track number: {track_number}')

                    try:
                        track_num = int(track_number)
                        # print(f'Track number: {track_num}')
                        if 1 <= track_num <= 100:
                            results.append(True)
                        else:
                            print(f'Track number {track_num} is out of range for {fn}')
                            results.append(False)
                    except ValueError:
                        print(f'Track number {track_number} is not a valid number for {fn}')
                        results.append(False)

class CDTagCheck:
    def __init__(self, config):
        self.config = config

    def tag_info(self, file):
        try:
            audio = EasyID3(file)
            cd_number = audio.get('TPOS', ['Unknown'])[0]
            return cd_number
        except Exception as e:
            print(f'Error reading CD number tag for {file}: {e}')

    def cd_tag_check(self):
        results = []
        for root, dirs, files in os.walk(self.config['base_directory']):
            for file in files:
                if file.endswith('.mp3'):
                    fn = os.path.join(root, file)
                    
                    cd_number = self.tag_info(fn)
                    if cd_number == 'Unknown':
                        if 'CD1' in fn:
                            cd_number = '1'
                        elif 'CD2' in fn:
                            cd_number = '2'
                        elif 'CD3' in fn:
                            cd_number = '3'
                        elif 'CD4' in fn:
                            cd_number = '4'
                        elif 'CD5' in fn:
                            cd_number = '5'
                        elif 'CD6' in fn:
                            cd_number = '6'
                        elif 'CD7' in fn:
                            cd_number = '7'
                        elif 'CD8' in fn:
                            cd_number = '8'
                        elif 'CD9' in fn:
                            cd_number = '9'
                        elif 'CD10' in fn:
                            cd_number = '10'
                        else:
                            print(f'CD number {cd_number} is not specified in the filename for {fn}')
                            results.append(False)
                            continue
                    try:
                        audio = EasyID3(fn)
                        audio['discnumber'] = cd_number
                        audio.save()
                        print(f'Set CD number to {cd_number} for {fn}')
                        results.append(True)
                    except Exception as e:
                        print(f'Error writing CD number tag for {fn}: {e}')
                        results.append(False)

class RenameFileWithTagInfo:
    def __init__(self, config):
        self.config = config

    def tag_info(self, file):
        try:
            audio = EasyID3(file)
            artist = audio.get('artist', ['Unknown'])[0]
            album = audio.get('album', ['Unknown'])[0]
            title = audio.get('title', ['Unknown'])[0]
            track_number = audio.get('tracknumber', ['Unknown'])[0]
            cd_number = audio.get('discnumber', ['Unknown'])[0]
            return cd_number, track_number, artist, album, title
        except Exception as e:
            print(f'Error reading tags for {file}: {e}')

    def rename_file(self, file, cd_number, track_number, artist, album, title):
        artist = artist.title()
        artist = artist.replace(" ", "_")

        album = album.title()
        album = album.replace(" ", "_")

        title = title.title()
        title = title.replace(" ", "_")
        new_prefix = f"{self.config['base_directory']}/{artist}/{album}/"
        new_name = f'{cd_number}_{track_number}_-_{artist}_-_{album}_-_{title}.mp3'
        new_path = os.path.join(new_prefix, new_name)
        if file is not new_path:
            os.renames(file, new_path)
            print(f'Renamed {file} to\n\t {new_path}')
        else:
            print(f'No changes needed.')

    def rename_files(self):
        for root, dirs, files in os.walk(self.config['base_directory']):
            for file in files:
                if file.endswith('.mp3'):
                    file_path = os.path.join(root, file)
                    cd_number, track_number, artist, album, title = self.tag_info(file_path)
                    self.rename_file(file_path, cd_number, track_number, artist, album, title)

class ExtractAlbumArt:
    def __init__(self, config):
        self.config = config

    def create_thumb_dir(self):
        if not os.path.exists(self.config['thumbnail_directory']):
            os.makedirs(self.config['thumbnail_directory'])

    def get_dir_list(self):
        dir_list = []
        for root, dirs, files in os.walk(self.config['base_directory']):
            for file in files:
                dir_list.append(root)
        return dir_list
    
    def glob_dir_for_first_mp3(self, adir):
        try:
            mp3_glob = glob.glob(f'{adir}/*.mp3')
            first_mp3 = mp3_glob[0]
            return first_mp3
        except IndexError:
            print(adir)

    def extract_album_art(self, mp3_path):
        try:
            audio = EasyID3(mp3_path)
            artwork = audio.get('APIC:', None)
            if artwork is not None:
                artist = audio.get('artist', ['Unknown'])[0]
                album = audio.get('album', ['Unknown'])[0]
                artist = artist.title()
                artist = artist.replace(" ", "_")
                album = album.title()
                album = album.replace(" ", "_")
                file_path = f'{self.config["thumbnail_directory"]}/{artist}_-_{album}.jpg'
                # print(f'extracted {file_path}')
                
                with open(f'{file_path}', 'wb') as img:
                    img.write(artwork[0])
                print(f'Extracted album art for {file_path}')
            else:
                print(f'No album art found for {mp3_path}')
        except Exception as e:
            print(f'Error extracting album art for {mp3_path}: {e}')

if __name__ == '__main__':
    # if config['convert_png_to_jpg']:
    #     png_converter = ConvertPngFiles(config).convert_png_files()

    # if config['convert_flac_to_mp3']:
    #     flac_converter = ConvertFlacToMp3(config).convert_flac_files()

    # if config['remove_special_characters']:
    #     RSC = RemoveSpecialCharacters(config).remove_special_characters()

    ArtTC = ArtistTagCheck(config).check_artist_tag()
    AlbTC = AlbumTagCheck(config).check_album_tag()
    TitTC = TitleTagCheck(config).check_title_tag()
    track = TrackNumberTagCheck(config).track_tag_check()
    print(track)
    cd = CDTagCheck(config).cd_tag_check()
    print(cd)
    RFTI = RenameFileWithTagInfo(config).rename_files()
    EA = ExtractAlbumArt(config)
    EA.create_thumb_dir()
    dlist = EA.get_dir_list()
    for adir in dlist:
        mp3 = EA.glob_dir_for_first_mp3(adir)
        print(mp3)
        # EA.extract_album_art(mp3)

    

    
