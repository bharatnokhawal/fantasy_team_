import pandas as pd

# Load the dataset
data = pd.read_csv('IPl Ball-by-Ball 2008-2023.csv')

# Preprocess the data: handle missing values, encode categorical variables, etc.
data.fillna(0, inplace=True)
data['batsman'] = data['batsman'].astype('category').cat.codes
data['bowler'] = data['bowler'].astype('category').cat.codes
data['batting_team'] = data['batting_team'].astype('category').cat.codes
data['bowling_team'] = data['bowling_team'].astype('category').cat.codes

# Extract relevant features
features = data[['batsman','bowler' ,'batting_team', 'bowling_team', 'batsman_runs', 'is_wicket', 'fielder']]
target = data['points']  # Assuming 'points' is the target variable
