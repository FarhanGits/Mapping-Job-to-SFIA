import json


full_page = 2

job_data = []
for i in range(1, full_page + 1):
    print(f"Page ke {i}")
    # Import data berisi kumpulan job_id yang didapat, Run menggunakan venv di directory "Code - Mapping to SFIA", ganti path sesuai kebutuhan!
    with open(
        f"./Scraping/LinkedIn/dump/jobID-IS-dump-page{i}.json", "r", encoding="utf-8"
    ) as data:
        job_list = json.load(data)

    # Extract advertiser IDs from each item in the 'data' list
    for item in job_list["included"]:
        title = item.get("title")
        urn = item.get("entityUrn", "")
        if urn.startswith("urn:li:fsd_jobPosting:"):
            id = urn.split(":")[-1]

        print(title)
        print(id)
        print(" ")

        # job_data.append({"job_id": id, "job_title": title})

# Run menggunakan venv di directory "Code - Mapping to SFIA", ganti path sesuai kebutuhan!
# with open(
#     "./Scraping/LinkedIn/dump/jobID-IS-dump-full.json",
#     "w",
#     encoding="utf-8",
# ) as f:
#     json.dump(data, f, ensure_ascii=False, indent=4)
# print(job_data)
