#Recommendation Engine for where we should go

# Where we are going 
destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "Sao Paulo, Brazil", "Cairo, Egypt"]

#test travelers
#This is a traveler (a user of The Boredless Tourist application) whose name is Erin Wilkes who likes historical buildings and art. 
# Erin is in China right now, hopefully we can find some good places to show her.
test_traveler = ["Erin WIlkes", "Shanghai, China", ["historical site", "art"]]
attractions = [[], [], [], [], []]


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


#function for adding attractions to attraction index
def add_attraction(destination, attraction): 
  destination_index = get_destination_index(destination)
  attractions[destination_index].append(attraction)
  return attractions


#attactions list
add_attraction("Los Angeles, USA", ["Venice Beach", ["beach"]])
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("Sao Paulo, Brazil", ["Sao Paulo Zoo", ["zoo"]])
add_attraction("Sao Paulo, Brazil", ["Patio do Colegio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])


#Lets find the best places to go for our travelers
def find_attractions(destination, interests):
  destination_index = get_destination_index(destination)
  attractions_in_city = attractions[destination_index]
  attractions_with_interest = []

#access the index and save to variable for next part 
  for possible_attraction in attractions_in_city:
    attraction_tags = possible_attraction[1]

#loop through lists to find interests that are same 
    for interest in interests:
      if interest in attraction_tags:
        attractions_with_interest.append(possible_attraction[0])
        break
          
  return attractions_with_interest

la_arts = find_attractions("Los Angeles, USA", ["art"])  

print(la_arts)


