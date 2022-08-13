/* This file serves as the container that holds all of the ingredients in the list. 
Importing necessary components:
 we need the IngredientToAdd in order to create the Ingredient to Add List 
 */ 

 import React from 'react';
 import IngredientToAdd from './IngredientToAdd';

 // maps over list(object) to return individual components, like the actual ingredient on the list
 const IngredientToAddList = ({ingredList}) => {
    return (
        <div>
            {ingredList.map(toAdd => {
                return (
                    <IngredientToAdd toAdd={toAdd} />
                )
            })}
        </div>
    );
 };
  
 export default IngredientToAddList;