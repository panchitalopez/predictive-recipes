import requests
import json


##-----------------------------------------------Spoonacular API Call---------------------------------------------------
##IMPORTANT FOR LOCAL RUN
##Get your rapid api key and host from https://rapidapi.com/spoonacular/api/recipe-food-nutrition/
##After logging in with GitHub click the subscribe to test and the free option
##The header parameters are in any of the sample requests, paste key in the quotes
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
one = steps[0]["step"]
textquery = ""
for i in steps:
    textquery = textquery + i["step"] + "\n"
##-----------------------------------------------Meaningcloud API Call---------------------------------------------------
payload={
    'key': '8b38fc74a8a6e9be5b5eef2c7a768fd9',
    'lang': 'ENGLISH',
    'txt': 'YOUR TEXT HERE'
}

##response = requests.post(url, data=payload)









