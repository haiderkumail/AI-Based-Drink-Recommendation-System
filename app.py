import streamlit as st
import json
from recommendation_engine import recommend_cocktails, recommend_cocktails_by_ingredient

# Load the mood-to-cocktail mapping from the moods.json file
def load_mood_cocktails():
    with open('moods.json', encoding='utf-8') as f:
        return json.load(f)

# Load recipes from the 'recipes.json' file
with open('recipes.json', encoding='utf-8') as f:
    recipes_data = json.load(f)['recipes']

# Load mood-cocktail mappings
mood_cocktail_mapping = load_mood_cocktails()

st.title('AI Cocktail and Drinks Assistant')

# Input from the user
user_preference = st.text_input('Enter your preferred ingredient, cocktail name, or mood (e.g., "Negroni", "Gin", "Happy"):').strip()

if user_preference:
    user_preference_lower = user_preference.lower()  # Convert input to lowercase for case-insensitive matching

    # Check if the user input is a mood
    if user_preference_lower in mood_cocktail_mapping:
        # If mood is matched, recommend cocktails based on the mood
        recommended_cocktails = mood_cocktail_mapping[user_preference_lower]
        st.subheader(f"Recommended Cocktails for your mood: {user_preference.capitalize()}")
        for cocktail in recommended_cocktails:
            st.markdown(f"- {cocktail}")
    else:
        # If the user input is not a mood, process it as an ingredient or cocktail name
        recommended_cocktails = []

        # Try to find cocktails by ingredient (partial match)
        cocktails_by_ingredient = recommend_cocktails_by_ingredient(user_preference, recipes_data)
        if cocktails_by_ingredient:
            recommended_cocktails.extend(cocktails_by_ingredient)

        # Try to find cocktails by name (partial match)
        cocktails_by_name = recommend_cocktails(user_preference, recipes_data)
        if cocktails_by_name:
            recommended_cocktails.extend(cocktails_by_name)

        # Remove duplicates by converting the list to a set and back to a list
        recommended_cocktails = list(set(recommended_cocktails))

        # Display recommended cocktails
        if recommended_cocktails:
            st.subheader("Recommended Cocktails:")
            for cocktail in recommended_cocktails:
                st.markdown(f"- {cocktail}")
        else:
            st.write("No recommendations found. Try another ingredient, cocktail name, or mood.")
else:
    st.write("Please enter a mood, ingredient, or cocktail name to get recommendations.")



