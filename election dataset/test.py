import pandas as pd

df = pd.read_csv("usa-2016-presidential-election-by-county.csv",delimiter=";")

print(df)

with pd.ExcelWriter("test.xlsx", engine = "xlsxwriter") as writer:
    df.to_excel(writer,sheet_name="test",index=False)