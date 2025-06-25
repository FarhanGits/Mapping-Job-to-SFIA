import ast
import pandas as pd
import qe_function

# Run menggunakan venv di directory "Code - Mapping to SFIA", ganti path sesuai kebutuhan!
data = pd.read_excel("Mapping/docs/skills/jobs/computer-science/compare/compare-csjobs_skillner-bert.xlsx")
data = pd.DataFrame(data)

array_job = []
array_job_compare = []
for i, job in data.iterrows():
    skills = job["description_skills"]
    # print(skills) # debug

    # Buat dictionary dulu
    job_dict = {"description_skills": skills}

    if pd.notna(skills):
        desc_skills = ast.literal_eval(skills)
        synonym = qe_function.get_synonyms(desc_skills)
        hypernym = qe_function.get_hypernyms(desc_skills)
        hyponym = qe_function.get_hyponyms(desc_skills)

        # 1. Sinonim
        # 2. Sinonim & Hipernim
        # 3. Sinonim, Hipernim, & Hiponim
        job_dict["description_skills_expanded"] = list(set(desc_skills + synonym + hypernym + hyponym))
        # print(list(set(desc_skills + synonym + hypernym + hyponym))) # debug
    else:
        desc_skills = ""
        synonym = ""
        hypernym = ""
        hyponym = ""

    array_job.append(job_dict)
    array_job_compare.append({
        "job_source": job["job_source"],
        "keyword": job["company"],
        "job_title": job["job_title"],
        "company": job["company"],
        "job_description": skills,
        "description_skills": desc_skills,
        "description_skills_expanded": list(set(desc_skills + synonym + hypernym + hyponym))
    })

qe_job = pd.DataFrame(array_job)
qe_job_compare = pd.DataFrame(array_job_compare)

qe_job.to_excel("Mapping/docs/qe/jobs/computer-science/csjobs_skillner-bert_synonym_hypernym_hyponym.xlsx", index=False, engine="openpyxl")
qe_job_compare.to_excel("Mapping/docs/qe/jobs/computer-science/compare/compare-csjobs_skillner-bert_synonym_hypernym_hyponym.xlsx", index=False, engine="openpyxl")