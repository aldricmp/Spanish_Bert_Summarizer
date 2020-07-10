# Keyword generator using spaCy's ENR
import spacy
from itertools import *
from collections import Counter


# Keyword generation with no spaces between words, sorted by entity type
def spacy_enr_keywords(text, spacy_model):
    nlp = spacy.load(spacy_model)
    result = []
    list_ents = []
    per = []
    org = []
    loc = []
    misc = []
    doc = nlp(text)
    # Create dictionary with entity types as keys
    entities = {key: list(g) for key, g in groupby(sorted(doc.ents, key=lambda x: x.label_), lambda x: x.label_)}
    # remove spaces bewtween words
    if entities.get('PER') != None:
        for x in entities['PER']:
            x = str(x.text).replace(" ", "")
            per.append(x)
    if entities.get('ORG') != None:
        for x in entities['ORG']:
            x = str(x.text).replace(" ", "")
            org.append(x)
    if entities.get('LOC') != None:
        for x in entities['LOC']:
            x = str(x.text).replace(" ", "")
            loc.append(x)
    if entities.get('MISC') != None:
        for x in entities['MISC']:
            x = str(x.text).replace(" ", "")
            misc.append(x)
    for ents in doc.ents:
        list_ents.append(ents)
        ents_no_spaces = str(ents.text).replace(" ", "")
        result.append(ents_no_spaces)
        # Return Entities as string with No spaces between word (maybe turn it to pandas dataset?)
    return per, org, loc, misc, result

# Hashtagging keywords
def hashtag_keywords(body, spacy_model):
    per, org, loc, misc, all = spacy_enr_keywords(body, spacy_model)
    per_hashtags = [('#' + x[0]) for x in Counter(per).most_common(10)]
    org_hashtags = [('#' + x[0]) for x in Counter(org).most_common(10)]
    loc_hashtags = [('#' + x[0]) for x in Counter(loc).most_common(10)]
    misc_hashtags = [('#' + x[0]) for x in Counter(misc).most_common(10)]
    all_hashtags = [('#' + x[0]) for x in Counter(all).most_common(10)]
    per_hashtags = ' '.join(per_hashtags)
    org_hashtags = ' '.join(org_hashtags)
    loc_hashtags = ' '.join(loc_hashtags)
    misc_hashtags = ' '.join(misc_hashtags)
    all_hashtags = ' '.join(all_hashtags)
    return per_hashtags, org_hashtags, loc_hashtags, misc_hashtags, all_hashtags
