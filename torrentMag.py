#!/usr/bin/env python3

import libtorrent as lt
import time

class DownloadTor:
    def __init__(self, magnetlink):
        self.ses = lt.session()
        self.ses.listen_on(6881, 6891)
        self.params = {
            'save_path': '/home/pi/Downloads/NewDownloads/',
            'storage_mode': lt.storage_mode_t(2),
            'paused': False,
            'auto_managed': True,
            'duplicate_is_error': True,
        }
        self.handle = lt.add_magnet_uri(self.ses, magnetlink, self.params)

    def startDownload(self):
        self.ses.start_dht()

        print('downloading metadata...')
        while (not self.handle.has_metadata()):
            time.sleep(1)
        print('got metadata, starting torrent download...')
        while (self.handle.status().state != lt.torrent_status.seeding):
            s = self.handle.status()
            state_str = ['queued', 'checking', 'downloading metadata', \
                    'downloading', 'finished', 'seeding', 'allocating']
            print('%.2f%% complete (down: %.1f kb/s up: %.1f kB/s peers: %d) %s' % \
                    (s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000, \
                    s.num_peers, state_str[s.state]))
            time.sleep(5)