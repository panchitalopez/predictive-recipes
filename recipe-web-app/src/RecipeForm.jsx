/* 
Left off here, this part doesn't fully work.
This is the form for the recipe list, I tried to use JSX to implement it which would later be converted
Can delete if not needed since we said the ingredients would be independent of the predictive model. 
*/ 

import React from 'react';
import { useState } from "react";
export default function RecipeMakerForm() {
    const [recipeInfo, setRecipeInfo] = useState({
        name: "",
        steps: "",
      });

    const handleChange = (event) => {
    setRecipeInfo({ ...recipeInfo, [event.target.name]: event.target.value });
  };

    const handleSubmit = (event) => {
    // prevents the submit button from refreshing the page
    event.preventDefault();
    console.log(recipeInfo);
  };

    return (
      <div>
        <form>
          <div>
            <h2>Recipe Form</h2>
          </div>
          <div>
            <input
              type="text"
              name="name"
              placeholder="Enter recipe name"
              value={recipeInfo.name}
              onChange={handleChange}
            />
          </div>
          <div>
            <input
              type="steps"
              name="Recipe Steps"
              placeholder="Enter recipe steps"
              value={recipeInfo.steps}
              onChange={handleChange}
            />
            <button>Submit Recipe Info</button>
          </div>
        </form>
      </div>
    );
  }
  