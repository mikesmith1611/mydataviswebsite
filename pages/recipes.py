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

layout = html.Div([
            html.Div([components.nutritionViolinGraph], style={'width': '100%'}),
            html.Div([
                html.Div([
                    components.nutritionViolinGroupDropDown
                ], style={'float': 'left', 'width': 150}),
                html.Div([
                    components.nutritionViolinMetricDropDown
                ], style={'float': 'left', 'width': 150}),

                html.Div([
                    components.nutritionViolinTypeDropDown
                ], style={'float': 'left', 'width': 150})
            ], className='row')
        ], className='container')


@app.callback(Output('nutritionViolinGraph', 'figure'),
              [Input('nutritionViolinGroupDropDown', 'value'),
               Input('nutritionViolinMetricDropDown', 'value'),
               Input('nutritionViolinTypeDropDown', 'value')])
def updateNutritionViolinGraph(group, metric, nutritionType):
    return figures.nutritionViolin(dfNutririon, metric, group, nutritionType)
