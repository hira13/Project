
#ID of the URL for the species threat that page its on 
ID = 6924,3753,3744,3745,3746,3755,3747,3748,4248,4819,5953,6923,12436,14925,15642,6929,41586,6927,6928,6925,6926,20468,22780,22781,23049,23050,23060,23051,23061,899,41587,23052,23053,23059,23062,41588

#open a new file to add the urls 
url = open(urllist.txt,'w')

#creating a loop to insert all the IDs into the URL to download the html to scrape for threat numbers 
for lines in ID:
	URL = "http://www.iucnredlist.org/details/classify/%s/0" %lines
	print URL
	#will add the url to the new file 
	if URL is None:
		print URL
	else:
		url.write(URL)

#closes the file 
url.close()

##################Code to get the species threat and use that to make dictionary#################
#opens the list of species with the url 
url = open(urllist.txt,'r')
#gets results from the website 
result = requests.get('url')
from bs4 import BeautifulSoup: 

#saves the website information as content 
content = BeautifulSoup(result.content)

#makes the content into a string 
aa = str(content)

#splits the lines so that you can run regex
bb = aa.splitlines()

#pattern that will search for the specific speceis names 
###### NEED NEW SEARCH TERM ##########
### starting point r"^<fieldset class="accordion-data">"

pattern = r"\"sciname\">(\w+ \w+)</span>"

#A for loop that searches for the names in the file 
for lines in bb:
    name1 = re.search(pattern, str(lines), re.I)
    if name1 is None:
        continue
    else:
        species = name1.group(1)
        print threat

