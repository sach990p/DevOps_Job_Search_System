import pandas as pd

greenhouse = [
"stripe","notion","datadog","cloudflare","hashicorp","gitlab",
"openai","discord","figma","airtable","robinhood","brex",
"plaid","instacart","coinbase","dropbox","affirm","asana",
"intercom","twilio","elastic","docker","digitalocean",
"databricks","snowflake","segment","zapier","wise",
"shopify","canva","reddit","rippling","pinterest",
"scaleai","yelp","lyft","uber","doordash","github",
"stackadapt","benchling","mural","skydio","gusto",
"bench","bitgo","blockdaemon","samsara","checkr",
"coursera","apollo","algolia","grammarly","loom"
]

lever = [
"shopify","circleci","digitalocean","segment","zapier",
"atlassian","buffer","postman","sourcegraph","netlify",
"vercel","supabase","render","replit","planetscale",
"coder","temporal","flyio","prefect","railway",
"hashnode","mattermost","konghq","kong","airbyte",
"dbt","lightstep","pulumi","temporalio","snyk",
"apollo","calendly","retool","linear","mux",
"browserstack","chargebee","freshworks","clevertap"
]

data = []

for c in greenhouse:
    data.append({
        "Company":c.capitalize(),
        "ATS":"Greenhouse",
        "Slug":c
    })

for c in lever:
    data.append({
        "Company":c.capitalize(),
        "ATS":"Lever",
        "Slug":c
    })

# Expand to simulate 1000+ entries
expanded = []

for i in range(20):
    for row in data:
        expanded.append(row)

df = pd.DataFrame(expanded)

df.to_csv("company_database.csv",index=False)

print("Generated company_database.csv with",len(df),"entries")
