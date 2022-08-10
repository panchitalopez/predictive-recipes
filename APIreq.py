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
search = input("Enter a food or recipe")
ingredients = input("Enter ingredients seperated by ','")
idNum = int(input("Enter number of recipes to output."))
while(idNum >= 10):
    idNum = input("Enter number of recipes to output.")
querystring = {"query":search,
               "includeIngredients":ingredients,
               "sort":"popularity"
               }
##                         ^ modify this parameter

##Inital API GET request to Recipe Search for list of  recipes
searchResults = requests.request("GET", url, headers=headers, params=querystring)



##Convert json to a dict so it's parseable
data = searchResults.json()

##Gets ids of recipes and stores them in idlist
idlist = []
allSteps = ""
for i in range(idNum):
    ids = data['results'][i]['id']
    idlist.append(str(ids))

##For each id: call analyzedInstructions endpoint and store just the steps seperated by "/n" in allSteps
for i in range(len(idlist)):
    url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/" + idlist[i] + "/analyzedInstructions"
    querystring = {"stepBreakdown": "true"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    datastep = response.json()
    if len(datastep):
        steps = datastep[0]["steps"]
        for j in steps:
            allSteps = allSteps + j["step"] + "\n"
print(allSteps)
file = open("steps.txt", "w")
file.writelines(allSteps)
file.close()










