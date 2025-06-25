import ast
import traceback, pandas as pd
import qe_function

# Run menggunakan venv di directory "Code - Mapping to SFIA", ganti path sesuai kebutuhan!
# data = pd.read_excel("Mapping/docs/skills/sfia/sfia-9_skillner.xlsx")
data = pd.read_excel("Mapping/docs/skills/sfia/sfia-9_skillner-bert.xlsx")
data = pd.DataFrame(data)

levels = [f"Level {i} Skills" for i in range(1, 8)]

array_sfia = []
for i, row in data.iterrows():
    # Ambil skill
    skill = row["Skill"]

    # Buat dictionary
    sfia_dict = {"Skill": skill}

    # Looping per level
    for j, col in enumerate(levels, start=1):
        raw_data = row[col]

        if pd.notna(raw_data):
            # Disini untuk merubah data string ke array asli (walaupun di excel penulisannya array, tetap dibaca string biasa)
            level_skills = ast.literal_eval(raw_data)

            # ============================== QUERY EXPANSION DISINI ==============================
            synonym = qe_function.get_synonyms(level_skills)
            hypernym = qe_function.get_hypernyms(level_skills)
            hyponym = qe_function.get_hyponyms(level_skills)
            
            # 1. Sinonim
            # 2. Sinonim & Hipernim
            # 3. Sinonim, Hipernim, & Hiponim
            sfia_dict[f"Level {j} Skills"] = list(set(level_skills + synonym + hypernym + hyponym))
        else:
            sfia_dict[f"Level {j} Skills"] = ""

    array_sfia.append(sfia_dict)

qe_sfia = pd.DataFrame(array_sfia)
qe_sfia.to_excel("Mapping/docs/qe/sfia/sfia-9_skillner-bert_synonym_hypernym_hyponym.xlsx", index=False)
