# Streamlit Front End for Spanish Bert Summarizer
import base64
import streamlit as st
import summ as sm

body = '''
La operación lo tenía todo para que saliera bien. Un científico con una carrera en ascenso, querido en su pueblo y respetado por sus investigaciones en cardiología molecular. 
Un académico reconocido con cara de buena gente, que se movía por las mejores universidades gracias a sus títulos, y una misión relativamente fácil de ejecutar. 
Su aspecto le ayudaba. Héctor Alejandro Cabrera Fuentes, robusto y bajo de estatura, nació hace 35 años en El Espinal, una pequeña comunidad de Oaxaca, uno de los Estados más pobres de México. Tenía pasaporte con varios visados y transitaba sin problemas por Estados Unidos, Francia o Alemania. 
Era, en resumen, un candidato perfecto para que Rusia se fijara en él.
El último encargo que le hicieron era proporcionar fotos y datos sobre un agente estadounidense del FBI que estaba investigando las actividades del espionaje ruso en Florida. Pero algo salió mal y el Agente Karla de Oaxaca fue detenido el pasado 17 de febrero en Miami. Atrapado entre dos superpotencias, como si se tratara de un thriller de la Guerra Fría, Cabrera admitió ante el FBI que Rusia lo había presionado para que se convirtiera en informante a cambio de sacar del país a las dos hijas que tiene con una mujer rusa. Cuando el caso llegó a las noticias se revelaron todo tipo de detalles rocambolescos: una confesión que enterraba la reputación de uno de los científicos más prometedores de México, dos esposas separadas por más de 8.000 kilómetros de distancia y tres continentes involucrados en una trama de espionaje y conspiración internacional.
¿Trabajando para Putin? ¿Espía ruso? ¿Otra esposa? "Son patrañas", responde su tía, Ana García, de 66 años. Para los habitantes de El Espinal, un humilde municipio de 10.000 habitantes, Héctor Cabrera es prácticamente un héroe. Becado para formarse como microbiólogo en la Universidad de Kazán (Rusia). Galardonado por el entonces presidente Dimitri Medvédev con el premio a la mejor tesis de maestría. Doctor con honores por la Universidad de Giessen (Alemania). Conferenciante de la Sociedad Europea de Cardiología. Contratado por la Universidad Nacional de Singapur como uno de los principales investigadores de un estudio sobre enfermedades cardiovasculares.
En Oaxaca, Cabrera era el genio que hablaba seis idiomas y que llegó a alturas inesperadas en un lugar acostumbrado antiguamente a ver crecer solo el trigo y el sorgo. "Nací en un lugar donde la gente tiene que trabajar duro para tener una vida mejor y con ese mantra he llegado adonde estoy", escribía el investigador en una carta enviada a la Universidad de Giessen en 2017. "No me cabe en la cabeza que Hectorcito sea un espía", lamenta su tío Javier Fuentes, de 64 años. En su pueblo hay quienes piensan que una mano negra movida por EE UU intenta terminar con su reputación debido a sus investigaciones científicas.
Hasta que fue detenido, el científico trabajaba como investigador en la Escuela de Medicina de la Universidad de Duke y en la Universidad Nacional de Singapur, donde tenía un sueldo de 7.500 dólares mensuales. Paralelamente recibía 5.000 dólares por trabajar para una compañía israelí con sede en Alemania. El científico reconoció en un tribunal de Florida que su patrimonio era de 100.000 dólares repartidos en cuentas bancarias de México y Estados Unidos.
Parte de ese dinero lo usaba para ayudar a su pueblo. "Lo veía y pensaba: 'Me gustaría ser como él", dice Nashira Solórzano, una joven de 17 años beneficiada por la asociación Por Oaxaca Más Investigadores, fundada por Cabrera, con una estancia de investigación en octubre pasado. "Nunca me imaginé visitar Singapur, me abrió el panorama de lo que quería ser como músico y como persona. Nos ayudó muchísimo", explica Yoel Matus, de 17 años, miembro del grupo de marimba Perlas y Diamantes, que visitó Asia en 2017 gracias a las gestiones de Cabrera.
"Siempre que venía, nos qruedábamos tomando unos tragos y nos lo contábamos todo: deslices, problemas, lo que fuera", explica Hazael Matus, alcalde de El Espinal y una de las personas más cercanas a Cabrera, a quien conoce desde hace más de una década. "Nunca me habló de una novia o una familia rusa, nunca me dijo que tuviera problemas con algún Gobierno, que alguien lo estuviera amenazando", asegura. El alcalde habló con Cabrera por última vez apenas cuatro días antes de su detención en Miami, a donde el científico había ido a festejar el cumpleaños de uno de sus hijos mexicanos, según le contó.
La única versión conocida sobre el papel que desempeñaba Cabrera es la declaración jurada que realizó el lunes 17 de febrero durante la vista oral en Florida, en la que admitía que empezó a espiar en 2018. Cabrera llegó en 2004 a Voronezh, una ciudad industrial del centro de Rusia, sin saber una palabra de ruso y en una época en la que eran frecuentes los ataques hacia los extranjeros; incluso fue agredido una vez. En 2005 se marchó a Kazán, una ciudad de la República de Tatarstán, cerca de los Urales, donde se quedó cinco años y fue un estudiante notable, según varias fuentes. La Universidad Federal de Kazán, una de las principales del país, no quiso comentar el caso y ha cerrado todas las páginas que mencionan a Cabrera.
Cabrera se casó en Kazán con una joven musulmana, Aliyá Valéyeva. Tras la insistencia de su suegra rusa, tuvieron una ceremonia tradicional en la mezquita principal de Tatarstán. En una fotografía de ese día, recogida por la prensa local como noticia de que un joven mexicano relevante en la universidad se había unido a una joven tártara, aparece Cabrera sonriente, tocado con el sombrero típico. Ella, con un ramo de rosas rosas y un velo blanco. "Alejandro hablaba ruso perfecto, sin acento y sabía muchas palabras en tártaro", cuenta Lika Isaeva, que lo entrevistó para el diario local Nuestra Casa Tatarstán. Isaeva, ahora periodista en Komsomólskaya Pravda, asegura que Cabrera tenía mucha vida social y un conocido de esa época resalta que el científico mexicano era "algo mujeriego".
En 2010, Cabrera y Valéyeva se fueron juntos de Kazán a Alemania. Allí estuvieron varios años hasta que el científico se mudó a Singapur. Ni Isaeva, que mantuvo contacto durante años con la pareja, ni otros conocidos en Kazán saben nada desde hace tiempo de Aliya Valeyéva ni de las dos hijas que tienen en común. No están ni siquiera seguros de que ella haya vuelto a Tatarstán, pero están convencidos de que siguen casados. También creen factible que Cabrera estuviera intentando obtener visados y papeles para ellas.
Según el sumario judicial estadounidense, un agente ruso le ofreció a Cabrera facilitar la salida de sus hijas de Rusia —que habían regresado de Alemania junto con su madre para tramitar sus pasaportes y fueron retenidas por agentes de aduana rusos por razones que se desconocen—, a cambio de que realizara una misión para ellos. "Podemos ayudarnos mutuamente", le dijo el misterioso hombre que lo buscó tras una conferencia en Moscú.
Desde entonces empezó a colaborar con ellos y ha viajado al menos cinco veces en los últimos meses a Moscú. En su última misión, los servicios secretos rusos pidieron a Cabrera que localizara el automóvil de un agente del FBI, obtuviera el número de placa y anotara la ubicación física del vehículo. Para ello se coló en una zona residencial de Miami aprovechando que se abrió la puerta y que otro vehículo estaba entrando. Su operación fue tan poco sutil que llamó la atención del equipo de seguridad del edificio, que en minutos encontró al hombre y a su esposa mexicana tomando fotos con su teléfono y los expulsó del lugar.
Aquello levantó las sospechas y en el aeropuerto pidieron revisar sus pertenencias. Los agentes inspeccionaron el teléfono de la esposa de Cabrera y encontraron una imagen de la matrícula del vehículo de la fuente del Gobierno de EE UU en la carpeta de "eliminados recientemente" de su teléfono que había sido enviada por WhatsApp. "Cuando se le preguntó sobre la imagen, Cabrera Fuentes admitió que le había encargado a su compañera que tomara la foto", señala el sumario. 
Lo precipitado de su confesión, el uso de una red poco discreta para transmitir información que se supone sensible y el desastre de la operación contrasta con el retrato del conspirador extranjero que pintan los fiscales estadounidenses.
Una conversación entre el alcalde y la esposa de Cabrera revela detalles que no se conocían sobre lo que sucedió en las horas previas a la detención, después del altercado con los guardias del edificio. 
"Iban a volar a México por la tarde [16 de febrero] e iban con poco tiempo para abordar, les pasaba seguido", relata Matus. 
La pareja llegó al control migratorio del aeropuerto y les pidieron que sacaran su teléfono. 
"Me dijo que los pusieron en cuartos separados y los interrogaron hasta las dos o tres de la mañana", cuenta. Siempre según esta versión, la pareja perdió el vuelo y pasó la noche en un hotel de Miami. 
Al día siguiente, Cabrera regresó al aeropuerto con su esposa y su hija, les entregó dos pases de abordar y les dijo: "Yo no me voy, tengo que quedarme a resolver un problema", ante la sorpresa de su esposa.
Fuentes diplomáticas creen que el servicio de inteligencia ruso podría tener interés en vigilar a un "grupo de traidores rusos" que se han afincado en Miami. 
Creen que podrian tener "algo sobre él" que pueda resultar dañino, lo que le ha podido llevar a colaborar. Eso, señalan, "no es infrecuente".
Las autoridades estadounidenses lo acusan de conspirar y de actuar para un Gobierno extranjero y si es declarado culpable podría ser condenado a cadena perpetua. "Lo que más le duele a la familia es que Héctor se quedó completamente solo, nadie le contesta el teléfono, todos le dieron la espalda", dice el alcalde, que mandó la semana pasada una carta al Gobierno mexicano para que interviniera en favor de Cabrera.
El caso se ha convertido en una carrera contra reloj. 
Con las cuentas de Cabrera congeladas, sus allegados buscan conseguir tres millones de pesos (más de 150.000 dólares) para contratar a un abogado y encarar el juicio, que empieza el próximo 3 de marzo. 
Los bancos han negado el préstamo y su círculo cercano ya se organiza para conseguir el dinero. 
El alcalde, los vecinos, los músicos y los jóvenes estudiantes no paran de darle vueltas a lo ocurrido con su vecino más ilustre. 
¿Habrá hecho enojar con sus descubrimientos a las grandes farmacéuticas?
 ¿Se volvió una moneda de cambio entre Rusia y Estados Unidos?
 ¿Es parte de una persecución científica? 
"No queremos que lo liberen, lo único fque pedimos es que Héctor tenga un juicio justo y una defensa real", afirma el alcalde Matus.
'''

# Parameters
coreference = True
greedyness = 0.40
min_lenght = 75
max_lenght = 600
spacy_model = ('es_core_news_sm', 'es_core_news_md', 'es_core_news_lg')
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
