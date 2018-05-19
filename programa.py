from letras import Letra
import urllib.request
import re
from bs4 import BeautifulSoup
import time
import sqlite3

class Programa:
    def __init__(self):
        self.url = 'https://www.azlyrics.com/lyrics/'
        self.fecha=time.strftime("%d/%m/%Y")
        self.con = sqlite3.connect("musica.db")
        self.cursor = self.con.cursor()
        
    def buscar(self,cancion,artista):
        letra=Letra(cancion,'',self.fecha)
        print ('Abriendo sitio=>')
        artista=artista.replace(' ','')
        cancion=cancion.replace(' ','')
        print (self.url+artista+'/'+cancion+'.html')
        try:
            fhandler = urllib.request.urlopen(self.url+artista+'/'+cancion+'.html')
        except urllib.error.HTTPError:
            print ('No pudo encontrarse el recurso')
        else :
            html = fhandler.read()
            soup = BeautifulSoup(html,'html.parser')
            tags = soup.find_all('div')
            taglist = list(tags)
            contador=0
            for tag in taglist:
                contador+=1
                clase=tag.get('class',None)
                if clase is not None:
                    if 'ringtone' in clase:
                        break
            for hijo in taglist[contador].children:
                if hijo.string is not None:
                    letra.letra+=hijo.string
            letra.letra=letra.letra.replace('\'','´')
            query='INSERT INTO letras(nombre_cancion,letra,fecha_busqueda) VALUES(\''+letra.nombre_cancion+'\',\''+letra.letra+'\',\''+letra.fecha_busqueda+'\')'
            self.cursor.execute(query)
            self.con.commit()
            print ('Registro insertado')
            
    def salir(self):
        self.cursor.close()
        self.con.close()
        return False


programa=Programa()
artista = input ('Escriba un artista o banda: ')
cancion = input('Escriba una cancion: ')
programa.buscar(cancion,artista)
programa.salir()
