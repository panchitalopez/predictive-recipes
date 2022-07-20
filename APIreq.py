import requests
import json

headers = {
	"X-RapidAPI-Key": "0369576e5bmsh492d05bb416cdb5p10406fjsn243cabb13c2e",
	"X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
}


url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/complexSearch"
##query for the GET Search Recipes request
querystring = {"query":"pasta"}


##API GET request to Recipe Search for recipes
response = requests.request("GET", url, headers=headers, params=querystring)


##Convert json to a dict so it's parseable
data = response.json()

##Gets id of recipe
ids = data['results'][1]['id']

##Makes another API request to Analyzed Instructions endpoint to get steps
id = str(ids)
url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/" + id + "/analyzedInstructions"
querystring = {"stepBreakdown":"true"}
response = requests.request("GET", url, headers=headers, params=querystring)

data = response.json()

##Saves steps in the form steps: {'number': , 'step':...}
steps = data[0]["steps"]
print(steps)










