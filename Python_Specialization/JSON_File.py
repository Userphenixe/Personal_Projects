import urllib.request
import json
# Import WEB Data as a JSON file, store it as a dictionary
liste = list()
link = input("Veuillez entrez le nom du site:")
data = urllib.request.urlopen(link)
js = json.load(data)
# Iterating the dictionary and store the 'count' element in a liste, then printing the sum of the elements in the list
for i in js['comments']:
    liste.append(i['count'])
print(sum(liste))