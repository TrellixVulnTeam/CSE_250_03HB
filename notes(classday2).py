#%% 

# Libraries
import pandas as pd
import altair as alt
import numpy as np
alt.data_transformers.enable('json')

names = pd.read_csv("https://raw.githubusercontent.com/byuidatascience/data4names/master/data-raw/names_year/names_year.csv")# Data info: https://github.com/byuidatascience/data4names/blob/master/data.md


#%%
# Selecting one name
names.query('name == "Katie"')

names[names['name'] == "Katie"]


# %%
# Selecting Multiple Names

names[(names['name'] == "Katie") | (names['name'] == "Shaniqua")]


names_list = ["Katie", "Asher"]



names[names["name"].isin(names_list)]

names.query('name == "Joseph" | name == "Brigham"')


# Below two are the same
names.query('name == @names_list')
names.query('name in @names_list')

#%%
names_list = ["Joseph", "Brigham"]
names[names['name'].isin(names_list)]

(
names[names['name']
    .isin(names_list)]
    .groupby('name')
    .mean()
    [['AZ', 'Total']]
    .sort_values('AZ', ascending = False)
)

#%%
names_list = ["Joseph", "Brigham"]

graph_data = (names
    .query('name in @names_list')
    .groupby('name')
    .mean()
    .filter(['AZ', 'Total'])
    .sort_values('AZ', ascending = False)
)
    
(alt.Chart(graph_data)
    .mark_line()
    .encode( 
        x = 'year',
        y = 'Total',
        color = 'name'
    )
)


# %%

