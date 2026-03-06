import pandas as pd
import requests
from datetime import datetime

df = pd.read_excel("recruiters.xlsx")

for index,row in df.iterrows():

    company = row["Company"]

    try:

        career_page = f"https://www.google.com/search?q={company}+careers"

        df.loc[index,"Career Page"] = career_page
        df.loc[index,"ATS Platform"] = "Unknown"

        # Example simple detection logic
        df.loc[index,"DevOps Jobs"] = "Possible"
        df.loc[index,"Cloud Jobs"] = "Possible"
        df.loc[index,"Python Jobs"] = "Possible"
        df.loc[index,"DevSecOps Jobs"] = "Possible"

        df.loc[index,"DevOps Hiring Probability"] = "Medium"

        df.loc[index,"Last Checked"] = datetime.now().strftime("%Y-%m-%d")

    except:
        pass

df.to_excel("recruiters.xlsx",index=False)

print("Company sheet updated")
