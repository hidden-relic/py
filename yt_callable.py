import re
from pytube import YouTube, Search, Playlist
from pytube.cli import on_progress
from validators import url as is_url
from time import sleep
from sys import exit as ex
from sys import platform as pf
import datetime

music_dir = '\\storage\\emulated\\0\\audio' if pf == 'linux' else 'C:\\giz\\Music'


def red(t):
    return "\033[91m {}\033[00m".format(t)


def green(t):
    return "\033[92m {}\033[00m".format(t)


def get_vid(query, title):
    yt = YouTube(query, on_progress_callback=on_progress)
    yt.streams.filter(only_audio=True, adaptive=True).order_by('abr').desc().first().download(music_dir)
    # yt.streams.filter(only_audio=True).first().download(output_path='C:\giz\music')
    print('Getting '+title+'...', '(:')


def main():

    t = True
    luck = False
    queries = []

    while t:
        lucky = 'ON' if luck else 'OFF'

        print('<< Enter a valid YouTube URL or the title of a video',
              '<< [D]ownload the list, [P]laylist, or [Q]uit')
        print('<< Feeling Lucky is '+lucky+' ([L]ucky Toggle)')
        query = input('>> ')

        if query == 'q':
            t = False
            print('Enjoy!')
            sleep(3)
            ex()

        elif query == 'd':
            for q in queries:
                url, title = q[0], q[1]
                get_vid(url, title)
                del q

        elif query == 'l':
            luck = not luck

        elif query == 'p':
            print('<< URL of a playlist or a video from a playlist')
            query = input('>> ')
            if is_url(query) is True:
                pl = Playlist(query)
                pl._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
                print(f'Got playlist: {pl.title}')
                print(str(len(pl.video_urls))+' files found')
                for video in pl.videos:
                    queries.append((video.watch_url, video.title))
                    print(video.title+' queued')
            else:
                print(str(query)+' is not a valid URL.')
        else:
            if is_url(query) is True:
                title = YouTube(query).title
                queries.append((query, title))
                print(title+' queued')
            else:
                s = Search(query)
                if luck:
                    url = 'https://www.youtube.com/watch?v='+str(s.results[0].video_id)
                    queries.append((url, s.results[0].title))
                    print(s.results[0].title+' queued')
                else:
                    print(str(len(s.results))+' results:')
                    for i, vid in enumerate(s.results):
                        print('['+str(i+1)+'] '+vid.title+' (' +
                              str(datetime.timedelta(seconds=vid.length))+')')
                    query = input('>> ')
                    url = 'https://www.youtube.com/watch?v='+s.results[int(query)-1].video_id
                    queries.append((url, s.results[int(query)-1].title))
                    print(s.results[int(query)-1].title+' queued')


if __name__ == '__main__':
    main()
