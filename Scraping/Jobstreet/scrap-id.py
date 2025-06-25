import requests, json
import jobstreet_params

# URL and Headers from Network -> Headers
url = jobstreet_params.url

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
    "Connection": "keep-alive",
    "Authorization": jobstreet_params.auth.strip(),
    "Referer": jobstreet_params.referer,
}

job_data = []

session = requests.session()
session.headers.update(headers)
response = session.get(url)

if response.status_code == 200:
    data = response.json()

    # Extract advertiser IDs from each item in the 'data' list
    for item in data["data"]:
        job = {
            "job_id": item["id"],
            "job_title": item["title"],
            "company": item["advertiser"][("description")],
            "listing_date": item["listingDate"],
        }
        job_data.append(job)
else:
    print(response.status_code)

# Syntax ini (open() dan job_data = data + job_data) untuk scraping-id page 2-seterusnya, COMMENT jika masih di page 1
# Run menggunakan venv di directory "Code - Mapping to SFIA", ganti path sesuai kebutuhan!
with open(
    f"./Scraping/{jobstreet_params.job_portal}/id/7 days v5/jobID-{jobstreet_params.ISorCS_Jobs}-{jobstreet_params.keyword_name}-7_days_v5.json",
    "r",
    encoding="utf-8",
) as f:
    former_id = json.load(f)
job_data = former_id + job_data

# Run menggunakan venv di directory "Code - Mapping to SFIA", ganti path sesuai kebutuhan!
with open(
    f"./Scraping/{jobstreet_params.job_portal}/id/7 days v5/jobID-{jobstreet_params.ISorCS_Jobs}-{jobstreet_params.keyword_name}-7_days_v5.json",
    "w",
    encoding="utf-8",
) as f:
    json.dump(job_data, f, ensure_ascii=False, indent=4)