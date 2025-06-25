import traceback
import pandas as pd

import spacy
from spacy.matcher import PhraseMatcher

from skillNer.general_params import SKILL_DB
from skillNer.skill_extractor_class import SkillExtractor

nlp = spacy.load("en_core_web_lg")
skill_extractor = SkillExtractor(nlp, SKILL_DB, PhraseMatcher)


# SkillNER
def skillNER(text):
    level_annotate = skill_extractor.annotate(text)

    full_matches_level = []
    for skills in level_annotate["results"]["full_matches"]:
        full_matches_level.append(skills["doc_node_value"])

    ngram_scored_level = []
    for skills in level_annotate["results"]["ngram_scored"]:
        ngram_scored_level.append(skills["doc_node_value"])
    annotated_level_skills = full_matches_level + ngram_scored_level

    all_level_skills = set(annotated_level_skills)
    level_skills = []
    for skills in all_level_skills:
        level_skills.append(skills)
    # level_skills = ", ".join(level_skills)

    return level_skills


# Run menggunakan venv di directory "Code - Mapping to SFIA", ganti path sesuai kebutuhan!
# data = pd.read_excel("./docs/sfia-9_en.xlsx")
data = pd.read_excel("./Mapping/docs/sfia-9_en.xlsx")
data = pd.DataFrame(data)

hasil_coba_ekstrak = []
for index in range(len(data)):

    # print("data ke ", index)
    skill = data.at[index, "Skill"]
    level_1 = data.at[index, "Level 1 description"]
    level_2 = data.at[index, "Level 2 description"]
    level_3 = data.at[index, "Level 3 description"]
    level_4 = data.at[index, "Level 4 description"]
    level_5 = data.at[index, "Level 5 description"]
    level_6 = data.at[index, "Level 6 description"]
    level_7 = data.at[index, "Level 7 description"]

    try:
        # Level 1
        if pd.notna(level_1):
            level1_skills = skillNER(level_1)
        else:
            level1_skills = ""

        # Level 2
        if pd.notna(level_2):
            level2_skills = skillNER(level_2)
        else:
            level2_skills = ""

        # Level 3
        if pd.notna(level_3):
            level3_skills = skillNER(level_3)
        else:
            level3_skills = ""

        # Level 4
        if pd.notna(level_4):
            level4_skills = skillNER(level_4)
        else:
            level4_skills = ""

        # Level 5
        if pd.notna(level_5):
            level5_skills = skillNER(level_5)
        else:
            level5_skills = ""

        # Level 6
        if pd.notna(level_6):
            level6_skills = skillNER(level_6)
        else:
            level6_skills = ""

        # Level 7
        if pd.notna(level_7):
            level7_skills = skillNER(level_7)
        else:
            level7_skills = ""

        hasil_coba_ekstrak.append(
            {
                "Skill": skill,
                "Level 1 Skills": level1_skills,
                "Level 2 Skills": level2_skills,
                "Level 3 Skills": level3_skills,
                "Level 4 Skills": level4_skills,
                "Level 5 Skills": level5_skills,
                "Level 6 Skills": level6_skills,
                "Level 7 Skills": level7_skills,
            }
        )

    except:
        traceback.print_exc()
        break

hasil_ekstrak = pd.DataFrame(hasil_coba_ekstrak)

# print(hasil_ekstrak)
# print(hasil_coba_ekstrak)

# Run menggunakan venv di directory "Code - Mapping to SFIA", ganti path sesuai kebutuhan!
# hasil_ekstrak.to_excel('./docs/sfia-9-skills.xlsx', index=False)
hasil_ekstrak.to_excel("./Mapping/docs/sfia-9_skillner.xlsx", index=False)
print("Ekstraksi SFIA - SkillNER selesai!")
