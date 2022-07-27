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
##                         ^ modify this parameter

##Inital API GET request to Recipe Search for list of  recipes
response = requests.request("GET", url, headers=headers, params=querystring)


##Convert json to a dict so it's parseable
data = response.json()

##Gets ids of recipes and stores them in idlist
idlist = []
allSteps = ""
for i in range(3):
    ids = data['results'][i]['id']
    idlist.append(str(ids))

##For each id: call analyzedInstructions endpoint and store just the steps seperated by "/n" in allSteps
for i in range(len(idlist)):
    url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/" + idlist[i] + "/analyzedInstructions"
    querystring = {"stepBreakdown": "true"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    datastep = response.json()
    steps = datastep[0]["steps"]
    for j in steps:
        allSteps = allSteps + j["step"] + "\n"

print(allSteps)











