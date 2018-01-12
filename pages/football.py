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
    html.H4("Football", className='display-4'),
    html.P("This application is for exploring Premier League data", className='lead'),
    html.Hr(className="my-4"),
], className='jumbotron mt-2 pb-4 pt-4')

layout = html.Div([
            jumbotron,
        ], className='container')