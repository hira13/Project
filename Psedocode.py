#Get the information about a specific species from the smithsonian website (canidae)
	#hand write the name of the species or use requests.get to get the informatino from the site 
#compare the data against IUNC and download that information in ipython to store into a dictionary 
	#import requests
	#result = requests.get("name of site")
	#result
	#from bs4 import BeautifulSoup
		#soup = BeautifulSoup(result.content)
		#soup.find("a")
		#parse this information to extract what I need 
#Make a dictionary with all the information of the threats to that particular species 
	#store my data in threatdict={}
	#threatdict[currentSp]
	#currentSp = "Canis lupus"
	#threatdict[currentSp] = [1.2]
	#threatdict[currentSp]
	#if I want to add more information to the current species I am storing information for 
		#threatdict[currentSp].append(2.3)
		#threatdict[currentSp]
#Anyone can search the dictionary to see if a certain level of threath based on the ones assigned by IUNC is applicable to the 
#species they are interested in by 
	#1.6 in threatdict[currentSp]
	#the program will tell the user if this threat is present to this particular species 
#if not there is a loop that will allow the user to append the dictionary to include that threat 
	#if not currentthreat in threatdict[currentSp]:
	#current threat is an arbitrary number the user can assign to add to the list or search for it ex: 
		#1.6 in threatdict[currentSp]
		#currentthreat = 1.6
   	#threatdict[currentSp].append(currentthreat)
	#threatdict[currentSp]


