from nltk.corpus import wordnet

# Sinonim
def synonyms(word):
    synonyms_set = set()
    sets = wordnet.synsets(word)
    for item in sets:
        for lemmas in item.lemmas():
            term = lemmas.name()
            synonyms_set.add(term)
    synonyms = []
    for synonym in synonyms_set:
        synonyms.append(synonym)
    return synonyms


def get_synonyms(skill_list):
    synonym_terms = []
    for skill in skill_list:
        term = synonyms(skill)
        synonym_terms.append(term)

    synonym = []
    for terms in synonym_terms:
        for term in terms:
            synonym.append(term)
    return synonym


# Hipernim
def hypernyms(word):
    hypernyms_set = set()
    sets = wordnet.synsets(word)
    for item in sets:
        for hypernym in item.hypernyms():
            for lemmas in hypernym.lemmas():
                term = lemmas.name()
                hypernyms_set.add(term)
    hypernyms = []
    for hypernym in hypernyms_set:
        hypernyms.append(hypernym)
    return hypernyms


def get_hypernyms(skill_list):
    hypernym_terms = []
    for skill in skill_list:
        term = hypernyms(skill)
        hypernym_terms.append(term)

    hypernym = []
    for terms in hypernym_terms:
        for term in terms:
            hypernym.append(term)
    return hypernym


# Hiponim
def hyponyms(word):
    hyponyms_set = set()
    sets = wordnet.synsets(word)
    for item in sets:
        for hyponym in item.hyponyms():
            for lemmas in hyponym.lemmas():
                term = lemmas.name()
                hyponyms_set.add(term)
    hyponyms = []
    for hyponym in hyponyms_set:
        hyponyms.append(hyponym)
    return hyponyms


def get_hyponyms(skill_list):
    hyponym_terms = []
    for skill in skill_list:
        term = hyponyms(skill)
        hyponym_terms.append(term)

    hyponym = []
    for terms in hyponym_terms:
        for term in terms:
            hyponym.append(term)
    return hyponym
