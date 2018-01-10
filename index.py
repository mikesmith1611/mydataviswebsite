import dash_core_components as dcc
import dash_html_components as html
import dash
from dash.dependencies import Input, Output, State
import pandas as pd
import components
from pages import recipes, home

from app import app

layout = html.Div([
    html.Div([
        html.Div([
        # html.Img(src="https://visualpharm.com/assets/936/Combo%20Chart-595b40b65ba036ed117d3e42.svg", height=30),
        'DataViz'
        ], className='navbar-brand'),
            html.Ul([
                html.Li([dcc.Link('Home', className='nav-link', href='/home')], className='nav-item active'),
                html.Li([dcc.Link('Recipes', className='nav-link', href='/recipes')], className='nav-item')
            ], className='navbar-nav mr-auto')
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
    else:
        print(pathname)
        return 404

if __name__ == "__main__":
    app.run_server(host="0.0.0.0", debug=True)