import urllib.request
import re
from bs4 import BeautifulSoup


artista = input ('Escriba un artista o banda:')
cancion = input('Escriba una cancion')

url = 'https://www.azlyrics.com/lyrics/' + artista + '/' + cancion + '.html'
print ('Abriendo sitio...')


try:

	fhandler = urllib.request.urlopen(url)

except urllib.error.HTTPError:
	print ('No pudo encontrarse el recurso')

else :
	html = fhandler.read()
	soup = BeautifulSoup(html,'html.parser')
	tags = soup.find_all('div')


	tagslist = list(tags)

	contador = 0 

	for tag in taglist:
		contador +=1
		clase = tag.get('class',None)


		if clase is not None:
			if 'ringtone' in clase:
				break
	for hijo in taglist[contador].children:
		if hijo.strong is not None:
			print(hijo.string)	

