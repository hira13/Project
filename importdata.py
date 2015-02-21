import requests 
#gets the data from IUCN website
result = requests.get("http://www.iucnredlist.org/search/link/54e81cb0-ebeac44e")

from bs4 import BeautifulSoup
  	#sets soup to scrap the site 
  	soup = BeautifulSoup(result.content)
  	#finds the species names with the id 
  	film_pane = soup.find(id='searchResults')
  	#finds the spceis names with the id 
  	name_li = film_pane.find_all("li")
  	#loop created to print and add the species names 
  	for li in name_li:
  		div = li.find_all("div", class_="desc")
  		name = div.find_all("a", class_="title")
  		spname = name.find_all("span", class_="sciname")
  		print spname
  	#opens a new text file to save the species names 
  	listsp = open('species_list.txt', 'w')
  	#writes all the names out 
  	listsp.write(all_names)
  	#closes the list 
  	listsp.close()

	Print: "List of species in Canidae Family:"
