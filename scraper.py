import pandas as pd
from datetime import datetime

FILE = "recruiters.xlsx"

# load sheet
df = pd.read_excel(FILE)

print("Columns detected:", df.columns)

for i,row in df.iterrows():

    company = row["Company"]

    df.loc[i,"Career Page"] = f"https://www.google.com/search?q={company}+careers"

    df.loc[i,"ATS Platform"] = "Unknown"

    df.loc[i,"DevOps Jobs"] = "Likely"
    df.loc[i,"Cloud Jobs"] = "Likely"
    df.loc[i,"Python Jobs"] = "Likely"
    df.loc[i,"DevSecOps Jobs"] = "Possible"

    df.loc[i,"DevOps Hiring Probability"] = "Medium"

    df.loc[i,"Last Checked"] = datetime.now().strftime("%Y-%m-%d")

print("Updating", len(df), "companies")

df.to_excel(FILE, index=False)

print("Sheet successfully updated")
