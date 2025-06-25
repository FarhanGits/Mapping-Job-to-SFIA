import requests, json
import linkedin_params

# URL and Headers from = F12 -> Network -> (Search API Link) -> Headers
url = linkedin_params.url

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36",
    "Accept": "application/vnd.linkedin.normalized+json+2.1",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9,id;q=0.8",
    "Cookie": linkedin_params.cookies.strip(),
    "Csrf-Token": linkedin_params.csrf_token,
    "Priority": "u=1, i",
    "Referer": linkedin_params.referer,
    "Sec-Ch-Ua": '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"Windows"',
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "X-Li-Lang": "en_US",
    "X-Li-Page-Instance": "urn:li:page:d_flagship3_search_srp_jobs;chCzcjpIRJmbf7/jsQrGeg==",
    "X-Li-Pem-Metadata": "Voyager - Careers - Jobs Search=jobs-search-results,Voyager - Careers - Critical - careers-api=jobs-search-results",
    "X-Li-Prefetch": "1",
    "X-Li-Track": '{"clientVersion":"1.13.35352","mpVersion":"1.13.35352","osName":"web","timezoneOffset":7,"timezone":"Asia/Jakarta", "deviceFormFactor":"DESKTOP","mpName":"voyager-web","displayDensity":1.25,"displayWidth":1920,"displayHeight":1080}',
    "X-Restli-Protocol-Version": "2.0.0",
}

session = requests.session()
session.headers.update(headers)
response = session.get(url)

job_data = []

if response.status_code == 200:
    data = response.json()

    # Extract advertiser IDs from each item in the 'data' list
    for item in data["included"][1:]:
        urn = item.get("entityUrn", "")
        if urn.startswith("urn:li:fsd_jobPosting:"):
            id = urn.split(":")[-1]

            job = {"job_id": id, "job_title": item["title"]}

            job_data.append(job)
else:
    print(response.status_code)

# Syntax ini (open() dan job_data = data + job_data) untuk scraping-id page 2-seterusnya, COMMENT jika masih di page 1
# Run menggunakan venv di directory "Code - Mapping to SFIA", ganti path sesuai kebutuhan!
# with open(
#     f"./Scraping/{linkedin_params.job_portal}/id/7 days v5/jobID-{linkedin_params.ISorCS_Jobs}-{linkedin_params.keyword_name}-7_days_v5.json",
#     "r",
#     encoding="utf-8",
# ) as f:
#     former_id = json.load(f)
# job_data = former_id + job_data

# Run menggunakan venv di directory "Code - Mapping to SFIA", ganti path sesuai kebutuhan!
with open(
    f"./Scraping/{linkedin_params.job_portal}/id/7 days v5/jobID-{linkedin_params.ISorCS_Jobs}-{linkedin_params.keyword_name}-7_days_v5.json",
    "w",
    encoding="utf-8",
) as f:
    json.dump(job_data, f, ensure_ascii=False, indent=4)