import re, pandas as pd

fe_regex = r"\b(fresh graduate|fresh graduates|freshgraduate|freshgraduates)\b"
exp_regex = r"\b(\d+[\+|\-]?)\s*(year|years)\b.*\b(experience|experiences)\b|\b(experience|experiences)\b.*\b(\d+[\+|\-]?)\s*(year|years)\b"

job_path = "Scraping/docs/computer-science/7 days v5/translated-combinedList_CSJobs_7_days_v5.xlsx"
job_list = pd.read_excel(job_path)
job_list = pd.DataFrame(job_list)

valid_job = []
invalid_job = []
for i, job in job_list.iterrows():
    job_description = job["job_description"]
    
    exp_pattern = re.compile(exp_regex, re.IGNORECASE)
    exp_match = exp_pattern.search(job_description)

    if re.search(fe_regex, job_description, re.IGNORECASE):
        matches = list(re.finditer(fe_regex, job_description, re.IGNORECASE))
        for match in matches:
            start = max(0, match.start() - 50)  # ambil 50 karakter sebelum kata fresh graduate
            context = job_description[start:match.start()]
            if re.search(r"\b(no|not|not for|without|except)\b", context):
                # Negasi ditemukan, anggap tidak valid meskipun ada kata fresh graduates karena di depannya terdapat kata negatif
                invalid_job.append(job)
            else:
                # Fresh graduate valid
                valid_job.append(job)
    elif exp_match:
        years = None
        # Ambil angka tahun yg ditemukan
        for group in exp_match.groups():
            if group and group.isdigit():
                years = int(group)
                break
        if years is not None and years >= 1:
            # Terdapat minimal tahun pengalaman >= 1 tahun, tidak valid
            invalid_job.append(job)
        else:
            invalid_job.append(job) # gatau
    else:
        # Tidak ada persyaratan, valid
        valid_job.append(job)

valid_job = pd.DataFrame(valid_job)
invalid_job = pd.DataFrame(invalid_job)

print(f"Total job: {len(job_list)}")
print(f"Total job valid: {len(valid_job)}")
print(f"Total job invalid: {len(invalid_job)}")

# valid_job.to_excel("Scraping/docs/computer-science/7 days v5/CSJobs_7_days_v5.xlsx", index=False, engine="openpyxl")
# invalid_job.to_excel("Scraping/docs/computer-science/7 days v5/(deprecated)-CSJobs_7_days_v5.xlsx", index=False, engine="openpyxl")