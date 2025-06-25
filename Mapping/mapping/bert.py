import pandas as pd, ast, torch
from transformers import BertTokenizer, BertModel
from sklearn.metrics.pairwise import cosine_similarity

sfia_path = pd.read_excel("D:/Kuliah/Skripsi/Code - Mapping to SFIA/Mapping/docs/sfia/sfia-9_skillner-bert.xlsx")
sfia = pd.DataFrame(sfia_path).head(1)

job_path = pd.read_excel("D:/Kuliah/Skripsi/Code - Mapping to SFIA/Mapping/docs/jobs/information-systems/(dump)-isjobs_skillner-bert_3weeeks.xlsx")
job = pd.DataFrame(job_path).head(1)

tokenizer = BertTokenizer.from_pretrained("google-bert/bert-base-uncased")
model = BertModel.from_pretrained("google-bert/bert-base-uncased")

levels = [f"Level {i} Skills" for i in range(1, 8)]

# Combine (set()) description skills per job
def setJobSkills():
    desc_skills_set = set()
    for i, desc in job.iterrows():
        desc_skills = ast.literal_eval(desc["description_skills"])
        try:
            desc_skills_set.update(desc_skills)
        except Exception as e:
            print(f"Terjadi error di data {i}: {e}")
    desc_skills_set = " ".join(desc_skills_set)
    return desc_skills_set

# Combine description skills per job (allows double)
def combineJobSkills():
    desc_skills_free = []
    for i, desc in job.iterrows():
        desc_skills = ast.literal_eval(desc["description_skills"])
        try:
            desc_skills_free.extend(desc_skills)
        except Exception as e:
            print(f"Terjadi error di data {i}: {e}")
    desc_skills_free = " ".join(desc_skills_free)
    return desc_skills_free

# BERT extraction
def bert(text):
    inputs = tokenizer(text, return_tensors='pt', truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
    # Ambil mean dari semua token embeddings (kecuali padding)
    embeddings = outputs.last_hidden_state.squeeze(0)
    attention_mask = inputs['attention_mask'].squeeze(0)
    mask = attention_mask.unsqueeze(-1).expand(embeddings.size()).float()
    masked_embeddings = embeddings * mask
    summed = torch.sum(masked_embeddings, dim=0)
    summed_mask = torch.clamp(mask.sum(dim=0), min=1e-9)
    mean_pooled = summed / summed_mask
    return mean_pooled.numpy()

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

            # BERT
            sfia_bert = bert(level_skills)
            job_bert = bert(setJobSkills())

            # Count similarity
            similarity_matrix = cosine_similarity([sfia_bert], [job_bert])
            similarity = (similarity_matrix[0][0])
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

# mapping.to_excel("D:/Kuliah/Skripsi/Code - Mapping to SFIA/Mapping/mapping/docs/information-systems_skillner-bert_tf-idf.xlsx", index=False)

mapping