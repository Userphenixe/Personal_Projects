import urllib.request
import warnings
import bs4
from bs4 import BeautifulSoup
warnings.filterwarnings("ignore", category=bs4.XMLParsedAsHTMLWarning)
# Using the BeautifulSoup and Warning Libraries to Retrieve XML web data
liste = list()
link = input("Veuillez entrez le nom du site:")
data = urllib.request.urlopen(link)
format = BeautifulSoup(data, "html.parser")
tags = format('count')
for i in tags:
    j = i.getText()
    liste.append(int(j))
print(sum(liste))