# %% 
import pandas as pd   # to load and transform data
import numpy as np    # for math/stat calculations
import altair as alt

#%%
# from url to pandas dataframe
url = "https://raw.githubusercontent.com/byuidatascience/data4missing/master/data-raw/flights_missing/flights_missing.json" 
cars = pd.read_json(url)

# or from file to pandas dataframe
# cars = pd.read_json("mtcars_missing.json")


# %% 
cars.sort_values('by = ")

# %%
alt.Chart(cars).mark_circle().encode(x = 'mpg', y = 'hp')
# %%
