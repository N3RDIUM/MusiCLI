from __future__ import unicode_literals
import youtube_dl
import shutil, os
from ytmusicapi import YTMusic
from tinytag import TinyTag
import json

if not os.path.isfile('userdata.json'):
    with open('userdata.json', 'w') as f:
        f.write('[]')

def get_song_data(path):
    tag = TinyTag.get(path)
    return [tag.title, tag.artist, tag.album, tag.duration]

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
            'quiet': True
        }

    # search for a song
    def search(self, query):
        results = self.ytmusic.search(query)
        return results

    def download(self, id):
        dl = youtube_dl.YoutubeDL(self.default_args)
        file_path = "./" + dl.prepare_filename(dl.extract_info(f'https://www.youtube.com/watch?v={id}', download=False)).replace('webm', 'mp3')
        file_path_new = dl.extract_info(f'https://www.youtube.com/watch?v={id}', download=False)['title'] + '.mp3'
        if not os.path.isfile('./music/' + file_path_new):
            dl.download([f'https://www.youtube.com/watch?v={id}'])
        if not os.path.isdir('./music'):
            os.mkdir('./music')
        try:
            shutil.move(file_path, file_path_new)
            try:
                shutil.move(file_path_new, './music/')
            except FileExistsError:
                os.remove(file_path_new)
        except:
            pass

        info = dl.extract_info(f'https://www.youtube.com/watch?v={id}', download=False)
        # open json file and add song to it
        with open('userdata.json', 'r') as f:
            data = json.load(f)
            data.append({
                'title': info['title'],
                'artist': info['artist'],
                'duration': info['duration'],
                'description': info['description'],
                'thumbnail': info['thumbnail'],
                'path': './music/' + file_path_new
            })
            found = []
            for song in data:
                if not song in found:
                    found.append(song)
            data = found
            with open('userdata.json', 'w') as f:
                json.dump(data, f)

    # search and download a song
    def download_song(self, query=None, id=None):
        if query:
            results = self.search(query)
            id = results[0]['videoId']
            self.download(id)
        elif id:
            self.download(id)

# test
if __name__ == '__main__':
    music = MusicDownloader()
    music.download_song('Nigel Stanford - One hundred hunters')
