from __future__ import unicode_literals
import youtube_dl
import shutil, os
from ytmusicapi import YTMusic

class MusicDownloader:
    def __init__(self):
        self.ytmusic = YTMusic()
        self.default_args = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

    # search for a song
    def search(self, query):
        results = self.ytmusic.search(query)
        return results



    def download(self, id):
        dl = youtube_dl.YoutubeDL(self.default_args)
        file_path = "./" + dl.prepare_filename(dl.extract_info(f'https://www.youtube.com/watch?v={id}', download=False)).replace('webm', 'mp3')
        if not os.path.isfile(file_path):
            dl.download([f'https://www.youtube.com/watch?v={id}'])
            shutil.move(file_path, file_path.replace('webm', 'mp3'))
        else:
            if not os.path.isfile('./music'):
                os.mkdir('./music')
            shutil.move(file_path, './music/')

    # search and download a song
    def download_song(self, query):
        results = self.search(query)
        id = results[0]['videoId']
        self.download(id)

# test
if __name__ == '__main__':
    music = MusicDownloader()
    music.download_song('NightKILLA - nine circles')
