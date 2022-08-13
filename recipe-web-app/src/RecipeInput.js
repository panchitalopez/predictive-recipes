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
        let querystring = {
            "query":this.name,
            "includeIngredients":this.ingredients,
            "sort":"popularity"
        };
        return querystring
    }
}
module.exports = RecipeInput;
