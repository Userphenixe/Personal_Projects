import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
# Importing the BeautifulSoup library to retrieve HTML web data.
liste = list()
link = input("Veuillez entrez le lien du site:")
handle = urllib.request.urlopen(link)
text = BeautifulSoup(handle, 'html.parser')
numbers = text('span')
for i in numbers:
    j = i.getText()
    liste.append(int(j))
print(sum(liste))