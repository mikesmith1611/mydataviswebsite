from bs4 import BeautifulSoup
import re
import requests
import time
import json
import os
import numpy as np

def getCategories(url):

    r  = requests.get(url + '/recipes/')

    data = r.text

    soup = BeautifulSoup(data)
    categories = []
    for link in soup.find_all('a'):
        href = link.get('href')
        if href.startswith(url):
            categories.append(href)
    return categories

def getSubCategories(category):

    r  = requests.get(category)

    data = r.text

    soup = BeautifulSoup(data)
    recipes = []
    for link in soup.find_all('a'):
        href = link.get('href')
        if href.startswith(category):
            recipes.append(href)
    return recipes

def getRecipes(subCategory):
    r  = requests.get(subCategory)
    data = r.text
    soup = BeautifulSoup(data)
    recipes = []
    Nhash = 0
    for link in soup.find_all('a'):
        href = link.get('href')
        if href == '#':
            Nhash += 1
        if href is None or Nhash < 3:
            continue
        if href.startswith("/recipes/"):
            recipes.append(href)
    return recipes

def getIngredients(recipe):
    r  = requests.get(url + recipe)
    data = r.text
    soup = BeautifulSoup(data)
    ingredients = []
    mydivs = soup.findAll("div", { "class" : "recipe-ingredients" })
    for div in mydivs:
        lists = div.find_all('li')
        for row in lists:
            ingredient = row.text.strip()
            ingredient = re.sub(' +', ' ', ingredient)
            ingredients.append(ingredient)
    return ingredients


def getNutrition(recipe):
    r  = requests.get(url + recipe)
    data = r.text
    soup = BeautifulSoup(data)

    descriptions = []
    mydivs = soup.findAll("div", { "class" : "nutrition-item-desc" })
    for div in mydivs:
        text = div.text.strip()
        if text in descriptions:
            break
        descriptions.append(text)

    amounts = []
    mydivs = soup.findAll("div", { "class" : "nutrition-item-top" })
    for i, div in enumerate(mydivs):
        text = div.text.strip()
        if text == '-':
            text = None
        if i == len(descriptions):
            break
        amounts.append(text)

    percents = []
    mydivs = soup.findAll("div", { "class" : "nutrition-item-bottom" })
    for i, div in enumerate(mydivs):
        text = div.text.strip()
        if text == '-':
            text = None
        if i == len(descriptions):
            break
        percents.append(text)

    return [descriptions, amounts, percents]


url = "http://www.jamieoliver.com"

categories = getCategories(url)

data = {}
for category in categories:
    categoryName = category.split('/')[-2]
    data[categoryName] = {}
    subCategories = getSubCategories(category)
    os.system('mkdir raw-data/' + categoryName)
    for subCategory in subCategories:
        subCategoryName = subCategory.split('/')[-1]
        if subCategoryName == '':
            subCategoryName = subCategory.split('/')[-2]
        directory = 'raw-data/{0}/{1}'.format(categoryName, subCategoryName)
        r = os.system('mkdir {0}'.format(directory))
        if os.path.exists('{0}/recipes.json'.format(directory)):
            continue
        data[categoryName][subCategoryName] = {}
        time.sleep(1)
        recipes = getRecipes(subCategory)
        for recipe in recipes:
            recipeName = recipe.split('/')[-2]
            time.sleep(1 + np.random.random())
            print(categoryName, subCategoryName, recipeName)
            retry = True
            while retry:
                try:
                    ingredients = getIngredients(recipe)
                    nutrition = getNutrition(recipe)
                    retry = False
                except:
                    time.sleep(10)
            data[categoryName][subCategoryName][recipeName] = {}
            data[categoryName][subCategoryName][recipeName]['ingredients'] = ingredients
            data[categoryName][subCategoryName][recipeName]['nutrition'] = nutrition
        filename = 'raw-data/{0}/{1}/recipes.json'.format(categoryName, subCategoryName)
        with open(filename, "w+") as outfile:
            json.dump(data[categoryName][subCategoryName], outfile, indent=4)