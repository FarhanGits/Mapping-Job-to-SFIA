import time, pandas as pd
from datetime import datetime

# Cek lama waktu ekstraksi
print(
    f"Ekstraksi skill dimulai pada jam {datetime.now().hour}:{datetime.now().minute}:{datetime.now().second}"
)
start = time.perf_counter()

import spacy
from spacy.matcher import PhraseMatcher

from skillNer.general_params import SKILL_DB
from skillNer.skill_extractor_class import SkillExtractor

nlp = spacy.load("en_core_web_lg")
skill_extractor = SkillExtractor(nlp, SKILL_DB, PhraseMatcher)

# SkillNER
def skillNER(desc):
    desc_annotate = skill_extractor.annotate(desc)

    full_matches_desc = []
    for skills in desc_annotate["results"]["full_matches"]:
        full_matches_desc.append(skills["doc_node_value"])

    ngram_scored_desc = []
    for skills in desc_annotate["results"]["ngram_scored"]:
        ngram_scored_desc.append(skills["doc_node_value"])
    annotated_desc_skills = full_matches_desc + ngram_scored_desc

    all_desc_skills = set(annotated_desc_skills)
    desc_skills = []
    for skills in all_desc_skills:
        desc_skills.append(skills)
    # level_skills = ", ".join(level_skills)

    return desc_skills

# Run menggunakan venv di directory "Code - Mapping to SFIA", ganti path sesuai kebutuhan!
job_path = "Scraping/docs/computer-science/CSJobs.xlsx"
job_list = pd.read_excel(job_path)
job_list = pd.DataFrame(job_list)

job_skill = []
job_skill_compare = []
for i, job in job_list.iterrows():
    print(f"{i}. {job['job_title']}") # debugging skillner
    job_description = job["job_description"]
    desc_skills = skillNER(job_description)

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

# Run menggunakan venv di directory "Code - Mapping to SFIA", ganti path sesuai kebutuhan!
job_skill.to_excel("Mapping/docs/skills/jobs/computer-science/csjobs_skillner.xlsx", index=False)
job_skill_compare.to_excel("Mapping/docs/skills/jobs/computer-science/compare/compare-csjobs_skillner.xlsx", index=False)

end = time.perf_counter()
print(f"Ekstraksi skill selesai dalam {end - start:.6f} detik")