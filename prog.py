from bs4 import BeautifulSoup
import urllib

pokedex_url = urllib.urlopen('http://pokemondb.net/pokedex').read()
soup = BeautifulSoup(pokedex_url)

print soup