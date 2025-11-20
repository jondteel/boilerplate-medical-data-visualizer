import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
#df['overweight'] = (df['weight'] / ((df['height'] / 100) ** 2) > 25).astype(int)
df['overweight'] = np.where(df['weight'] / ((df['height'] / 100) ** 2) > 25, 1, 0)


# 3
#df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['cholesterol'] = np.where(df['cholesterol'] > 1, 1, 0)
#df['gluc'] = (df['gluc'] > 1).astype(int)
df['gluc'] = np.where(df['gluc'] > 1, 1, 0)


# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'], var_name='item', value_name='measure')


    # 6
    df_cat = df_cat.groupby(['cardio', 'item', 'measure']).size().reset_index(name='total')
    

    # 7
    ctplt = sns.catplot(data=df_cat, x='item', y='total', hue='measure', kind='bar', col='cardio')


    # 8
    fig = ctplt.fig


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
