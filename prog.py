from bs4 import BeautifulSoup
import urllib.request

req = urllib.request.Request('http://pokemondb.net/sprites', headers={'User-Agent': 'Mozilla/5.0'})
pdx_html = urllib.request.urlopen(req).read()

soup = BeautifulSoup(pdx_html).prettify().encode('UTF-8')

#get everything in this format (a class="ent-name")
# 1-<a class="ent-name" 
# 2- download sprite < href="/sprites/aggron">
#
# use some github lib to batch upload

