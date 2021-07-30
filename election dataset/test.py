import pandas as pd
import os

primary_df = pd.read_csv("us-2016-primary-results.csv", delimiter=";")
election_df = pd.read_csv("usa-2016-presidential-election-by-county.csv", delimiter=";")

primary_df.info()
election_df.info()
