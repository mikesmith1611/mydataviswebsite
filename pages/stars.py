import dash_core_components as dcc
import dash_html_components as html
import dash
from dash.dependencies import Input, Output, State
import pandas as pd
import components
import data
import figures
import plotly.graph_objs as go
from astropy.io import fits
from astropy.wcs import WCS
import numpy as np

from app import app

img = fits.open('parsed-data/NB_mosaic_shrink.fits')



minimum, maximum = np.nanpercentile(img[0].data, [25, 99.9])
mask1 = img[0].data > maximum
mask2 = img[0].data < minimum
mask3 = img[0].data != img[0].data
img[0].data[mask3] = minimum
img[0].data[mask1] = maximum
img[0].data[mask2] = minimum

trace1 = dict(type='heatmapgl', z=np.log10(img[0].data), colorscale='Greys')

df = pd.read_csv('parsed-data/OBstars.csv', delimiter='|')
df = df[df['A0'] < 7.82]
wcs = WCS(img[0].header)
x, y = wcs.wcs_world2pix(df['RAJ2000'], df['DEJ2000'], 1)
df['x'] = x
df['y'] = y
df['size'] = (1.25 * (10 ** df['logTeff'])) / 5000
df['marker'] = 'Circle'
df['marker'][df['logTeff'] > 4.477] == 'Triangle'
df['VPHASOB1'] = df['VPHAS-OB1']
# colors = [
#     "#%02x%02x%02x" % (int(r), int(g), int(b))
#                        for r, g, b, _ in
#                        255*mpl.cm.jet(mpl.colors.Normalize(vmax=10)(df['A0']))
# ]
# colors = [i.upper() for i in colors]

# df['color'] = colors
df['alpha'] = 0.9

trace2 = go.Scatter(
    x=df['x'],
    y=df['y'],
    mode='markers',
    marker=dict(
        size=df['size'],
        color = df['A0'], #set color equal to a variable
        colorscale='Viridis',
        showscale=True
    )
)
data = [trace1]

layout = dict(autosize=True)
fig = dict(data=data, layout=layout)

graph = html.Div([dcc.Graph(id='carina', figure=fig)], style={'width': '100%'})
jumbotron = html.Div([
    html.H4("Stars", className='display-4'),
    html.P("This application is for exploring astronomy data.", className='lead'),
    html.Hr(className="my-4"),
], className='jumbotron mt-2 pb-4 pt-4')


layout = html.Div([
            jumbotron,
            graph
        ], className='container')