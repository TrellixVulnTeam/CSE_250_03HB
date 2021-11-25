# %%
import pandas as pd
import altair as alt

from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics


denver_dwelling = pd.read_csv("https://github.com/byuidatascience/data4dwellings/raw/master/data-raw/dwellings_ml/dwellings_ml.csv")
dwellings_ml = pd.read_csv("https://github.com/byuidatascience/data4dwellings/raw/master/data-raw/dwellings_ml/dwellings_ml.csv")

# %%
# "X" or "independent"
features = dwellings_ml.drop(columns = ['before1980', 'yrbuilt','parcel'])

# "y" or "dependent" or "outcome"
targets = dwellings_ml.before1980

# %%
# split the data!
x_train, x_test, y_train, y_test = train_test_split(features, targets, test_size = .34, random_state = 76)

# %%
# create the model
classifier = GaussianNB()

# train the model
classifier.fit(x_train, y_train)

# make predictions
y_predicted = classifier.predict(x_test)

# evaluate model (see how good the model is)
metrics.accuracy_score(y_test, y_predicted)
# %%
