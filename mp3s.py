#! /usr/bin/env python3

import sys, os
import glob
import string
import eyed3
import time
import junk

args = sys.argv[1:]

#Changes - in the arguments for blank spaces
i = 0
for a in args:
	args[i] = a.replace('-', ' ')
	i+=1
	
class Song:
	def __init__(self, song, artist, album, genre, num):
		#File attributes
		self.song = eyed3.load(song)
		self.song_name = song
		self.artist = artist
		self.album = album
		self.genre = genre
		self.num = num
	
	def filter_name(self):
		if ' - ' in self.song_name:
			self.song_name = self.song_name.split(' - ')[1]
	
		if '-' in self.song_name:
			self.song_name = self.song_name.split('-')[0]
		
		for a in junk.junk:
			if a in self.song_name:
				self.song_name = self.song_name.split(a)[0]
	
	def metadata(self):
		#Sets the metadata tags
		self.song.tag.title = self.song_name
		self.song.tag.artist = self.artist
		self.song.tag.album = self.album
		self.song.tag.genre = self.genre
		self.song.tag.track_num = self.num
		
		self.song.tag.save()


n = 1	#File counter
while True:
		
	#oldest file
	arq = min(glob.glob('*.mp3'), key=os.path.getctime)

	#if the oldest file has not been already renamed by mp3s
	if '-' in arq:
		try:
			#Changes Metadata
			Musica = Song(arq, args[0], args[1], args[2], n)
			Musica.filter_name()
			Musica.metadata()
					
			#Renames file
			os.rename(arq, Musica.song_name+'.mp3')
					
			print('\033[96m' + arq + '\033[0m', '---->','\033[92m' + Musica.song_name+'.mp3' + '\033[0m')
			
			#Next file
			n+=1
		except:
			break
				
	else:
		break
		
print('\n')
print('\033[93m' + 'Artist: ' + '\033[0m','\033[97m' + args[0]+'\033[0m')
print('\033[93m' + 'Album: ' + '\033[0m','\033[97m' + args[1]+'\033[0m')
print('\033[93m' + 'Genre: ' + '\033[0m','\033[97m' + args[2]+ '\033[0m')
