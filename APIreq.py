import requests
import json


##IMPORTANT FOR LOCAL RUN
##Get your rapid api key and host from https://rapidapi.com/spoonacular/api/recipe-food-nutrition/
##After logging in with GitHub click the subscribe to test and the free option
##The header parameters are in any of the sample requests
headers = {

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










