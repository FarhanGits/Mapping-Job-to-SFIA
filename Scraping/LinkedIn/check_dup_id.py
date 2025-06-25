import json
import linkedin_params

# Import ID Lengkap (IS / CS)
with open(linkedin_params.full_id_path_cs, "r", encoding='utf-8') as data:
    full_id = json.load(data)

# Import ID Baru
with open(f"./Scraping/{linkedin_params.job_portal}/id/7 days v5/jobID-{linkedin_params.ISorCS_Jobs}-{linkedin_params.keyword_name}-7_days_v5.json", "r", encoding='utf-8') as data:
    new_id = json.load(data)

print(f"{linkedin_params.job_portal} {linkedin_params.job_category} {linkedin_params.keyword_name}:")

# Buat kombinasi job_title & company
existing_jobs = set()
for job in full_id:
    existed = f"{job['job_id']} - {job['job_title']}"
    existing_jobs.add(existed)

duped = []
new_scraped = []

for job in new_id:
    new = f"{job['job_id']} - {job['job_title']}"
    if new in existing_jobs:
        duped.append(job)
    elif new not in existing_jobs:
        new_scraped.append(job)
    else:
        pass
print(f"Ada {len(duped)} job terduplikat, 5 diantaranya:")
print(duped[:5])
print(f"Ada {len(new_scraped)} job baru didapat, 5 diantaranya:")
print(new_scraped[:5])

# # Simpan file "new" baru:
# with open(
#     f"./Scraping/{linkedin_params.job_portal}/id/7 days v5/jobID-{linkedin_params.ISorCS_Jobs}-{linkedin_params.keyword_name}-7_days_v5.json",
#     "w",
#     encoding="utf-8",
# ) as f:
#     json.dump(new_scraped, f, ensure_ascii=False, indent=4)

# # Simpan ke list full
# print(f"Total ID {linkedin_params.ISorCS_Jobs} sebelumnya: {len(full_id)}")

# full_id += new_scraped
# with open(linkedin_params.full_id_path_cs,
#     "w",
#     encoding="utf-8",
# ) as f:
#     json.dump(full_id, f, ensure_ascii=False, indent=4)

# print(f"Total ID {linkedin_params.ISorCS_Jobs}: {len(full_id)}")