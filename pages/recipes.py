import dash_core_components as dcc
import dash_html_components as html
import dash
from dash.dependencies import Input, Output, State
import pandas as pd
import components
import data
import figures

from app import app

dfNutririon = data.dfNutririon

jumbotron = html.Div([
    html.H4("Recipes", className='display-4'),
    html.P("This application is for exploring the recipe data scraped from www.jamieoliver.com.", className='lead'),
    html.Hr(className="my-4"),
], className='jumbotron mt-2 pb-1 pt-4')

plot1text = dcc.Markdown(
"""
### Nutrition by category

This is a violin plot showing the distribution of nutritional values of recipes as categorized on [www.jamieoliver.com](https://www.jamieoliver.com).
Use the dropdown boxes to select the category, nutritional variable and unit. The distributions are ordered by their median
value decreasing from left to right. They are also coloured according to their median value.
"""
)


plot1 = html.Div([
            html.Div([
                html.Div([
                    html.Label('Category'),
                    components.nutritionViolinGroupDropDown
                ], style={'float': 'left', 'width': 150, 'padding-left': '20px'}),

                html.Div([
                    html.Label('Variable'),
                    components.nutritionViolinTypeDropDown
                ], style={'float': 'left', 'width': 150, 'padding-left': '10px'}),
                html.Div([
                    html.Label('Unit'),
                    components.nutritionViolinMetricDropDown
                ], style={'float': 'left', 'width': 150, 'padding-left': '10px'}),
            ], className='row justify-content-center'),
            html.Div([components.nutritionViolinGraph], style={'width': '100%'})
        ])

plot2text = dcc.Markdown(
"""
### Ingredient frequency by category

This bar chart shows the frequency of the selected ingridents in each subcategory. 
Select multiple ingredients to see the frequency of combinations of ingredients.
"""
)

plot2 = html.Div([
            html.Div([
                html.Div([
                    html.Label('Category'),
                    components.ingredientsGroupDropDown
                ], style={'float': 'left', 'width': 150, 'padding-left': '20px'}),

                html.Div([
                    html.Label('Ingredient'),
                    components.ingredientsDropDown
                ], style={'float': 'left', 'width': 500, 'padding-left': '10px'}),
            ], className='row justify-content-center'),
            html.Div([components.ingredientGraph], style={'width': '100%'})
        ])

layout = html.Div([
            html.Div([
                jumbotron,
                plot1text
            ], className='container'),
            html.Div([plot1], className='container-fluid mt-8'),
            html.Div([plot2text,
                    plot2], className='container mt-8')
        ])



@app.callback(Output('ingredientGraph', 'figure'),
              [Input('ingredientsGroupDropDown', 'value'),
               Input('ingredientsDropDown', 'value')])
def updateNutritionViolinGraph(group, ingredients):
    return figures.ingredientDist(dfNutririon, group, ingredients)


@app.callback(Output('nutritionViolinGraph', 'figure'),
              [Input('nutritionViolinGroupDropDown', 'value'),
               Input('nutritionViolinMetricDropDown', 'value'),
               Input('nutritionViolinTypeDropDown', 'value')])
def updateNutritionViolinGraph(group, metric, nutritionType):
    return figures.nutritionViolin(dfNutririon, metric, group, nutritionType)

