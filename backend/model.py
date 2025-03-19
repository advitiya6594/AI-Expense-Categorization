import random

# Dummy ML model for categorization
def predict_category(description):
    categories = ["Groceries", "Restaurants", "Utilities", "Rent", "Transportation"]
    return random.choice(categories)
