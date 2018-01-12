import dash_core_components as dcc
import dash_html_components as html
import dash
from dash.dependencies import Input, Output, State
import pandas as pd
import components
import data
import figures


app = dash.Dash()
app.title = 'DataSmith'

app.config.suppress_callback_exceptions = True
app.css.append_css({'external_url': 'https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.3/css/bootstrap.min.css'})
app.css.append_css({'external_url': '/static/custom.css'})

app.scripts.append_script({'external_url': 'https://code.jquery.com/jquery-3.2.1.slim.min.js'})
app.scripts.append_script({'external_url': 'https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js'})
app.scripts.append_script({'external_url': 'https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.3/js/bootstrap.min.js'})
app.scripts.append_script({'external_url': '/static/custom.js'})


#   <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
#     <span class="navbar-toggler-icon"></span>
#   </button>
