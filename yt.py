from pytube import YouTube, Search
from pytube.cli import on_progress
from validators import url as is_url
from os.path import exists as file_exists
from time import sleep
from sys import exit as ex
import datetime

music_dir = '/storage/emulated/0/Music/'

def red(t):
    return "\033[91m {}\033[00m".format(t)


def green(t):
    return "\033[92m {}\033[00m".format(t)


def get_vid(query, title):
    
    def on_complete(stream, file_path):
    	print('<< GOT: '+file_path)
    	print('<< Roll the dice on lyrics? [Y]es or [N]o')
    	caption=yt.captions.get_by_language_code['en'] if input() == 'y' else False
    	if caption:
    		file = music_dir+title+'.txt'
    		lyrics = caption.generate_srt_captions()
    		mode = 'w' if file_exists(file) else 'c'
    		f = open(file, mode)
    		f.write(lyrics)
    		f.close()
    		print('<< GOT: '+title+' lyrics')

    print('<< GET: '+title+'...', '(:')
    yt = YouTube(query, on_progress_callback=on_progress, on_complete_callback=on_complete)
    yt.streams.filter(only_audio=True).first().download(output_path=music_dir)
    

def main():

    t = True
    luck = True
    queries = []

    while t:
        lucky = 'ON' if luck else 'OFF'

        print('<< Enter a valid YouTube URL or the title of a video')
        print('<< [D]ownload the list or [Q]uit')
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
