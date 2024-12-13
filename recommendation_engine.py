# # recommendation_engine.py
# import pandas as pd
# from sklearn.metrics.pairwise import cosine_similarity
# from data_preparation import load_data, prepare_features

# # Load and prepare data
# ingredients_path = 'ingredients.json'
# recipes_path = 'recipes.json'
# ingredients, recipes = load_data(ingredients_path, recipes_path)
# cocktails_df = prepare_features(ingredients, recipes)

# def calculate_similarity():
#     similarity_matrix = cosine_similarity(cocktails_df.values)
#     return pd.DataFrame(similarity_matrix, index=cocktails_df.index, columns=cocktails_df.index)

# def recommend_cocktails(cocktail_name, top_n=5):
#     similarity_matrix = calculate_similarity()
#     if cocktail_name not in similarity_matrix.index:
#         return f"No data for cocktail named '{cocktail_name}'."
#     similarities = similarity_matrix[cocktail_name]
#     recommended = similarities.sort_values(ascending=False)[1:top_n+1]
#     return recommended.index.tolist()


import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from data_preparation import load_data, prepare_features

# Load and prepare data
ingredients_path = 'ingredients.json'
recipes_path = 'recipes.json'
moods_path = 'moods.json' 
ingredients, recipes, moods = load_data(ingredients_path, recipes_path, moods_path)

# Function to prepare features based on recipes and ingredients
def prepare_features(ingredients, recipes):
    # Create a list of all the unique ingredients from the recipes
    all_ingredients = []
    for recipe in recipes:
        for ingredient in recipe['ingredients']:
            all_ingredients.append(ingredient['ingredient'])

    # Create a DataFrame where each row represents a cocktail and each column represents an ingredient
    ingredient_set = list(set(all_ingredients))
    cocktails_list = []

    for recipe in recipes:
        cocktail_ingredients = [ingredient['ingredient'] for ingredient in recipe['ingredients']]
        cocktail_features = [1 if ingredient in cocktail_ingredients else 0 for ingredient in ingredient_set]
        cocktails_list.append(cocktail_features)

    cocktails_df = pd.DataFrame(cocktails_list, columns=ingredient_set)
    cocktails_df['name'] = [recipe['name'] for recipe in recipes]
    return cocktails_df.set_index('name')


def calculate_similarity():
    similarity_matrix = cosine_similarity(cocktails_df.values)
    return pd.DataFrame(similarity_matrix, index=cocktails_df.index, columns=cocktails_df.index)


def recommend_cocktails(cocktail_name, recipes, top_n=5):
    recommended_cocktails = []

    # Loop through each recipe and check if the cocktail name partially matches
    for recipe in recipes:
        if cocktail_name.lower() in recipe['name'].lower():  # partial, case-insensitive match
            recommended_cocktails.append(recipe['name'])

    return recommended_cocktails


# Function to recommend cocktails based on an ingredient
def recommend_cocktails_by_ingredient(ingredient, recipes):
    recommended_cocktails = []

    # Iterate through each recipe in the list
    for recipe in recipes:
        # Loop through the ingredients of each recipe
        for ingredient_item in recipe['ingredients']:
            # Check if the ingredient matches partially (case-insensitive)
            if ingredient.lower() in ingredient_item['ingredient'].lower():
                recommended_cocktails.append(recipe['name'])  # Add recipe name to the list

    return recommended_cocktails


