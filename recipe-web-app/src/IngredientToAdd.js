//Single row(in this case, ingredient) from the list of ingredients
import React from 'react';
 
const IngredientToAdd = ({toAdd}) => {
   return (
       <div>
           {toAdd.task}
       </div>
   );
};
 
export default IngredientToAdd;