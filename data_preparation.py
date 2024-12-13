# import json
# import pandas as pd
# import numpy as np

# # def load_data(ingredients_path, recipes_path):
# #     with open(ingredients_path) as file:
# #         ingredients = json.load(file)
# #     with open(recipes_path) as file:
# #         recipes = json.load(file)
# #     return ingredients, recipes

# def load_data(ingredients_path, recipes_path):
#     # Open ingredients file
#     with open(moods_path, encoding='utf-8') as file:
#         moods = json.load(file)
    
#     # Open recipes file
#     with open(recipes_path, encoding='utf-8') as file:
#         recipes = json.load(file)

#     return ingredients, recipes

# def prepare_features(ingredients, recipes):
#     all_ingredients = list(ingredients.keys())
#     cocktails_features = {recipe['name']: np.zeros(len(all_ingredients), dtype=int) for recipe in recipes}
#     for recipe in recipes:
#         for ingredient in recipe['ingredients']:
#             if 'ingredient' in ingredient and ingredient['ingredient'] in all_ingredients:
#                 index = all_ingredients.index(ingredient['ingredient'])
#                 cocktails_features[recipe['name']][index] = 1
#     return pd.DataFrame.from_dict(cocktails_features, orient='index', columns=all_ingredients)


# def save_features(df, path='cocktail_features.csv'):
#     df.to_csv(path)

# if __name__ == "__main__":
#     ingredients_path = 'ingredients.json'
#     recipes_path = 'recipes.json'
#     ingredients, recipes = load_data(ingredients_path, recipes_path)



import json
import pandas as pd
import numpy as np

def load_data(ingredients_path, recipes_path, moods_path):
    # Open ingredients file
    with open(ingredients_path, encoding='utf-8') as file:
        ingredients = json.load(file)
    
    # Open recipes file
    with open(recipes_path, encoding='utf-8') as file:
        recipes = json.load(file)
    
    # Open moods file
    with open(moods_path, encoding='utf-8') as file:
        moods = json.load(file)

    return ingredients, recipes, moods

def prepare_features(ingredients, recipes):
    # Extract the list of ingredients from the ingredients data
    all_ingredients = list(ingredients.keys())

    # Prepare a feature matrix where each cocktail has a vector of 1s and 0s for ingredients
    cocktails_features = {recipe['name']: np.zeros(len(all_ingredients), dtype=int) for recipe in recipes}
    
    # Fill the feature matrix
    for recipe in recipes:
        for ingredient in recipe['ingredients']:
            if 'ingredient' in ingredient and ingredient['ingredient'] in all_ingredients:
                index = all_ingredients.index(ingredient['ingredient'])
                cocktails_features[recipe['name']][index] = 1

    return pd.DataFrame.from_dict(cocktails_features, orient='index', columns=all_ingredients)

def save_features(df, path='cocktail_features.csv'):
    # Save the features dataframe to a CSV file
    df.to_csv(path)

if __name__ == "__main__":
    # Define paths for the files
    ingredients_path = 'ingredients.json'
    recipes_path = 'recipes.json'
    moods_path = 'moods.json'

    # Load data from the files
    ingredients, recipes, moods = load_data(ingredients_path, recipes_path, moods_path)

    # Prepare the feature matrix for cocktails
    features_df = prepare_features(ingredients, recipes)

    # Save the feature matrix to a CSV file
    save_features(features_df)

    features_df = prepare_features(ingredients, recipes)
    save_features(features_df)
