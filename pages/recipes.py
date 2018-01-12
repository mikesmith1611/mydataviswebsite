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
    html.H4("Recipe Nutrition", className='display-4'),
    html.P("This application is for exploring the nutrional content of recipes on www.jamieoliver.com.", className='lead'),
    html.Hr(className="my-4"),
], className='jumbotron mt-2 pb-4 pt-4')


plot1 = html.Div([
            html.Div([components.nutritionViolinGraph], style={'width': '100%'}),
            html.Div([
                html.Div([
                    components.nutritionViolinGroupDropDown
                ], style={'float': 'left', 'width': 150, 'padding-left': '20px'}),
                html.Div([
                    components.nutritionViolinMetricDropDown
                ], style={'float': 'left', 'width': 150, 'padding-left': '10px'}),

                html.Div([
                    components.nutritionViolinTypeDropDown
                ], style={'float': 'left', 'width': 150, 'padding-left': '10px'})
            ], className='row justify-content-center')
        ], className='chart-area')

layout = html.Div([
            jumbotron,
            plot1
        ], className='container')


@app.callback(Output('nutritionViolinGraph', 'figure'),
              [Input('nutritionViolinGroupDropDown', 'value'),
               Input('nutritionViolinMetricDropDown', 'value'),
               Input('nutritionViolinTypeDropDown', 'value')])
def updateNutritionViolinGraph(group, metric, nutritionType):
    return figures.nutritionViolin(dfNutririon, metric, group, nutritionType)
