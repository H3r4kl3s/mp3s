#! /usr/bin/env python3

import sys, os
import glob
import string
import eyed3
import time

args = sys.argv[1:]

#Substitui o - dos argumentos por um espaço
i = 0
for a in args:
	args[i] = a.replace('-', ' ')
	i+=1
	
class Song:
	def __init__(self, song, artist, album, genre, num):
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
		
		if '(Official' in self.song_name or '(official' in self.song_name or '[official' in self.song_name or '[OFF' in self.song_name:
			self.song_name = self.song_name.split('(')[0]	
	
	def metadata(self):
		self.song.tag.title = self.song_name
		self.song.tag.artist = self.artist
		self.song.tag.album = self.album
		self.song.tag.genre = self.genre
		self.song.tag.track_num = self.num
		
		self.song.tag.save()

n = 1

#Se houver
while True:
		
	#Musica mais antiga
	arq = min(glob.glob('*.mp3'), key=os.path.getctime)

	#Se o mais antigo não tiver sido alterado
	if '-' in arq:
		try:
			#Altera Metadata
			Musica = Song(arq, args[0], args[1], args[2], n)
			Musica.filter_name()
			Musica.metadata()
					
			#Renomeia arquivo
			os.rename(arq, Musica.song_name+'.mp3')
					
			print('\033[96m' + arq + '\033[0m', '---->','\033[92m' + Musica.song_name+'.mp3' + '\033[0m')
			
			#Proxima musica		
			n+=1
		except:
			break
				
	else:
		break
		
print('\n')
print('\033[93m' + 'Artist: ' + '\033[0m','\033[97m' + args[0]+'\033[0m')
print('\033[93m' + 'Album: ' + '\033[0m','\033[97m' + args[1]+'\033[0m')
print('\033[93m' + 'Genre: ' + '\033[0m','\033[97m' + args[2]+ '\033[0m')
