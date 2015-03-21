#this creates my dictionary to use for looking up the species 
dict = {'Atelocynus microtis':(2,2.1,2.3,5,5.1,5.3,8),'Canis adustus':(5,5.1),'Canis aureus':0,'Canis latrans':0,'Canis lupus':(2,2.3,5,5.1),'Canis mesomelas':(5,5.1),'Canis rufus':(4,4.1,5,5.1,8),'Canis simensis':(2,2.1,2.3,4,4.1,5,5.1,6,6.2,8,8.1),'Cerdocyon thous':0,'Chrysocyon brachyurus':(2,2.1,4,4.1,5,5.1,8.1),'Cuon alpinus':(1,1.1,2,2.1,5,5.1,7,7.3,8,8.1,8.2),'Dusicyon australis':(5,5.1),'Lycaon pictus':(1,1.1,2,2.1,2.3,3,3.1,3.2,4,4.1,5,5.1,6,6.1,8,8.1,11,11.3),'Nyctereutes procyonoides':(4,4.1,5,5.1,8,8.2,9,9.2,9.3),'Otocyon megalotis':(5,5.1,8,8.2,11,11.2),'Pseudalopex culpaeus':(5,5.1),'Pseudalopex fulvipes':(1,1.4),'Pseudalopex griseus':(5,5.1),'Pseudalopex sechurae':(1,1.1,2,2.1,5,5.1),'Pseudalopex vetulus':(2,2.3),'Speothos venaticus':(1,1.1,2,2.1,2.2,2.3,5,5.1,8,8.1),'Urocyon cinereoargenteus':(1,1.4,1.5,1.9,3,3.6,14,14.1,14.2,14.5),'Urocyon littoralis':(8,8.1),'Vulpes bengalensis':(1,1.2,2,2.1,2.3,5,5.1,8,8.2),'Vulpes cana':(6,8),'Vulpes chama':(5,5.1,9,9.3),'Vulpes corsac':(2,2.3,5,5.1),'Vulpes ferrilata':(5,5.1),'Vulpes lagopus':(5,5.1,8,8.2,9,9.3),'Vulpes macrotis':(1,1.1,2,2.1,2.3,3.3,4.1,5),'Vulpes pallida':(2,2.1,2.3,3,3.1,4,4.1,5,5.1,11,11.1),'Vulpes rueppellii':(1,1.1,5,5.1,8),'Vulpes velox':(1,1.2,2,2.1,3,3.1,4,4.1,5,5.1,8),'Vulpes vulpes':0,'Vulpes zerda':(1,5.1)}

#this will ask the user for the name they want to search for 
name = raw_input("Species Name: ")

#this will search for the name of the species and print out the name and the threats 
for key,value in dict.iteritems():
	if key.startswith(name):
		print key,value
	else:
		key.ex

#this asks for the threat number to search for 
threat = raw_input("Threat Number: ")

#this will search the dictionaries for the values if the user wants to search for a species threat 
def search(values,searchFor):
    for key,value in dict.iteritems():
        if value = threat 
                print key,value
    else:
    	value.ex

#if the species threat is not in the dictionary it will add it 
#Not sure how to do this but got this so far 
for name in dict 
    dict[name]=values
    print dict 

#asks for new values to update the species 
name = raw_input("Name of Species you would like to update:")
threat = raw_input("Threat of species you'd like to update")
#update the dictionary with new threats 
dict.update({name:threat})