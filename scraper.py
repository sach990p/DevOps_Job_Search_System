import requests
import pandas as pd
import os
import time
from datetime import datetime

API_KEY = os.environ["GOOGLE_API_KEY"]
CX = os.environ["SEARCH_ENGINE_ID"]

queries = [
"site:linkedin.com/in DevOps recruiter Pune",
"site:linkedin.com/in Cloud recruiter Pune",
"site:linkedin.com/in DevOps hiring manager India",
"site:linkedin.com/in Site reliability recruiter India",
"site:linkedin.com/in Kubernetes recruiter"
]

results = []

def detect_work_mode(text):

    text = text.lower()

    if "remote" in text:
        return "Remote"

    if "hybrid" in text:
        return "Hybrid"

    if "onsite" in text or "on-site" in text:
        return "Onsite"

    return "Unknown"


def detect_location(text):

    text = text.lower()

    if "pune" in text:
        return "Pune"

    if "bangalore" in text:
        return "Bangalore"

    if "india" in text:
        return "India"

    return "Unknown"


def google_search(query):

    url = "https://www.googleapis.com/customsearch/v1"

    params = {
        "key": API_KEY,
        "cx": CX,
        "q": query,
        "num": 10
    }

    response = requests.get(url, params=params)
    data = response.json()

    if "items" not in data:
        return []

    return data["items"]


for query in queries:

    print("Searching:", query)

    items = google_search(query)

    for item in items:

        title = item.get("title","")
        link = item.get("link","")
        snippet = item.get("snippet","")

        if "linkedin.com/in/" not in link:
            continue

        recruiter = title.split("-")[0]

        work_mode = detect_work_mode(snippet)

        location = detect_location(snippet)

        results.append({

            "Company": "Unknown",
            "Hiring Role": query,
            "Recruiter Name": recruiter,
            "LinkedIn Profile": link,
            "Work Mode": work_mode,
            "Location": location,
            "Date Found": datetime.now().strftime("%Y-%m-%d")

        })

    time.sleep(2)


df = pd.DataFrame(results)

try:

    old = pd.read_excel("recruiters.xlsx")

    df = pd.concat([old, df])

    df = df.drop_duplicates(subset=["LinkedIn Profile"])

except:

    pass


df.to_excel("recruiters.xlsx", index=False)

print("Recruiter database updated")
print("Total recruiters:", len(df))
