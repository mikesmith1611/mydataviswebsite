import dash_core_components as dcc
import data
import numpy as np


dfNutririon = data.dfNutririon

nutritionViolinGraph = dcc.Graph(id='nutritionViolinGraph')
nutritionViolinGroupDropDown = dcc.Dropdown(
    id='nutritionViolinGroupDropDown',
    options=[{'value': i, 'label': i.capitalize()} for i in np.unique(dfNutririon.category)],
    value=dfNutririon.category[0]
)

nutritionViolinMetricDropDown = dcc.Dropdown(
    id='nutritionViolinMetricDropDown',
    options=[{'label': 'Amount (g)', 'value': 'Amount'},
             {'label': 'Percent', 'value': 'Percent'}],
    value='Amount'
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
    value='Calories'
)