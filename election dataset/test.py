import pandas as pd

primary_df = pd.read_csv("us-2016-primary-results.csv", delimiter=";")
election_df = pd.read_csv("usa-2016-presidential-election-by-county.csv", delimiter=";")

print(primary_df.head())
print(election_df.head())

print(primary_df.describe())
print(election_df.describe())