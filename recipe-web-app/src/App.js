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

const axios = require("axios");
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


    // First API call to complexSearch to get array of food items
    // const callAPI = (options) => {
    function callAPI(options) {
        var id_List = "";
        axios.request(options).then(function (response) {
            console.log(response.data.results);
            for (let i = 0; i < response.data.results.length; i++) {
                id_List = id_List.concat(" ", String(response.data.results[i].id));
            }
            setIdList(id_List);
            console.log(id_List)
            return id_List;
        }).catch(function (error) {
            console.error(error);
        });
        return id_List;
    }
    function getAllSteps(id) {
        let aUrl = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/'+ id +'/analyzedInstructions';
        const options2 = {
            method: 'GET',
            url: aUrl,
            params: {stepBreakdown: 'true'},
            headers: {
                "X-RapidAPI-Key": "0369576e5bmsh492d05bb416cdb5p10406fjsn243cabb13c2e",
                "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
            }
        };
        var steps = "";
        console.log(options2);
        axios.request(options2).then(function (response2) {
            console.log(response2.data[0].steps);
            for(let i =0; i < response2.data[0].steps.length; i++) {
                steps = steps.concat(response2.data[0].steps[i].step);
            }
            console.log(steps);
            return steps;
        }).catch(function (error) {
            console.error(error);
        });
        return steps;
    }

// useState returns a stateful value (a component that holds some state)
// const [variable that holds the state, method used to update the state]

// Basic syntax for useState hook is like this: 
// const [ variable, setVariable ] = useState(<initState?>); 


// This is what will be displayed in the web browser: 
    const [ingredList, setIngredList] = useState(data);
    const [idList, setIdList] = useState([]);
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
        let query = recipeSearch.buildQuery()
        console.log(query);

        var id_List = "";
        var ArrayIDs;
        // Query the API to get a String of food IDs
        axios.request(query).then(function (response) {
            console.log(response.data.results);
            for (let i = 0; i < response.data.results.length; i++) {
                console.log(response.data.results[i].sourceUrl);
                id_List = id_List.concat(" ", String(response.data.results[i].id));
            }
            id_List = id_List.slice(1);
            ArrayIDs = id_List.split(" ");
            setIdList(ArrayIDs);
        }).catch(function (error) {
            console.error(error);
        });
        let idListClone = JSON.parse(JSON.stringify({idList}));
        console.log(idListClone.idList);
        // Loops through list of ids and prints steps in the console
        for (let x = 0; x < idListClone.idList.length; x++) {
            getAllSteps(idListClone.idList[x]);

        }
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
                        <div>
                            <label>Recipe Ingredients
                                <input
                                    type="text"
                                    name="ingredients"
                                    placeholder="Enter ',' separated list"
                                    defaultValue={recipe.ingredients}
                                    onChange={handleChange}
                                />
                            </label>
                            <button onClick={handleSubmit}>Submit Recipe Info</button>
                        </div>
                    </form>
                    {/*<IngredientForm addIngredient={addIngredient}/>*/}
                    {/*<IngredientToAddList ingredList = {ingredList}/>*/}
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
