import json
import glob
import pandas as pd
import numpy as np
import re

pattern = re.compile("\\b([0-9]+|g|ml|kg|cm|oz|fluid|cups|quarts|pound|bunch|bunches|free-range|jar|jarred|small|large|medium|teaspoons|teaspoon|tablespoon|tablespoons|x|cm|inch|fresh|of|the|for|a|to|garnish|plus|dashes|dash|sprig|juice|[^\u0000-\u007F]+)\\W", re.I)


def parseNutrition():
    allIngredients = []
    table = []
    categories = glob.glob('./raw-data/*')
    for category in categories:
        subCategories = glob.glob(category + '/*/recipes.json')
        for subCategory in subCategories:
            df = pd.read_json(subCategory)
            for recipe in df.columns:
                ingredients = df[recipe]['ingredients']
                ingredientjoined = ''
                for ingredient in ingredients:
                    ing = re.sub(pattern, '', ingredient).split(',')[0]
                    ing = ing.replace('(', '')
                    ing = ing.replace(')', '')
                    ing = ing.lower()
                    ing = re.sub(r'\w*\d\w*', '', ing).strip()
                    allIngredients += ing.split(' ')
                    ingredientjoined += (' ' + ing)

                row = dict(
                    category=category.split('/')[-1],
                    subCategory=subCategory.split('/')[-2],
                    recipe=recipe,
                    ingredients=ingredientjoined 
                )
                nutrition = df[recipe]['nutrition']
                for i, group in enumerate(nutrition[0]):
                    try:
                        row[group + 'Amount'] = float(nutrition[1][i].strip('g'))
                    except:
                        row[group + 'Amount'] = np.nan
                    try:
                        row[group + 'Percent'] = float(nutrition[2][i].strip('%'))
                    except:
                        row[group + 'Percent'] = np.nan
                table.append(row)
    df = pd.DataFrame(table)
    df.to_json('./parsed-data/nutrition.json')
    f = open('./parsed-data/ingredients.json', 'w+')
    print(len(allIngredients))
    print(len(np.unique(allIngredients)))
    json.dump(list(np.unique(allIngredients)), f)
    f.close()

    
