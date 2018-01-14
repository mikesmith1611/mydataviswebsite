import pandas as pd
import json
dfNutririon = pd.read_json('./parsed-data/nutrition.json')

ingredients = pd.read_json('./parsed-data/ingredients.json')[0]
