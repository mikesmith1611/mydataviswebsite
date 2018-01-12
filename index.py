import dash_core_components as dcc
import dash_html_components as html
import dash
from dash.dependencies import Input, Output, State
import pandas as pd
import components
from pages import recipes, home, football, stars
from flask import send_from_directory
import os
from app import app

#   <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
#     <span class="navbar-toggler-icon"></span>
#   </button>

layout = html.Div([
    html.Div([
        html.Div([
        # html.Img(src="https://visualpharm.com/assets/936/Combo%20Chart-595b40b65ba036ed117d3e42.svg", height=30),
        'DataSmith'
        ], className='navbar-brand'),
        html.Div([
            html.Ul([
                html.Li([dcc.Link('Home', className='nav-link', href='/home', id='/home')], className='nav-item active'),
                html.Li([dcc.Link('Recipes', className='nav-link', href='/recipes', id='/home')], className='nav-item'),
                html.Li([dcc.Link('Stars', className='nav-link', href='/stars', id='/stars')], className='nav-item'),
                html.Li([dcc.Link('About', className='nav-link', href='/about', id='/about')], className='nav-item')
            ], className='navbar-nav bd-navbar-nav flex-row mr-auto')
        ], className='navbar-nav-scroll')
    ], className="navbar navbar-expand-sm navbar-dark bg-dark"),
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content'),
])


app.layout = layout

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/recipes':
        print(pathname)
        return recipes.layout
    elif pathname == '/home':
        return home.layout
    elif pathname == '/stars':
        return stars.layout
    elif pathname == '/football':
        return football.layout
    else:
        print(pathname)
        return 404

@app.server.route('/static/<path:path>')
def static_file(path):
    static_folder = os.path.join(os.getcwd(), 'static')
    return send_from_directory(static_folder, path)

if __name__ == "__main__":
    app.run_server(host="0.0.0.0", debug=True)