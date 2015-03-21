############### Script to pull out species names #############
import re
import requests 

#gets results from the website 
result = requests.get('http://www.iucnredlist.org/search/link/54e81cb0-ebeac44e')
from bs4 import BeautifulSoup 

#saves the website information as content 
content = BeautifulSoup(result.content)

#makes the content into a string 
aa = str(content)

#splits the lines so that you can run regex
bb = aa.splitlines()

#pattern that will search for the specific speceis names 
pattern = r"\"sciname\">(\w+ \w+)</span>"

#open a text file to save the output of the list
names  = open('species_list.txt', 'w')

#A for loop that searches for the names in the file 
for lines in bb:
    name1 = re.search(pattern, str(lines), re.I)
    if name1 is None:
        continue
    else:
        species = name1.group(1)
        #writes the names of the species in this line 
        names.write(species)
        print species
        


# Closes the file new text file 
names.close()


