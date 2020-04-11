import os

import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# get the data
titanic_train_file = os.path.join(BASE_DIR, 'data/test.csv')
titanic_train_data = pd.read_csv(titanic_train_file)

titanic_train_data.describe()