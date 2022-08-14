
import requests
import random
import urllib.parse





api_key = 'AIzaSyA6PlZk4J8p6s8Nfm_p1nX58Lk6gOyMYX0'
food_places = {}

address = str(input(("where you at:\n")))
lat_and_lon_url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(address) +'?format=json'

get_lon_and_lat = requests.get(lat_and_lon_url).json()

latitude = (get_lon_and_lat[0]["lat"])
longitude = (get_lon_and_lat[0]["lon"])

radius = float(input("how many miles you willing to walk;\n"))


what_they_want = str(input(("what do you want:\n")))
restaurants_url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=' + latitude + '%2C' + longitude +'&radius=' + str(radius * float(1609.0)) + '&type=restaurant&keyword=' + what_they_want + '&key=' + api_key

data = {}
headers = {}
food_places = {}

get_restaurants = requests.request("GET", restaurants_url)
get_restaurants_json = get_restaurants.json()



i = 0 
for i in range(len(get_restaurants_json['results'])):
	food_places[i] = get_restaurants_json['results'][i]['name']
	i+=1


print(random.choice(food_places))


#print(get_resturants.text)
