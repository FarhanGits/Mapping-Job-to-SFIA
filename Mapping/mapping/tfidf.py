import pandas as pd, ast
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

job_path = pd.read_excel("D:/Kuliah/Skripsi/Code - Mapping to SFIA/Mapping/docs/qe/jobs/information-systems/isjobs_skillner-bert_synonym.xlsx")
job = pd.DataFrame(job_path)

sfia_path = pd.read_excel("D:/Kuliah/Skripsi/Code - Mapping to SFIA/Mapping/docs/qe/sfia/sfia-9_skillner-bert_synonym.xlsx")
sfia = pd.DataFrame(sfia_path)

vectorizer = TfidfVectorizer()

levels = [f"Level {i} Skills" for i in range(1, 8)]

# Combine (set()) description skills per job
def setJobSkills():
    desc_skills_set = set()
    for i, desc in job.iterrows():

        # Perhatikan nama kolom skill:
        # - "description_skills" untuk skillner/-bert TANPA query-expansion
        # - "description_skills_expanded" untuk skillner/-bert DENGAN query-expansion
        desc_skills = ast.literal_eval(desc["description_skills_expanded"])
        try:
            desc_skills_set.update(desc_skills)
        except Exception as e:
            print(f"Ada error di data {i}: {e}")
    desc_skills_set = " ".join(desc_skills_set)
    return desc_skills_set

# # Combine description skills per job (allows double)
# def combineJobSkills():
#     desc_skills_free = []
#     for i, desc in job.iterrows():
#         desc_skills = ast.literal_eval(desc["description_skills_expanded"])
#         try:
#             desc_skills_free.extend(desc_skills)
#         except Exception as e:
#             print(f"Ada error di data {i}: {e}")
#     desc_skills_free = " ".join(desc_skills_free)
#     return desc_skills_free

mapping = []
# Looping per skill sfia
for i, skill in sfia.iterrows():
    # Ambil skill
    skills = skill["Skill"]

    # Buat dictionary
    sfia_dict = {"Skill": skills}
    
    # Looping per level
    for j, level in enumerate(levels, start=1):
        sfia_skills = skill[level]

        if pd.notna(sfia_skills):
            level_skills = ast.literal_eval(sfia_skills)
            level_skills = " ".join(level_skills)

            # TF-IDF
            tfidf_matrix = vectorizer.fit_transform([level_skills, setJobSkills()])

            # Count similarity
            similarity_matrix = cosine_similarity(tfidf_matrix, tfidf_matrix)
            similarity = (similarity_matrix[0][1])
            # similarity = (similarity_matrix[0][1]) * 100
            similarity = round(similarity, 2)

        else:
            similarity = ""
        
        # if similarity:
        #     sims = float(similarity)
        #     if sims >= 0.5:
        #         print(f"{skill['Skill']} - Level {j} = {similarity}")

        sfia_dict[f"Level {j}"] = similarity
    
    mapping.append(sfia_dict)

mapping = pd.DataFrame(mapping)

mapping.to_excel("D:/Kuliah/Skripsi/Code - Mapping to SFIA/Mapping/docs/mapping/information-systems/tes-information-systems_skillner-bert_synonym_tf-idf.xlsx", index=False, engine="openpyxl")

mapping