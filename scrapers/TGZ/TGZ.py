#!/usr/bin/python3

import re
import time
import TGZlib as tgzlib
import sqlite3
import logging

from pprint import pprint

def main():

    start_time = time.time()
    print("Start time: {}".format(start_time))
    # Create a logger
    logger = logging.getLogger(__name__)

    # Set the log level
    logger.setLevel(logging.DEBUG)

    # Create a file handler
    file_handler = logging.FileHandler('/home/pi/eztv-dl/scrapers/TGZ_log.txt')

    # Set the formatter for the file handler
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s'))

    # Add the file handler to the logger
    logger.addHandler(file_handler)



    _ = tgzlib.DownLoad().clean_download_dir()
    data = tgzlib.DownLoad().download_file()

    lines_list = tgzlib.Utils().read_the_file(data)

    tv_list_raw = tgzlib.Utils().filter_by_TV(lines_list)
    tv_list = tgzlib.Utils().create_tv_dict_list(tv_list_raw)

    movie_list_raw = tgzlib.Utils().filter_by_Movies(lines_list)
    mov_list = tgzlib.Utils().create_mov_dict_list(movie_list_raw)

    # pprint(tv_list)

    # connection = sqlite3.connect('/media/charliepi/HD/eztv-dl/scrapers/TGZ.db')
    connection = sqlite3.connect('/home/pi/eztv-dl/scrapers/TGZ.db')
    cursor = connection.cursor()

    tgzlib.SQL().create_tv_table(cursor, connection)
    tgzlib.SQL().insert_tv(cursor, connection, tv_list)

    tgzlib.SQL().create_movies_table(cursor, connection)
    tgzlib.SQL().insert_movies(cursor, connection, mov_list)

    stats = {
        'tv': len(tv_list),
        'movies': len(mov_list),
        'total': len(lines_list)
    }

    #Search rss feed for new episodes
    new_episode_list = []
    for tv in tv_list:
        andor_search = tgzlib.TVSearch().andor_search(tv)
        if andor_search != None:
            new_episode_list.append(andor_search[1])

        lower_decks_search = tgzlib.TVSearch().lower_decks_search(tv)
        if lower_decks_search != None:
            new_episode_list.append(lower_decks_search[1])

        discovery_search = tgzlib.TVSearch().discovery_search(tv)
        if discovery_search != None:
            new_episode_list.append(discovery_search[1])

        mandalorian_search = tgzlib.TVSearch().mandalorian_search(tv)
        if mandalorian_search != None:
            new_episode_list.append(mandalorian_search[1])

        orville_search = tgzlib.TVSearch().orville_search(tv)
        if orville_search != None:
            new_episode_list.append(orville_search[1])

        for_all_man_kind_search = tgzlib.TVSearch().for_all_man_kind_search(tv)
        if for_all_man_kind_search != None:
            new_episode_list.append(for_all_man_kind_search[1])

        bad_batch_search = tgzlib.TVSearch().bad_batch_search(tv)
        if bad_batch_search != None:
            new_episode_list.append(bad_batch_search[1])

        wheel_of_time_search = tgzlib.TVSearch().wheel_of_time_search(tv)
        if wheel_of_time_search != None:
            new_episode_list.append(wheel_of_time_search[1])

        foundation_search = tgzlib.TVSearch().foundation_search(tv)
        if foundation_search != None:
            new_episode_list.append(foundation_search[1])

        visions_search = tgzlib.TVSearch().starwarsvisions_search(tv)
        if visions_search != None:
            new_episode_list.append(visions_search[1])

        startrekprodigy_search = tgzlib.TVSearch().startrekprodigy_search(tv)
        if startrekprodigy_search != None:
            new_episode_list.append(startrekprodigy_search[1])

        bookofbobafett_search = tgzlib.TVSearch().bookofbobafett_search(tv)
        if bookofbobafett_search != None:
            new_episode_list.append(bookofbobafett_search[1])

        continental_search = tgzlib.TVSearch().continental_search(tv)
        if continental_search != None:
            new_episode_list.append(continental_search[1])

        halo_search = tgzlib.TVSearch().halo_search(tv)
        if halo_search != None:
            new_episode_list.append(halo_search[1])

        strangenewworlds_search = tgzlib.TVSearch().strangenewworlds_search(tv)
        if strangenewworlds_search != None:
            new_episode_list.append(strangenewworlds_search[1])

        prehistoric_planet_search = tgzlib.TVSearch().prehistoricplanet_search(tv)
        if prehistoric_planet_search != None:
            new_episode_list.append(prehistoric_planet_search[1])

        obiwankenobi_search = tgzlib.TVSearch().obiwankenobi_search(tv)
        if obiwankenobi_search != None:
            new_episode_list.append(obiwankenobi_search[1])

        groot_search = tgzlib.TVSearch().groot_search(tv)
        if groot_search != None:
            new_episode_list.append(groot_search[1])

        houseofthedragon_search = tgzlib.TVSearch().houseofthedragon_search(tv)
        if houseofthedragon_search != None:
            new_episode_list.append(houseofthedragon_search[1])

        lordoftherings_search = tgzlib.TVSearch().lordoftherings_search(tv)
        if lordoftherings_search != None:
            new_episode_list.append(lordoftherings_search[1])

        silo_search = tgzlib.TVSearch().silo_search(tv)
        if silo_search != None:
            new_episode_list.append(silo_search[1])

        ahso_search = tgzlib.TVSearch().ahsoka_search(tv)
        if ahso_search != None:
            new_episode_list.append(ahso_search[1])

        droidstory_search = tgzlib.TVSearch().droidstory_search(tv)
        if droidstory_search != None:
            new_episode_list.append(droidstory_search[1])

        wakanda_search = tgzlib.TVSearch().wakanda_search(tv)
        if wakanda_search != None:
            new_episode_list.append(wakanda_search[1])

        acolyte_search = tgzlib.TVSearch().acolyte_search(tv)
        if acolyte_search != None:
            new_episode_list.append(acolyte_search[1])

        lando_search = tgzlib.TVSearch().lando_search(tv)
        if lando_search != None:
            new_episode_list.append(lando_search[1])


    pprint(list(set(new_episode_list)))
    logger.info(list(set(new_episode_list)))
    pprint(stats)
    logger.info(stats)
    tv_count = tgzlib.SQL().tv_count(cursor)
    mov_count = tgzlib.SQL().movie_count(cursor)
    print("TV DB Count: {}".format(tv_count[0]))
    logger.info("TV DB Count: {}".format(tv_count[0]))
    print("Movie DB Count: {}".format(mov_count[0]))
    logger.info("Movies DB Count: {}".format(mov_count[0]))
    end_time = time.time()
    seconds = end_time - start_time
    print("Elapsed Time: {} sec".format(seconds))
    logger.info("Elapsed Time: {} sec".format(seconds))

    minutes = seconds / 60
    print("Elapsed Time: {} min".format(minutes))
    logger.info("Elapsed Time: {} min".format(minutes))
    logger.info("\n\n")

if __name__ == "__main__":
    main()