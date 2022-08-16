var searchQuery =
    {
        recipeName: "",
        recipeIngredients: "",
        numResults: 5
    };

var querystring = {"query":searchQuery.recipeName,
    "includeIngredients":searchQuery.recipeIngredients,
    "sort":"popularity"
};


module.exports = {searchQuery};

// Class for the recipe search query
class RecipeInput {
    constructor(name = "", ingredients = "", results = 5) {
        this.name = name;
        this.ingredients = ingredients;
        this.results = results;
    }
// GETTERS
    getName() {
        return this.name;
    }

    getIngredients() {
        return this.ingredients;
    }

    getResults() {
        return this.results;
    }

    // Function to build searchquery string
    buildQuery() {
        const options = {
            method: 'GET',
            url: 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/complexSearch',
            params: {
                query:this.name,
                includeIngredients:this.ingredients,
                addRecipeInformation: 'true',
                sort:"popularity"
            },
            headers: {
                "X-RapidAPI-Key": "0369576e5bmsh492d05bb416cdb5p10406fjsn243cabb13c2e",
                "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
            }
        };
        return options;
    }

}
module.exports = RecipeInput;
