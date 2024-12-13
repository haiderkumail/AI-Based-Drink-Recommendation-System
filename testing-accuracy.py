import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import CountVectorizer

# Load the JSON data (Make sure the file path is correct)
df = pd.read_json('recipes.json')

# Extract the 'name' and 'ingredients' from the 'recipes' column
names = []
ingredients_list = []

for recipe in df['recipes']:
    names.append(recipe['name'])  # Extract the name of the cocktail
    ingredients = [ingredient['ingredient'] for ingredient in recipe['ingredients']]  # Extract ingredients
    ingredients_list.append(' '.join(ingredients))  # Join ingredients as a single string

# Create new columns in the dataframe
df['name'] = names
df['ingredients'] = ingredients_list

# Now you can use the 'ingredients' column as features
X = df['ingredients']  # Features are the ingredients (text data)
y = df['name']  # Target is the 'name' (cocktail name)

# Text vectorization
vectorizer = CountVectorizer()
X_text = vectorizer.fit_transform(X)

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X_text, y, test_size=0.2, random_state=42)

# Initialize and train the model
model = MultinomialNB()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy * 100:.2f}%')
