import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
df['overweight'] = 0 if (df['weight'] / ((df['height'] / 100) ** 2)) <= 25 else 1

# 3
df['cholesterol'] = 0 if df['cholesterol'] == 1 else 1
df['gluc'] = 0 if df['gluc'] == 1 else 1


# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'], var_name='item', value_name='measure')


    # 6
    df_cat = df_cat.groupby(['cardio', 'item', 'measure']).size().reset_index(name='total')
    

    # 7
    ctplt = sns.catplot(data=df_cat, x='cardio', y='count', hue='item', kind='bar')


    # 8
    fig = ctplt.figure


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = None

    # 12
    corr = None

    # 13
    mask = None



    # 14
    fig, ax = None

    # 15



    # 16
    fig.savefig('heatmap.png')
    return fig
