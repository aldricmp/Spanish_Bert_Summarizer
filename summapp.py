# Streamlit Front End for Spanish Bert Summarizer
import base64
import streamlit as st
import summ as sm


f=open("nota.txt", "r")
body=f.read()
# Parameters
coreference = True
greedyness = 0.40
min_lenght = 75
max_lenght = 600
spacy_model = ('es_core_news_sm', 'es_core_news_md')
bert_model_dic = ("dccuchile/bert-base-spanish-wwm-cased",
                  "mrm8488/bert-spanish-cased-finetuned-pos",
                  "mrm8488/bert-spanish-cased-finetuned-ner")

# SideBar Widgets
st.sidebar.image("http://www.scientive-ai.com/wp-content/uploads/2020/06/scientive_logo_300.png")
st.sidebar.markdown('# Parámetros')
bert_model = st.sidebar.selectbox(label='Modelo Bert', options=bert_model_dic)
spacy_model = st.sidebar.selectbox(label='SpaCy', options=spacy_model)
greedyness = st.sidebar.slider('Greedyness', 0.35, 0.45, greedyness)
min_lenght = st.sidebar.number_input('Min Lenght', 30, 500, min_lenght)
max_lenght = st.sidebar.number_input('Max Lenght', 30, 600, max_lenght)
coreference = st.sidebar.checkbox('Coreference', coreference)

# Main Page
st.image("http://www.scientive-ai.com/wp-content/uploads/2020/06/scientive_logo_300.png")
st.title('Resumen de Textos')
'''
## Entrada
'''
body = st.text_area(value=body, height=350, label='')
if st.button('Resumir'):
    summarized_text = sm.Summ(spacy_model, body, coreference, greedyness, min_lenght, max_lenght, bert_model)
    '''
    ## Resumen
    '''
    st.write(summarized_text)
    df = summarized_text
    csv = df
    b64 = base64.b64encode(df.encode()).decode()  # some strings <-> bytes conversions necessary here
    href = f'<a href="data:file/csv;base64,{b64}" download="resumen.txt">Descargar Resumen</a>'
    st.markdown(href, unsafe_allow_html=True)
