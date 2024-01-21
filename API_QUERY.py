# %% [markdown]
# * Note: GDPR Compliance
# * Ensure compliance with GDPR principles:
# * 1. Lawfulness, fairness, and transparency
# * 2. Purpose limitation
# * 3. Data minimization (collect only necessary data)
# * 4. Accuracy
# * 5. Storage limitation
# * No personal data is handled.

# %%
import requests
import pandas as pd

# API endpoint for food data
url = "https://edamam-food-and-grocery-database.p.rapidapi.com/api/food-database/v2/parser"

# Query parameters including the ingredient ("CHAMPAGNE")
querystring = {"ingr": "CHAMPAGNE"}

# Headers with RapidAPI key and host
headers = {
    "X-RapidAPI-Key": "ec18763f1cmsh43624451fb1c86bp154c63jsn4725da5f0bc0",
    "X-RapidAPI-Host": "edamam-food-and-grocery-database.p.rapidapi.com"
}

# Make a GET request to the API
response = requests.get(url, headers=headers, params=querystring)

# Extract information about the top 10 products
top_10_products = response.json()['hints'][:10]

# Create a DataFrame with relevant data
df = pd.DataFrame([
    {
        'foodId': product['food']['foodId'],
        'label': product['food']['label'],
        'category': product['food']['category'],
        'foodContentsLabel': product['food'].get('foodContentsLabel', 'NaN'),
        'image': product['food'].get('image', 'NaN')
    }
    for product in top_10_products
])

# Save data to CSV file
csv_filename = 'top_10_products2.csv'
df.to_csv(csv_filename, index=False, encoding='utf-8')

print(f'The data has been saved to {csv_filename}')