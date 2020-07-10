# Streamlit Front End for News Media Analysis
import base64
import streamlit as st
import summ as sm
import keywordgen as kw
import cloudgenerator as wc
import newsscrapper as ns
import time

# Model Parameters
ratio = 0.2
coreference = True
greediness = 0.40
min_lenght = 75
max_lenght = 600
spacy_model = ('es_core_news_sm', 'es_core_news_md')
bert_model_dic = ("dccuchile/bert-base-spanish-wwm-cased",
                  "mrm8488/bert-spanish-cased-finetuned-pos",
                  "mrm8488/bert-spanish-cased-finetuned-ner")
# Input paramaters
instagram_html = ''
tweet_html = ''
video_html = ''
url = 'https://www.milenio.com/politica/amlo-visita-presidente-mexico-aterriza-washington'

# SideBar Widgets
st.sidebar.image("http://www.scientive-ai.com/wp-content/uploads/2020/06/scientive_logo_300.png")
st.sidebar.markdown('# Ajustes')
st.sidebar.number_input('Ratio %', 0.0, 1.0, ratio)
min_lenght = st.sidebar.number_input('Cantidad mínima de caracteres en oración', 30, 500, min_lenght)
max_lenght = st.sidebar.number_input('Cantidad máxima de caracteres en oración', 30, 600, max_lenght)
st.sidebar.markdown('## Parámetros avanzados')
coreference = st.sidebar.checkbox('Coreference', coreference)
if coreference:
    greediness = st.sidebar.slider('Coreference Greediness', 0.35, 0.45, greediness)
bert_model = st.sidebar.selectbox(label='BERT', options=bert_model_dic)
spacy_model = st.sidebar.selectbox(label='SpaCy', options=spacy_model)

# Main Page

# Header
st.image("http://www.scientive-ai.com/wp-content/uploads/2020/06/scientive_logo_300.png")
st.title('Análisis de Notas Informativas')

# Source Selection
'''## Fuente'''
input_selection = st.radio(label='', options=('URL', 'Texto'))
# Get URL content or example text from file ==> load it on text area
if input_selection == 'URL':
    '''### Introduce la dirección URL de la nota a resumir:'''
    url_input = st.text_input('', url)
    news_article, body, tweet_html, video_html, instagram_html = ns.get_news_from_url(url_input)

if input_selection == 'Texto':
    '''### Teclea o pega la nota a resumir'''
    # Load example text from file
    f = open("misc/nota.txt", "r")
    body = f.read()
    # Turn off  all other news features
    news_article = None

'''### Nota Informativa:'''
body = st.text_area(value=body, height=350, label='')

# Process News Contet
if st.button('Resumir'):
    tic = time.time()
    with st.spinner('Leyendo...'):

        # Generate hashtagged keywords
        per_hashtags, org_hashtags, loc_hashtags, misc_hashtags, all_hashtags = kw.hashtag_keywords(body, spacy_model)
        # Generate wordcloud
        wordcloud = wc.generate_wordcloud(all_hashtags)

    with st.spinner('Resumiendo, puede tomarme un momento...'):
        # Summarize News Text
        summarized_text = sm.Summ(spacy_model, body, ratio, coreference, greediness, min_lenght, max_lenght, bert_model)
    st.success('!Listo¡')

    # Display Results
    '''## Resumen'''
    if news_article:
        '''### Título:'''
        st.markdown('''### ''' + ''.join(news_article.title))
        '''#### Autor(es):'''
        st.markdown(' '.join(news_article.authors))
        '''#### Fecha:'''
        st.write(news_article.publish_date)
        '''#### Imágen Principal:'''
        st.image(news_article.top_image, width=600)
    '''#### Nube de Palabras:'''
    st.image(wordcloud)
    '''#### Palabras clave:'''
    '''#### Frecuencia'''
    st.write(all_hashtags)
    '''#### Personas'''
    st.write(per_hashtags)
    '''#### Organizaciones'''
    st.write(org_hashtags)
    '''#### Ubicaciones'''
    st.write(loc_hashtags)
    '''#### Misceláneas (candidatas a eliminar)'''
    st.markdown('''~~''' + misc_hashtags + '''~~''')
    '''#### Resumen:'''
    st.write(summarized_text)

    saved_text = all_hashtags + "\r\n" + per_hashtags + "\r\n" + org_hashtags + "\r\n" + loc_hashtags + "\r\n" \
                 + misc_hashtags + "\r\n" + summarized_text + "\r\n" + tweet_html + "\r\n" + instagram_html + "\r\n" + \
                 video_html
    # some strings <-> bytes conversions necessary here
    b64 = base64.b64encode(saved_text.encode()).decode()
    # Generate download link
    href = f'<a href="data:file/txt;base64,{b64}" download="resumen.txt">Descargar Resumen</a>'
    st.markdown(href, unsafe_allow_html=True)

    if news_article:
        '''### Twitter:'''
        st.markdown(tweet_html, unsafe_allow_html=True)
        '''### Instagram:'''
        st.markdown(instagram_html, unsafe_allow_html=True)
        '''### Videos:'''
        st.markdown(''.join(news_article.movies), unsafe_allow_html=True)
        if video_html != '':
            st.video(str(video_html))
    toc=time.time()
    st.write('Terminado en ' + "{:.2f} ".format(toc-tic)+'segs.')