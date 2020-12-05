import requests # à installer via un pip install requests dans les CMD
from bs4 import BeautifulSoup
import json
import codecs
from pprint import pprint

# https://naruto.fandom.com/wiki/Category:Characters?from=S
# https://naruto.fandom.com/wiki/Samui
#url = f"https://naruto.fandom.com/wiki/Category:Characters"

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
personnages = []

for lettre in alphabet :
    url = f"https://naruto.fandom.com/wiki/Category:Characters?from={lettre}"
    page = requests.get(url)
    html = page.text
    soup = BeautifulSoup(html, "lxml")
    mydivs = soup.findAll("ul", {"class": "category-page__members-for-char"})[0].find_all('a')
    for i in range(0, len(mydivs), 2):
        peronnage = {}
        url = "https://naruto.fandom.com/wiki" + mydivs[i]["href"]
        name = mydivs[i]["title"]
        try:
            url_image = mydivs[i].img["data-src"]
        except:
            url_image = "pas d'image d'identité"
        peronnage['nom'] = name
        peronnage['url'] = url
        peronnage['image'] = url_image
        print(peronnage)
        personnages.append(peronnage)
pprint(personnages)
fichier = 'naruto.json'
#json_string = json.dumps(personnages, sort_keys=True, indent=4, ensure_ascii=False).encode('utf8')
#print(json_string)

with codecs.open(fichier, 'w', encoding='utf8') as json_file:
    json.dump(personnages, json_file, ensure_ascii=False)

