import re
from pytube import YouTube, Search, Playlist
from pytube.cli import on_progress
from validators import url as is_url
from time import sleep
from sys import exit as ex
from sys import platform as pf
import datetime
import configparser
from pathlib import Path
import os


def main():
	dir_path = os.path.dirname(os.path.realpath(__file__))
	cfg = configparser.ConfigParser()
	cfgfile=dir_path+'\\config.cfg'
	cfg.read(Path(cfgfile))
	config=cfg['yt-get']
	luck=config.getboolean('lucky')
	results=config.getint('results')
	music_dir=config["dir"]
	
	def checkPath(path):
		p = Path(path)
		if not p.is_dir():
			del p
			print(">> Please choose a valid download directory: ")
			p=input("<< ")
			checkPath(p)
		else:
			config["dir"]=os.fspath(p)
			with open(cfgfile, 'w') as configfile:
				cfg.write(configfile)
			return os.fspath(p)
			
	def get_vid(query, title):
		yt = YouTube(query, on_progress_callback=on_progress)
		yt.streams.filter(only_audio=True, adaptive=True, file_extension='mp4').order_by('abr').desc().first().download(music_dir)
		print('Getting '+title+'...', ':|')
		# yt.streams.filter(only_audio=True).first().download(output_path='C:\giz\music')
	
	music_dir=checkPath(music_dir)    
	queries = []
	t = True
	while t:
		lucky = 'ON' if luck else 'OFF'
		print('\n<< Enter a valid YouTube URL or the title of a video')
		print('<< [D]ownload the list, [P]laylist, or [Q]uit')
		print('<< or press [H] for a better explanation')
		print('<< -------------------------------------------------')
		print('<< Feeling Lucky is '+lucky+' ([L]ucky Toggle)')
		print('<< Downloading to: '+music_dir+' :: [C]hange')
		
		query = input('\n>> ')

		if query == 'c':
			print('<< Change download directory:')
			music_dir=checkPath(input('>> '))
			print('<< Directory changed: '+music_dir)
			
		elif query == 'h':
			f=open(dir_path+'\\README.txt', 'r')
			print('\n[HELP]\n', f.read(), '\n[END]\n')
			f.close()
		
		elif query == 'q':
			t = False
			print('Enjoy!')
			sleep(1)
			ex()
		
		elif query == 'd':
			for q in queries:
				url, title = q[0], q[1]
				get_vid(url, title)
				del q
		
		elif query == 'l':
			luck = not luck
			
		elif query == 'p':
			print('\n<< URL of a playlist or a video from a playlist')
			query = input('\n>> ')
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
				print('\n<< Searching... Please wait.')
				title = YouTube(query).title
				queries.append((query, title))
				print(title+' queued')
			else:
				print('\n<< Searching... Please wait.')
				s = Search(query)
				if luck:
					url = 'https://www.youtube.com/watch?v='+str(s.results[0].video_id)
					queries.append((url, s.results[0].title))
					print('\n>>> '+s.results[0].title+' queued <<<\n')
				else:
					print(str(min(len(s.results), results))+' results:')
					for i, vid in enumerate(s.results):
						if i <= (results-1):
							print('['+str(i+1)+'] '+vid.title+' ('+str(datetime.timedelta(seconds=vid.length))+')')
					query = input('\n>> ')
					url = 'https://www.youtube.com/watch?v='+s.results[int(query)-1].video_id
					queries.append((url, s.results[int(query)-1].title))
					print('\n>>> '+s.results[int(query)-1].title+' queued <<<\n')


if __name__ == '__main__':
    main()
