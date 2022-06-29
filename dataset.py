import pandas as pd
import string
import numpy as np
import csv

df = pd.read_csv('RecipeNLG_dataset.csv')
# Reads dataset from file into DataFrame df

tokens = '\n'.join(df['NER'])
print(type(tokens))
print(tokens[2])
# Checking whether it was read properly

##############################################################
#
#  Identifying methods for shrinking dataset:
#
#  Remove recipes with "step" to avoid cross-step references
df = df[df['ingredients'].str.contains("step|Step") == false]

#  Remove recipes with mix-all which might skew model to mix-all recipes
df = df[df['ingredients'].str.contains("all|All") == false]

#  Remove recipes with indirect instructions (mix "first, nextlast, both")
df = df[df['ingredients'].str.contains("first|last") == false]

#  Remove "as directed" recipes as this should not be a possibility (could mess up predictive text model)**
df = df[df['ingredients'].str.contains("as directed") == false]

#  Remove * as alternative ingredients are marked in directions with a *and are not accounted for (could mess up predictive text model)** and
df = df[df['ingredients'].str.contains("*") == false]

#  Remove recipes with few ingredients, directions, titles

#  Manually define dataset to use for "learning" to avoid language misunderstandings
df.to_csv('filtered.zip', index=False)
