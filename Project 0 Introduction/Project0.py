#%% Libraries
import pandas as pd
import altair as alt
import numpy as np
# alt.data_transformers.enable('json')


#%% Data

names_year = pd.read_csv("C:/Users/brigh/OneDrive - BYU-Idaho/8th Semester- Fall 2021/CSE 250 Data Science Programming/names_year.csv")

#%% How does your name at your birth year compare to its use historically?

my_name = names_year.query('name == "Brigham"')
# my_name.head()


# %%
chart = (alt.Chart(my_name)
            .mark_line().encode(
                x = alt.X('year:O', title = "Year"),
                y = alt.Y('Total:Q', title = "Total")
))
chart
