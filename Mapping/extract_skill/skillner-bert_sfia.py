# Libraly
import traceback
import pandas as pd
from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline

# Load the pre-trained model and tokenizer
model_name = "Nucha/Nucha_SkillNER_BERT"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForTokenClassification.from_pretrained(model_name)

# Create a NER pipeline
ner_pipeline = pipeline(
    "ner", model=model, tokenizer=tokenizer, aggregation_strategy="simple"
)


# SkillNER - BERT
def skillNERBERT(level):
    ner_results = ner_pipeline(level)

    all_skills = []
    for entity in ner_results:
        all_skills.append(entity["word"])

    level_skills = []
    all_skills = set(all_skills)
    for skills in all_skills:
        level_skills.append(skills)

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
            level1_skills = skillNERBERT(level_1)
        else:
            level1_skills = ""

        # Level 2
        if pd.notna(level_2):
            level2_skills = skillNERBERT(level_2)
        else:
            level2_skills = ""

        # Level 3
        if pd.notna(level_3):
            level3_skills = skillNERBERT(level_3)
        else:
            level3_skills = ""

        # Level 4
        if pd.notna(level_4):
            level4_skills = skillNERBERT(level_4)
        else:
            level4_skills = ""

        # Level 5
        if pd.notna(level_5):
            level5_skills = skillNERBERT(level_5)
        else:
            level5_skills = ""

        # Level 6
        if pd.notna(level_6):
            level6_skills = skillNERBERT(level_6)
        else:
            level6_skills = ""

        # Level 7
        if pd.notna(level_7):
            level7_skills = skillNERBERT(level_7)
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
        traceback.print_exc
        break

hasil_ekstrak = pd.DataFrame(hasil_coba_ekstrak)

# print(hasil_ekstrak)
# print(hasil_coba_ekstrak)

# Run menggunakan venv di directory "Code - Mapping to SFIA", ganti path sesuai kebutuhan!
# hasil_ekstrak.to_excel('./docs/sfia-9-skills.xlsx', index=False)
hasil_ekstrak.to_excel("./Mapping/docs/sfia-9_skillner-bert.xlsx", index=False)
print("Ekstraksi SFIA - SkillNER-BERT selesai!")
