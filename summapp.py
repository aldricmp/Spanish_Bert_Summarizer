# Streamlit Front End for Spanish Bert Summarizer
import base64
import streamlit as st
import summ as sm
import keywordgen as kw
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud,ImageColorGenerator
import numpy as np
from PIL import Image

f = open("nota.txt", "r")
body = f.read()
# Parameters
ratio=0.2
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
st.sidebar.markdown('# Ajustes')
st.sidebar.number_input('Ratio %',0.0,1.0,ratio)
min_lenght = st.sidebar.number_input('Cantidad mínima de caracteres en oración', 30, 500, min_lenght)
max_lenght = st.sidebar.number_input('Cantidad máxima de caracteres en oración', 30, 600, max_lenght)
st.sidebar.markdown('## Parámetros avanzados')
coreference = st.sidebar.checkbox('Coreference', coreference)
if coreference:
    greedyness = st.sidebar.slider('Coreference Greediness', 0.35, 0.45, greedyness)
bert_model = st.sidebar.selectbox(label='BERT', options=bert_model_dic)
spacy_model = st.sidebar.selectbox(label='SpaCy', options=spacy_model)




# Main Page
st.image("http://www.scientive-ai.com/wp-content/uploads/2020/06/scientive_logo_300.png")
st.title('Resumen de Textos')
'''
## Entrada
### Introduce el texto a resumir
'''
body = st.text_area(value=body, height=350, label='')
if st.button('Resumir'):
    per, org, loc, misc, entity_text = kw.get_enr_keywords(body, spacy_model)
    per_hashtags = [('#' + x[0]) for x in Counter(per).most_common(10)]
    org_hashtags = [('#' + x[0]) for x in Counter(org).most_common(10)]
    loc_hashtags = [('#' + x[0]) for x in Counter(loc).most_common(10)]
    misc_hashtags = [('#' + x[0]) for x in Counter(misc).most_common(100)]
    hashtags = [('#' + x[0]) for x in Counter(entity_text).most_common(10)]
    per_hashtags = ' '.join(per_hashtags)
    org_hashtags = ' '.join(org_hashtags)
    loc_hashtags = ' '.join(loc_hashtags)
    misc_hashtags = ' '.join(misc_hashtags)
    hashtags = ' '.join(hashtags)


    summarized_text = sm.Summ(spacy_model, body,ratio, coreference, greedyness, min_lenght, max_lenght, bert_model)

    '''## Resumen'''
    '''#### Nube de Palabras'''
    mask = np.array(Image.open("mex.png"))
    wordcloud_mex = WordCloud(background_color="white", mode="RGBA", max_words=1000, mask=mask).generate(
        ' '.join(entity_text))
    image_colors = ImageColorGenerator(mask)
    plt.figure(figsize=[5, 3])
    plt.imshow(wordcloud_mex.recolor(color_func=image_colors), interpolation="bilinear")
    plt.axis("off")
    wordcloud_mex.to_file("flag_cloud.png")
    st.image("flag_cloud.png")
    '''#### Palabras clave'''
    '''#### Frecuencia'''
    st.write(hashtags)
    '''#### Personas'''
    st.write(per_hashtags)
    '''#### Organizaciones'''
    st.write(org_hashtags)
    '''#### Ubicaciones'''
    st.write(loc_hashtags)
    '''#### Misceláneas (candidatas a eliminar)'''
    st.write(misc_hashtags)
    '''#### Resumen'''
    st.write(summarized_text)
    df = hashtags + "\r\n"+ per_hashtags + "\r\n"+ org_hashtags + "\r\n"+ loc_hashtags + "\r\n"+ misc_hashtags + "\r\n"+ summarized_text
    csv = df
    b64 = base64.b64encode(df.encode()).decode()  # some strings <-> bytes conversions necessary here
    href = f'<a href="data:file/csv;base64,{b64}" download="resumen.txt">Descargar Resumen</a>'
    st.markdown(href, unsafe_allow_html=True)












