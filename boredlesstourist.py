#Recommendation Engine for where we should go

# Where we are going 
destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "Sao Paulo, Brazil", "Cairo, Egypt"]

#test travelers
#This is a traveler (a user of The Boredless Tourist application) whose name is Erin Wilkes who likes historical buildings and art. 
# Erin is in China right now, hopefully we can find some good places to show her.
test_traveler = ["Erin WIlkes", "Shanghai, China", ["historical site", "art"]]


#function for suggestions
def get_destination_index(destination):
  
  destination_index  = destinations.index(destination)

  return destination_index

#access traveler list index for traveler location
def get_traveler_location(traveler):
  
  traveler_destination = traveler[1]

  traveler_destination_index = get_destination_index(traveler_destination)

  return traveler_destination_index

test_destination_index = get_traveler_location(test_traveler)

#test the index of our test traveler
print(test_destination_index)