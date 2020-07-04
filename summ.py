#  Substractive summarizer function implementing BERT EXTRACITVE SUMMARIZER
#  BERT EXTRACTIVE SUMMARIZER => https://pypi.org/project/bert-extractive-summarizer/
#  HuuginFace Pretrained BERT MODEL => https://huggingface.co/mrm8488/bert-spanish-cased-finetuned-pos
#  SpaCy => https://spacy.io/usage/models
#  StreamLite =>https://www.streamlit.io

from summarizer import Summarizer
from summarizer.coreference_handler import CoreferenceHandler
from transformers import *


def Summ(spacy_model, body,ratio, coreference, greedyness, min_lenght,max_lenght,bert_model ):
    # Loading Spanish BETO custom model (output_hidden_states must be set to True) and tokenizer
    custom_config = AutoConfig.from_pretrained(pretrained_model_name_or_path=bert_model)
    custom_config.output_hidden_states = True
    custom_tokenizer = AutoTokenizer.from_pretrained(bert_model)
    custom_model = AutoModel.from_pretrained(bert_model, config=custom_config)

    handler = CoreferenceHandler(spacy_model=spacy_model, greedyness=greedyness)
    if coreference:
        model = Summarizer(custom_model=custom_model, custom_tokenizer=custom_tokenizer, sentence_handler=handler)
        result = model(body, min_length=min_lenght)
        full = ''.join(result)

    else:
        model = Summarizer(custom_model=custom_model, custom_tokenizer=custom_tokenizer)
        result = model(body, ratio=ratio,min_length=min_lenght,max_lenght=max_lenght)
        full = ''.join(result)
    return full
