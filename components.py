import dash_core_components as dcc
import data
import numpy as np


dfNutririon = data.dfNutririon

nutritionViolinGraph = dcc.Graph(id='nutritionViolinGraph')
nutritionViolinGroupDropDown = dcc.Dropdown(
    id='nutritionViolinGroupDropDown',
    options=[{'value': i, 'label': i.capitalize()} for i in np.unique(dfNutririon.category)],
    value='world',
    clearable=False
)

nutritionViolinMetricDropDown = dcc.Dropdown(
    id='nutritionViolinMetricDropDown',
    options=[{'label': 'Amount (g)', 'value': 'Amount'},
             {'label': 'Percent', 'value': 'Percent'}],
    value='Amount',
    clearable=False
)

nutritionViolinTypeDropDown = dcc.Dropdown(
    id='nutritionViolinTypeDropDown',
    options=[{'label': 'Calories', 'value': 'Calories'},
              {'label': 'Carbs', 'value': 'Carbs'},
              {'label': 'Fat', 'value': 'Fat'},
              {'label': 'Protein', 'value': 'Protein'},
              {'label': 'Salt', 'value': 'Salt'},
              {'label': 'Saturates', 'value': 'Saturates'},
              {'label': 'Sugars', 'value': 'Sugars'},
              {'label': 'Fibre', 'value': 'Fibre'}
              ],
    value='Calories',
    clearable=False
)


ingredients = data.ingredients
ingredientGraph = dcc.Graph(id='ingredientGraph')

ingredientsDropDown = dcc.Dropdown(
    id='ingredientsDropDown',
    options=[{'value': i, 'label': i.capitalize()} for i in ingredients],
    value='chicken',
    multi=True,
    clearable=False
)

ingredientsGroupDropDown = dcc.Dropdown(
    id='ingredientsGroupDropDown',
    options=[{'value': i, 'label': i.capitalize()} for i in np.unique(dfNutririon.category)],
    value='world',
    clearable=False
)