#pylint:disable=C0301
#pylint:disable=W0603
#pylint:disable=W0613
#pylint:disable=W0621
#pylint:disable=C0103
#pylint:disable=C0116
import tkinter as tk
from pytube import YouTube as yt
from os.path import exists as file_exists

the_urls = ['https://m.youtube.com/watch?v=5mm163wWKL8', 'https://m.youtube.com/watch?v=6eFcSesrP6A', 'https://m.youtube.com/watch?v=61u2iwVV8oM']

debug = False

title_lbl, grabstream_lbl, video_lbl, dl_lbl = '', '', '', ''
myfont = ('Verdana', 6)
mysmallerfont = ('Verdana', 4)
audiodir = '/storage/emulated/0/Music/'
root = tk.Tk()
hand = ''
#root.geometry('500x300')
# Size of the window
#root.resizable(0, 0)

def progress_callback(stream, chunk, bytes_remaining):
	size = stream.filesize
	p = 0
	while p <= 100:
		# progress = p
		prog.config(str(p)+'%')
		p = percent(bytes_remaining, size)
		
def complete_callback(self, stream, file_handle):
	global dl_lbl
	dl_lbl[0].config('done')
	tk.Label(root, text=file_handle, width=100, font=myfont).pack()
	dl_lbl.pop(0)

def percent(tem, total):
	perc = (float(tem) / float(total)) * float(100)
	return perc

 def download():
	global title_lbl, grabstream_lbl, video_lbl, dl_lbl
	url = link_enter.get()
	if url != '':
		the_urls.append(url)
	for link in the_urls:
		url = yt(link, on_progress_callback=progress_callback, on_complete_callback=complete_callback)
		title_lbl = tk.Label(root, text=url.title, font=myfont)
		title_lbl.pack()
		stream = url.streams
		if debug:
			stream_lbl = tk.Text(root, height=3, width=100, font=myfont)
			stream_lbl.pack()
			stream_lbl.insert(1.0, stream)
		filtered = stream.filter(only_audio=True)
		if debug:
			filtered_lbl = tk.Text(root, height=3, width=100, font=myfont)
			filtered_lbl.pack()
			filtered_lbl.insert(1.0, filtered)
		video = filtered.first()
		grabstream_lbl = tk.Label(root, text='grabbing audio stream', width=100, font=myfont)
		grabstream_lbl.pack()
		#video_lbl = []
		#for key, val in video:
			#video_lbl.append(tk.Label(root, text=key+': '+val, width=100, font=mysmallerfont).pack())
		dl_lbl = []
		dl_lbl.append(tk.Label(root, text='downloading...', width=100, font=myfont).pack())
		video.download(output_path=audiodir)

tk.Label(root, text="Download Youtube videos for free", font=myfont).pack()
tk.Label(root, text="Paste your link here", font=myfont).pack()
link_enter = tk.Entry(root, width=70)
#link_enter.insert(0, the_url)
link_enter.pack()

tk.Button(root, text='Download', font=myfont, bg='green', command=download).pack()
prog = tk.Label(root, text='', width=100, font=myfont, fg='blue')
prog.pack()

root.mainloop()
