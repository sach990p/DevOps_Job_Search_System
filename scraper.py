import requests
import pandas as pd
import csv
import time
import os

keywords = [
"devops",
"site reliability",
"sre",
"cloud engineer",
"platform engineer",
"infrastructure engineer",
"devsecops"
]

results = []

def scrape_greenhouse(slug):

    url = f"https://boards-api.greenhouse.io/v1/boards/{slug}/jobs"

    r = requests.get(url,timeout=10)

    data = r.json()

    for job in data["jobs"]:

        title = job["title"].lower()

        if any(k in title for k in keywords):

            results.append({
                "company": slug,
                "title": job["title"],
                "location": job["location"]["name"],
                "link": job["absolute_url"]
            })


def scrape_lever(slug):

    url = f"https://api.lever.co/v0/postings/{slug}?mode=json"

    r = requests.get(url,timeout=10)

    data = r.json()

    for job in data:

        title = job["text"].lower()

        if any(k in title for k in keywords):

            results.append({
                "company": slug,
                "title": job["text"],
                "location": job["categories"]["location"],
                "link": job["hostedUrl"]
            })


with open("company_database.csv") as file:

    reader = csv.DictReader(file)

    for row in reader:

        company = row["Company"]
        ats = row["ATS"]
        slug = row["Slug"]

        try:

            if ats == "Greenhouse":
                scrape_greenhouse(slug)

            elif ats == "Lever":
                scrape_lever(slug)

            time.sleep(0.3)

        except:
            pass


df = pd.DataFrame(results)

try:

    old = pd.read_excel("devops_jobs.xlsx")

    df = pd.concat([old,df]).drop_duplicates()

except:
    pass


df.to_excel("devops_jobs.xlsx",index=False)

print("Job database updated")
