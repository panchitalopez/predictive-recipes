/* 
Form that will: 
1. allow for a user to input an entry 
2. Click on submit button and have a function to add the entry to the list.  
- Logically: Have to keep track of the changes as we go as well as if the input changes. 

Form Logic

There are four main things that we need to have to make our forms work:

1. Local state (usingthe useState() hook)
2. Our form component with an input value that is assigned to the aligning variable
3. A function that handles the state’s changes
4. A function to handle the form submission 
*/ 

import React, { useState } from 'react';

const IngredientForm = ({ addIngredient }) => {
// useState returns a stateful value (a component that holds some state)
// const [variable that holds the state, method used to update the state]
// Initial state = empty so we put "" 
// Input value should = state variable. Here, it is userInput 
    const [ userInput, setUserInput ] = useState(''); 

    // e is an event handling function which allows variable to interact with the object 
    // when user types in the entry box, it will update to most recent input 
    const handleChange = (e) => {
        setUserInput(e.currentTarget.value)
    }
    
    // as the "submit" button is pressed this will add the event into the array 
    const handleSubmit = (e) => {
        e.preventDefault(); //preventDefault is typically used in forms 
        addIngredient(userInput);
        setUserInput(""); //resets to empty string once submitted 
    }
    return (
        <form onSubmit={handleSubmit}>
            <input value={userInput} type="text" onChange={handleChange} placeholder="Enter ingredient..."/>
            <button>Add ingredient</button>  
        </form>
    );
};

export default IngredientForm;
