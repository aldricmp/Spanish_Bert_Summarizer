import spacy
from itertools import *

f = open("nota.txt", "r")
text = f.read()


def get_enr_keywords(text, spacy_model):
    nlp = spacy.load(spacy_model)
    result = []
    list_ents = []
    per = []
    org = []
    loc = []
    misc = []

    doc = nlp(text)
    entities = {key: list(g) for key, g in groupby(sorted(doc.ents, key=lambda x: x.label_), lambda x: x.label_)}
    for x in entities['PER']:
        x = str(x.text).replace(" ", "")
        per.append(x)
    for x in entities['ORG']:
        org.append(x.text)
    for x in entities['LOC']:
        loc.append(x.text)
    for x in entities['MISC']:
        misc.append(x.text)
    for ents in doc.ents:
        list_ents.append(ents)
        ents_no_spaces = str(ents.text).replace(" ", "")
        result.append(ents_no_spaces)
    return per,org,loc,misc,result  # Return words as string
