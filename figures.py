import pandas as pd
import plotly.graph_objs as go
import plotly.figure_factory as ff
import numpy as np
import violin


def nutritionViolin(df, data_header, category, nutritionType):
    
    df = df[df.category == category]
    data_header = nutritionType + data_header
    df = df[df[data_header] == df[data_header]]
    noiseFix = (0.00001*np.random.rand(len(df)))
    df[data_header] = df[data_header] + noiseFix
    print(data_header, category, nutritionType)
    g = df.groupby('subCategory').count()
    mask = np.array(g[data_header] <= 1)
    bad = np.array(g.index[mask])
    for b in bad:
        df = df[df['subCategory'] != b]

    median = df.groupby('subCategory').median()
    group_stats = dict(zip(median.index, median[data_header]))

    fig = violin.create_violin(df, use_colorscale=True,
    group_stats=group_stats, title=category.capitalize(),
                           data_header=data_header,
                           group_header='subCategory',
                           width='100%',
                           height=600)
    return fig

def ingredientDist(df, category, ingredients):
    
    df = df[df.category == category]
    mask = np.ones(len(df), dtype=bool)
    for ingredient in ingredients:
        mask &= df['ingredients'].str.contains(ingredient)
    total = df.groupby('subCategory').count()['recipe']
    dfIng = df[mask]
    dfIng = dfIng.groupby('subCategory').count()['recipe']
    mask2 = np.in1d(total.index, dfIng.index)
    notIn = total[~mask2]
    In = total[mask2]
    frac = dfIng / In
    x = np.array(list(frac.index) + list(notIn.index))
    y = np.array(list(frac.values) + [0] * len(notIn))
    print(notIn, x, y)
    mask = np.argsort(y)
    y = y[mask][:: -1]
    x = x[mask][:: -1]
    trace = go.Bar(
        x=x,
        y=y
    )
    return go.Figure(data=[trace])

import data
from sklearn.cluster import KMeans


category = 'world'
df = data.dfNutririon
ingreients = data.ingredients

df = df[df['category']  == 'world']



