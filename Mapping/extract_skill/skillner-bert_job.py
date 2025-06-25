import time, pandas as pd
from datetime import datetime
from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline

# Cek lama waktu ekstraksi
print(
    f"Ekstraksi skill dimulai pada jam {datetime.now().hour}:{datetime.now().minute}:{datetime.now().second}"
)
start = time.perf_counter()

# Load the pre-trained model and tokenizer
model_name = "Nucha/Nucha_SkillNER_BERT"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForTokenClassification.from_pretrained(model_name)

# Create a NER pipeline
ner_pipeline = pipeline(
    "ner", model=model, tokenizer=tokenizer, aggregation_strategy="simple"
)

# SkillNER - BERT
def skillNERBERT(desc):
    ner_results = ner_pipeline(desc)

    all_skills = []
    for entity in ner_results:
        all_skills.append(entity["word"])

    all_skills = set(all_skills)
    desc_skills = []
    for skills in all_skills:
        desc_skills.append(skills)

    return desc_skills

# Run menggunakan venv di directory "Code - Mapping to SFIA", ganti path sesuai kebutuhan!
job_path = "Scraping/docs/computer-science/CSJobs.xlsx"
job_list = pd.read_excel(job_path)
job_list = pd.DataFrame(job_list)

job_skill = []
job_skill_compare = []
for i, job in job_list.iterrows():
    print(f"{i}. {job['job_title']}") # debugging skillner-bert
    job_description = job["job_description"]
    desc_skills = skillNERBERT(job_description)

    job_skill.append({
        "description_skills": desc_skills
    })

    job_skill_compare.append({
        "job_source": job["job_source"],
        "keyword": job["company"],
        "job_title": job["job_title"],
        "company": job["company"],
        "job_description": job_description,
        "description_skills": desc_skills
    })

job_skill = pd.DataFrame(job_skill)
job_skill_compare = pd.DataFrame(job_skill_compare)

job_skill.to_excel("Mapping/docs/skills/jobs/computer-science/csjobs_skillner-bert.xlsx", index=False)
job_skill_compare.to_excel("Mapping/docs/skills/jobs/computer-science/compare/compare-csjobs_skillner-bert.xlsx", index=False)

end = time.perf_counter()
print(f"Ekstraksi skill selesai dalam {end - start:.6f} detik")