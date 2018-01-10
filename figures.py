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


