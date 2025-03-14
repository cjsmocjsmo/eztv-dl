import argparse
import sqlite3
import os
import re
from pprint import pprint

CREATOR = re.compile(r"The Creator")
GODZILLA = re.compile(r"Godzilla Minus One")
MARVELS = re.compile(r"The Marvels")

ANDOR = (re.compile(r"andor"), re.compile(r"s02e01"))
LOKI = (re.compile(r"loki"), re.compile(r"s03e01"))
LOWER_DECKS = (re.compile(r"lower decks"), re.compile(r"s05e01"))
DISCOVERY = (re.compile(r"discovery"), re.compile(r"s05e01"))
MANDALORIAN = (re.compile(r"mandalorian"), re.compile(r"s04e01"))
ORVILLE = (re.compile(r"orville"), re.compile(r"s04e01"))
FOR_ALL_MANKIND = (re.compile("for all man kind"), re.compile(r"s04e01"))
BAD_BATCH = (re.compile(r"bad batch"), re.compile(r"s03e01"))
WHEEL_OF_TIME = (re.compile(r"wheel of time"), re.compile(r"s03e01"))
FOUNDATION = (re.compile(r"foundation"), re.compile(r"s03e01"))
STAR_WARS_VISIONS = (re.compile(r"star wars visions"), re.compile(r"s02e01"))
STAR_TREK_PRODIGY = (re.compile(r"star trek prodigy"), re.compile(r"s02e01"))
BOOK_OF_BOBA_FETT = (re.compile(r"book of boba fett"), re.compile(r"s02e01"))
CONTINENTAL = (re.compile(r"continental"), re.compile(r"s02e01"))
HALO = (re.compile(r"halo"), re.compile(r"s02e01"))
STRANGE_NEW_WORLDS = (re.compile(r"strange new worlds"), re.compile(r"s02e01"))
PRE_HISTORIC_PLANET = (re.compile(r"prehistoric planet"), re.compile(r"s02e01"))
OBI_WAN_KENOBI = (re.compile(r"obi wan kenobi"), re.compile(r"s02e01"))
GROOT = (re.compile(r"groot"), re.compile(r"s02e01"))
HOUSE_OF_THE_DRAGON = (re.compile(r"house of the dragon"), re.compile(r"s02e01"))
LORD_OF_THE_RINGS = (re.compile(r"lord of the rings the rings of power"), re.compile(r"s02e01"))
SILO = (re.compile(r"silo"), re.compile(r"s02e01"))
AHSOKA = (re.compile(r"ahsoka"), re.compile(r"s02e01"))
WAKANDA = (re.compile(r"wakanda"), re.compile(r"s01e01"))
ACOLYTE = (re.compile(r"acolyte"), re.compile(r"s01e01"))
LANDO = (re.compile(r"lando"), re.compile(r"s01e01"))
MONARCK_LEGACY_OF_MONSTERS = (re.compile(r"monarck legacy of monsters"), re.compile(r"s01e01"))

#monack legacy of monsters

def get_movie_list():
	conn = sqlite3.connect('/home/pi/eztv-dl/scrapers/TGZ.db')
	cur = conn.cursor()
	cur.execute("SELECT title FROM movies")
	rows = cur.fetchall()
	cur.close()
	conn.close()
	new_mov_list = []
	for row in rows:
		new_mov_list.append(row[0])
	return new_mov_list

def get_tv_list():
	conn = sqlite3.connect('/home/pi/eztv-dl/scrapers/TGZ.db')
	cur = conn.cursor()
	cur.execute("SELECT title FROM tv")
	rows = cur.fetchall()
	cur.close()
	conn.close()
	new_tv_list = []
	for row in rows:
		new_tv_list.append(row[0])
	return new_tv_list

def search_for_term(term, list):
	found_list = []
	for item in list:
		if re.search(term, item) != None:
			found_list.append(item)
	return found_list

def search_for_season(season, atitle):
	if re.search(season, atitle) != None:
		return atitle
	else:
		return None





def main(args):
	print("catagory: {}\nterm: {}\ndefault: {}\nseason: {}".format(args.catagory, args.term, args.default, args.season))
	tv_list = ["t", "T", "tv", "TV", "tel", "Tel"]
	mov_list = ["m", "M", "mov", "MOV", "movie", "Movie", "movies", "Movies"]
	if args.catagory == None and args.term == None and args.default == None:
		print("Please enter a catagory, term, or default")
		os.exit(1)
	elif args.catagory != None and args.term != None and args.default != None:
		print("Using -d with -c and -t not allowed")
		os.exit(1)
	elif args.catagory != None and args.term != None and args.default == None:
		mov_foundterms = ""
		tv_foundterms = []
		if args.catagory in mov_list:
			mlist = get_movie_list()
			mov_foundterms = search_for_term(args.term, mlist)
			pprint(mov_foundterms)

		found_episode = []
		if args.catagory in tv_list:
			tlist = get_tv_list()
			foundterms = search_for_term(args.term, tlist)
			if args.season != None:
				for term in foundterms:
					episode = search_for_season(args.season, term)
					if episode != None:
						found_episode.append(episode)

		pprint(found_episode)
	elif args.catagory == None and args.term == None and args.default != None:
		mov_list = get_movie_list()
		movs_found_list = []
		tv_found_list = []
		for mov in mov_list:
			if re.search(CREATOR, mov) != None:
				movs_found_list.append(mov)
			elif re.search(GODZILLA, mov) != None:
				movs_found_list.append(mov)

		tv_list = get_tv_list()
		tv_found_list = []
		for tv in tv_list:
			if re.search(ANDOR[0], tv) != None and re.search(ANDOR[1], tv) != None:
				tv_found_list.append(tv)
			elif re.search(LOKI[0], tv) != None and re.search(LOKI[1], tv) != None:
				tv_found_list.append(tv)
			elif re.search(LOWER_DECKS[0], tv) != None and re.search(LOWER_DECKS[1], tv) != None:
				tv_found_list.append(tv)
			elif re.search(DISCOVERY[0], tv) != None and re.search(DISCOVERY[1], tv) != None:
				tv_found_list.append(tv)
			elif re.search(MANDALORIAN[0], tv) != None and re.search(MANDALORIAN[1], tv) != None:
				tv_found_list.append(tv)
			elif re.search(ORVILLE[0], tv) != None and re.search(ORVILLE[1], tv) != None:
				tv_found_list.append(tv)
			elif re.search(FOR_ALL_MANKIND[0], tv) != None and re.search(FOR_ALL_MANKIND[1], tv) != None:
				tv_found_list.append(tv)
			elif re.search(BAD_BATCH[0], tv) != None and re.search(BAD_BATCH[1], tv) != None:
				tv_found_list.append(tv)
			elif re.search(WHEEL_OF_TIME[0], tv) != None and re.search(WHEEL_OF_TIME[1], tv) != None:
				tv_found_list.append(tv)
			elif re.search(FOUNDATION[0], tv) != None and re.search(FOUNDATION[1], tv) != None:
				tv_found_list.append(tv)
			elif re.search(STAR_WARS_VISIONS[0], tv) != None and re.search(STAR_WARS_VISIONS[1], tv) != None:
				tv_found_list.append(tv)
			elif re.search(STAR_TREK_PRODIGY[0], tv) != None and re.search(STAR_TREK_PRODIGY[1], tv) != None:
				tv_found_list.append(tv)
			elif re.search(BOOK_OF_BOBA_FETT[0], tv) != None and re.search(BOOK_OF_BOBA_FETT[1], tv) != None:
				tv_found_list.append(tv)
			elif re.search(CONTINENTAL[0], tv) != None and re.search(CONTINENTAL[1], tv) != None:
				tv_found_list.append(tv)
			elif re.search(HALO[0], tv) != None and re.search(HALO[1], tv) != None:
				tv_found_list.append(tv)
			elif re.search(STRANGE_NEW_WORLDS[0], tv) != None and re.search(STRANGE_NEW_WORLDS[1], tv) != None:
				tv_found_list.append(tv)
			elif re.search(PRE_HISTORIC_PLANET[0], tv) != None and re.search(PRE_HISTORIC_PLANET[1], tv) != None:
				tv_found_list.append(tv)
			elif re.search(OBI_WAN_KENOBI[0], tv) != None and re.search(OBI_WAN_KENOBI[1], tv) != None:
				tv_found_list.append(tv)
			elif re.search(GROOT[0], tv) != None and re.search(GROOT[1], tv) != None:
				tv_found_list.append(tv)
			elif re.search(HOUSE_OF_THE_DRAGON[0], tv) != None and re.search(HOUSE_OF_THE_DRAGON[1], tv) != None:
				tv_found_list.append(tv)
			elif re.search(LORD_OF_THE_RINGS[0], tv) != None and re.search(LORD_OF_THE_RINGS[1], tv) != None:
				tv_found_list.append(tv)
			elif re.search(SILO[0], tv) != None and re.search(SILO[1], tv) != None:
				tv_found_list.append(tv)
			elif re.search(AHSOKA[0], tv) != None and re.search(AHSOKA[1], tv) != None:
				tv_found_list.append(tv)
			elif re.search(WAKANDA[0], tv) != None and re.search(WAKANDA[1], tv) != None:
				tv_found_list.append(tv)
			elif re.search(ACOLYTE[0], tv) != None and re.search(ACOLYTE[1], tv) != None:
				tv_found_list.append(tv)
			elif re.search(LANDO[0], tv) != None and re.search(LANDO[1], tv) != None:
				tv_found_list.append(tv)
			elif re.search(MONARCK_LEGACY_OF_MONSTERS[0], tv) != None and re.search(MONARCK_LEGACY_OF_MONSTERS[1], tv) != None:
				tv_found_list.append(tv)
			else:
				pass
		pprint(tv_found_list)
		pprint(movs_found_list)
		# return (tv_found_list, movs_found_list)

	else:
		print("something went wrong")

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="A simple CLI program")
	parser.add_argument("--catagory", "-c", help="TV or Movie")
	parser.add_argument("--term", "-t", help="Text to search for")
	parser.add_argument("--season", "-s", help="Season to search for")
	parser.add_argument("--default", "-d", help="Scan default list yes or no")
	args = parser.parse_args()

	main(args)
