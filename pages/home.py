import dash_core_components as dcc
import dash_html_components as html
import dash
from dash.dependencies import Input, Output, State

from app import app
    
layout = html.Div([
            html.Div([
                html.Img(src="https://cdn.jamieoliver.com/recipe-database/oldImages/xtra_med/786_5_1350297947.jpg", className="card-img-top"),
                html.Div([
                    html.H5('Recipes', className="card-title"),
                    html.P('Recipe nutirion by category', className='card-text'),
                    dcc.Link('Explore', href='/recipes', className="btn btn-primary")
                    ], className="card-body")
                ], className="card mt-2", style={"width": "18rem"})


        ], className='container')
