import dash_core_components as dcc
import dash_html_components as html
import dash
from dash.dependencies import Input, Output, State

from app import app


jumbotron = html.Div([
    html.H1("DataSmith", className='display-4'),
    html.P("Welcome to DataSmith, a website dedicated to the analysis and visualisation of data scraped from accross the web.", className='lead'),
    html.Hr(className="my-4"),
    html.P("Explore the pages below!")
], className='jumbotron mt-2 pb-4 pt-4')

def card(img, title, text, href):
    card =  html.Div([
                html.Img(src=img, className="card-img-top", height=200),
                html.Div([
                    html.H5(title, className="card-title"),
                    html.P(text, className='card-text'),
                    dcc.Link('Explore', href=href, className="btn btn-primary")
                    ], className="card-body")
                ], className="card mt-2", style={"width": "200px"})
    return card

recipes = card("https://cdn.jamieoliver.com/library/images/Jamie-Social.jpg",
               "Recipes", "Recipe nutirion by category", '/recipes')
stars = card("https://cdn.shopify.com/s/files/1/0616/2685/products/Star-Cluster-Westerlund-II_206bd3ba-0f71-4846-97ff-8f7868ade783_1024x1024.jpg?v=1447965286",
               "Stars", "The massive star population in Carina", '/stars')
football = card("https://s3.amazonaws.com/premierleague-static-files/premierleague/pl_icon.png",
                "Football", "The Premier League", '/football')

cards = html.Div([
    html.Div([
        html.Div([recipes], className='col-sm-auto'),
        html.Div([stars], className='col-sm-auto'),
        html.Div([football], className='col-sm-auto')
    ], className='row justify-content-around')
])
layout = html.Div([
            jumbotron,
            cards
        ], className='container')
