/* 
Form to submit for a recipe search by recipe name
*/
import IngredientForm from './IngredientForm';

import React, { useState } from "react";
const RecipeInput = require('./RecipeInput');

export default function RecipeMakerForm() {

    const [recipe, setRecipe] = useState({
        name: "",
        ingredients: ""
    });

    const handleChange = (event) => {
        setRecipe({ ...recipe, [event.target.name]: event.target.value });
    };

    const handleSubmit = (event) => {
        // prevents the submit button from refreshing the page
        event.preventDefault();
        console.log(recipe);
        const recipeSearch = new RecipeInput(recipe.name, recipe.ingredients)
    };

    return (
        <div>
            <form onSubmit={handleSubmit}>
                <div>
                    <h2>Recipe Form</h2>
                </div>
                <div>
                    <input
                        type="text"
                        name="name"
                        placeholder="Enter recipe name"
                        value={recipe.name}
                        onChange={handleChange}
                    />
                    <button>Submit Recipe Info</button>
                </div>
            </form>
        </div>
    );
}

  