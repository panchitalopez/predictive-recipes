// Importing necessary components: 

import RecipeForm from "./RecipeForm.jsx";

import './App.css';
// Three main components: Header, Ingredients, Form to submit ingredients 
//Importing the header: 
import Header from './Header';

//Importing the mock dataset: 
import data from './data.json';

//Importing hooks to be able to hold the mock dataset 
import React, { useState } from 'react';

//Importing the components to map: 
import IngredientToAddList from './IngredientToAddList';
import IngredientForm from './IngredientForm';
import RecipeInput from "./RecipeInput";

function App() {

    /*
    This adds entry via setIngredList which sets a new array.
    By allowing the addIngredient to have access to that state, a new array will successfully be created.
    Takes in the user input that’s from the form’s component state.
    Makes a copy of the list so it isn't directly affected.
    */

    const addIngredient = (userInput) => {
        let copy = [...ingredList];
        copy = [...copy, { id: ingredList.length + 1, task: userInput, complete: false }];
        setIngredList(copy);
    }

    // const getSteps = (options) => {
    //     axios.request(options).then(function (response) {
    //         console.log(response.data);
    //     }).catch(function (error) {
    //         console.error(error);
    //     });
    // }

// useState returns a stateful value (a component that holds some state)
// const [variable that holds the state, method used to update the state]

// Basic syntax for useState hook is like this: 
// const [ variable, setVariable ] = useState(<initState?>); 


// This is what will be displayed in the web browser: 
    const [ingredList, setIngredList] = useState(data);
    const [recipe, setRecipe] = useState({
        name: "",
        ingredients: ""
    });

    const handleChange = (event) => {
        const value = event.target.value;
        setRecipe({ ...recipe, [event.target.name]: value });
    };

    // On submission, creates a new object of type RecipeInput with the parameters for name and ingredients, then builds a Query using said parameters and calls API
    const handleSubmit = (event) => {
        // prevents the submit button from refreshing the page
        event.preventDefault();
        console.log(recipe);
        let recipeSearch = new RecipeInput(recipe.name, recipe.ingredients);
        console.log(recipeSearch.buildQuery());
    };

    return (
        <div className="App">
            <Header/>
            <div className ="row">
                <div className = "col">
                    {/*<RecipeForm />*/}
                    <form onSubmit={handleSubmit}>
                        <h2>Recipe Form</h2>
                        <label>Recipe Name
                            <input
                                type="text"
                                name="name"
                                placeholder="Enter recipe name"
                                defaultValue={recipe.name}
                                onChange={handleChange}
                            />
                        </label>
                        <label>Recipe Ingredients
                            <input
                                type="text"
                                name="ingredients"
                                placeholder="Enter ingredient list"
                                defaultValue={recipe.ingredients}
                                onChange={handleChange}
                            />
                        </label>
                        <button onClick={handleSubmit}>Submit Recipe Info</button>
                    </form>
                    <IngredientForm addIngredient={addIngredient}/>
                    <IngredientToAddList ingredList = {ingredList}/>
                </div>
                <div className = "input-container">
                    <div className ="input-steps">
                        <input
                            type="text"
                            id = "input"
                            placeholder = "Start typing recipe here..."
                        />
                    </div>
                </div>
            </div>
        </div>
    );

}

export default App;
