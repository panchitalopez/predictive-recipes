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

// useState returns a stateful value (a component that holds some state)
// const [variable that holds the state, method used to update the state]

// Basic syntax for useState hook is like this: 
// const [ variable, setVariable ] = useState(<initState?>); 


// This is what will be displayed in the web browser: 
  const [ingredList, setIngredList] = useState(data);  
  return (
    <div className="App">
    <Header/> 
    <IngredientToAddList ingredList = {ingredList}/>
    <IngredientForm addIngredient={addIngredient}/>
    <RecipeForm /> 
  
    </div>
  );

  } 

export default App;
