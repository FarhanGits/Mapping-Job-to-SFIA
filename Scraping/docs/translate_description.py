import pandas as pd, time
from datetime import datetime
from deep_translator import GoogleTranslator

print(
    f"Translate dimulai pada jam {datetime.now().hour}:{datetime.now().minute}:{datetime.now().second}"
)
start = time.perf_counter()


# Import data berisi kumpulan job yang didapat, Run menggunakan venv di directory "Code - Mapping to SFIA", ganti path sesuai kebutuhan!
full_job_path = "Scraping/docs/computer-science/7 days v5/combinedList_CSJobs_7_days_v5.xlsx"
full_jobs = pd.read_excel(full_job_path)
full_jobs = pd.DataFrame(full_jobs)

combined = []
long_length = []
for i, job in full_jobs.iterrows():
    
    if len(job['job_description']) < 5000:
        job_description = GoogleTranslator(source="auto", target="en").translate(job["job_description"])

        combined.append(
            {
                "job_source": job["job_source"],
                "keyword": job["keyword"],
                "job_title": job["job_title"],
                "company": job["company"],
                "job_description": job_description
            }
        )
        print(f"Telah translate job ke {i+1}")
    else:
        long_length.append({
            "job_source": job["job_source"],
            "job_title": job["job_title"],
            "company": job["company"]
        })
        print(f"Job ke {i+1} kepanjangan, karakternya {len(job['job_description'])}")
        combined.append(
            {
                "job_source": job["job_source"],
                "keyword": job["keyword"],
                "job_title": job["job_title"],
                "company": job["company"],
                "job_description": job["job_description"]
            }
        )

print(f"Yang kepanjangan:\n{long_length}")
combined = pd.DataFrame(combined)
combined.to_excel("Scraping/docs/computer-science/7 days v5/translated-combinedList_CSJobs_7_days_v5.xlsx", index=False)

print(
    f"Translate berakhir pada jam {datetime.now().hour}:{datetime.now().minute}:{datetime.now().second}"
)

end = time.perf_counter()
print(f"Translate selesai dalam {end - start:.6f} detik")