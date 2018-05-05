import os
from collections import Counter

genres = set(["crime", "fantasy", "romance", "scifi"])
path = "C:/Users/Stefan Doehler/Documents/NN & Lang/genredetector/data"
for genre in os.listdir(path):
    if genre in genres:
    	words = []
    	for file in os.listdir(path + "/" + genre):
    		print(file)
    		with open(path + "/" + genre + "/" + file, encoding="utf8") as f:
    			words.extend(x.lower() for x in f.read().split())
    	counts = Counter(words)
    	print(genre, [(key, count) for key, count in counts.items() if 100 <= count <= 200])
    	break
    			


