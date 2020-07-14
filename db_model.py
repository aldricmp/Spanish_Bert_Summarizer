# coding: utf-8
from sqlalchemy import BigInteger, Column, DECIMAL, DateTime, Float, ForeignKey, Index, Integer, LargeBinary, String, TEXT, Table, Unicode
from sqlalchemy.dialects.mssql import BIT, SMALLDATETIME, UNIQUEIDENTIFIER
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


t_Base_completa = Table(
    'Base completa', metadata,
    Column('Id', Integer, nullable=False),
    Column('TW_ID', Unicode(255)),
    Column('TW_UserID', Float(53)),
    Column('TW_ScreenName', Unicode(255)),
    Column('TW_SinceID', Float(53)),
    Column('TW_MaxID', Float(53)),
    Column('TW_Count', Float(53)),
    Column('TW_Cursor', Float(53)),
    Column('TW_IncludeRetweets', Float(53)),
    Column('TW_ExcludeReplies', Float(53)),
    Column('TW_IncludeEntities', Float(53)),
    Column('TW_IncludeUserEntities', Float(53)),
    Column('TW_IncludeMyRetweet', Float(53)),
    Column('TW_OEmbedUrl', Unicode(255)),
    Column('TW_OEmbedMaxWidth', Float(53)),
    Column('TW_OEmbedHideMedia', Float(53)),
    Column('TW_OEmbedHideThread', Float(53)),
    Column('TW_OEmbedOmitScript', Float(53)),
    Column('TW_OEmbedAlign', Unicode(255)),
    Column('TW_OEmbedRelated', Unicode(255)),
    Column('TW_OEmbedLanguage', Unicode(255)),
    Column('TW_CreatedAt', DateTime),
    Column('TW_StatusID', Unicode(255)),
    Column('TW_Text', Unicode),
    Column('TW_Source', Unicode(255)),
    Column('TW_Truncated', Float(53)),
    Column('TW_InReplyToStatusID', Float(53)),
    Column('TW_InReplyToUserID', Float(53)),
    Column('TW_FavoriteCount', Float(53)),
    Column('TW_Favorited', Float(53)),
    Column('TW_InReplyToScreenName', Unicode(255)),
    Column('TW_Coordinates', Unicode(255)),
    Column('TW_Place', Unicode(255)),
    Column('TW_Annotation', Unicode(255)),
    Column('TW_Entities', Unicode(255)),
    Column('TW_ExtendedEntities', Unicode(255)),
    Column('TW_TrimUser', Float(53)),
    Column('TW_IncludeContributorDetails', Unicode(255)),
    Column('TW_RetweetCount', Float(53)),
    Column('TW_Retweeted', Float(53)),
    Column('TW_PossiblySensitive', Float(53)),
    Column('TW_RetweetedStatus', Float(53)),
    Column('TW_CurrentUserRetweet', Float(53)),
    Column('TW_QuotedStatusID', Float(53)),
    Column('TW_QuotedStatus', Unicode(255)),
    Column('TW_WithheldCopyright', Float(53)),
    Column('TW_WithheldInCountries', Unicode(255)),
    Column('TW_WithheldScope', Unicode(255)),
    Column('TW_MetaData', Float(53)),
    Column('TW_Lang', Unicode(255)),
    Column('TW_Map', Unicode(255)),
    Column('TW_TweetIDs', Unicode(255)),
    Column('TW_T_ID', Float(53)),
    Column('TW_INSERTADO', DateTime)
)


class CAGENCIA(Base):
    __tablename__ = 'C_AGENCIA'

    AG_ID = Column(BigInteger, primary_key=True)
    AG_NOMBRE = Column(String(200, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    AG_LG_ID = Column(BigInteger, nullable=False)


class CCLASIFICACION(Base):
    __tablename__ = 'C_CLASIFICACION'

    CL_ID = Column(Integer, primary_key=True)
    CL_PADRE_ID = Column(Integer, nullable=False)
    CL_NOMBRE = Column(String(collation='SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    CL_DESCRIPCION = Column(String(collation='SQL_Latin1_General_CP1_CI_AS'), nullable=False)


class CESTATUSSUSCRIPTOR(Base):
    __tablename__ = 'C_ESTATUS_SUSCRIPTOR'

    SS_ID = Column(Integer, primary_key=True)
    SS_DESCRIPCION = Column(String(200, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)


class CGRUPO(Base):
    __tablename__ = 'C_GRUPO'

    GR_ID = Column(Integer, primary_key=True)
    GR_NOMBRE_GRUPO = Column(String(2000, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)


class CMODULO(Base):
    __tablename__ = 'C_MODULO'

    MOD_ID = Column(Integer, primary_key=True)
    MOD_DESCRIPCION = Column(Unicode(200), nullable=False)


class CNLLAYOUT(Base):
    __tablename__ = 'C_NLLAYOUT'

    NL_ID = Column(Integer, primary_key=True)
    NL_NOMBRE = Column(String(2000, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)


class COFICINA(Base):
    __tablename__ = 'C_OFICINA'

    OFICINA_ID = Column(Integer, primary_key=True)
    OFICINA_NOMBRE = Column(String(2000, 'SQL_Latin1_General_CP1_CI_AS'))


class CPAI(Base):
    __tablename__ = 'C_PAIS'

    PAIS_ID = Column(Integer, primary_key=True)
    PAIS_NOMBRE = Column(String(200, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)


class CPERIODICIDAD(Base):
    __tablename__ = 'C_PERIODICIDAD'

    PER_ID = Column(Integer, primary_key=True)
    PER_NOMBRE = Column(String(1000, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    PER_DIAS = Column(Integer, nullable=False)
    PER_ACTIVO = Column(BIT, nullable=False)


class CPRODUCTO(Base):
    __tablename__ = 'C_PRODUCTOS'

    PR_ID = Column(Integer, primary_key=True)
    PR_NOMBRE = Column(String(1000, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)


class CTIPOCAPTURA(Base):
    __tablename__ = 'C_TIPO_CAPTURA'

    TCA_ID = Column(Integer, primary_key=True)
    TCA_NOMBRE = Column(String(100, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)


class CTIPOMEDIO(Base):
    __tablename__ = 'C_TIPO_MEDIO'

    TM_ID = Column(Integer, primary_key=True)
    TM_NOMBRE = Column(String(300, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)


class CTIPONOTA(Base):
    __tablename__ = 'C_TIPO_NOTA'

    TN_ID = Column(BigInteger, primary_key=True)
    TN_NOMBRE = Column(String(1000, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)


class CTIPOUSUARIO(Base):
    __tablename__ = 'C_TIPO_USUARIO'

    TU_ID = Column(Integer, primary_key=True)
    TU_NOMBRE = Column(String(100, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)


class IAAUDIOHEADER(Base):
    __tablename__ = 'IA_AUDIO_HEADER'

    AU_ID = Column(Integer, primary_key=True)
    AU_WORK_PATH = Column(String(2000, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    AU_STATUS = Column(String(100, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    AU_FECHA_INICIO = Column(DateTime)
    AU_FECHA_FIN = Column(DateTime)
    AU_NOMBRE = Column(String(collation='SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    AU_BYTE = Column(LargeBinary, nullable=False)


class KAPI(Base):
    __tablename__ = 'K_API'
    __table_args__ = (
        Index('NonClusteredIndex-20170220-180157', 'API_ID', 'API_SUS_ID', 'API_KEY'),
    )

    API_ID = Column(Integer, primary_key=True)
    API_SUS_ID = Column(Integer, nullable=False)
    API_KEY = Column(String(500, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    API_LIMIT = Column(Integer, nullable=False)
    API_LASTRESQUEST = Column(DateTime, nullable=False)
    API_STARTDATE = Column(DateTime, nullable=False)


class KDIVISA(Base):
    __tablename__ = 'K_DIVISAS'

    D_ID = Column(Integer, primary_key=True)
    D_NOMBRE = Column(String(500, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    D_VALOR = Column(DECIMAL(18, 4), nullable=False)
    D_FECHA = Column(DateTime, nullable=False)


class KGLOBALPOST(Base):
    __tablename__ = 'K_GLOBAL_POST'

    GLP_ID = Column(Integer, primary_key=True)
    GLP_TIPO = Column(String(2000, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    GLP_FECHA = Column(DateTime, nullable=False)
    GLP_ARCHIVO = Column(String(2000, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)


class KLOG(Base):
    __tablename__ = 'K_LOG'

    LOG_ID = Column(Integer, primary_key=True)
    LOG_MENSAGE = Column(String(collation='SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    LOG_IP = Column(String(100, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    LOG_MAQUINA = Column(String(1000, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    LOG_TIPO = Column(String(1000, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    LOG_USUARIO = Column(String(1000, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    LOG_FECHA = Column(DateTime, nullable=False)


class KLOG2018(Base):
    __tablename__ = 'K_LOG_2018'
    __table_args__ = (
        Index('NonClusteredIndex-20180720-095849', 'LOG_ID', 'LOG_MENSAGE', 'LOG_IP', 'LOG_FECHA'),
    )

    LOG_ID = Column(Integer, primary_key=True)
    LOG_MENSAGE = Column(String(collation='SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    LOG_IP = Column(String(100, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    LOG_MAQUINA = Column(String(1000, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    LOG_TIPO = Column(String(1000, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    LOG_USUARIO = Column(String(1000, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    LOG_FECHA = Column(DateTime, nullable=False)


class KLOG2019(Base):
    __tablename__ = 'K_LOG_2019'

    LOG_ID = Column(Integer, primary_key=True)
    LOG_MENSAGE = Column(String(collation='SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    LOG_IP = Column(String(100, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    LOG_MAQUINA = Column(String(1000, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    LOG_TIPO = Column(String(1000, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    LOG_USUARIO = Column(String(1000, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    LOG_FECHA = Column(DateTime, nullable=False)


t_K_NEWSLETTER_2019 = Table(
    'K_NEWSLETTER_2019', metadata,
    Column('NW_ID', Integer, nullable=False),
    Column('NW_NC_ID', Integer, nullable=False),
    Column('NW_SUS_ID', Integer, nullable=False),
    Column('NW_FECHA', DateTime, nullable=False),
    Column('NW_TITULO', String(2000, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False),
    Column('NW_GUID', UNIQUEIDENTIFIER, nullable=False)
)


t_K_NEWSLETTER_ARCHIVE_2016 = Table(
    'K_NEWSLETTER_ARCHIVE_2016', metadata,
    Column('NW_ID', Integer, nullable=False),
    Column('NW_NC_ID', Integer, nullable=False),
    Column('NW_SUS_ID', Integer, nullable=False),
    Column('NW_FECHA', DateTime, nullable=False),
    Column('NW_TITULO', String(2000, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False),
    Column('NW_GUID', UNIQUEIDENTIFIER, nullable=False)
)


t_K_NEWSLETTER_ARCHIVE_2017 = Table(
    'K_NEWSLETTER_ARCHIVE_2017', metadata,
    Column('NW_ID', Integer, nullable=False),
    Column('NW_NC_ID', Integer, nullable=False),
    Column('NW_SUS_ID', Integer, nullable=False),
    Column('NW_FECHA', DateTime, nullable=False),
    Column('NW_TITULO', String(2000, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False),
    Column('NW_GUID', UNIQUEIDENTIFIER, nullable=False)
)


t_K_NEWSLETTER_DETALLE_2019 = Table(
    'K_NEWSLETTER_DETALLE_2019', metadata,
    Column('NWD_ID', Integer, nullable=False),
    Column('NWD_NW_ID', Integer, nullable=False),
    Column('NWD_NOTAID', BigInteger, nullable=False),
    Column('NWD_NOTA', TEXT(2147483647, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False),
    Column('NWD_NOMRE_MEDIO', Unicode(2000), nullable=False),
    Column('NWD_TIPO_MEDIO', Unicode(2000), nullable=False),
    Column('NWD_MENU_DISPLAY', Integer),
    Column('NWD_MENU', Unicode(2000)),
    Column('NWD_TEMA', Unicode(2000)),
    Column('NWD_TEMA_DISPLAY', Integer),
    Column('NWD_SECCION', Unicode(2000)),
    Column('NWD_PAGINA', Unicode(2000)),
    Column('NWD_COSTO', Unicode(2000)),
    Column('NWD_TITULO', Unicode(2000)),
    Column('NWD_TIPO_NOTA', Unicode(2000)),
    Column('NWD_CALIFICACION', Unicode(2000)),
    Column('NWD_AUTORES', Unicode(2000)),
    Column('NWD_FECHA_PUBLICACION', DateTime),
    Column('NWD_DURACION', Unicode(2000)),
    Column('NWD_URL', Unicode(2000)),
    Column('NWD_TESTIGOS', String(8000, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('NWD_MENU_LG_ID', Integer),
    Column('NWD_TEMAPADRE_LG_ID', Integer),
    Column('NWD_TEMAHIJO_LG_ID', Integer),
    Column('NWD_MEDIO_LG_ID', Integer),
    Column('NWD_MEDIO_LOGO', Unicode(2000)),
    Column('NWD_ORDEN', Integer, nullable=False)
)


t_K_NEWSLETTER_DETALLE_ARCHIVE_2016 = Table(
    'K_NEWSLETTER_DETALLE_ARCHIVE_2016', metadata,
    Column('NWD_ID', Integer, nullable=False),
    Column('NWD_NW_ID', Integer, nullable=False),
    Column('NWD_NOTAID', BigInteger, nullable=False),
    Column('NWD_NOTA', TEXT(2147483647, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False),
    Column('NWD_NOMRE_MEDIO', Unicode(2000), nullable=False),
    Column('NWD_TIPO_MEDIO', Unicode(2000), nullable=False),
    Column('NWD_MENU_DISPLAY', Integer),
    Column('NWD_MENU', Unicode(2000)),
    Column('NWD_TEMA', Unicode(2000)),
    Column('NWD_TEMA_DISPLAY', Integer),
    Column('NWD_SECCION', Unicode(2000)),
    Column('NWD_PAGINA', Unicode(2000)),
    Column('NWD_COSTO', Unicode(2000)),
    Column('NWD_TITULO', Unicode(2000)),
    Column('NWD_TIPO_NOTA', Unicode(2000)),
    Column('NWD_CALIFICACION', Unicode(2000)),
    Column('NWD_AUTORES', Unicode(2000)),
    Column('NWD_FECHA_PUBLICACION', DateTime),
    Column('NWD_DURACION', Unicode(2000)),
    Column('NWD_URL', Unicode(2000)),
    Column('NWD_TESTIGOS', String(8000, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('NWD_MENU_LG_ID', Integer),
    Column('NWD_TEMAPADRE_LG_ID', Integer),
    Column('NWD_TEMAHIJO_LG_ID', Integer),
    Column('NWD_MEDIO_LG_ID', Integer),
    Column('NWD_MEDIO_LOGO', Unicode(2000))
)


t_K_NEWSLETTER_DETALLE_ARCHIVE_2017 = Table(
    'K_NEWSLETTER_DETALLE_ARCHIVE_2017', metadata,
    Column('NWD_ID', Integer, nullable=False),
    Column('NWD_NW_ID', Integer, nullable=False),
    Column('NWD_NOTAID', BigInteger, nullable=False),
    Column('NWD_NOTA', TEXT(2147483647, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False),
    Column('NWD_NOMRE_MEDIO', Unicode(2000), nullable=False),
    Column('NWD_TIPO_MEDIO', Unicode(2000), nullable=False),
    Column('NWD_MENU_DISPLAY', Integer),
    Column('NWD_MENU', Unicode(2000)),
    Column('NWD_TEMA', Unicode(2000)),
    Column('NWD_TEMA_DISPLAY', Integer),
    Column('NWD_SECCION', Unicode(2000)),
    Column('NWD_PAGINA', Unicode(2000)),
    Column('NWD_COSTO', Unicode(2000)),
    Column('NWD_TITULO', Unicode(2000)),
    Column('NWD_TIPO_NOTA', Unicode(2000)),
    Column('NWD_CALIFICACION', Unicode(2000)),
    Column('NWD_AUTORES', Unicode(2000)),
    Column('NWD_FECHA_PUBLICACION', DateTime),
    Column('NWD_DURACION', Unicode(2000)),
    Column('NWD_URL', Unicode(2000)),
    Column('NWD_TESTIGOS', String(8000, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('NWD_MENU_LG_ID', Integer),
    Column('NWD_TEMAPADRE_LG_ID', Integer),
    Column('NWD_TEMAHIJO_LG_ID', Integer),
    Column('NWD_MEDIO_LG_ID', Integer),
    Column('NWD_MEDIO_LOGO', Unicode(2000))
)


class KNOTATRACK(Base):
    __tablename__ = 'K_NOTA_TRACK'

    NL_ID = Column(BigInteger, primary_key=True)
    NL_SUSU_ID = Column(Integer)
    NL_DATE = Column(DateTime, nullable=False)
    NL_N_ID = Column(BigInteger, nullable=False)
    NL_IP = Column(String(500, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)


class KOCHOCOLUMNA(Base):
    __tablename__ = 'K_OCHO_COLUMNAS'

    OC_ID = Column(Integer, primary_key=True)
    OC_NOTA_ID = Column(BigInteger, nullable=False)
    OC_TITULO = Column(String(collation='SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    OC_NOMBRE_MEDIO = Column(String(collation='SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    OC_FECHA = Column(DateTime, nullable=False)


class KPORTADA(Base):
    __tablename__ = 'K_PORTADAS'

    POR_ID = Column(Integer, primary_key=True)
    POR_FECHA = Column(DateTime, nullable=False)
    POR_TESTIGO = Column(Unicode, nullable=False)


class KPROCESO(Base):
    __tablename__ = 'K_PROCESO'
    __table_args__ = (
        Index('NonClusteredIndex-20170523-161350', 'KP_ID', 'KP_SUS_ID'),
        Index('NonClusteredIndex-20170328-071128', 'KP_ID', 'KP_SUS_ID', unique=True)
    )

    KP_ID = Column(Integer, primary_key=True)
    KP_SUS_ID = Column(Integer, nullable=False)
    KP_FECHA_ULT_PROCESO = Column(DateTime, nullable=False)
    KP_ESTATUS = Column(String(1000, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)


class KTEMA(Base):
    __tablename__ = 'K_TEMA'
    __table_args__ = (
        Index('_dta_index_K_TEMA_5_1895677801__K1_2_3_4_5_6_9987_4364_8066', 'T_ID', 'T_NOMBRE', 'T_DESCRIPCION', 'T_LOGO', 'T_ES_MEDIO', 'T_TIPO_NOTA'),
        Index('_dta_index_K_TEMA_5_1895677801__K1_2_3_4_5_6_9987', 'T_ID', 'T_NOMBRE', 'T_DESCRIPCION', 'T_LOGO', 'T_ES_MEDIO', 'T_TIPO_NOTA'),
        Index('_dta_index_K_TEMA_5_1895677801__K1_2_3_4_5_6_9987_4364_8066_1912', 'T_ID', 'T_NOMBRE', 'T_DESCRIPCION', 'T_LOGO', 'T_ES_MEDIO', 'T_TIPO_NOTA'),
        Index('_dta_index_K_TEMA_5_1895677801__K1_3_4_5_6_9987_4364_8066', 'T_ID', 'T_DESCRIPCION', 'T_LOGO', 'T_ES_MEDIO', 'T_TIPO_NOTA'),
        Index('_dta_index_K_TEMA_5_1895677801__K5_K1', 'T_ID', 'T_ES_MEDIO'),
        Index('_dta_stat_1895677801_5_1', 'T_ID', 'T_ES_MEDIO'),
        Index('_dta_index_K_TEMA_5_1895677801__K1_3_4_5_6', 'T_ID', 'T_DESCRIPCION', 'T_LOGO', 'T_ES_MEDIO', 'T_TIPO_NOTA'),
        Index('_dta_index_K_TEMA_5_1895677801__K1_2_3_4_5_6_9987_4364_8066_1912_4149', 'T_ID', 'T_NOMBRE', 'T_DESCRIPCION', 'T_LOGO', 'T_ES_MEDIO', 'T_TIPO_NOTA'),
        Index('_dta_index_K_TEMA_5_1895677801__K1_3_4_5_6_9987_4364_8066_1912', 'T_ID', 'T_DESCRIPCION', 'T_LOGO', 'T_ES_MEDIO', 'T_TIPO_NOTA'),
        Index('_dta_index_K_TEMA_5_1895677801__K1_2_3_4_5_6', 'T_ID', 'T_NOMBRE', 'T_DESCRIPCION', 'T_LOGO', 'T_ES_MEDIO', 'T_TIPO_NOTA'),
        Index('_dta_index_K_TEMA_5_1895677801__K1_3_4_5_6_9987', 'T_ID', 'T_DESCRIPCION', 'T_LOGO', 'T_ES_MEDIO', 'T_TIPO_NOTA'),
        Index('_dta_index_K_TEMA_5_1895677801__K5_K1_9987', 'T_ID', 'T_ES_MEDIO'),
        Index('_dta_index_K_TEMA_5_1895677801__K1_2_3_4_5_6_9987_4364', 'T_ID', 'T_NOMBRE', 'T_DESCRIPCION', 'T_LOGO', 'T_ES_MEDIO', 'T_TIPO_NOTA'),
        Index('_dta_index_K_TEMA_5_1895677801__K1_3_4_5_6_9987_4364', 'T_ID', 'T_DESCRIPCION', 'T_LOGO', 'T_ES_MEDIO', 'T_TIPO_NOTA')
    )

    T_ID = Column(Integer, primary_key=True, index=True)
    T_NOMBRE = Column(String(1000, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    T_DESCRIPCION = Column(String(1000, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    T_LOGO = Column(String(1000, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    T_ES_MEDIO = Column(BIT, index=True)
    T_TIPO_NOTA = Column(String(4000, 'SQL_Latin1_General_CP1_CI_AS'))


t_K_TEMA_DELETE = Table(
    'K_TEMA_DELETE', metadata,
    Column('T_ID', Integer, nullable=False),
    Column('T_NOMBRE', String(1000, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False),
    Column('T_DESCRIPCION', String(1000, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False),
    Column('T_LOGO', String(1000, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False),
    Column('T_ES_MEDIO', BIT),
    Column('T_TIPO_NOTA', String(4000, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_K_TEMA_MEDIO_DELETE = Table(
    'K_TEMA_MEDIO_DELETE', metadata,
    Column('TM_ID', BigInteger, nullable=False),
    Column('TM_T_ID', Integer, nullable=False),
    Column('TM_ME_ID', BigInteger, nullable=False)
)


t_K_TEMA_TERMINO_DELETE = Table(
    'K_TEMA_TERMINO_DELETE', metadata,
    Column('TTE_ID', Integer, nullable=False),
    Column('TTE_PALABRA', String(2000, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False),
    Column('TTE_TIPO_BUSQUEDA', Integer, nullable=False),
    Column('TTE_T_ID', Integer, nullable=False),
    Column('TTT_TERMINO_ID', Integer, nullable=False),
    Column('TTE_ACTIVO', BIT, nullable=False),
    Column('TTE_TIPO_TERMINO', Integer, nullable=False),
    Column('TTE_CON', String(100, 'SQL_Latin1_General_CP1_CI_AS'))
)


class KVIDEODROPBOX(Base):
    __tablename__ = 'K_VIDEO_DROPBOX'
    __table_args__ = (
        Index('NonClusteredIndex-20190601-134727', 'KV_ARCHIVO', 'KV_DP_LINK', unique=True),
    )

    KV_ID = Column(BigInteger, primary_key=True)
    KV_ARCHIVO = Column(String(3000, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    KV_DP_LINK = Column(String(3000, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)


class MMONITOREO(Base):
    __tablename__ = 'M_MONITOREO'

    MO_ID = Column(Integer, primary_key=True)
    MO_USU_ID = Column(BigInteger, nullable=False)
    MO_ME_ID = Column(Integer)
    MO_SEC_ID = Column(Integer)
    MO_AVANCE = Column(String(5000, 'SQL_Latin1_General_CP1_CI_AS'))
    MO_PANTALLA = Column(String(5000, 'SQL_Latin1_General_CP1_CI_AS'))
    MO_PING = Column(String(5000, 'SQL_Latin1_General_CP1_CI_AS'))
    MO_FECHA = Column(DateTime)


class MSESION(Base):
    __tablename__ = 'M_SESION'

    SE_ID = Column(Integer, primary_key=True)
    SE_USU_ID = Column(BigInteger, nullable=False)
    SE_FECHA_INICIO = Column(DateTime, nullable=False)
    SE_LAST_PING = Column(DateTime, nullable=False)
    SE_IP = Column(String(500, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)


class TWBI(Base):
    __tablename__ = 'TW_BI'
    __table_args__ = (
        Index('NonClusteredIndex-20200408-232136', 'BI_ID', 'BI_FECHA', 'BI_ALCANCE', 'BI_POTENCIAL', 'BI_T_ID', 'BT_TW_COUNT', unique=True),
    )

    BI_ID = Column(Integer, primary_key=True)
    BI_FECHA = Column(DateTime, nullable=False)
    BI_ALCANCE = Column(Integer, nullable=False)
    BI_POTENCIAL = Column(Integer, nullable=False)
    BI_T_ID = Column(Integer, nullable=False)
    BT_TW_COUNT = Column(Integer, nullable=False)


t_X_GRUPO_BACKUP = Table(
    'X_GRUPO_BACKUP', metadata,
    Column('NG_ID', Integer, nullable=False),
    Column('NG_N_ID', BigInteger, nullable=False),
    Column('NG_MSG_ID', Integer, nullable=False),
    Column('NG_VALOR', String(2000, 'SQL_Latin1_General_CP1_CI_AS'))
)


class XNOTA(Base):
    __tablename__ = 'X_NOTA'

    N_ID = Column(BigInteger, primary_key=True)
    SINCRONIZAD = Column(DateTime, nullable=False)


class XNOTA2018(Base):
    __tablename__ = 'X_NOTA_2018'

    N_ID = Column(BigInteger, primary_key=True)
    SINCRONIZAD = Column(DateTime, nullable=False)


class Sysdiagram(Base):
    __tablename__ = 'sysdiagrams'
    __table_args__ = (
        Index('UK_principal_name', 'name', 'principal_id', unique=True),
    )

    name = Column(Unicode(128), nullable=False)
    principal_id = Column(Integer, nullable=False)
    diagram_id = Column(Integer, primary_key=True)
    version = Column(Integer)
    definition = Column(LargeBinary)


class CESTADO(Base):
    __tablename__ = 'C_ESTADO'

    ESTADO_ID = Column(Integer, primary_key=True)
    ESTATDO_NOMBRE = Column(String(1000, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    ESTADO_PAIS_ID = Column(ForeignKey('C_PAIS.PAIS_ID'), nullable=False)

    C_PAI = relationship('CPAI')


class CGRUPOOPCIONE(Base):
    __tablename__ = 'C_GRUPO_OPCIONES'

    GRO_ID = Column(Integer, primary_key=True)
    GRO_GR_ID = Column(ForeignKey('C_GRUPO.GR_ID'), nullable=False)
    GRO_OPCION = Column(String(2000, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)

    C_GRUPO = relationship('CGRUPO')


class CSUBMODULO(Base):
    __tablename__ = 'C_SUBMODULO'

    SMOD_ID = Column(Integer, primary_key=True)
    SMOD_MOD_ID = Column(ForeignKey('C_MODULO.MOD_ID'), nullable=False)
    SMOD_DESCRIPCION = Column(String(200, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)

    C_MODULO = relationship('CMODULO')


class CSUSCRIPTOR(Base):
    __tablename__ = 'C_SUSCRIPTOR'

    SUS_ID = Column(Integer, primary_key=True)
    SUS_NOMBRE = Column(String(8000, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    SUS_DESCRIPCION = Column(String(8000, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    SUS_SS_ID = Column(ForeignKey('C_ESTATUS_SUSCRIPTOR.SS_ID'), nullable=False)
    SUS_LOGO = Column(String(8000, 'SQL_Latin1_General_CP1_CI_AS'))
    SUS_FECHA_SUSCRIPCION = Column(DateTime, nullable=False)
    SUS_PR_BUSQUEDA_AVANZADA = Column(Integer, nullable=False)
    SUS_PR_EDICION_IMPRESA = Column(Integer, nullable=False)
    SUS_PR_REPORTES = Column(Integer, nullable=False)
    SUS_PR_PDA = Column(Integer, nullable=False)
    SUS_NEWSLLETER = Column(Integer)
    SUS_LG_ID = Column(Integer, nullable=False)
    SUS_CONTACTO = Column(String(1000, 'SQL_Latin1_General_CP1_CI_AS'))
    SUS_CORREOE = Column(String(1000, 'SQL_Latin1_General_CP1_CI_AS'))
    SUS_TELEFONO = Column(String(1000, 'SQL_Latin1_General_CP1_CI_AS'))
    SUS_DIRECCION = Column(String(1000, 'SQL_Latin1_General_CP1_CI_AS'))
    SUS_COSTO = Column(DECIMAL(18, 2))
    SUS_USU_ID_EJECUTIVO = Column(Integer)
    SUS_NOMBRE_EJECUTIVO = Column(String(1000, 'SQL_Latin1_General_CP1_CI_AS'))
    SUS_USU_ID_VENDEDOR = Column(Integer)
    SUS_NOMBRE_VENDEDOR = Column(String(1000, 'SQL_Latin1_General_CP1_CI_AS'))
    SUS_URL = Column(String(1000, 'SQL_Latin1_General_CP1_CI_AS'))
    SUS_COLOR_PRINCIPAL = Column(String(1000, 'SQL_Latin1_General_CP1_CI_AS'))
    SUS_COLOR_SECUNDARIO = Column(String(1000, 'SQL_Latin1_General_CP1_CI_AS'))
    SUS_COLOR_FUENTE = Column(String(1000, 'SQL_Latin1_General_CP1_CI_AS'))
    SUS_GIRO = Column(String(1000, 'SQL_Latin1_General_CP1_CI_AS'))
    SUS_OBSERVACIONES = Column(String(1000, 'SQL_Latin1_General_CP1_CI_AS'))
    SUS_RAZON_SOCIAL = Column(String(1000, 'SQL_Latin1_General_CP1_CI_AS'))
    SUS_CORREO_FISCAL = Column(String(1000, 'SQL_Latin1_General_CP1_CI_AS'))
    SUS_TELEFONO_FISCAL = Column(String(1000, 'SQL_Latin1_General_CP1_CI_AS'))
    SUS_RFC = Column(String(1000, 'SQL_Latin1_General_CP1_CI_AS'))
    SUS_PERIODO_FACTURACION = Column(String(1000, 'SQL_Latin1_General_CP1_CI_AS'))
    SUS_TIPO_PAGO = Column(String(1000, 'SQL_Latin1_General_CP1_CI_AS'))
    SUS_TIPO_GLOBAL = Column(String(1000, 'SQL_Latin1_General_CP1_CI_AS'))
    SUS_OFICINA_ID = Column(ForeignKey('C_OFICINA.OFICINA_ID'))

    C_OFICINA = relationship('COFICINA')
    C_ESTATUS_SUSCRIPTOR = relationship('CESTATUSSUSCRIPTOR')


class IAAUDIODETAIL(Base):
    __tablename__ = 'IA_AUDIO_DETAIL'

    AUD_ID = Column(Integer, primary_key=True)
    AUD_AU_ID = Column(ForeignKey('IA_AUDIO_HEADER.AU_ID'), nullable=False)
    AUD_BLOQUE = Column(LargeBinary, nullable=False)
    AUD_TEXTO = Column(TEXT(2147483647, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    AUD_MINUTO_ORDEN = Column(Integer, nullable=False)

    IA_AUDIO_HEADER = relationship('IAAUDIOHEADER')


class KTEMAESTADO(Base):
    __tablename__ = 'K_TEMA_ESTADO'

    TE_ID = Column(Integer, primary_key=True)
    TE_T_ID = Column(ForeignKey('K_TEMA.T_ID'), nullable=False)
    TE_ESTADO_ID = Column(Integer, nullable=False)

    K_TEMA = relationship('KTEMA')


class KTEMAPAI(Base):
    __tablename__ = 'K_TEMA_PAIS'

    TP_ID = Column(Integer, primary_key=True)
    TP_T_ID = Column(ForeignKey('K_TEMA.T_ID'), nullable=False)
    TP_PAIS_ID = Column(ForeignKey('C_PAIS.PAIS_ID'), nullable=False)

    C_PAI = relationship('CPAI')
    K_TEMA = relationship('KTEMA')


class KTEMATERMINO(Base):
    __tablename__ = 'K_TEMA_TERMINO'
    __table_args__ = (
        Index('_dta_index_K_TEMA_TERMINO_5_1115151018__K4_K7_1_2_3_5_6_8_9987', 'TTE_ID', 'TTE_PALABRA', 'TTE_TIPO_BUSQUEDA', 'TTE_T_ID', 'TTT_TERMINO_ID', 'TTE_ACTIVO', 'TTE_TIPO_TERMINO', 'TTE_CON'),
        Index('_dta_index_K_TEMA_TERMINO_5_1115151018__K1_3_9987', 'TTE_ID', 'TTE_TIPO_BUSQUEDA'),
        Index('_dta_index_K_TEMA_TERMINO_5_1115151018__K1_2_3_4_5_6_7_8', 'TTE_ID', 'TTE_PALABRA', 'TTE_TIPO_BUSQUEDA', 'TTE_T_ID', 'TTT_TERMINO_ID', 'TTE_ACTIVO', 'TTE_TIPO_TERMINO', 'TTE_CON'),
        Index('_dta_index_K_TEMA_TERMINO_5_1115151018__K4_K7_1_2_3_5_6_8_9987_4364', 'TTE_ID', 'TTE_PALABRA', 'TTE_TIPO_BUSQUEDA', 'TTE_T_ID', 'TTT_TERMINO_ID', 'TTE_ACTIVO', 'TTE_TIPO_TERMINO', 'TTE_CON'),
        Index('_dta_index_K_TEMA_TERMINO_5_1115151018__K1_3', 'TTE_ID', 'TTE_TIPO_BUSQUEDA'),
        Index('_dta_index_K_TEMA_TERMINO_5_1115151018__K1_2_9987', 'TTE_ID', 'TTE_PALABRA'),
        Index('_dta_index_K_TEMA_TERMINO_5_1115151018__K4_K7_1_2_3_5_6_8', 'TTE_ID', 'TTE_PALABRA', 'TTE_TIPO_BUSQUEDA', 'TTE_T_ID', 'TTT_TERMINO_ID', 'TTE_ACTIVO', 'TTE_TIPO_TERMINO', 'TTE_CON'),
        Index('_dta_index_K_TEMA_TERMINO_5_1115151018__K4_1_2_3_5_6_7_8', 'TTE_ID', 'TTE_PALABRA', 'TTE_TIPO_BUSQUEDA', 'TTE_T_ID', 'TTT_TERMINO_ID', 'TTE_ACTIVO', 'TTE_TIPO_TERMINO', 'TTE_CON'),
        Index('_dta_index_K_TEMA_TERMINO_5_1115151018__K1_2', 'TTE_ID', 'TTE_PALABRA'),
        Index('_dta_index_K_TEMA_TERMINO_5_1115151018__K1_8', 'TTE_ID', 'TTE_CON'),
        Index('_dta_index_K_TEMA_TERMINO_5_1115151018__K1_2_3_4_5_6_7_8_9987', 'TTE_ID', 'TTE_PALABRA', 'TTE_TIPO_BUSQUEDA', 'TTE_T_ID', 'TTT_TERMINO_ID', 'TTE_ACTIVO', 'TTE_TIPO_TERMINO', 'TTE_CON')
    )

    TTE_ID = Column(Integer, primary_key=True, index=True)
    TTE_PALABRA = Column(String(2000, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    TTE_TIPO_BUSQUEDA = Column(Integer, nullable=False)
    TTE_T_ID = Column(ForeignKey('K_TEMA.T_ID'), nullable=False, index=True)
    TTT_TERMINO_ID = Column(Integer, nullable=False)
    TTE_ACTIVO = Column(BIT, nullable=False, index=True)
    TTE_TIPO_TERMINO = Column(Integer, nullable=False)
    TTE_CON = Column(String(100, 'SQL_Latin1_General_CP1_CI_AS'))

    K_TEMA = relationship('KTEMA')


class KTEMATIPONOTA(Base):
    __tablename__ = 'K_TEMA_TIPO_NOTA'

    TTN_ID = Column(BigInteger, primary_key=True)
    TTN_TN_ID = Column(ForeignKey('C_TIPO_NOTA.TN_ID'), nullable=False)
    TTN_T_ID = Column(ForeignKey('K_TEMA.T_ID'), nullable=False)

    C_TIPO_NOTA = relationship('CTIPONOTA')
    K_TEMA = relationship('KTEMA')


class KWITTER(Base):
    __tablename__ = 'K_WITTER'
    __table_args__ = (
        Index('NonClusteredIndex-20200326-111238', 'TW_ID', 'TW_UserID', 'TW_ScreenName', 'TW_SinceID', 'TW_MaxID', 'TW_Count', 'TW_Cursor', 'TW_IncludeRetweets', 'TW_ExcludeReplies', 'TW_IncludeEntities', 'TW_IncludeUserEntities', 'TW_IncludeMyRetweet', 'TW_OEmbedUrl', 'TW_OEmbedMaxWidth', 'TW_OEmbedHideMedia', 'TW_OEmbedHideThread', 'TW_OEmbedOmitScript', 'TW_OEmbedAlign', 'TW_OEmbedRelated', 'TW_OEmbedLanguage', 'TW_CreatedAt', 'TW_StatusID', 'TW_Text', 'TW_Source', 'TW_Truncated', 'TW_InReplyToStatusID', 'TW_InReplyToUserID', 'TW_FavoriteCount', 'TW_Favorited', 'TW_InReplyToScreenName', 'TW_Coordinates', 'TW_Place', 'TW_Annotation', 'TW_Entities', 'TW_ExtendedEntities', 'TW_TrimUser', 'TW_IncludeContributorDetails', 'TW_RetweetCount', 'TW_Retweeted', 'TW_PossiblySensitive', 'TW_RetweetedStatus', 'TW_CurrentUserRetweet', 'TW_QuotedStatusID', 'TW_QuotedStatus', 'TW_WithheldCopyright', 'TW_WithheldInCountries', 'TW_WithheldScope', 'TW_MetaData', 'TW_Lang', 'TW_Map', 'TW_TweetIDs', 'TW_T_ID', 'TW_INSERTADO', unique=True),
        Index('NonClusteredIndex-20200326-111122', 'TW_ID', 'TW_UserID', 'TW_StatusID', 'TW_T_ID', unique=True)
    )

    TW_ID = Column(BigInteger, primary_key=True)
    TW_UserID = Column(BigInteger)
    TW_ScreenName = Column(String(8000, 'SQL_Latin1_General_CP1_CI_AS'))
    TW_SinceID = Column(BigInteger)
    TW_MaxID = Column(BigInteger)
    TW_Count = Column(Integer)
    TW_Cursor = Column(BigInteger)
    TW_IncludeRetweets = Column(BIT)
    TW_ExcludeReplies = Column(BIT)
    TW_IncludeEntities = Column(BIT)
    TW_IncludeUserEntities = Column(BIT)
    TW_IncludeMyRetweet = Column(BIT)
    TW_OEmbedUrl = Column(String(8000, 'SQL_Latin1_General_CP1_CI_AS'))
    TW_OEmbedMaxWidth = Column(Integer)
    TW_OEmbedHideMedia = Column(BIT)
    TW_OEmbedHideThread = Column(BIT)
    TW_OEmbedOmitScript = Column(BIT)
    TW_OEmbedAlign = Column(String(8000, 'SQL_Latin1_General_CP1_CI_AS'))
    TW_OEmbedRelated = Column(String(8000, 'SQL_Latin1_General_CP1_CI_AS'))
    TW_OEmbedLanguage = Column(String(8000, 'SQL_Latin1_General_CP1_CI_AS'))
    TW_CreatedAt = Column(DateTime)
    TW_StatusID = Column(BigInteger)
    TW_Text = Column(String(8000, 'SQL_Latin1_General_CP1_CI_AS'))
    TW_Source = Column(String(8000, 'SQL_Latin1_General_CP1_CI_AS'))
    TW_Truncated = Column(BIT)
    TW_InReplyToStatusID = Column(BigInteger)
    TW_InReplyToUserID = Column(BigInteger)
    TW_FavoriteCount = Column(Integer)
    TW_Favorited = Column(BIT)
    TW_InReplyToScreenName = Column(String(8000, 'SQL_Latin1_General_CP1_CI_AS'))
    TW_Coordinates = Column(String(8000, 'SQL_Latin1_General_CP1_CI_AS'))
    TW_Place = Column(String(8000, 'SQL_Latin1_General_CP1_CI_AS'))
    TW_Annotation = Column(String(8000, 'SQL_Latin1_General_CP1_CI_AS'))
    TW_Entities = Column(String(8000, 'SQL_Latin1_General_CP1_CI_AS'))
    TW_ExtendedEntities = Column(String(8000, 'SQL_Latin1_General_CP1_CI_AS'))
    TW_TrimUser = Column(BIT)
    TW_IncludeContributorDetails = Column(String(8000, 'SQL_Latin1_General_CP1_CI_AS'))
    TW_RetweetCount = Column(Integer)
    TW_Retweeted = Column(BIT)
    TW_PossiblySensitive = Column(BIT)
    TW_RetweetedStatus = Column(String(8000, 'SQL_Latin1_General_CP1_CI_AS'))
    TW_CurrentUserRetweet = Column(BigInteger)
    TW_QuotedStatusID = Column(BigInteger)
    TW_QuotedStatus = Column(String(8000, 'SQL_Latin1_General_CP1_CI_AS'))
    TW_WithheldCopyright = Column(BIT)
    TW_WithheldInCountries = Column(String(8000, 'SQL_Latin1_General_CP1_CI_AS'))
    TW_WithheldScope = Column(String(8000, 'SQL_Latin1_General_CP1_CI_AS'))
    TW_MetaData = Column(String(8000, 'SQL_Latin1_General_CP1_CI_AS'))
    TW_Lang = Column(String(8000, 'SQL_Latin1_General_CP1_CI_AS'))
    TW_Map = Column(String(8000, 'SQL_Latin1_General_CP1_CI_AS'))
    TW_TweetIDs = Column(String(8000, 'SQL_Latin1_General_CP1_CI_AS'))
    TW_T_ID = Column(ForeignKey('K_TEMA.T_ID'), nullable=False)
    TW_INSERTADO = Column(DateTime, nullable=False)

    K_TEMA = relationship('KTEMA')


class TWBIHASHTAG(Base):
    __tablename__ = 'TW_BI_HASHTAG'
    __table_args__ = (
        Index('NonClusteredIndex-20200408-232211', 'BIH_ID', 'BIH_BI_ID', 'BIH_HASHTAG', 'BIH_SIZE', unique=True),
    )

    BIH_ID = Column(Integer, primary_key=True)
    BIH_BI_ID = Column(ForeignKey('TW_BI.BI_ID'), nullable=False)
    BIH_HASHTAG = Column(String(2000, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    BIH_SIZE = Column(Integer, nullable=False)

    TW_BI = relationship('TWBI')


class TWBINUBE(Base):
    __tablename__ = 'TW_BI_NUBE'
    __table_args__ = (
        Index('NonClusteredIndex-20200408-232245', 'BIN_ID', 'BIN_BI_ID', 'BIN_PALABRA', 'BIN_SIZE', unique=True),
    )

    BIN_ID = Column(Integer, primary_key=True)
    BIN_BI_ID = Column(ForeignKey('TW_BI.BI_ID'), nullable=False)
    BIN_PALABRA = Column(String(2000, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    BIN_SIZE = Column(Integer, nullable=False)

    TW_BI = relationship('TWBI')


class TWBITOPTW(Base):
    __tablename__ = 'TW_BI_TOP_TW'
    __table_args__ = (
        Index('NonClusteredIndex-20200408-232323', 'BIW_ID', 'BIW_TW_ID', 'BIW_BI_ID', unique=True),
    )

    BIW_ID = Column(Integer, primary_key=True)
    BIW_TW_ID = Column(BigInteger, nullable=False)
    BIW_BI_ID = Column(ForeignKey('TW_BI.BI_ID'), nullable=False)

    TW_BI = relationship('TWBI')


class TWBITOPUSUARIO(Base):
    __tablename__ = 'TW_BI_TOP_USUARIOS'
    __table_args__ = (
        Index('NonClusteredIndex-20200408-232349', 'BIT_ID', 'BIT_BI_ID', 'BIT_USUARIO', 'BIT_DESC_USUARIO', 'BIT_MENCIONES', 'BIT_FOLLOW', 'BIT_FAV', 'BIT_RT', unique=True),
    )

    BIT_ID = Column(Integer, primary_key=True)
    BIT_BI_ID = Column(ForeignKey('TW_BI.BI_ID'), nullable=False)
    BIT_USUARIO = Column(String(2000, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    BIT_DESC_USUARIO = Column(String(2000, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    BIT_MENCIONES = Column(Integer, nullable=False)
    BIT_FOLLOW = Column(Integer, nullable=False)
    BIT_FAV = Column(Integer, nullable=False)
    BIT_RT = Column(Integer, nullable=False)

    TW_BI = relationship('TWBI')


class CACCIONSUBMODULO(Base):
    __tablename__ = 'C_ACCION_SUBMODULO'

    ASM_ID = Column(Integer, primary_key=True)
    ASM_SMOD_ID = Column(ForeignKey('C_SUBMODULO.SMOD_ID'), nullable=False)
    ASM_DESCRIPCION = Column(String(200, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)

    C_SUBMODULO = relationship('CSUBMODULO')


class CCIUDAD(Base):
    __tablename__ = 'C_CIUDAD'

    CIUDAD_ID = Column(Integer, primary_key=True)
    CIUDAD_NOMBRE = Column(String(1000, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    CIUDAD_ESTADO_ID = Column(ForeignKey('C_ESTADO.ESTADO_ID'), nullable=False)

    C_ESTADO = relationship('CESTADO')


class CMEDIO(Base):
    __tablename__ = 'C_MEDIO'
    __table_args__ = (
        Index('_dta_index_C_MEDIO_5_651149365_49239816_K1_3_4_8_9_10_11_12_13_14_15_16_17_18_19_20_21_22_23_24_25_26_27_28_29_30_31_32_33_34', 'ME_ID', 'ME_NOMBRE', 'ME_NOMBRE_CORTO', 'ME_LOGO', 'ME_LOGO_1', 'ME_VISIBLE', 'ME_EDIT_ID', 'ME_TIRAJE', 'ME_PER_ID', 'ME_CIUDAD_ID', 'ME_COSTO', 'ME_TCA_ID', 'ME_URL', 'ME_SUPLEMENTO', 'ME_FORMA_ADQUISICION', 'ME_TELEFONO', 'ME_DIRECCION', 'ME_DIRECTOR', 'ME_FACEBOOK', 'ME_TWITTER', 'ME_CLASIFICACION', 'ME_TIER', 'ME_TIPO_DE_COBERTURA', 'ME_LINK_DESCARGA', 'ME_CLIENTE', 'ME_DIAS_DE_TRANSMISION', 'ME_RAITING', 'ME_FORMACAPTURA', 'ME_TIPO_TRANSMISION', 'ME_FECHA_PUBLICACION_APROX'),
        Index('_dta_index_C_MEDIO_5_651149365__K2_K7_1_3_8_8258', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_TM_ID', 'ME_LOGO'),
        Index('_dta_index_C_MEDIO_5_651149365__K8_1_3_8066', 'ME_ID', 'ME_NOMBRE', 'ME_LOGO'),
        Index('_dta_index_C_MEDIO_5_651149365__K7_K5_K6_K1_2_1040', 'ME_ID', 'ME_LG_ID', 'ME_PAIS_ID', 'ME_ESTADO_ID', 'ME_TM_ID'),
        Index('_dta_index_C_MEDIO_5_651149365__K1_K7_3_8_12', 'ME_ID', 'ME_NOMBRE', 'ME_TM_ID', 'ME_LOGO', 'ME_TIRAJE'),
        Index('_dta_index_C_MEDIO_5_651149365__K7_K13_K5_K6_9987_4364', 'ME_PAIS_ID', 'ME_ESTADO_ID', 'ME_TM_ID', 'ME_PER_ID'),
        Index('_dta_index_C_MEDIO_5_651149365__K1_K7_K2_2894', 'ME_ID', 'ME_LG_ID', 'ME_TM_ID'),
        Index('_dta_index_C_MEDIO_5_651149365__K1_K7_K2_3_8_1912', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_TM_ID', 'ME_LOGO'),
        Index('_dta_index_C_MEDIO_5_651149365__K7_1_3_9987_4364_8066_1912', 'ME_ID', 'ME_NOMBRE', 'ME_TM_ID'),
        Index('_dta_index_C_MEDIO_5_651149365__K7_K2_K1_4864', 'ME_ID', 'ME_LG_ID', 'ME_TM_ID'),
        Index('_dta_index_C_MEDIO_5_651149365__K2_K7_1_3_8_4149', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_TM_ID', 'ME_LOGO'),
        Index('_dta_index_C_MEDIO_5_651149365__K7_K1_3_4149', 'ME_ID', 'ME_NOMBRE', 'ME_TM_ID'),
        Index('_dta_index_C_MEDIO_5_651149365__K1_3_8_9850', 'ME_ID', 'ME_NOMBRE', 'ME_LOGO'),
        Index('_dta_index_C_MEDIO_5_651149365__K1_K7_3_5201', 'ME_ID', 'ME_NOMBRE', 'ME_TM_ID'),
        Index('_dta_index_C_MEDIO_5_651149365__K2_K7_1_3_8_2533', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_TM_ID', 'ME_LOGO'),
        Index('_dta_index_C_MEDIO_5_651149365__K1_3_7_4864', 'ME_ID', 'ME_NOMBRE', 'ME_TM_ID'),
        Index('_dta_index_C_MEDIO_5_651149365__K7_K2_K1_3_8_9085', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_TM_ID', 'ME_LOGO'),
        Index('_dta_index_C_MEDIO_5_651149365__K1_K7_K2_5201', 'ME_ID', 'ME_LG_ID', 'ME_TM_ID'),
        Index('_dta_index_C_MEDIO_5_651149365__K7_K1_3_8_12', 'ME_ID', 'ME_NOMBRE', 'ME_TM_ID', 'ME_LOGO', 'ME_TIRAJE'),
        Index('_dta_index_C_MEDIO_5_651149365__K2_K7_1_9987_4364', 'ME_ID', 'ME_LG_ID', 'ME_TM_ID'),
        Index('_dta_index_C_MEDIO_5_651149365__K7_K1_2_3_8_12_1912', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_TM_ID', 'ME_LOGO', 'ME_TIRAJE'),
        Index('_dta_index_C_MEDIO_5_651149365__K7_K2_K1_6497', 'ME_ID', 'ME_LG_ID', 'ME_TM_ID'),
        Index('_dta_index_C_MEDIO_5_651149365_93568848_K1_K7_3_8_12', 'ME_ID', 'ME_NOMBRE', 'ME_TM_ID', 'ME_LOGO', 'ME_TIRAJE'),
        Index('_dta_index_C_MEDIO_5_651149365_104889936_K7_K1_3_8_12', 'ME_ID', 'ME_NOMBRE', 'ME_TM_ID', 'ME_LOGO', 'ME_TIRAJE'),
        Index('_dta_index_C_MEDIO_5_651149365_70953536_K8_1_3', 'ME_ID', 'ME_NOMBRE', 'ME_LOGO'),
        Index('_dta_index_C_MEDIO_5_651149365__K1_3_8_1040', 'ME_ID', 'ME_NOMBRE', 'ME_LOGO'),
        Index('_dta_index_C_MEDIO_5_651149365__K8_1_2_3_7_8066', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_TM_ID', 'ME_LOGO'),
        Index('_dta_index_C_MEDIO_5_651149365_70953536_K1_3_8', 'ME_ID', 'ME_NOMBRE', 'ME_LOGO'),
        Index('_dta_index_C_MEDIO_5_651149365_104890048_K7_K1_3_8_12', 'ME_ID', 'ME_NOMBRE', 'ME_TM_ID', 'ME_LOGO', 'ME_TIRAJE'),
        Index('_dta_index_C_MEDIO_5_651149365__K7_K2_K1_3_8_1771', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_TM_ID', 'ME_LOGO'),
        Index('_dta_index_C_MEDIO_5_651149365__K8_1_3_1912', 'ME_ID', 'ME_NOMBRE', 'ME_LOGO'),
        Index('_dta_index_C_MEDIO_5_651149365__K1_K7_3_1912', 'ME_ID', 'ME_NOMBRE', 'ME_TM_ID'),
        Index('_dta_index_C_MEDIO_5_651149365__K1_K7_3_8_12_2894', 'ME_ID', 'ME_NOMBRE', 'ME_TM_ID', 'ME_LOGO', 'ME_TIRAJE'),
        Index('_dta_index_C_MEDIO_5_651149365_70953536_K7_K1_K2_3_8', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_TM_ID', 'ME_LOGO'),
        Index('_dta_index_C_MEDIO_5_651149365__K1_K7_K2_3_8_4149', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_TM_ID', 'ME_LOGO'),
        Index('_dta_index_C_MEDIO_5_651149365_104889936_K1_3_7_8_12', 'ME_ID', 'ME_NOMBRE', 'ME_TM_ID', 'ME_LOGO', 'ME_TIRAJE'),
        Index('_dta_index_C_MEDIO_5_651149365__K1_3_7_8_12_6355', 'ME_ID', 'ME_NOMBRE', 'ME_TM_ID', 'ME_LOGO', 'ME_TIRAJE'),
        Index('_dta_index_C_MEDIO_5_651149365_70953536_K2_K7_1_3_8', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_TM_ID', 'ME_LOGO'),
        Index('_dta_index_C_MEDIO_5_651149365_49239816_K8_1_3', 'ME_ID', 'ME_NOMBRE', 'ME_LOGO'),
        Index('_dta_index_C_MEDIO_5_651149365__K7_1', 'ME_ID', 'ME_TM_ID'),
        Index('_dta_index_C_MEDIO_5_651149365__K2_K7_1_3_8_5201', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_TM_ID', 'ME_LOGO'),
        Index('_dta_index_C_MEDIO_5_651149365_104889936_K1_K7_3_8_12', 'ME_ID', 'ME_NOMBRE', 'ME_TM_ID', 'ME_LOGO', 'ME_TIRAJE'),
        Index('_dta_index_C_MEDIO_5_651149365__K7_K1_3_8066', 'ME_ID', 'ME_NOMBRE', 'ME_TM_ID'),
        Index('_dta_index_C_MEDIO_5_651149365_49239816_K1_K7_K2_3_8', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_TM_ID', 'ME_LOGO'),
        Index('_dta_index_C_MEDIO_5_651149365_70953536_K7_K2_K1_3_8', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_TM_ID', 'ME_LOGO'),
        Index('_dta_index_C_MEDIO_5_651149365__K1_K7_K2_6497', 'ME_ID', 'ME_LG_ID', 'ME_TM_ID'),
        Index('_dta_index_C_MEDIO_5_651149365_104890048_K1_3_7_8_12', 'ME_ID', 'ME_NOMBRE', 'ME_TM_ID', 'ME_LOGO', 'ME_TIRAJE'),
        Index('_dta_index_C_MEDIO_5_651149365__K7_K1_3_8_12_9910', 'ME_ID', 'ME_NOMBRE', 'ME_TM_ID', 'ME_LOGO', 'ME_TIRAJE'),
        Index('_dta_index_C_MEDIO_5_651149365_70953536_K1_K7_K2_3_8', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_TM_ID', 'ME_LOGO'),
        Index('_dta_index_C_MEDIO_5_651149365__K7_K2_K1_1040', 'ME_ID', 'ME_LG_ID', 'ME_TM_ID'),
        Index('_dta_index_C_MEDIO_5_651149365_49239816_K1_K7_3_8_12', 'ME_ID', 'ME_NOMBRE', 'ME_TM_ID', 'ME_LOGO', 'ME_TIRAJE'),
        Index('_dta_index_C_MEDIO_5_651149365_49239816_K7_K1_K2_3_8', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_TM_ID', 'ME_LOGO'),
        Index('_dta_index_C_MEDIO_5_651149365_104890048_K1_K7_3_8_12', 'ME_ID', 'ME_NOMBRE', 'ME_TM_ID', 'ME_LOGO', 'ME_TIRAJE'),
        Index('_dta_index_C_MEDIO_5_651149365_70952360_K7_K1_3_8_12', 'ME_ID', 'ME_NOMBRE', 'ME_TM_ID', 'ME_LOGO', 'ME_TIRAJE'),
        Index('_dta_index_C_MEDIO_5_651149365__K1_3_8_1771', 'ME_ID', 'ME_NOMBRE', 'ME_LOGO'),
        Index('_dta_index_C_MEDIO_5_651149365__K7_K1_3_8_12_6075', 'ME_ID', 'ME_NOMBRE', 'ME_TM_ID', 'ME_LOGO', 'ME_TIRAJE'),
        Index('_dta_index_C_MEDIO_5_651149365_49239816_K1_3_8', 'ME_ID', 'ME_NOMBRE', 'ME_LOGO'),
        Index('_dta_index_C_MEDIO_5_651149365_70953536_K8_1_2_3_7', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_TM_ID', 'ME_LOGO'),
        Index('_dta_index_C_MEDIO_5_651149365__K7_K13_K5_K6_9987_4364_8066_1912', 'ME_PAIS_ID', 'ME_ESTADO_ID', 'ME_TM_ID', 'ME_PER_ID'),
        Index('_dta_index_C_MEDIO_5_651149365__K7_K2_K1_3_8_2533', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_TM_ID', 'ME_LOGO'),
        Index('_dta_index_C_MEDIO_5_651149365_100452352_K1_K7_3_8_12', 'ME_ID', 'ME_NOMBRE', 'ME_TM_ID', 'ME_LOGO', 'ME_TIRAJE'),
        Index('_dta_index_C_MEDIO_5_651149365_49279848_K1_3_7_8_12', 'ME_ID', 'ME_NOMBRE', 'ME_TM_ID', 'ME_LOGO', 'ME_TIRAJE'),
        Index('_dta_index_C_MEDIO_5_651149365_70953536_K1_3_7_8_12', 'ME_ID', 'ME_NOMBRE', 'ME_TM_ID', 'ME_LOGO', 'ME_TIRAJE'),
        Index('_dta_index_C_MEDIO_5_651149365__K1_2_3_4_5_6_7_8_9_10_11_12_13_14_15_16_17_18_9987', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_NOMBRE_CORTO', 'ME_PAIS_ID', 'ME_ESTADO_ID', 'ME_TM_ID', 'ME_LOGO', 'ME_LOGO_1', 'ME_VISIBLE', 'ME_EDIT_ID', 'ME_TIRAJE', 'ME_PER_ID', 'ME_CIUDAD_ID', 'ME_COSTO', 'ME_TCA_ID', 'ME_URL', 'ME_SUPLEMENTO'),
        Index('_dta_index_C_MEDIO_5_651149365__K1_K7_K2_1410', 'ME_ID', 'ME_LG_ID', 'ME_TM_ID'),
        Index('_dta_index_C_MEDIO_5_651149365__K7_K5_K6_1_2_3_4_8_9_10_11_12_13_14_15_16_17_18_19_20_21_22_23_24_25_26_27_28_29_30_31_32_33_34', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_NOMBRE_CORTO', 'ME_PAIS_ID', 'ME_ESTADO_ID', 'ME_TM_ID', 'ME_LOGO', 'ME_LOGO_1', 'ME_VISIBLE', 'ME_EDIT_ID', 'ME_TIRAJE', 'ME_PER_ID', 'ME_CIUDAD_ID', 'ME_COSTO', 'ME_TCA_ID', 'ME_URL', 'ME_SUPLEMENTO', 'ME_FORMA_ADQUISICION', 'ME_TELEFONO', 'ME_DIRECCION', 'ME_DIRECTOR', 'ME_FACEBOOK', 'ME_TWITTER', 'ME_CLASIFICACION', 'ME_TIER', 'ME_TIPO_DE_COBERTURA', 'ME_LINK_DESCARGA', 'ME_CLIENTE', 'ME_DIAS_DE_TRANSMISION', 'ME_RAITING', 'ME_FORMACAPTURA', 'ME_TIPO_TRANSMISION', 'ME_FECHA_PUBLICACION_APROX'),
        Index('_dta_index_C_MEDIO_5_651149365__K7_K1_3', 'ME_ID', 'ME_NOMBRE', 'ME_TM_ID'),
        Index('_dta_index_C_MEDIO_5_651149365__K1_3_7_8_12', 'ME_ID', 'ME_NOMBRE', 'ME_TM_ID', 'ME_LOGO', 'ME_TIRAJE'),
        Index('_dta_index_C_MEDIO_5_651149365_70952360_K1_3_7_8_12', 'ME_ID', 'ME_NOMBRE', 'ME_TM_ID', 'ME_LOGO', 'ME_TIRAJE'),
        Index('_dta_index_C_MEDIO_5_651149365__K7_1_9987', 'ME_ID', 'ME_TM_ID'),
        Index('_dta_index_C_MEDIO_5_651149365__K1_K7_3', 'ME_ID', 'ME_NOMBRE', 'ME_TM_ID'),
        Index('_dta_index_C_MEDIO_5_651149365_70953536_K1_K7_3_8_12', 'ME_ID', 'ME_NOMBRE', 'ME_TM_ID', 'ME_LOGO', 'ME_TIRAJE'),
        Index('_dta_index_C_MEDIO_5_651149365__K1_K7_K6_2_3_4_5_8_9_10_11_12_13_14_15_16_17_18_19_20_21_22_23_24_25_26_27_28_29_30_31_32_33_34', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_NOMBRE_CORTO', 'ME_PAIS_ID', 'ME_ESTADO_ID', 'ME_TM_ID', 'ME_LOGO', 'ME_LOGO_1', 'ME_VISIBLE', 'ME_EDIT_ID', 'ME_TIRAJE', 'ME_PER_ID', 'ME_CIUDAD_ID', 'ME_COSTO', 'ME_TCA_ID', 'ME_URL', 'ME_SUPLEMENTO', 'ME_FORMA_ADQUISICION', 'ME_TELEFONO', 'ME_DIRECCION', 'ME_DIRECTOR', 'ME_FACEBOOK', 'ME_TWITTER', 'ME_CLASIFICACION', 'ME_TIER', 'ME_TIPO_DE_COBERTURA', 'ME_LINK_DESCARGA', 'ME_CLIENTE', 'ME_DIAS_DE_TRANSMISION', 'ME_RAITING', 'ME_FORMACAPTURA', 'ME_TIPO_TRANSMISION', 'ME_FECHA_PUBLICACION_APROX'),
        Index('_dta_index_C_MEDIO_5_651149365__K1_K7', 'ME_ID', 'ME_TM_ID'),
        Index('_dta_index_C_MEDIO_5_651149365__K7_K6_K1_2_3_4_5_8_9_10_11_12_13_14_15_16_17_18_19_20_21_22_23_24_25_26_27_28_29_30_31_32_33_34', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_NOMBRE_CORTO', 'ME_PAIS_ID', 'ME_ESTADO_ID', 'ME_TM_ID', 'ME_LOGO', 'ME_LOGO_1', 'ME_VISIBLE', 'ME_EDIT_ID', 'ME_TIRAJE', 'ME_PER_ID', 'ME_CIUDAD_ID', 'ME_COSTO', 'ME_TCA_ID', 'ME_URL', 'ME_SUPLEMENTO', 'ME_FORMA_ADQUISICION', 'ME_TELEFONO', 'ME_DIRECCION', 'ME_DIRECTOR', 'ME_FACEBOOK', 'ME_TWITTER', 'ME_CLASIFICACION', 'ME_TIER', 'ME_TIPO_DE_COBERTURA', 'ME_LINK_DESCARGA', 'ME_CLIENTE', 'ME_DIAS_DE_TRANSMISION', 'ME_RAITING', 'ME_FORMACAPTURA', 'ME_TIPO_TRANSMISION', 'ME_FECHA_PUBLICACION_APROX'),
        Index('_dta_index_C_MEDIO_5_651149365__K1_2_3_4_5_6_7_8_9_10_11_12_13_14_15_16_17_18_19_20_21_22_23_24_25_26_27_28_29_30_31_32_33_34', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_NOMBRE_CORTO', 'ME_PAIS_ID', 'ME_ESTADO_ID', 'ME_TM_ID', 'ME_LOGO', 'ME_LOGO_1', 'ME_VISIBLE', 'ME_EDIT_ID', 'ME_TIRAJE', 'ME_PER_ID', 'ME_CIUDAD_ID', 'ME_COSTO', 'ME_TCA_ID', 'ME_URL', 'ME_SUPLEMENTO', 'ME_FORMA_ADQUISICION', 'ME_TELEFONO', 'ME_DIRECCION', 'ME_DIRECTOR', 'ME_FACEBOOK', 'ME_TWITTER', 'ME_CLASIFICACION', 'ME_TIER', 'ME_TIPO_DE_COBERTURA', 'ME_LINK_DESCARGA', 'ME_CLIENTE', 'ME_DIAS_DE_TRANSMISION', 'ME_RAITING', 'ME_FORMACAPTURA', 'ME_TIPO_TRANSMISION', 'ME_FECHA_PUBLICACION_APROX'),
        Index('_dta_index_C_MEDIO_5_651149365_70952360_K1_K7_3_8_12', 'ME_ID', 'ME_NOMBRE', 'ME_TM_ID', 'ME_LOGO', 'ME_TIRAJE'),
        Index('_dta_index_C_MEDIO_5_651149365__K18_K1_K7_1912', 'ME_ID', 'ME_TM_ID', 'ME_SUPLEMENTO'),
        Index('_dta_index_C_MEDIO_5_651149365__K1_3_7_9987', 'ME_ID', 'ME_NOMBRE', 'ME_TM_ID'),
        Index('_dta_index_C_MEDIO_5_651149365__K7_K13_K5_K6_9987_4364_8066_1912_4149', 'ME_PAIS_ID', 'ME_ESTADO_ID', 'ME_TM_ID', 'ME_PER_ID'),
        Index('_dta_index_C_MEDIO_5_651149365_49239816_K7_K2_K1_3_8', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_TM_ID', 'ME_LOGO'),
        Index('_dta_index_C_MEDIO_5_651149365__K7_K13_K5_K6_9987_4364_8066', 'ME_PAIS_ID', 'ME_ESTADO_ID', 'ME_TM_ID', 'ME_PER_ID'),
        Index('_dta_index_C_MEDIO_5_651149365_70953536_K7_K1_3_8_12', 'ME_ID', 'ME_NOMBRE', 'ME_TM_ID', 'ME_LOGO', 'ME_TIRAJE'),
        Index('_dta_index_C_MEDIO_5_651149365__K7_1_3_6', 'ME_ID', 'ME_NOMBRE', 'ME_ESTADO_ID', 'ME_TM_ID'),
        Index('_dta_index_C_MEDIO_5_651149365__K1_2_3_4_5_6_7_8_9_10_11_12_13_14_15_16_17_18_9987_4364', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_NOMBRE_CORTO', 'ME_PAIS_ID', 'ME_ESTADO_ID', 'ME_TM_ID', 'ME_LOGO', 'ME_LOGO_1', 'ME_VISIBLE', 'ME_EDIT_ID', 'ME_TIRAJE', 'ME_PER_ID', 'ME_CIUDAD_ID', 'ME_COSTO', 'ME_TCA_ID', 'ME_URL', 'ME_SUPLEMENTO'),
        Index('_dta_index_C_MEDIO_5_651149365_104889936_K1_2_3_4_5_6_7_8_9_10_11_12_13_14_15_16_17_18_19_20_21_22_23_24_25_26_27_28_29_30_31_', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_NOMBRE_CORTO', 'ME_PAIS_ID', 'ME_ESTADO_ID', 'ME_TM_ID', 'ME_LOGO', 'ME_LOGO_1', 'ME_VISIBLE', 'ME_EDIT_ID', 'ME_TIRAJE', 'ME_PER_ID', 'ME_CIUDAD_ID', 'ME_COSTO', 'ME_TCA_ID', 'ME_URL', 'ME_SUPLEMENTO', 'ME_FORMA_ADQUISICION', 'ME_TELEFONO', 'ME_DIRECCION', 'ME_DIRECTOR', 'ME_FACEBOOK', 'ME_TWITTER', 'ME_CLASIFICACION', 'ME_TIER', 'ME_TIPO_DE_COBERTURA', 'ME_LINK_DESCARGA', 'ME_CLIENTE', 'ME_DIAS_DE_TRANSMISION', 'ME_RAITING', 'ME_FORMACAPTURA', 'ME_TIPO_TRANSMISION', 'ME_FECHA_PUBLICACION_APROX'),
        Index('_dta_index_C_MEDIO_5_651149365__K1_K7_2_3_8_12', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_TM_ID', 'ME_LOGO', 'ME_TIRAJE'),
        Index('_dta_index_C_MEDIO_5_651149365_49239816_K2_K7_1_3_8', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_TM_ID', 'ME_LOGO'),
        Index('_dta_index_C_MEDIO_5_651149365__K6_K7_1_3', 'ME_ID', 'ME_NOMBRE', 'ME_ESTADO_ID', 'ME_TM_ID'),
        Index('_dta_index_C_MEDIO_5_651149365__K7_K1', 'ME_ID', 'ME_TM_ID'),
        Index('_dta_index_C_MEDIO_5_651149365__K7_K1_8066', 'ME_ID', 'ME_TM_ID'),
        Index('_dta_index_C_MEDIO_5_651149365__K7_K1_9987_4364_8066', 'ME_ID', 'ME_TM_ID'),
        Index('_dta_index_C_MEDIO_5_651149365__K6_1_2_3_4_5_7_8_9_10_11_12_13_14_15_16_17_18_19_20_21_22_23_24_25_26_27_28_29_30_31_32_33_34', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_NOMBRE_CORTO', 'ME_PAIS_ID', 'ME_ESTADO_ID', 'ME_TM_ID', 'ME_LOGO', 'ME_LOGO_1', 'ME_VISIBLE', 'ME_EDIT_ID', 'ME_TIRAJE', 'ME_PER_ID', 'ME_CIUDAD_ID', 'ME_COSTO', 'ME_TCA_ID', 'ME_URL', 'ME_SUPLEMENTO', 'ME_FORMA_ADQUISICION', 'ME_TELEFONO', 'ME_DIRECCION', 'ME_DIRECTOR', 'ME_FACEBOOK', 'ME_TWITTER', 'ME_CLASIFICACION', 'ME_TIER', 'ME_TIPO_DE_COBERTURA', 'ME_LINK_DESCARGA', 'ME_CLIENTE', 'ME_DIAS_DE_TRANSMISION', 'ME_RAITING', 'ME_FORMACAPTURA', 'ME_TIPO_TRANSMISION', 'ME_FECHA_PUBLICACION_APROX'),
        Index('_dta_index_C_MEDIO_5_651149365__K1_3_7_9987_4364', 'ME_ID', 'ME_NOMBRE', 'ME_TM_ID'),
        Index('_dta_index_C_MEDIO_5_651149365__K1_K7_K5_K6_2_3_4_8_9_10_11_12_13_14_15_16_17_18_19_20_21_22_23_24_25_26_27_28_29_30_31_32_33_', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_NOMBRE_CORTO', 'ME_PAIS_ID', 'ME_ESTADO_ID', 'ME_TM_ID', 'ME_LOGO', 'ME_LOGO_1', 'ME_VISIBLE', 'ME_EDIT_ID', 'ME_TIRAJE', 'ME_PER_ID', 'ME_CIUDAD_ID', 'ME_COSTO', 'ME_TCA_ID', 'ME_URL', 'ME_SUPLEMENTO', 'ME_FORMA_ADQUISICION', 'ME_TELEFONO', 'ME_DIRECCION', 'ME_DIRECTOR', 'ME_FACEBOOK', 'ME_TWITTER', 'ME_CLASIFICACION', 'ME_TIER', 'ME_TIPO_DE_COBERTURA', 'ME_LINK_DESCARGA', 'ME_CLIENTE', 'ME_DIAS_DE_TRANSMISION', 'ME_RAITING', 'ME_FORMACAPTURA', 'ME_TIPO_TRANSMISION', 'ME_FECHA_PUBLICACION_APROX'),
        Index('_dta_index_C_MEDIO_5_651149365_49239816_K8_1_2_3_7', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_TM_ID', 'ME_LOGO'),
        Index('_dta_index_C_MEDIO_5_651149365__K1_K7_5201_6497', 'ME_ID', 'ME_TM_ID'),
        Index('_dta_index_C_MEDIO_5_651149365__K1_K7_1912', 'ME_ID', 'ME_TM_ID'),
        Index('_dta_index_C_MEDIO_5_651149365__K7_K6_1_3', 'ME_ID', 'ME_NOMBRE', 'ME_ESTADO_ID', 'ME_TM_ID'),
        Index('_dta_index_C_MEDIO_5_651149365__K1_3_4_8_9_10_11_12_13_14_15_16_17_18_19_20_21_22_23_24_25_26_27_28_29_30_31_32_33_34', 'ME_ID', 'ME_NOMBRE', 'ME_NOMBRE_CORTO', 'ME_LOGO', 'ME_LOGO_1', 'ME_VISIBLE', 'ME_EDIT_ID', 'ME_TIRAJE', 'ME_PER_ID', 'ME_CIUDAD_ID', 'ME_COSTO', 'ME_TCA_ID', 'ME_URL', 'ME_SUPLEMENTO', 'ME_FORMA_ADQUISICION', 'ME_TELEFONO', 'ME_DIRECCION', 'ME_DIRECTOR', 'ME_FACEBOOK', 'ME_TWITTER', 'ME_CLASIFICACION', 'ME_TIER', 'ME_TIPO_DE_COBERTURA', 'ME_LINK_DESCARGA', 'ME_CLIENTE', 'ME_DIAS_DE_TRANSMISION', 'ME_RAITING', 'ME_FORMACAPTURA', 'ME_TIPO_TRANSMISION', 'ME_FECHA_PUBLICACION_APROX'),
        Index('_dta_index_C_MEDIO_5_651149365__K7_K1_3_9987', 'ME_ID', 'ME_NOMBRE', 'ME_TM_ID'),
        Index('_dta_index_C_MEDIO_5_651149365__K7_1_3_6_9987', 'ME_ID', 'ME_NOMBRE', 'ME_ESTADO_ID', 'ME_TM_ID'),
        Index('_dta_index_C_MEDIO_5_651149365__K1_3_7_8_12_9987', 'ME_ID', 'ME_NOMBRE', 'ME_TM_ID', 'ME_LOGO', 'ME_TIRAJE'),
        Index('_dta_index_C_MEDIO_5_651149365__K7_K6_1_2_3_4_5_8_9_10_11_12_13_14_15_16_17_18_19_20_21_22_23_24_25_26_27_28_29_30_31_32_33_34', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_NOMBRE_CORTO', 'ME_PAIS_ID', 'ME_ESTADO_ID', 'ME_TM_ID', 'ME_LOGO', 'ME_LOGO_1', 'ME_VISIBLE', 'ME_EDIT_ID', 'ME_TIRAJE', 'ME_PER_ID', 'ME_CIUDAD_ID', 'ME_COSTO', 'ME_TCA_ID', 'ME_URL', 'ME_SUPLEMENTO', 'ME_FORMA_ADQUISICION', 'ME_TELEFONO', 'ME_DIRECCION', 'ME_DIRECTOR', 'ME_FACEBOOK', 'ME_TWITTER', 'ME_CLASIFICACION', 'ME_TIER', 'ME_TIPO_DE_COBERTURA', 'ME_LINK_DESCARGA', 'ME_CLIENTE', 'ME_DIAS_DE_TRANSMISION', 'ME_RAITING', 'ME_FORMACAPTURA', 'ME_TIPO_TRANSMISION', 'ME_FECHA_PUBLICACION_APROX'),
        Index('_dta_index_C_MEDIO_5_651149365__K7_K1_K5_K6_2_3_4_8_9_10_11_12_13_14_15_16_17_18_19_20_21_22_23_24_25_26_27_28_29_30_31_32_33_', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_NOMBRE_CORTO', 'ME_PAIS_ID', 'ME_ESTADO_ID', 'ME_TM_ID', 'ME_LOGO', 'ME_LOGO_1', 'ME_VISIBLE', 'ME_EDIT_ID', 'ME_TIRAJE', 'ME_PER_ID', 'ME_CIUDAD_ID', 'ME_COSTO', 'ME_TCA_ID', 'ME_URL', 'ME_SUPLEMENTO', 'ME_FORMA_ADQUISICION', 'ME_TELEFONO', 'ME_DIRECCION', 'ME_DIRECTOR', 'ME_FACEBOOK', 'ME_TWITTER', 'ME_CLASIFICACION', 'ME_TIER', 'ME_TIPO_DE_COBERTURA', 'ME_LINK_DESCARGA', 'ME_CLIENTE', 'ME_DIAS_DE_TRANSMISION', 'ME_RAITING', 'ME_FORMACAPTURA', 'ME_TIPO_TRANSMISION', 'ME_FECHA_PUBLICACION_APROX'),
        Index('_dta_index_C_MEDIO_5_651149365_49239816_K7_K1_3_8_12', 'ME_ID', 'ME_NOMBRE', 'ME_TM_ID', 'ME_LOGO', 'ME_TIRAJE'),
        Index('_dta_index_C_MEDIO_5_651149365__K1_K7_3_4364', 'ME_ID', 'ME_NOMBRE', 'ME_TM_ID'),
        Index('_dta_index_C_MEDIO_5_651149365__K7_K2_K1_2894', 'ME_ID', 'ME_LG_ID', 'ME_TM_ID'),
        Index('_dta_index_C_MEDIO_5_651149365__K1_K6_9987', 'ME_ID', 'ME_ESTADO_ID'),
        Index('_dta_index_C_MEDIO_5_651149365__K6_K7_1_3_4364', 'ME_ID', 'ME_NOMBRE', 'ME_ESTADO_ID', 'ME_TM_ID'),
        Index('_dta_index_C_MEDIO_5_651149365__K1_K7_K5_K6_2', 'ME_ID', 'ME_LG_ID', 'ME_PAIS_ID', 'ME_ESTADO_ID', 'ME_TM_ID'),
        Index('_dta_index_C_MEDIO_5_651149365__K1_K7_K5_K6_2_5201', 'ME_ID', 'ME_LG_ID', 'ME_PAIS_ID', 'ME_ESTADO_ID', 'ME_TM_ID'),
        Index('_dta_index_C_MEDIO_5_651149365__K7_K1_3_8_12_4364', 'ME_ID', 'ME_NOMBRE', 'ME_TM_ID', 'ME_LOGO', 'ME_TIRAJE'),
        Index('_dta_index_C_MEDIO_5_651149365__K1_3_8_6960', 'ME_ID', 'ME_NOMBRE', 'ME_LOGO'),
        Index('_dta_index_C_MEDIO_5_651149365__K6_K1_4364', 'ME_ID', 'ME_ESTADO_ID'),
        Index('_dta_index_C_MEDIO_5_651149365__K7_K6_1_3_9987', 'ME_ID', 'ME_NOMBRE', 'ME_ESTADO_ID', 'ME_TM_ID'),
        Index('_dta_index_C_MEDIO_5_651149365__K7_K5_K6_K1_2', 'ME_ID', 'ME_LG_ID', 'ME_PAIS_ID', 'ME_ESTADO_ID', 'ME_TM_ID'),
        Index('_dta_index_C_MEDIO_5_651149365_49239816_K1_3_7_8_12', 'ME_ID', 'ME_NOMBRE', 'ME_TM_ID', 'ME_LOGO', 'ME_TIRAJE'),
        Index('_dta_index_C_MEDIO_5_651149365__K1_K6_9987_4364', 'ME_ID', 'ME_ESTADO_ID'),
        Index('_dta_index_C_MEDIO_5_651149365__K7_K5_K6_K1_2_6497', 'ME_ID', 'ME_LG_ID', 'ME_PAIS_ID', 'ME_ESTADO_ID', 'ME_TM_ID'),
        Index('_dta_index_C_MEDIO_5_651149365__K1_K7_K5_K6_2_4149_5201', 'ME_ID', 'ME_LG_ID', 'ME_PAIS_ID', 'ME_ESTADO_ID', 'ME_TM_ID'),
        Index('_dta_index_C_MEDIO_5_651149365__K7_K5_K6_K1_2_3_4_8_9_10_11_12_13_14_15_16_17_18_19_20_21_22_23_24_25_26_27_28_29_30_31_32_33_', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_NOMBRE_CORTO', 'ME_PAIS_ID', 'ME_ESTADO_ID', 'ME_TM_ID', 'ME_LOGO', 'ME_LOGO_1', 'ME_VISIBLE', 'ME_EDIT_ID', 'ME_TIRAJE', 'ME_PER_ID', 'ME_CIUDAD_ID', 'ME_COSTO', 'ME_TCA_ID', 'ME_URL', 'ME_SUPLEMENTO', 'ME_FORMA_ADQUISICION', 'ME_TELEFONO', 'ME_DIRECCION', 'ME_DIRECTOR', 'ME_FACEBOOK', 'ME_TWITTER', 'ME_CLASIFICACION', 'ME_TIER', 'ME_TIPO_DE_COBERTURA', 'ME_LINK_DESCARGA', 'ME_CLIENTE', 'ME_DIAS_DE_TRANSMISION', 'ME_RAITING', 'ME_FORMACAPTURA', 'ME_TIPO_TRANSMISION', 'ME_FECHA_PUBLICACION_APROX'),
        Index('_dta_index_C_MEDIO_5_651149365__K6_K1_8066', 'ME_ID', 'ME_ESTADO_ID'),
        Index('_dta_index_C_MEDIO_5_651149365__K7_1_3', 'ME_ID', 'ME_NOMBRE', 'ME_TM_ID'),
        Index('_dta_index_C_MEDIO_5_651149365__K7_K1_K2_3_8_9987_4364_8066', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_TM_ID', 'ME_LOGO'),
        Index('_dta_index_C_MEDIO_5_651149365__K7_K5_K6_K1_2_6497_1040', 'ME_ID', 'ME_LG_ID', 'ME_PAIS_ID', 'ME_ESTADO_ID', 'ME_TM_ID'),
        Index('_dta_index_C_MEDIO_5_651149365__K1_2_3_6_7_8_12', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_ESTADO_ID', 'ME_TM_ID', 'ME_LOGO', 'ME_TIRAJE'),
        Index('_dta_index_C_MEDIO_5_651149365__K1_K7_K6_K5_2_3_4_8_9_10_11_12_13_14_15_16_17_18_19_20_21_22_23_24_25_26_27_28_29_30_31_32_33_', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_NOMBRE_CORTO', 'ME_PAIS_ID', 'ME_ESTADO_ID', 'ME_TM_ID', 'ME_LOGO', 'ME_LOGO_1', 'ME_VISIBLE', 'ME_EDIT_ID', 'ME_TIRAJE', 'ME_PER_ID', 'ME_CIUDAD_ID', 'ME_COSTO', 'ME_TCA_ID', 'ME_URL', 'ME_SUPLEMENTO', 'ME_FORMA_ADQUISICION', 'ME_TELEFONO', 'ME_DIRECCION', 'ME_DIRECTOR', 'ME_FACEBOOK', 'ME_TWITTER', 'ME_CLASIFICACION', 'ME_TIER', 'ME_TIPO_DE_COBERTURA', 'ME_LINK_DESCARGA', 'ME_CLIENTE', 'ME_DIAS_DE_TRANSMISION', 'ME_RAITING', 'ME_FORMACAPTURA', 'ME_TIPO_TRANSMISION', 'ME_FECHA_PUBLICACION_APROX'),
        Index('_dta_index_C_MEDIO_5_651149365__K2_K7_1_1912', 'ME_ID', 'ME_LG_ID', 'ME_TM_ID'),
        Index('_dta_index_C_MEDIO_5_651149365__K7_K1_9987_4364_8066_1912', 'ME_ID', 'ME_TM_ID'),
        Index('_dta_index_C_MEDIO_5_651149365__K7_1_3_9987_4364_8066', 'ME_ID', 'ME_NOMBRE', 'ME_TM_ID'),
        Index('_dta_index_C_MEDIO_5_651149365__K1_2_3_6_7_8_12_6497', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_ESTADO_ID', 'ME_TM_ID', 'ME_LOGO', 'ME_TIRAJE'),
        Index('_dta_index_C_MEDIO_5_651149365__K7_K6_K5_K1_2_3_4_8_9_10_11_12_13_14_15_16_17_18_19_20_21_22_23_24_25_26_27_28_29_30_31_32_33_', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_NOMBRE_CORTO', 'ME_PAIS_ID', 'ME_ESTADO_ID', 'ME_TM_ID', 'ME_LOGO', 'ME_LOGO_1', 'ME_VISIBLE', 'ME_EDIT_ID', 'ME_TIRAJE', 'ME_PER_ID', 'ME_CIUDAD_ID', 'ME_COSTO', 'ME_TCA_ID', 'ME_URL', 'ME_SUPLEMENTO', 'ME_FORMA_ADQUISICION', 'ME_TELEFONO', 'ME_DIRECCION', 'ME_DIRECTOR', 'ME_FACEBOOK', 'ME_TWITTER', 'ME_CLASIFICACION', 'ME_TIER', 'ME_TIPO_DE_COBERTURA', 'ME_LINK_DESCARGA', 'ME_CLIENTE', 'ME_DIAS_DE_TRANSMISION', 'ME_RAITING', 'ME_FORMACAPTURA', 'ME_TIPO_TRANSMISION', 'ME_FECHA_PUBLICACION_APROX'),
        Index('_dta_index_C_MEDIO_5_651149365_49279848_K7_K1_3_8_12', 'ME_ID', 'ME_NOMBRE', 'ME_TM_ID', 'ME_LOGO', 'ME_TIRAJE'),
        Index('_dta_index_C_MEDIO_5_651149365__K8_1_2_3_7_5201_6497', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_TM_ID', 'ME_LOGO'),
        Index('_dta_index_C_MEDIO_5_651149365__K1_K7_4149_5201', 'ME_ID', 'ME_TM_ID'),
        Index('_dta_index_C_MEDIO_5_651149365__K7_K1_K6_K5_2_3_4_8_9_10_11_12_13_14_15_16_17_18_19_20_21_22_23_24_25_26_27_28_29_30_31_32_33_', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_NOMBRE_CORTO', 'ME_PAIS_ID', 'ME_ESTADO_ID', 'ME_TM_ID', 'ME_LOGO', 'ME_LOGO_1', 'ME_VISIBLE', 'ME_EDIT_ID', 'ME_TIRAJE', 'ME_PER_ID', 'ME_CIUDAD_ID', 'ME_COSTO', 'ME_TCA_ID', 'ME_URL', 'ME_SUPLEMENTO', 'ME_FORMA_ADQUISICION', 'ME_TELEFONO', 'ME_DIRECCION', 'ME_DIRECTOR', 'ME_FACEBOOK', 'ME_TWITTER', 'ME_CLASIFICACION', 'ME_TIER', 'ME_TIPO_DE_COBERTURA', 'ME_LINK_DESCARGA', 'ME_CLIENTE', 'ME_DIAS_DE_TRANSMISION', 'ME_RAITING', 'ME_FORMACAPTURA', 'ME_TIPO_TRANSMISION', 'ME_FECHA_PUBLICACION_APROX'),
        Index('_dta_index_C_MEDIO_5_651149365__K7_K2_K1_3_8_9850', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_TM_ID', 'ME_LOGO'),
        Index('_dta_index_C_MEDIO_5_651149365__K7_K1_3_1912', 'ME_ID', 'ME_NOMBRE', 'ME_TM_ID'),
        Index('_dta_index_C_MEDIO_5_651149365__K8_1_3_1040_1771', 'ME_ID', 'ME_NOMBRE', 'ME_LOGO'),
        Index('_dta_index_C_MEDIO_5_651149365__K1_3_7_8_12_9987_4364', 'ME_ID', 'ME_NOMBRE', 'ME_TM_ID', 'ME_LOGO', 'ME_TIRAJE'),
        Index('_dta_index_C_MEDIO_5_651149365_104889936_K7_K6_K5_K1_2_3_4_8_9_10_11_12_13_14_15_16_17_18_19_20_21_22_23_24_25_26_27_28_29_30_', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_NOMBRE_CORTO', 'ME_PAIS_ID', 'ME_ESTADO_ID', 'ME_TM_ID', 'ME_LOGO', 'ME_LOGO_1', 'ME_VISIBLE', 'ME_EDIT_ID', 'ME_TIRAJE', 'ME_PER_ID', 'ME_CIUDAD_ID', 'ME_COSTO', 'ME_TCA_ID', 'ME_URL', 'ME_SUPLEMENTO', 'ME_FORMA_ADQUISICION', 'ME_TELEFONO', 'ME_DIRECCION', 'ME_DIRECTOR', 'ME_FACEBOOK', 'ME_TWITTER', 'ME_CLASIFICACION', 'ME_TIER', 'ME_TIPO_DE_COBERTURA', 'ME_LINK_DESCARGA', 'ME_CLIENTE', 'ME_DIAS_DE_TRANSMISION', 'ME_RAITING', 'ME_FORMACAPTURA', 'ME_TIPO_TRANSMISION', 'ME_FECHA_PUBLICACION_APROX'),
        Index('_dta_index_C_MEDIO_5_651149365_49279848_K1_K7_3_8_12', 'ME_ID', 'ME_NOMBRE', 'ME_TM_ID', 'ME_LOGO', 'ME_TIRAJE'),
        Index('_dta_index_C_MEDIO_5_651149365__K1_K7_3_4149', 'ME_ID', 'ME_NOMBRE', 'ME_TM_ID'),
        Index('_dta_index_C_MEDIO_5_651149365__K7_K1_3_8_12_8066', 'ME_ID', 'ME_NOMBRE', 'ME_TM_ID', 'ME_LOGO', 'ME_TIRAJE'),
        Index('_dta_index_C_MEDIO_5_651149365_104889936_K7_K1_K6_K5_2_3_4_8_9_10_11_12_13_14_15_16_17_18_19_20_21_22_23_24_25_26_27_28_29_30_', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_NOMBRE_CORTO', 'ME_PAIS_ID', 'ME_ESTADO_ID', 'ME_TM_ID', 'ME_LOGO', 'ME_LOGO_1', 'ME_VISIBLE', 'ME_EDIT_ID', 'ME_TIRAJE', 'ME_PER_ID', 'ME_CIUDAD_ID', 'ME_COSTO', 'ME_TCA_ID', 'ME_URL', 'ME_SUPLEMENTO', 'ME_FORMA_ADQUISICION', 'ME_TELEFONO', 'ME_DIRECCION', 'ME_DIRECTOR', 'ME_FACEBOOK', 'ME_TWITTER', 'ME_CLASIFICACION', 'ME_TIER', 'ME_TIPO_DE_COBERTURA', 'ME_LINK_DESCARGA', 'ME_CLIENTE', 'ME_DIAS_DE_TRANSMISION', 'ME_RAITING', 'ME_FORMACAPTURA', 'ME_TIPO_TRANSMISION', 'ME_FECHA_PUBLICACION_APROX'),
        Index('_dta_index_C_MEDIO_5_651149365__K1_K7_K2_3_8_2533', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_TM_ID', 'ME_LOGO'),
        Index('_dta_index_C_MEDIO_5_651149365__K2_K7_1_9987', 'ME_ID', 'ME_LG_ID', 'ME_TM_ID'),
        Index('_dta_index_C_MEDIO_5_651149365_104890048_K7_K6_K5_K1_2_3_4_8_9_10_11_12_13_14_15_16_17_18_19_20_21_22_23_24_25_26_27_28_29_30_', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_NOMBRE_CORTO', 'ME_PAIS_ID', 'ME_ESTADO_ID', 'ME_TM_ID', 'ME_LOGO', 'ME_LOGO_1', 'ME_VISIBLE', 'ME_EDIT_ID', 'ME_TIRAJE', 'ME_PER_ID', 'ME_CIUDAD_ID', 'ME_COSTO', 'ME_TCA_ID', 'ME_URL', 'ME_SUPLEMENTO', 'ME_FORMA_ADQUISICION', 'ME_TELEFONO', 'ME_DIRECCION', 'ME_DIRECTOR', 'ME_FACEBOOK', 'ME_TWITTER', 'ME_CLASIFICACION', 'ME_TIER', 'ME_TIPO_DE_COBERTURA', 'ME_LINK_DESCARGA', 'ME_CLIENTE', 'ME_DIAS_DE_TRANSMISION', 'ME_RAITING', 'ME_FORMACAPTURA', 'ME_TIPO_TRANSMISION', 'ME_FECHA_PUBLICACION_APROX'),
        Index('_dta_index_C_MEDIO_5_651149365__K8_1_2_3_7_4364', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_TM_ID', 'ME_LOGO'),
        Index('_dta_index_C_MEDIO_5_651149365__K1_K7_K5_K6_2_4149_5201_6497', 'ME_ID', 'ME_LG_ID', 'ME_PAIS_ID', 'ME_ESTADO_ID', 'ME_TM_ID'),
        Index('_dta_index_C_MEDIO_5_651149365_104889936_K7_K1_2_3_4_5_6_8_9_10_11_12_13_14_15_16_17_18_19_20_21_22_23_24_25_26_27_28_29_30_31_', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_NOMBRE_CORTO', 'ME_PAIS_ID', 'ME_ESTADO_ID', 'ME_TM_ID', 'ME_LOGO', 'ME_LOGO_1', 'ME_VISIBLE', 'ME_EDIT_ID', 'ME_TIRAJE', 'ME_PER_ID', 'ME_CIUDAD_ID', 'ME_COSTO', 'ME_TCA_ID', 'ME_URL', 'ME_SUPLEMENTO', 'ME_FORMA_ADQUISICION', 'ME_TELEFONO', 'ME_DIRECCION', 'ME_DIRECTOR', 'ME_FACEBOOK', 'ME_TWITTER', 'ME_CLASIFICACION', 'ME_TIER', 'ME_TIPO_DE_COBERTURA', 'ME_LINK_DESCARGA', 'ME_CLIENTE', 'ME_DIAS_DE_TRANSMISION', 'ME_RAITING', 'ME_FORMACAPTURA', 'ME_TIPO_TRANSMISION', 'ME_FECHA_PUBLICACION_APROX'),
        Index('_dta_index_C_MEDIO_5_651149365_104890048_K7_K1_K6_K5_2_3_4_8_9_10_11_12_13_14_15_16_17_18_19_20_21_22_23_24_25_26_27_28_29_30_', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_NOMBRE_CORTO', 'ME_PAIS_ID', 'ME_ESTADO_ID', 'ME_TM_ID', 'ME_LOGO', 'ME_LOGO_1', 'ME_VISIBLE', 'ME_EDIT_ID', 'ME_TIRAJE', 'ME_PER_ID', 'ME_CIUDAD_ID', 'ME_COSTO', 'ME_TCA_ID', 'ME_URL', 'ME_SUPLEMENTO', 'ME_FORMA_ADQUISICION', 'ME_TELEFONO', 'ME_DIRECCION', 'ME_DIRECTOR', 'ME_FACEBOOK', 'ME_TWITTER', 'ME_CLASIFICACION', 'ME_TIER', 'ME_TIPO_DE_COBERTURA', 'ME_LINK_DESCARGA', 'ME_CLIENTE', 'ME_DIAS_DE_TRANSMISION', 'ME_RAITING', 'ME_FORMACAPTURA', 'ME_TIPO_TRANSMISION', 'ME_FECHA_PUBLICACION_APROX'),
        Index('_dta_index_C_MEDIO_5_651149365_93568848_K7_K1_3_8_12', 'ME_ID', 'ME_NOMBRE', 'ME_TM_ID', 'ME_LOGO', 'ME_TIRAJE'),
        Index('_dta_index_C_MEDIO_5_651149365__K1_3_7_2894', 'ME_ID', 'ME_NOMBRE', 'ME_TM_ID'),
        Index('_dta_index_C_MEDIO_5_651149365_104890048_K7_K1_2_3_4_5_6_8_9_10_11_12_13_14_15_16_17_18_19_20_21_22_23_24_25_26_27_28_29_30_31_', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_NOMBRE_CORTO', 'ME_PAIS_ID', 'ME_ESTADO_ID', 'ME_TM_ID', 'ME_LOGO', 'ME_LOGO_1', 'ME_VISIBLE', 'ME_EDIT_ID', 'ME_TIRAJE', 'ME_PER_ID', 'ME_CIUDAD_ID', 'ME_COSTO', 'ME_TCA_ID', 'ME_URL', 'ME_SUPLEMENTO', 'ME_FORMA_ADQUISICION', 'ME_TELEFONO', 'ME_DIRECCION', 'ME_DIRECTOR', 'ME_FACEBOOK', 'ME_TWITTER', 'ME_CLASIFICACION', 'ME_TIER', 'ME_TIPO_DE_COBERTURA', 'ME_LINK_DESCARGA', 'ME_CLIENTE', 'ME_DIAS_DE_TRANSMISION', 'ME_RAITING', 'ME_FORMACAPTURA', 'ME_TIPO_TRANSMISION', 'ME_FECHA_PUBLICACION_APROX'),
        Index('_dta_index_C_MEDIO_5_651149365__K8_1_2_3_7_6497', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_TM_ID', 'ME_LOGO'),
        Index('_dta_index_C_MEDIO_5_651149365_104889936_K1_K7_K6_K5_2_3_4_8_9_10_11_12_13_14_15_16_17_18_19_20_21_22_23_24_25_26_27_28_29_30_', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_NOMBRE_CORTO', 'ME_PAIS_ID', 'ME_ESTADO_ID', 'ME_TM_ID', 'ME_LOGO', 'ME_LOGO_1', 'ME_VISIBLE', 'ME_EDIT_ID', 'ME_TIRAJE', 'ME_PER_ID', 'ME_CIUDAD_ID', 'ME_COSTO', 'ME_TCA_ID', 'ME_URL', 'ME_SUPLEMENTO', 'ME_FORMA_ADQUISICION', 'ME_TELEFONO', 'ME_DIRECCION', 'ME_DIRECTOR', 'ME_FACEBOOK', 'ME_TWITTER', 'ME_CLASIFICACION', 'ME_TIER', 'ME_TIPO_DE_COBERTURA', 'ME_LINK_DESCARGA', 'ME_CLIENTE', 'ME_DIAS_DE_TRANSMISION', 'ME_RAITING', 'ME_FORMACAPTURA', 'ME_TIPO_TRANSMISION', 'ME_FECHA_PUBLICACION_APROX'),
        Index('_dta_index_C_MEDIO_5_651149365__K2_K7_1_8066', 'ME_ID', 'ME_LG_ID', 'ME_TM_ID'),
        Index('_dta_index_C_MEDIO_5_651149365_104889936_K1_K7_2_3_4_5_6_8_9_10_11_12_13_14_15_16_17_18_19_20_21_22_23_24_25_26_27_28_29_30_31_', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_NOMBRE_CORTO', 'ME_PAIS_ID', 'ME_ESTADO_ID', 'ME_TM_ID', 'ME_LOGO', 'ME_LOGO_1', 'ME_VISIBLE', 'ME_EDIT_ID', 'ME_TIRAJE', 'ME_PER_ID', 'ME_CIUDAD_ID', 'ME_COSTO', 'ME_TCA_ID', 'ME_URL', 'ME_SUPLEMENTO', 'ME_FORMA_ADQUISICION', 'ME_TELEFONO', 'ME_DIRECCION', 'ME_DIRECTOR', 'ME_FACEBOOK', 'ME_TWITTER', 'ME_CLASIFICACION', 'ME_TIER', 'ME_TIPO_DE_COBERTURA', 'ME_LINK_DESCARGA', 'ME_CLIENTE', 'ME_DIAS_DE_TRANSMISION', 'ME_RAITING', 'ME_FORMACAPTURA', 'ME_TIPO_TRANSMISION', 'ME_FECHA_PUBLICACION_APROX'),
        Index('_dta_index_C_MEDIO_5_651149365_93568736_K1_3_7_8_12', 'ME_ID', 'ME_NOMBRE', 'ME_TM_ID', 'ME_LOGO', 'ME_TIRAJE'),
        Index('_dta_index_C_MEDIO_5_651149365_104890048_K1_K7_K6_K5_2_3_4_8_9_10_11_12_13_14_15_16_17_18_19_20_21_22_23_24_25_26_27_28_29_30_', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_NOMBRE_CORTO', 'ME_PAIS_ID', 'ME_ESTADO_ID', 'ME_TM_ID', 'ME_LOGO', 'ME_LOGO_1', 'ME_VISIBLE', 'ME_EDIT_ID', 'ME_TIRAJE', 'ME_PER_ID', 'ME_CIUDAD_ID', 'ME_COSTO', 'ME_TCA_ID', 'ME_URL', 'ME_SUPLEMENTO', 'ME_FORMA_ADQUISICION', 'ME_TELEFONO', 'ME_DIRECCION', 'ME_DIRECTOR', 'ME_FACEBOOK', 'ME_TWITTER', 'ME_CLASIFICACION', 'ME_TIER', 'ME_TIPO_DE_COBERTURA', 'ME_LINK_DESCARGA', 'ME_CLIENTE', 'ME_DIAS_DE_TRANSMISION', 'ME_RAITING', 'ME_FORMACAPTURA', 'ME_TIPO_TRANSMISION', 'ME_FECHA_PUBLICACION_APROX'),
        Index('_dta_index_C_MEDIO_5_651149365_104890048_K1_K7_2_3_4_5_6_8_9_10_11_12_13_14_15_16_17_18_19_20_21_22_23_24_25_26_27_28_29_30_31_', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_NOMBRE_CORTO', 'ME_PAIS_ID', 'ME_ESTADO_ID', 'ME_TM_ID', 'ME_LOGO', 'ME_LOGO_1', 'ME_VISIBLE', 'ME_EDIT_ID', 'ME_TIRAJE', 'ME_PER_ID', 'ME_CIUDAD_ID', 'ME_COSTO', 'ME_TCA_ID', 'ME_URL', 'ME_SUPLEMENTO', 'ME_FORMA_ADQUISICION', 'ME_TELEFONO', 'ME_DIRECCION', 'ME_DIRECTOR', 'ME_FACEBOOK', 'ME_TWITTER', 'ME_CLASIFICACION', 'ME_TIER', 'ME_TIPO_DE_COBERTURA', 'ME_LINK_DESCARGA', 'ME_CLIENTE', 'ME_DIAS_DE_TRANSMISION', 'ME_RAITING', 'ME_FORMACAPTURA', 'ME_TIPO_TRANSMISION', 'ME_FECHA_PUBLICACION_APROX'),
        Index('_dta_index_C_MEDIO_5_651149365__K7_K1_K2_3_8', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_TM_ID', 'ME_LOGO'),
        Index('_dta_index_C_MEDIO_5_651149365_93568736_K1_K7_3_8_12', 'ME_ID', 'ME_NOMBRE', 'ME_TM_ID', 'ME_LOGO', 'ME_TIRAJE'),
        Index('_dta_index_C_MEDIO_5_651149365__K1_3_4_8_9_10_11_12_13_14_15_16_17_18_19_20_21_22_23_24_25_26_27_28_29_30_31_32_33_34_4364_8066', 'ME_ID', 'ME_NOMBRE', 'ME_NOMBRE_CORTO', 'ME_LOGO', 'ME_LOGO_1', 'ME_VISIBLE', 'ME_EDIT_ID', 'ME_TIRAJE', 'ME_PER_ID', 'ME_CIUDAD_ID', 'ME_COSTO', 'ME_TCA_ID', 'ME_URL', 'ME_SUPLEMENTO', 'ME_FORMA_ADQUISICION', 'ME_TELEFONO', 'ME_DIRECCION', 'ME_DIRECTOR', 'ME_FACEBOOK', 'ME_TWITTER', 'ME_CLASIFICACION', 'ME_TIER', 'ME_TIPO_DE_COBERTURA', 'ME_LINK_DESCARGA', 'ME_CLIENTE', 'ME_DIAS_DE_TRANSMISION', 'ME_RAITING', 'ME_FORMACAPTURA', 'ME_TIPO_TRANSMISION', 'ME_FECHA_PUBLICACION_APROX'),
        Index('_dta_index_C_MEDIO_5_651149365__K6_K1_2_3_4_5_7_8_9_10_11_12_13_14_15_16_17_18_19_20_21_22_23_24_25_26_27_28_29_30_31_32_33_34', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_NOMBRE_CORTO', 'ME_PAIS_ID', 'ME_ESTADO_ID', 'ME_TM_ID', 'ME_LOGO', 'ME_LOGO_1', 'ME_VISIBLE', 'ME_EDIT_ID', 'ME_TIRAJE', 'ME_PER_ID', 'ME_CIUDAD_ID', 'ME_COSTO', 'ME_TCA_ID', 'ME_URL', 'ME_SUPLEMENTO', 'ME_FORMA_ADQUISICION', 'ME_TELEFONO', 'ME_DIRECCION', 'ME_DIRECTOR', 'ME_FACEBOOK', 'ME_TWITTER', 'ME_CLASIFICACION', 'ME_TIER', 'ME_TIPO_DE_COBERTURA', 'ME_LINK_DESCARGA', 'ME_CLIENTE', 'ME_DIAS_DE_TRANSMISION', 'ME_RAITING', 'ME_FORMACAPTURA', 'ME_TIPO_TRANSMISION', 'ME_FECHA_PUBLICACION_APROX'),
        Index('_dta_index_C_MEDIO_5_651149365__K2_K7_1', 'ME_ID', 'ME_LG_ID', 'ME_TM_ID'),
        Index('_dta_index_C_MEDIO_5_651149365__K1_K6_2_3_4_5_7_8_9_10_11_12_13_14_15_16_17_18_19_20_21_22_23_24_25_26_27_28_29_30_31_32_33_34', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_NOMBRE_CORTO', 'ME_PAIS_ID', 'ME_ESTADO_ID', 'ME_TM_ID', 'ME_LOGO', 'ME_LOGO_1', 'ME_VISIBLE', 'ME_EDIT_ID', 'ME_TIRAJE', 'ME_PER_ID', 'ME_CIUDAD_ID', 'ME_COSTO', 'ME_TCA_ID', 'ME_URL', 'ME_SUPLEMENTO', 'ME_FORMA_ADQUISICION', 'ME_TELEFONO', 'ME_DIRECCION', 'ME_DIRECTOR', 'ME_FACEBOOK', 'ME_TWITTER', 'ME_CLASIFICACION', 'ME_TIER', 'ME_TIPO_DE_COBERTURA', 'ME_LINK_DESCARGA', 'ME_CLIENTE', 'ME_DIAS_DE_TRANSMISION', 'ME_RAITING', 'ME_FORMACAPTURA', 'ME_TIPO_TRANSMISION', 'ME_FECHA_PUBLICACION_APROX'),
        Index('_dta_index_C_MEDIO_5_651149365_51857368_K1_K7_3_8_12', 'ME_ID', 'ME_NOMBRE', 'ME_TM_ID', 'ME_LOGO', 'ME_TIRAJE'),
        Index('_dta_index_C_MEDIO_5_651149365__K1_3_7_8_12_1973', 'ME_ID', 'ME_NOMBRE', 'ME_TM_ID', 'ME_LOGO', 'ME_TIRAJE'),
        Index('_dta_index_C_MEDIO_5_651149365__K8_1_3_1040', 'ME_ID', 'ME_NOMBRE', 'ME_LOGO'),
        Index('_dta_index_C_MEDIO_5_651149365__K8_1_2_3_7', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_TM_ID', 'ME_LOGO'),
        Index('_dta_index_C_MEDIO_5_651149365_100452352_K6_K1_2_3_4_5_7_8_9_10_11_12_13_14_15_16_17_18_19_20_21_22_23_24_25_26_27_28_29_30_31_', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_NOMBRE_CORTO', 'ME_PAIS_ID', 'ME_ESTADO_ID', 'ME_TM_ID', 'ME_LOGO', 'ME_LOGO_1', 'ME_VISIBLE', 'ME_EDIT_ID', 'ME_TIRAJE', 'ME_PER_ID', 'ME_CIUDAD_ID', 'ME_COSTO', 'ME_TCA_ID', 'ME_URL', 'ME_SUPLEMENTO', 'ME_FORMA_ADQUISICION', 'ME_TELEFONO', 'ME_DIRECCION', 'ME_DIRECTOR', 'ME_FACEBOOK', 'ME_TWITTER', 'ME_CLASIFICACION', 'ME_TIER', 'ME_TIPO_DE_COBERTURA', 'ME_LINK_DESCARGA', 'ME_CLIENTE', 'ME_DIAS_DE_TRANSMISION', 'ME_RAITING', 'ME_FORMACAPTURA', 'ME_TIPO_TRANSMISION', 'ME_FECHA_PUBLICACION_APROX'),
        Index('_dta_index_C_MEDIO_5_651149365__K8_1_3', 'ME_ID', 'ME_NOMBRE', 'ME_LOGO'),
        Index('_dta_index_C_MEDIO_5_651149365__K7_K1_3_4364', 'ME_ID', 'ME_NOMBRE', 'ME_TM_ID'),
        Index('_dta_index_C_MEDIO_5_651149365__K1_K7_3_8_12_6221', 'ME_ID', 'ME_NOMBRE', 'ME_TM_ID', 'ME_LOGO', 'ME_TIRAJE'),
        Index('_dta_index_C_MEDIO_5_651149365_100452352_K1_K6_2_3_4_5_7_8_9_10_11_12_13_14_15_16_17_18_19_20_21_22_23_24_25_26_27_28_29_30_31_', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_NOMBRE_CORTO', 'ME_PAIS_ID', 'ME_ESTADO_ID', 'ME_TM_ID', 'ME_LOGO', 'ME_LOGO_1', 'ME_VISIBLE', 'ME_EDIT_ID', 'ME_TIRAJE', 'ME_PER_ID', 'ME_CIUDAD_ID', 'ME_COSTO', 'ME_TCA_ID', 'ME_URL', 'ME_SUPLEMENTO', 'ME_FORMA_ADQUISICION', 'ME_TELEFONO', 'ME_DIRECCION', 'ME_DIRECTOR', 'ME_FACEBOOK', 'ME_TWITTER', 'ME_CLASIFICACION', 'ME_TIER', 'ME_TIPO_DE_COBERTURA', 'ME_LINK_DESCARGA', 'ME_CLIENTE', 'ME_DIAS_DE_TRANSMISION', 'ME_RAITING', 'ME_FORMACAPTURA', 'ME_TIPO_TRANSMISION', 'ME_FECHA_PUBLICACION_APROX'),
        Index('_dta_index_C_MEDIO_5_651149365__K7_K5_K6_K1_2_5201', 'ME_ID', 'ME_LG_ID', 'ME_PAIS_ID', 'ME_ESTADO_ID', 'ME_TM_ID'),
        Index('_dta_index_C_MEDIO_5_651149365__K1_K7_K2_3_8', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_TM_ID', 'ME_LOGO'),
        Index('_dta_index_C_MEDIO_5_651149365__K1_K7_3_8066', 'ME_ID', 'ME_NOMBRE', 'ME_TM_ID'),
        Index('_dta_index_C_MEDIO_5_651149365__K10_1_2_3_4_5_6_7_8_9_11_12_13_14_15_16_17_18_19_20_21_22_23_24_25_26_27_28_29_30_31_32_33_34', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_NOMBRE_CORTO', 'ME_PAIS_ID', 'ME_ESTADO_ID', 'ME_TM_ID', 'ME_LOGO', 'ME_LOGO_1', 'ME_VISIBLE', 'ME_EDIT_ID', 'ME_TIRAJE', 'ME_PER_ID', 'ME_CIUDAD_ID', 'ME_COSTO', 'ME_TCA_ID', 'ME_URL', 'ME_SUPLEMENTO', 'ME_FORMA_ADQUISICION', 'ME_TELEFONO', 'ME_DIRECCION', 'ME_DIRECTOR', 'ME_FACEBOOK', 'ME_TWITTER', 'ME_CLASIFICACION', 'ME_TIER', 'ME_TIPO_DE_COBERTURA', 'ME_LINK_DESCARGA', 'ME_CLIENTE', 'ME_DIAS_DE_TRANSMISION', 'ME_RAITING', 'ME_FORMACAPTURA', 'ME_TIPO_TRANSMISION', 'ME_FECHA_PUBLICACION_APROX'),
        Index('_dta_index_C_MEDIO_5_651149365__K2_K7_1_3_8', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_TM_ID', 'ME_LOGO'),
        Index('_dta_index_C_MEDIO_5_651149365__K1_K7_4149', 'ME_ID', 'ME_TM_ID'),
        Index('_dta_index_C_MEDIO_5_651149365__K5_K6_K1_2_3_4_7_8_9_10_11_12_13_14_15_16_17_18_19_20_21_22_23_24_25_26_27_28_29_30_31_32_33_34', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_NOMBRE_CORTO', 'ME_PAIS_ID', 'ME_ESTADO_ID', 'ME_TM_ID', 'ME_LOGO', 'ME_LOGO_1', 'ME_VISIBLE', 'ME_EDIT_ID', 'ME_TIRAJE', 'ME_PER_ID', 'ME_CIUDAD_ID', 'ME_COSTO', 'ME_TCA_ID', 'ME_URL', 'ME_SUPLEMENTO', 'ME_FORMA_ADQUISICION', 'ME_TELEFONO', 'ME_DIRECCION', 'ME_DIRECTOR', 'ME_FACEBOOK', 'ME_TWITTER', 'ME_CLASIFICACION', 'ME_TIER', 'ME_TIPO_DE_COBERTURA', 'ME_LINK_DESCARGA', 'ME_CLIENTE', 'ME_DIAS_DE_TRANSMISION', 'ME_RAITING', 'ME_FORMACAPTURA', 'ME_TIPO_TRANSMISION', 'ME_FECHA_PUBLICACION_APROX'),
        Index('_dta_index_C_MEDIO_5_651149365__K1_K7_K2', 'ME_ID', 'ME_LG_ID', 'ME_TM_ID'),
        Index('_dta_index_C_MEDIO_5_651149365__K7_K1_9987', 'ME_ID', 'ME_TM_ID'),
        Index('_dta_index_C_MEDIO_5_651149365__K1_K5_K6_2_3_4_7_8_9_10_11_12_13_14_15_16_17_18_19_20_21_22_23_24_25_26_27_28_29_30_31_32_33_34', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_NOMBRE_CORTO', 'ME_PAIS_ID', 'ME_ESTADO_ID', 'ME_TM_ID', 'ME_LOGO', 'ME_LOGO_1', 'ME_VISIBLE', 'ME_EDIT_ID', 'ME_TIRAJE', 'ME_PER_ID', 'ME_CIUDAD_ID', 'ME_COSTO', 'ME_TCA_ID', 'ME_URL', 'ME_SUPLEMENTO', 'ME_FORMA_ADQUISICION', 'ME_TELEFONO', 'ME_DIRECCION', 'ME_DIRECTOR', 'ME_FACEBOOK', 'ME_TWITTER', 'ME_CLASIFICACION', 'ME_TIER', 'ME_TIPO_DE_COBERTURA', 'ME_LINK_DESCARGA', 'ME_CLIENTE', 'ME_DIAS_DE_TRANSMISION', 'ME_RAITING', 'ME_FORMACAPTURA', 'ME_TIPO_TRANSMISION', 'ME_FECHA_PUBLICACION_APROX'),
        Index('_dta_index_C_MEDIO_5_651149365__K7_K2_K1', 'ME_ID', 'ME_LG_ID', 'ME_TM_ID'),
        Index('_dta_index_C_MEDIO_5_651149365__K1_3_4_8_9_10_11_12_13_14_15_16_17_18_19_20_21_22_23_24_25_26_27_28_29_30_31_32_33_34_4364', 'ME_ID', 'ME_NOMBRE', 'ME_NOMBRE_CORTO', 'ME_LOGO', 'ME_LOGO_1', 'ME_VISIBLE', 'ME_EDIT_ID', 'ME_TIRAJE', 'ME_PER_ID', 'ME_CIUDAD_ID', 'ME_COSTO', 'ME_TCA_ID', 'ME_URL', 'ME_SUPLEMENTO', 'ME_FORMA_ADQUISICION', 'ME_TELEFONO', 'ME_DIRECCION', 'ME_DIRECTOR', 'ME_FACEBOOK', 'ME_TWITTER', 'ME_CLASIFICACION', 'ME_TIER', 'ME_TIPO_DE_COBERTURA', 'ME_LINK_DESCARGA', 'ME_CLIENTE', 'ME_DIAS_DE_TRANSMISION', 'ME_RAITING', 'ME_FORMACAPTURA', 'ME_TIPO_TRANSMISION', 'ME_FECHA_PUBLICACION_APROX'),
        Index('_dta_index_C_MEDIO_5_651149365_100452352_K1_K5_K6_2_3_4_7_8_9_10_11_12_13_14_15_16_17_18_19_20_21_22_23_24_25_26_27_28_29_30_', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_NOMBRE_CORTO', 'ME_PAIS_ID', 'ME_ESTADO_ID', 'ME_TM_ID', 'ME_LOGO', 'ME_LOGO_1', 'ME_VISIBLE', 'ME_EDIT_ID', 'ME_TIRAJE', 'ME_PER_ID', 'ME_CIUDAD_ID', 'ME_COSTO', 'ME_TCA_ID', 'ME_URL', 'ME_SUPLEMENTO', 'ME_FORMA_ADQUISICION', 'ME_TELEFONO', 'ME_DIRECCION', 'ME_DIRECTOR', 'ME_FACEBOOK', 'ME_TWITTER', 'ME_CLASIFICACION', 'ME_TIER', 'ME_TIPO_DE_COBERTURA', 'ME_LINK_DESCARGA', 'ME_CLIENTE', 'ME_DIAS_DE_TRANSMISION', 'ME_RAITING', 'ME_FORMACAPTURA', 'ME_TIPO_TRANSMISION', 'ME_FECHA_PUBLICACION_APROX'),
        Index('_dta_index_C_MEDIO_5_651149365__K1_3_8', 'ME_ID', 'ME_NOMBRE', 'ME_LOGO'),
        Index('_dta_index_C_MEDIO_5_651149365__K1_K7_K5_K6_2_1912', 'ME_ID', 'ME_LG_ID', 'ME_PAIS_ID', 'ME_ESTADO_ID', 'ME_TM_ID'),
        Index('_dta_index_C_MEDIO_5_651149365_100452352_K5_K6_K1_2_3_4_7_8_9_10_11_12_13_14_15_16_17_18_19_20_21_22_23_24_25_26_27_28_29_30_', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_NOMBRE_CORTO', 'ME_PAIS_ID', 'ME_ESTADO_ID', 'ME_TM_ID', 'ME_LOGO', 'ME_LOGO_1', 'ME_VISIBLE', 'ME_EDIT_ID', 'ME_TIRAJE', 'ME_PER_ID', 'ME_CIUDAD_ID', 'ME_COSTO', 'ME_TCA_ID', 'ME_URL', 'ME_SUPLEMENTO', 'ME_FORMA_ADQUISICION', 'ME_TELEFONO', 'ME_DIRECCION', 'ME_DIRECTOR', 'ME_FACEBOOK', 'ME_TWITTER', 'ME_CLASIFICACION', 'ME_TIER', 'ME_TIPO_DE_COBERTURA', 'ME_LINK_DESCARGA', 'ME_CLIENTE', 'ME_DIAS_DE_TRANSMISION', 'ME_RAITING', 'ME_FORMACAPTURA', 'ME_TIPO_TRANSMISION', 'ME_FECHA_PUBLICACION_APROX'),
        Index('_dta_index_C_MEDIO_5_651149365__K7_K1_2_3_8', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_TM_ID', 'ME_LOGO'),
        Index('_dta_index_C_MEDIO_5_651149365__K7_K2_K1_3_8', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_TM_ID', 'ME_LOGO'),
        Index('_dta_index_C_MEDIO_5_651149365__K1_2_3_4_5_6_7_8_9_10_11_12_13_14_15_16_17_18', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_NOMBRE_CORTO', 'ME_PAIS_ID', 'ME_ESTADO_ID', 'ME_TM_ID', 'ME_LOGO', 'ME_LOGO_1', 'ME_VISIBLE', 'ME_EDIT_ID', 'ME_TIRAJE', 'ME_PER_ID', 'ME_CIUDAD_ID', 'ME_COSTO', 'ME_TCA_ID', 'ME_URL', 'ME_SUPLEMENTO'),
        Index('_dta_index_C_MEDIO_5_651149365__K7_K5_K6_K1_2_4149', 'ME_ID', 'ME_LG_ID', 'ME_PAIS_ID', 'ME_ESTADO_ID', 'ME_TM_ID'),
        Index('_dta_index_C_MEDIO_5_651149365_100452352_K8_1_3', 'ME_ID', 'ME_NOMBRE', 'ME_LOGO'),
        Index('_dta_index_C_MEDIO_5_651149365_104889936_K1_2_3_4_5_6_7_8_9_10_11_12_13_14_15_16_17_18', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_NOMBRE_CORTO', 'ME_PAIS_ID', 'ME_ESTADO_ID', 'ME_TM_ID', 'ME_LOGO', 'ME_LOGO_1', 'ME_VISIBLE', 'ME_EDIT_ID', 'ME_TIRAJE', 'ME_PER_ID', 'ME_CIUDAD_ID', 'ME_COSTO', 'ME_TCA_ID', 'ME_URL', 'ME_SUPLEMENTO'),
        Index('_dta_index_C_MEDIO_5_651149365_100452352_K1_3_8', 'ME_ID', 'ME_NOMBRE', 'ME_LOGO'),
        Index('_dta_index_C_MEDIO_5_651149365__K7_1_3_9987', 'ME_ID', 'ME_NOMBRE', 'ME_TM_ID'),
        Index('_dta_index_C_MEDIO_5_651149365_100452352_K1_2_3_4_5_6_7_8_9_10_11_12_13_14_15_16_17_18', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_NOMBRE_CORTO', 'ME_PAIS_ID', 'ME_ESTADO_ID', 'ME_TM_ID', 'ME_LOGO', 'ME_LOGO_1', 'ME_VISIBLE', 'ME_EDIT_ID', 'ME_TIRAJE', 'ME_PER_ID', 'ME_CIUDAD_ID', 'ME_COSTO', 'ME_TCA_ID', 'ME_URL', 'ME_SUPLEMENTO'),
        Index('_dta_index_C_MEDIO_5_651149365__K1_2_3_4_5_6_7_8_9_10_11_12_13_14_15_16_17_18_8258_1410', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_NOMBRE_CORTO', 'ME_PAIS_ID', 'ME_ESTADO_ID', 'ME_TM_ID', 'ME_LOGO', 'ME_LOGO_1', 'ME_VISIBLE', 'ME_EDIT_ID', 'ME_TIRAJE', 'ME_PER_ID', 'ME_CIUDAD_ID', 'ME_COSTO', 'ME_TCA_ID', 'ME_URL', 'ME_SUPLEMENTO'),
        Index('_dta_index_C_MEDIO_5_651149365_100452352_K7_K1_K2_3_8', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_TM_ID', 'ME_LOGO'),
        Index('_dta_index_C_MEDIO_5_651149365__K7_K1_K2_3_8_9987', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_TM_ID', 'ME_LOGO'),
        Index('_dta_index_C_MEDIO_5_651149365_100452352_K1_3_4_8_9_10_11_12_13_14_15_16_17_18_19_20_21_22_23_24_25_26_27_28_29_30_31_32_33_34', 'ME_ID', 'ME_NOMBRE', 'ME_NOMBRE_CORTO', 'ME_LOGO', 'ME_LOGO_1', 'ME_VISIBLE', 'ME_EDIT_ID', 'ME_TIRAJE', 'ME_PER_ID', 'ME_CIUDAD_ID', 'ME_COSTO', 'ME_TCA_ID', 'ME_URL', 'ME_SUPLEMENTO', 'ME_FORMA_ADQUISICION', 'ME_TELEFONO', 'ME_DIRECCION', 'ME_DIRECTOR', 'ME_FACEBOOK', 'ME_TWITTER', 'ME_CLASIFICACION', 'ME_TIER', 'ME_TIPO_DE_COBERTURA', 'ME_LINK_DESCARGA', 'ME_CLIENTE', 'ME_DIAS_DE_TRANSMISION', 'ME_RAITING', 'ME_FORMACAPTURA', 'ME_TIPO_TRANSMISION', 'ME_FECHA_PUBLICACION_APROX'),
        Index('_dta_index_C_MEDIO_5_651149365__K1_K7_K2_3_8_1771', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_TM_ID', 'ME_LOGO'),
        Index('_dta_index_C_MEDIO_5_651149365__K18_K1_K7_8066', 'ME_ID', 'ME_TM_ID', 'ME_SUPLEMENTO'),
        Index('_dta_index_C_MEDIO_5_651149365_100452352_K7_K5_K6_K1_2_3_4_8_9_10_11_12_13_14_15_16_17_18_19_20_21_22_23_24_25_26_27_28_29_30_', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_NOMBRE_CORTO', 'ME_PAIS_ID', 'ME_ESTADO_ID', 'ME_TM_ID', 'ME_LOGO', 'ME_LOGO_1', 'ME_VISIBLE', 'ME_EDIT_ID', 'ME_TIRAJE', 'ME_PER_ID', 'ME_CIUDAD_ID', 'ME_COSTO', 'ME_TCA_ID', 'ME_URL', 'ME_SUPLEMENTO', 'ME_FORMA_ADQUISICION', 'ME_TELEFONO', 'ME_DIRECCION', 'ME_DIRECTOR', 'ME_FACEBOOK', 'ME_TWITTER', 'ME_CLASIFICACION', 'ME_TIER', 'ME_TIPO_DE_COBERTURA', 'ME_LINK_DESCARGA', 'ME_CLIENTE', 'ME_DIAS_DE_TRANSMISION', 'ME_RAITING', 'ME_FORMACAPTURA', 'ME_TIPO_TRANSMISION', 'ME_FECHA_PUBLICACION_APROX'),
        Index('_dta_index_C_MEDIO_5_651149365_100452352_K2_K7_1_3_8', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_TM_ID', 'ME_LOGO'),
        Index('_dta_index_C_MEDIO_5_651149365__K2_K7_1_4364', 'ME_ID', 'ME_LG_ID', 'ME_TM_ID'),
        Index('_dta_index_C_MEDIO_5_651149365_100452352_K7_K1_K5_K6_2_3_4_8_9_10_11_12_13_14_15_16_17_18_19_20_21_22_23_24_25_26_27_28_29_30_', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_NOMBRE_CORTO', 'ME_PAIS_ID', 'ME_ESTADO_ID', 'ME_TM_ID', 'ME_LOGO', 'ME_LOGO_1', 'ME_VISIBLE', 'ME_EDIT_ID', 'ME_TIRAJE', 'ME_PER_ID', 'ME_CIUDAD_ID', 'ME_COSTO', 'ME_TCA_ID', 'ME_URL', 'ME_SUPLEMENTO', 'ME_FORMA_ADQUISICION', 'ME_TELEFONO', 'ME_DIRECCION', 'ME_DIRECTOR', 'ME_FACEBOOK', 'ME_TWITTER', 'ME_CLASIFICACION', 'ME_TIER', 'ME_TIPO_DE_COBERTURA', 'ME_LINK_DESCARGA', 'ME_CLIENTE', 'ME_DIAS_DE_TRANSMISION', 'ME_RAITING', 'ME_FORMACAPTURA', 'ME_TIPO_TRANSMISION', 'ME_FECHA_PUBLICACION_APROX'),
        Index('_dta_index_C_MEDIO_5_651149365__K8_1_2_3_7_5201', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_TM_ID', 'ME_LOGO'),
        Index('_dta_index_C_MEDIO_5_651149365_100452352_K7_K2_K1_3_8', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_TM_ID', 'ME_LOGO'),
        Index('_dta_index_C_MEDIO_5_651149365_100452352_K1_K7_K5_K6_2_3_4_8_9_10_11_12_13_14_15_16_17_18_19_20_21_22_23_24_25_26_27_28_29_30_', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_NOMBRE_CORTO', 'ME_PAIS_ID', 'ME_ESTADO_ID', 'ME_TM_ID', 'ME_LOGO', 'ME_LOGO_1', 'ME_VISIBLE', 'ME_EDIT_ID', 'ME_TIRAJE', 'ME_PER_ID', 'ME_CIUDAD_ID', 'ME_COSTO', 'ME_TCA_ID', 'ME_URL', 'ME_SUPLEMENTO', 'ME_FORMA_ADQUISICION', 'ME_TELEFONO', 'ME_DIRECCION', 'ME_DIRECTOR', 'ME_FACEBOOK', 'ME_TWITTER', 'ME_CLASIFICACION', 'ME_TIER', 'ME_TIPO_DE_COBERTURA', 'ME_LINK_DESCARGA', 'ME_CLIENTE', 'ME_DIAS_DE_TRANSMISION', 'ME_RAITING', 'ME_FORMACAPTURA', 'ME_TIPO_TRANSMISION', 'ME_FECHA_PUBLICACION_APROX'),
        Index('_dta_index_C_MEDIO_5_651149365__K8_1_3_6497', 'ME_ID', 'ME_NOMBRE', 'ME_LOGO'),
        Index('_dta_index_C_MEDIO_5_651149365__K7_K13_K5_K6_9987', 'ME_PAIS_ID', 'ME_ESTADO_ID', 'ME_TM_ID', 'ME_PER_ID'),
        Index('_dta_index_C_MEDIO_5_651149365_100452352_K1_K7_K2_3_8', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_TM_ID', 'ME_LOGO'),
        Index('_dta_index_C_MEDIO_5_651149365__K7_K5_1_2_3_4_6_8_9_10_11_12_13_14_15_16_17_18_19_20_21_22_23_24_25_26_27_28_29_30_31_32_33_34', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_NOMBRE_CORTO', 'ME_PAIS_ID', 'ME_ESTADO_ID', 'ME_TM_ID', 'ME_LOGO', 'ME_LOGO_1', 'ME_VISIBLE', 'ME_EDIT_ID', 'ME_TIRAJE', 'ME_PER_ID', 'ME_CIUDAD_ID', 'ME_COSTO', 'ME_TCA_ID', 'ME_URL', 'ME_SUPLEMENTO', 'ME_FORMA_ADQUISICION', 'ME_TELEFONO', 'ME_DIRECCION', 'ME_DIRECTOR', 'ME_FACEBOOK', 'ME_TWITTER', 'ME_CLASIFICACION', 'ME_TIER', 'ME_TIPO_DE_COBERTURA', 'ME_LINK_DESCARGA', 'ME_CLIENTE', 'ME_DIAS_DE_TRANSMISION', 'ME_RAITING', 'ME_FORMACAPTURA', 'ME_TIPO_TRANSMISION', 'ME_FECHA_PUBLICACION_APROX'),
        Index('_dta_index_C_MEDIO_5_651149365__K1_K7_K2_3_8_1040', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_TM_ID', 'ME_LOGO'),
        Index('_dta_index_C_MEDIO_5_651149365__K7_K13_K5_K6', 'ME_PAIS_ID', 'ME_ESTADO_ID', 'ME_TM_ID', 'ME_PER_ID'),
        Index('_dta_index_C_MEDIO_5_651149365_100452352_K8_1_2_3_7', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_TM_ID', 'ME_LOGO'),
        Index('_dta_index_C_MEDIO_5_651149365__K2_K7_1_3_8_1771', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_TM_ID', 'ME_LOGO'),
        Index('_dta_index_C_MEDIO_5_651149365__K1_3_7', 'ME_ID', 'ME_NOMBRE', 'ME_TM_ID'),
        Index('NonClusteredIndex-20170124-223554', 'ME_ID', 'ME_LG_ID', 'ME_PAIS_ID', 'ME_ESTADO_ID', 'ME_TM_ID'),
        Index('_dta_index_C_MEDIO_5_651149365__K7_1_2_3_4_5_6_8_9_10_11_12_13_14_15_16_17_18_19_20_21_22_23_24_25_26_27_28_29_30_31_32_33_34', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_NOMBRE_CORTO', 'ME_PAIS_ID', 'ME_ESTADO_ID', 'ME_TM_ID', 'ME_LOGO', 'ME_LOGO_1', 'ME_VISIBLE', 'ME_EDIT_ID', 'ME_TIRAJE', 'ME_PER_ID', 'ME_CIUDAD_ID', 'ME_COSTO', 'ME_TCA_ID', 'ME_URL', 'ME_SUPLEMENTO', 'ME_FORMA_ADQUISICION', 'ME_TELEFONO', 'ME_DIRECCION', 'ME_DIRECTOR', 'ME_FACEBOOK', 'ME_TWITTER', 'ME_CLASIFICACION', 'ME_TIER', 'ME_TIPO_DE_COBERTURA', 'ME_LINK_DESCARGA', 'ME_CLIENTE', 'ME_DIAS_DE_TRANSMISION', 'ME_RAITING', 'ME_FORMACAPTURA', 'ME_TIPO_TRANSMISION', 'ME_FECHA_PUBLICACION_APROX'),
        Index('_dta_index_C_MEDIO_5_651149365__K1_K6', 'ME_ID', 'ME_ESTADO_ID'),
        Index('_dta_index_C_MEDIO_5_651149365__K1_K7_K2_8258', 'ME_ID', 'ME_LG_ID', 'ME_TM_ID'),
        Index('_dta_index_C_MEDIO_5_651149365__K6_K1', 'ME_ID', 'ME_ESTADO_ID'),
        Index('_dta_index_C_MEDIO_5_651149365__K7_K2_K1_1410', 'ME_ID', 'ME_LG_ID', 'ME_TM_ID'),
        Index('_dta_index_C_MEDIO_5_651149365__K7_K1_2_3_4_5_6_8_9_10_11_12_13_14_15_16_17_18_19_20_21_22_23_24_25_26_27_28_29_30_31_32_33_34', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_NOMBRE_CORTO', 'ME_PAIS_ID', 'ME_ESTADO_ID', 'ME_TM_ID', 'ME_LOGO', 'ME_LOGO_1', 'ME_VISIBLE', 'ME_EDIT_ID', 'ME_TIRAJE', 'ME_PER_ID', 'ME_CIUDAD_ID', 'ME_COSTO', 'ME_TCA_ID', 'ME_URL', 'ME_SUPLEMENTO', 'ME_FORMA_ADQUISICION', 'ME_TELEFONO', 'ME_DIRECCION', 'ME_DIRECTOR', 'ME_FACEBOOK', 'ME_TWITTER', 'ME_CLASIFICACION', 'ME_TIER', 'ME_TIPO_DE_COBERTURA', 'ME_LINK_DESCARGA', 'ME_CLIENTE', 'ME_DIAS_DE_TRANSMISION', 'ME_RAITING', 'ME_FORMACAPTURA', 'ME_TIPO_TRANSMISION', 'ME_FECHA_PUBLICACION_APROX'),
        Index('_dta_index_C_MEDIO_5_651149365__K7_K1_2_3_8_12', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_TM_ID', 'ME_LOGO', 'ME_TIRAJE'),
        Index('_dta_index_C_MEDIO_5_651149365__K1_3_8_4864', 'ME_ID', 'ME_NOMBRE', 'ME_LOGO'),
        Index('_dta_index_C_MEDIO_5_651149365__K7_K1_K2_3_8_9987_4364', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_TM_ID', 'ME_LOGO'),
        Index('_dta_index_C_MEDIO_5_651149365_49239816_K1_2_3_4_5_6_7_8_9_10_11_12_13_14_15_16_17_18', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_NOMBRE_CORTO', 'ME_PAIS_ID', 'ME_ESTADO_ID', 'ME_TM_ID', 'ME_LOGO', 'ME_LOGO_1', 'ME_VISIBLE', 'ME_EDIT_ID', 'ME_TIRAJE', 'ME_PER_ID', 'ME_CIUDAD_ID', 'ME_COSTO', 'ME_TCA_ID', 'ME_URL', 'ME_SUPLEMENTO'),
        Index('_dta_index_C_MEDIO_5_651149365__K1_K7_2_3_4_5_6_8_9_10_11_12_13_14_15_16_17_18_19_20_21_22_23_24_25_26_27_28_29_30_31_32_33_34', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_NOMBRE_CORTO', 'ME_PAIS_ID', 'ME_ESTADO_ID', 'ME_TM_ID', 'ME_LOGO', 'ME_LOGO_1', 'ME_VISIBLE', 'ME_EDIT_ID', 'ME_TIRAJE', 'ME_PER_ID', 'ME_CIUDAD_ID', 'ME_COSTO', 'ME_TCA_ID', 'ME_URL', 'ME_SUPLEMENTO', 'ME_FORMA_ADQUISICION', 'ME_TELEFONO', 'ME_DIRECCION', 'ME_DIRECTOR', 'ME_FACEBOOK', 'ME_TWITTER', 'ME_CLASIFICACION', 'ME_TIER', 'ME_TIPO_DE_COBERTURA', 'ME_LINK_DESCARGA', 'ME_CLIENTE', 'ME_DIAS_DE_TRANSMISION', 'ME_RAITING', 'ME_FORMACAPTURA', 'ME_TIPO_TRANSMISION', 'ME_FECHA_PUBLICACION_APROX'),
        Index('_dta_index_C_MEDIO_5_651149365__K7_K2_K1_3_8_6960', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_TM_ID', 'ME_LOGO'),
        Index('_dta_index_C_MEDIO_5_651149365_100452352_K7_K1_2_3_4_5_6_8_9_10_11_12_13_14_15_16_17_18_19_20_21_22_23_24_25_26_27_28_29_30_31_', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_NOMBRE_CORTO', 'ME_PAIS_ID', 'ME_ESTADO_ID', 'ME_TM_ID', 'ME_LOGO', 'ME_LOGO_1', 'ME_VISIBLE', 'ME_EDIT_ID', 'ME_TIRAJE', 'ME_PER_ID', 'ME_CIUDAD_ID', 'ME_COSTO', 'ME_TCA_ID', 'ME_URL', 'ME_SUPLEMENTO', 'ME_FORMA_ADQUISICION', 'ME_TELEFONO', 'ME_DIRECCION', 'ME_DIRECTOR', 'ME_FACEBOOK', 'ME_TWITTER', 'ME_CLASIFICACION', 'ME_TIER', 'ME_TIPO_DE_COBERTURA', 'ME_LINK_DESCARGA', 'ME_CLIENTE', 'ME_DIAS_DE_TRANSMISION', 'ME_RAITING', 'ME_FORMACAPTURA', 'ME_TIPO_TRANSMISION', 'ME_FECHA_PUBLICACION_APROX'),
        Index('_dta_index_C_MEDIO_5_651149365__K1_K7_3_8_12_9910', 'ME_ID', 'ME_NOMBRE', 'ME_TM_ID', 'ME_LOGO', 'ME_TIRAJE'),
        Index('_dta_index_C_MEDIO_5_651149365_51857368_K8_1_3', 'ME_ID', 'ME_NOMBRE', 'ME_LOGO'),
        Index('_dta_index_C_MEDIO_5_651149365_100452352_K1_K7_2_3_4_5_6_8_9_10_11_12_13_14_15_16_17_18_19_20_21_22_23_24_25_26_27_28_29_30_31_', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_NOMBRE_CORTO', 'ME_PAIS_ID', 'ME_ESTADO_ID', 'ME_TM_ID', 'ME_LOGO', 'ME_LOGO_1', 'ME_VISIBLE', 'ME_EDIT_ID', 'ME_TIRAJE', 'ME_PER_ID', 'ME_CIUDAD_ID', 'ME_COSTO', 'ME_TCA_ID', 'ME_URL', 'ME_SUPLEMENTO', 'ME_FORMA_ADQUISICION', 'ME_TELEFONO', 'ME_DIRECCION', 'ME_DIRECTOR', 'ME_FACEBOOK', 'ME_TWITTER', 'ME_CLASIFICACION', 'ME_TIER', 'ME_TIPO_DE_COBERTURA', 'ME_LINK_DESCARGA', 'ME_CLIENTE', 'ME_DIAS_DE_TRANSMISION', 'ME_RAITING', 'ME_FORMACAPTURA', 'ME_TIPO_TRANSMISION', 'ME_FECHA_PUBLICACION_APROX'),
        Index('_dta_index_C_MEDIO_5_651149365__K1_2_3_4_5_6_7_8_9_10_11_12_13_14_15_16_17_18_8258', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_NOMBRE_CORTO', 'ME_PAIS_ID', 'ME_ESTADO_ID', 'ME_TM_ID', 'ME_LOGO', 'ME_LOGO_1', 'ME_VISIBLE', 'ME_EDIT_ID', 'ME_TIRAJE', 'ME_PER_ID', 'ME_CIUDAD_ID', 'ME_COSTO', 'ME_TCA_ID', 'ME_URL', 'ME_SUPLEMENTO'),
        Index('_dta_index_C_MEDIO_5_651149365__K1_3_7_8_12_3923', 'ME_ID', 'ME_NOMBRE', 'ME_TM_ID', 'ME_LOGO', 'ME_TIRAJE'),
        Index('_dta_index_C_MEDIO_5_651149365_51857368_K1_3_8', 'ME_ID', 'ME_NOMBRE', 'ME_LOGO'),
        Index('_dta_index_C_MEDIO_5_651149365__K1_K7_5201', 'ME_ID', 'ME_TM_ID'),
        Index('_dta_index_C_MEDIO_5_651149365__K7_1_3_9987_4364', 'ME_ID', 'ME_NOMBRE', 'ME_TM_ID'),
        Index('_dta_index_C_MEDIO_5_651149365_51857368_K7_K1_K2_3_8', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_TM_ID', 'ME_LOGO'),
        Index('_dta_index_C_MEDIO_5_651149365__K7_K5_K1_2_3_4_6_8_9_10_11_12_13_14_15_16_17_18_19_20_21_22_23_24_25_26_27_28_29_30_31_32_33_34', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_NOMBRE_CORTO', 'ME_PAIS_ID', 'ME_ESTADO_ID', 'ME_TM_ID', 'ME_LOGO', 'ME_LOGO_1', 'ME_VISIBLE', 'ME_EDIT_ID', 'ME_TIRAJE', 'ME_PER_ID', 'ME_CIUDAD_ID', 'ME_COSTO', 'ME_TCA_ID', 'ME_URL', 'ME_SUPLEMENTO', 'ME_FORMA_ADQUISICION', 'ME_TELEFONO', 'ME_DIRECCION', 'ME_DIRECTOR', 'ME_FACEBOOK', 'ME_TWITTER', 'ME_CLASIFICACION', 'ME_TIER', 'ME_TIPO_DE_COBERTURA', 'ME_LINK_DESCARGA', 'ME_CLIENTE', 'ME_DIAS_DE_TRANSMISION', 'ME_RAITING', 'ME_FORMACAPTURA', 'ME_TIPO_TRANSMISION', 'ME_FECHA_PUBLICACION_APROX'),
        Index('_dta_index_C_MEDIO_5_651149365__K1_K7_K5_2_3_4_6_8_9_10_11_12_13_14_15_16_17_18_19_20_21_22_23_24_25_26_27_28_29_30_31_32_33_34', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_NOMBRE_CORTO', 'ME_PAIS_ID', 'ME_ESTADO_ID', 'ME_TM_ID', 'ME_LOGO', 'ME_LOGO_1', 'ME_VISIBLE', 'ME_EDIT_ID', 'ME_TIRAJE', 'ME_PER_ID', 'ME_CIUDAD_ID', 'ME_COSTO', 'ME_TCA_ID', 'ME_URL', 'ME_SUPLEMENTO', 'ME_FORMA_ADQUISICION', 'ME_TELEFONO', 'ME_DIRECCION', 'ME_DIRECTOR', 'ME_FACEBOOK', 'ME_TWITTER', 'ME_CLASIFICACION', 'ME_TIER', 'ME_TIPO_DE_COBERTURA', 'ME_LINK_DESCARGA', 'ME_CLIENTE', 'ME_DIAS_DE_TRANSMISION', 'ME_RAITING', 'ME_FORMACAPTURA', 'ME_TIPO_TRANSMISION', 'ME_FECHA_PUBLICACION_APROX'),
        Index('_dta_index_C_MEDIO_5_651149365__K7_K1_3_8_12_32', 'ME_ID', 'ME_NOMBRE', 'ME_TM_ID', 'ME_LOGO', 'ME_TIRAJE'),
        Index('_dta_index_C_MEDIO_5_651149365_51857368_K2_K7_1_3_8', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_TM_ID', 'ME_LOGO'),
        Index('_dta_index_C_MEDIO_5_651149365__K7_K1_9987_4364', 'ME_ID', 'ME_TM_ID'),
        Index('_dta_index_C_MEDIO_5_651149365__K7_K1_K5_2_3_4_6_8_9_10_11_12_13_14_15_16_17_18_19_20_21_22_23_24_25_26_27_28_29_30_31_32_33_34', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_NOMBRE_CORTO', 'ME_PAIS_ID', 'ME_ESTADO_ID', 'ME_TM_ID', 'ME_LOGO', 'ME_LOGO_1', 'ME_VISIBLE', 'ME_EDIT_ID', 'ME_TIRAJE', 'ME_PER_ID', 'ME_CIUDAD_ID', 'ME_COSTO', 'ME_TCA_ID', 'ME_URL', 'ME_SUPLEMENTO', 'ME_FORMA_ADQUISICION', 'ME_TELEFONO', 'ME_DIRECCION', 'ME_DIRECTOR', 'ME_FACEBOOK', 'ME_TWITTER', 'ME_CLASIFICACION', 'ME_TIER', 'ME_TIPO_DE_COBERTURA', 'ME_LINK_DESCARGA', 'ME_CLIENTE', 'ME_DIAS_DE_TRANSMISION', 'ME_RAITING', 'ME_FORMACAPTURA', 'ME_TIPO_TRANSMISION', 'ME_FECHA_PUBLICACION_APROX'),
        Index('_dta_index_C_MEDIO_5_651149365_93568848_K1_3_7_8_12', 'ME_ID', 'ME_NOMBRE', 'ME_TM_ID', 'ME_LOGO', 'ME_TIRAJE'),
        Index('_dta_index_C_MEDIO_5_651149365_51857368_K7_K2_K1_3_8', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_TM_ID', 'ME_LOGO'),
        Index('_dta_index_C_MEDIO_5_651149365_100452352_K7_K1_K5_2_3_4_6_8_9_10_11_12_13_14_15_16_17_18_19_20_21_22_23_24_25_26_27_28_29_30_', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_NOMBRE_CORTO', 'ME_PAIS_ID', 'ME_ESTADO_ID', 'ME_TM_ID', 'ME_LOGO', 'ME_LOGO_1', 'ME_VISIBLE', 'ME_EDIT_ID', 'ME_TIRAJE', 'ME_PER_ID', 'ME_CIUDAD_ID', 'ME_COSTO', 'ME_TCA_ID', 'ME_URL', 'ME_SUPLEMENTO', 'ME_FORMA_ADQUISICION', 'ME_TELEFONO', 'ME_DIRECCION', 'ME_DIRECTOR', 'ME_FACEBOOK', 'ME_TWITTER', 'ME_CLASIFICACION', 'ME_TIER', 'ME_TIPO_DE_COBERTURA', 'ME_LINK_DESCARGA', 'ME_CLIENTE', 'ME_DIAS_DE_TRANSMISION', 'ME_RAITING', 'ME_FORMACAPTURA', 'ME_TIPO_TRANSMISION', 'ME_FECHA_PUBLICACION_APROX'),
        Index('_dta_index_C_MEDIO_5_651149365_93568736_K7_K1_3_8_12', 'ME_ID', 'ME_NOMBRE', 'ME_TM_ID', 'ME_LOGO', 'ME_TIRAJE'),
        Index('_dta_index_C_MEDIO_5_651149365__K18_K1_K7', 'ME_ID', 'ME_TM_ID', 'ME_SUPLEMENTO'),
        Index('_dta_index_C_MEDIO_5_651149365_51857368_K1_2_3_4_5_6_7_8_9_10_11_12_13_14_15_16_17_18', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_NOMBRE_CORTO', 'ME_PAIS_ID', 'ME_ESTADO_ID', 'ME_TM_ID', 'ME_LOGO', 'ME_LOGO_1', 'ME_VISIBLE', 'ME_EDIT_ID', 'ME_TIRAJE', 'ME_PER_ID', 'ME_CIUDAD_ID', 'ME_COSTO', 'ME_TCA_ID', 'ME_URL', 'ME_SUPLEMENTO'),
        Index('_dta_index_C_MEDIO_5_651149365_100452352_K1_K7_K5_2_3_4_6_8_9_10_11_12_13_14_15_16_17_18_19_20_21_22_23_24_25_26_27_28_29_30_', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_NOMBRE_CORTO', 'ME_PAIS_ID', 'ME_ESTADO_ID', 'ME_TM_ID', 'ME_LOGO', 'ME_LOGO_1', 'ME_VISIBLE', 'ME_EDIT_ID', 'ME_TIRAJE', 'ME_PER_ID', 'ME_CIUDAD_ID', 'ME_COSTO', 'ME_TCA_ID', 'ME_URL', 'ME_SUPLEMENTO', 'ME_FORMA_ADQUISICION', 'ME_TELEFONO', 'ME_DIRECCION', 'ME_DIRECTOR', 'ME_FACEBOOK', 'ME_TWITTER', 'ME_CLASIFICACION', 'ME_TIER', 'ME_TIPO_DE_COBERTURA', 'ME_LINK_DESCARGA', 'ME_CLIENTE', 'ME_DIAS_DE_TRANSMISION', 'ME_RAITING', 'ME_FORMACAPTURA', 'ME_TIPO_TRANSMISION', 'ME_FECHA_PUBLICACION_APROX'),
        Index('_dta_index_C_MEDIO_5_651149365_51857368_K1_K7_K2_3_8', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_TM_ID', 'ME_LOGO'),
        Index('_dta_stat_651149365_18_1_7', 'ME_ID', 'ME_TM_ID', 'ME_SUPLEMENTO'),
        Index('_dta_index_C_MEDIO_5_651149365_51857368_K1_3_4_8_9_10_11_12_13_14_15_16_17_18_19_20_21_22_23_24_25_26_27_28_29_30_31_32_33_34', 'ME_ID', 'ME_NOMBRE', 'ME_NOMBRE_CORTO', 'ME_LOGO', 'ME_LOGO_1', 'ME_VISIBLE', 'ME_EDIT_ID', 'ME_TIRAJE', 'ME_PER_ID', 'ME_CIUDAD_ID', 'ME_COSTO', 'ME_TCA_ID', 'ME_URL', 'ME_SUPLEMENTO', 'ME_FORMA_ADQUISICION', 'ME_TELEFONO', 'ME_DIRECCION', 'ME_DIRECTOR', 'ME_FACEBOOK', 'ME_TWITTER', 'ME_CLASIFICACION', 'ME_TIER', 'ME_TIPO_DE_COBERTURA', 'ME_LINK_DESCARGA', 'ME_CLIENTE', 'ME_DIAS_DE_TRANSMISION', 'ME_RAITING', 'ME_FORMACAPTURA', 'ME_TIPO_TRANSMISION', 'ME_FECHA_PUBLICACION_APROX'),
        Index('_dta_index_C_MEDIO_5_651149365__K1_K7_K5_K6_2_4149', 'ME_ID', 'ME_LG_ID', 'ME_PAIS_ID', 'ME_ESTADO_ID', 'ME_TM_ID'),
        Index('_dta_index_C_MEDIO_5_651149365_100452352_K7_K5_K1_2_3_4_6_8_9_10_11_12_13_14_15_16_17_18_19_20_21_22_23_24_25_26_27_28_29_30_', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_NOMBRE_CORTO', 'ME_PAIS_ID', 'ME_ESTADO_ID', 'ME_TM_ID', 'ME_LOGO', 'ME_LOGO_1', 'ME_VISIBLE', 'ME_EDIT_ID', 'ME_TIRAJE', 'ME_PER_ID', 'ME_CIUDAD_ID', 'ME_COSTO', 'ME_TCA_ID', 'ME_URL', 'ME_SUPLEMENTO', 'ME_FORMA_ADQUISICION', 'ME_TELEFONO', 'ME_DIRECCION', 'ME_DIRECTOR', 'ME_FACEBOOK', 'ME_TWITTER', 'ME_CLASIFICACION', 'ME_TIER', 'ME_TIPO_DE_COBERTURA', 'ME_LINK_DESCARGA', 'ME_CLIENTE', 'ME_DIAS_DE_TRANSMISION', 'ME_RAITING', 'ME_FORMACAPTURA', 'ME_TIPO_TRANSMISION', 'ME_FECHA_PUBLICACION_APROX'),
        Index('_dta_index_C_MEDIO_5_651149365_51857368_K8_1_2_3_7', 'ME_ID', 'ME_LG_ID', 'ME_NOMBRE', 'ME_TM_ID', 'ME_LOGO')
    )

    ME_ID = Column(BigInteger, primary_key=True, index=True)
    ME_LG_ID = Column(BigInteger, nullable=False)
    ME_NOMBRE = Column(String(1000, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    ME_NOMBRE_CORTO = Column(String(1000, 'SQL_Latin1_General_CP1_CI_AS'))
    ME_PAIS_ID = Column(ForeignKey('C_PAIS.PAIS_ID'), nullable=False, index=True)
    ME_ESTADO_ID = Column(ForeignKey('C_ESTADO.ESTADO_ID'), index=True)
    ME_TM_ID = Column(ForeignKey('C_TIPO_MEDIO.TM_ID'), nullable=False, index=True)
    ME_LOGO = Column(String(200, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    ME_LOGO_1 = Column(String(200, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    ME_VISIBLE = Column(BIT, nullable=False)
    ME_EDIT_ID = Column(Integer, nullable=False)
    ME_TIRAJE = Column(Integer, nullable=False)
    ME_PER_ID = Column(ForeignKey('C_PERIODICIDAD.PER_ID'), nullable=False)
    ME_CIUDAD_ID = Column(Integer, nullable=False)
    ME_COSTO = Column(DECIMAL(18, 2))
    ME_TCA_ID = Column(ForeignKey('C_TIPO_CAPTURA.TCA_ID'))
    ME_URL = Column(String(1000, 'SQL_Latin1_General_CP1_CI_AS'))
    ME_SUPLEMENTO = Column(BIT, index=True)
    ME_FORMA_ADQUISICION = Column(String(1000, 'SQL_Latin1_General_CP1_CI_AS'))
    ME_TELEFONO = Column(String(1000, 'SQL_Latin1_General_CP1_CI_AS'))
    ME_DIRECCION = Column(String(1000, 'SQL_Latin1_General_CP1_CI_AS'))
    ME_DIRECTOR = Column(String(1000, 'SQL_Latin1_General_CP1_CI_AS'))
    ME_FACEBOOK = Column(String(1000, 'SQL_Latin1_General_CP1_CI_AS'))
    ME_TWITTER = Column(String(1000, 'SQL_Latin1_General_CP1_CI_AS'))
    ME_CLASIFICACION = Column(String(1000, 'SQL_Latin1_General_CP1_CI_AS'))
    ME_TIER = Column(String(1000, 'SQL_Latin1_General_CP1_CI_AS'))
    ME_TIPO_DE_COBERTURA = Column(String(1000, 'SQL_Latin1_General_CP1_CI_AS'))
    ME_LINK_DESCARGA = Column(String(1000, 'SQL_Latin1_General_CP1_CI_AS'))
    ME_CLIENTE = Column(String(1000, 'SQL_Latin1_General_CP1_CI_AS'))
    ME_DIAS_DE_TRANSMISION = Column(String(1000, 'SQL_Latin1_General_CP1_CI_AS'))
    ME_RAITING = Column(String(1000, 'SQL_Latin1_General_CP1_CI_AS'))
    ME_FORMACAPTURA = Column(String(1000, 'SQL_Latin1_General_CP1_CI_AS'))
    ME_TIPO_TRANSMISION = Column(String(1000, 'SQL_Latin1_General_CP1_CI_AS'))
    ME_FECHA_PUBLICACION_APROX = Column(String(1000, 'SQL_Latin1_General_CP1_CI_AS'))

    C_ESTADO = relationship('CESTADO')
    C_PAI = relationship('CPAI')
    C_PERIODICIDAD = relationship('CPERIODICIDAD')
    C_TIPO_CAPTURA = relationship('CTIPOCAPTURA')
    C_TIPO_MEDIO = relationship('CTIPOMEDIO')


class KMENUSUSCRIPTOR(Base):
    __tablename__ = 'K_MENU_SUSCRIPTOR'
    __table_args__ = (
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K2_K12_11_5201', 'MS_SUS_ID', 'MS_DISPLAY_LG_ID', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K12_K7_1_3_4_6_11_6497', 'MS_ID', 'MS_SUS_LG_ID', 'MS_MENU_LG_ID', 'MS_PADRE_ID', 'MS_NOMBRE', 'MS_DISPLAY_LG_ID', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K12_K1_K4_K6_K3_7', 'MS_ID', 'MS_SUS_LG_ID', 'MS_MENU_LG_ID', 'MS_PADRE_ID', 'MS_NOMBRE', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K3_K4_K6_K1_K12_7', 'MS_ID', 'MS_SUS_LG_ID', 'MS_MENU_LG_ID', 'MS_PADRE_ID', 'MS_NOMBRE', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K3_K6_K1_4', 'MS_ID', 'MS_SUS_LG_ID', 'MS_MENU_LG_ID', 'MS_PADRE_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K12_K1', 'MS_ID', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K1_K4_K6_K3_K12_7', 'MS_ID', 'MS_SUS_LG_ID', 'MS_MENU_LG_ID', 'MS_PADRE_ID', 'MS_NOMBRE', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K1_K12_7', 'MS_ID', 'MS_NOMBRE', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K3_1_4_6', 'MS_ID', 'MS_SUS_LG_ID', 'MS_MENU_LG_ID', 'MS_PADRE_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K11_1_7_12_9987_4364', 'MS_ID', 'MS_NOMBRE', 'MS_DISPLAY_LG_ID', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K3_K6_K1_K4_K12_7', 'MS_ID', 'MS_SUS_LG_ID', 'MS_MENU_LG_ID', 'MS_PADRE_ID', 'MS_NOMBRE', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K4_7', 'MS_MENU_LG_ID', 'MS_NOMBRE'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K2_1_3_4_5_6_7_8_9_10_11_12', 'MS_ID', 'MS_SUS_ID', 'MS_SUS_LG_ID', 'MS_MENU_LG_ID', 'MS_TIPO_VISTA_LG_ID', 'MS_PADRE_ID', 'MS_NOMBRE', 'MS_FECHA', 'MS_LOGO', 'MS_DESCRIPCION', 'MS_DISPLAY_LG_ID', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K4_K6_K1_K3_K12_7', 'MS_ID', 'MS_SUS_LG_ID', 'MS_MENU_LG_ID', 'MS_PADRE_ID', 'MS_NOMBRE', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K12_11', 'MS_DISPLAY_LG_ID', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K3_K6_K1_K4', 'MS_ID', 'MS_SUS_LG_ID', 'MS_MENU_LG_ID', 'MS_PADRE_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K6_K4_K3_K1_K12_7', 'MS_ID', 'MS_SUS_LG_ID', 'MS_MENU_LG_ID', 'MS_PADRE_ID', 'MS_NOMBRE', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K12_1_7', 'MS_ID', 'MS_NOMBRE', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K12_7', 'MS_NOMBRE', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K3_K12_K4_K6_K1_7', 'MS_ID', 'MS_SUS_LG_ID', 'MS_MENU_LG_ID', 'MS_PADRE_ID', 'MS_NOMBRE', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K4_K6_K1_K3', 'MS_ID', 'MS_SUS_LG_ID', 'MS_MENU_LG_ID', 'MS_PADRE_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K3_K12_1_4_6_7', 'MS_ID', 'MS_SUS_LG_ID', 'MS_MENU_LG_ID', 'MS_PADRE_ID', 'MS_NOMBRE', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K6_K3_K1_K11_4_7_12', 'MS_ID', 'MS_SUS_LG_ID', 'MS_MENU_LG_ID', 'MS_PADRE_ID', 'MS_NOMBRE', 'MS_DISPLAY_LG_ID', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K12_K1_7', 'MS_ID', 'MS_NOMBRE', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K4_K6_K3_K1_K12_7', 'MS_ID', 'MS_SUS_LG_ID', 'MS_MENU_LG_ID', 'MS_PADRE_ID', 'MS_NOMBRE', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K11_1_7_12', 'MS_ID', 'MS_NOMBRE', 'MS_DISPLAY_LG_ID', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K3_K4_K6_K1', 'MS_ID', 'MS_SUS_LG_ID', 'MS_MENU_LG_ID', 'MS_PADRE_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K3_K6_1_4', 'MS_ID', 'MS_SUS_LG_ID', 'MS_MENU_LG_ID', 'MS_PADRE_ID'),
        Index('NonClusteredIndex-20170517-210612', 'MS_ID', 'MS_SUS_LG_ID', 'MS_MENU_LG_ID', 'MS_PADRE_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K1_K3_K6_K11_4_7_12', 'MS_ID', 'MS_SUS_LG_ID', 'MS_MENU_LG_ID', 'MS_PADRE_ID', 'MS_NOMBRE', 'MS_DISPLAY_LG_ID', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K1_K11_7_12', 'MS_ID', 'MS_NOMBRE', 'MS_DISPLAY_LG_ID', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K3_K6_K1_K11_4_7_12', 'MS_ID', 'MS_SUS_LG_ID', 'MS_MENU_LG_ID', 'MS_PADRE_ID', 'MS_NOMBRE', 'MS_DISPLAY_LG_ID', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K1_K3_K6_4', 'MS_ID', 'MS_SUS_LG_ID', 'MS_MENU_LG_ID', 'MS_PADRE_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K11_K3_K6_1_4_7_12', 'MS_ID', 'MS_SUS_LG_ID', 'MS_MENU_LG_ID', 'MS_PADRE_ID', 'MS_NOMBRE', 'MS_DISPLAY_LG_ID', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K12_7_11', 'MS_NOMBRE', 'MS_DISPLAY_LG_ID', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K2_K12_11', 'MS_SUS_ID', 'MS_DISPLAY_LG_ID', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K3_K1_2_4_5_6_7_8_9_10_11_12_8066', 'MS_ID', 'MS_SUS_ID', 'MS_SUS_LG_ID', 'MS_MENU_LG_ID', 'MS_TIPO_VISTA_LG_ID', 'MS_PADRE_ID', 'MS_NOMBRE', 'MS_FECHA', 'MS_LOGO', 'MS_DESCRIPCION', 'MS_DISPLAY_LG_ID', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K3_K6_K1', 'MS_ID', 'MS_SUS_LG_ID', 'MS_PADRE_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K6_K3_K1_K11_4_7_12_1912', 'MS_ID', 'MS_SUS_LG_ID', 'MS_MENU_LG_ID', 'MS_PADRE_ID', 'MS_NOMBRE', 'MS_DISPLAY_LG_ID', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K3_K6_1_4_8066', 'MS_ID', 'MS_SUS_LG_ID', 'MS_MENU_LG_ID', 'MS_PADRE_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K2_K12_11_1912', 'MS_SUS_ID', 'MS_DISPLAY_LG_ID', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K12_K7_1_3_4_6_11', 'MS_ID', 'MS_SUS_LG_ID', 'MS_MENU_LG_ID', 'MS_PADRE_ID', 'MS_NOMBRE', 'MS_DISPLAY_LG_ID', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K1_K3_K6_K11_4_7_12_4149', 'MS_ID', 'MS_SUS_LG_ID', 'MS_MENU_LG_ID', 'MS_PADRE_ID', 'MS_NOMBRE', 'MS_DISPLAY_LG_ID', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K3_K6_K1_4_1912', 'MS_ID', 'MS_SUS_LG_ID', 'MS_MENU_LG_ID', 'MS_PADRE_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K2_K12', 'MS_SUS_ID', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K12_K7_1_3_4_6_11_4149', 'MS_ID', 'MS_SUS_LG_ID', 'MS_MENU_LG_ID', 'MS_PADRE_ID', 'MS_NOMBRE', 'MS_DISPLAY_LG_ID', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K1_K4_K6_K3_K12_7_6497', 'MS_ID', 'MS_SUS_LG_ID', 'MS_MENU_LG_ID', 'MS_PADRE_ID', 'MS_NOMBRE', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K1_K11_7_12_5201', 'MS_ID', 'MS_NOMBRE', 'MS_DISPLAY_LG_ID', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K6_K3_K1_K11_4_7_12_4149', 'MS_ID', 'MS_SUS_LG_ID', 'MS_MENU_LG_ID', 'MS_PADRE_ID', 'MS_NOMBRE', 'MS_DISPLAY_LG_ID', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K1_K4_K6_K3_K12_7_1040', 'MS_ID', 'MS_SUS_LG_ID', 'MS_MENU_LG_ID', 'MS_PADRE_ID', 'MS_NOMBRE', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K12_K2', 'MS_SUS_ID', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K4_7_6960', 'MS_MENU_LG_ID', 'MS_NOMBRE'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K3_K6_K1_K11_4_7_12_6497', 'MS_ID', 'MS_SUS_LG_ID', 'MS_MENU_LG_ID', 'MS_PADRE_ID', 'MS_NOMBRE', 'MS_DISPLAY_LG_ID', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K4_7_9850', 'MS_MENU_LG_ID', 'MS_NOMBRE'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K1_K3_K6_K11_4_7_12_5201', 'MS_ID', 'MS_SUS_LG_ID', 'MS_MENU_LG_ID', 'MS_PADRE_ID', 'MS_NOMBRE', 'MS_DISPLAY_LG_ID', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K1_K3_K6_4_1040', 'MS_ID', 'MS_SUS_LG_ID', 'MS_MENU_LG_ID', 'MS_PADRE_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K1_K11_7_12_6497', 'MS_ID', 'MS_NOMBRE', 'MS_DISPLAY_LG_ID', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K2_K4_1_3_5_6_7_8_9_10_11_12', 'MS_ID', 'MS_SUS_ID', 'MS_SUS_LG_ID', 'MS_MENU_LG_ID', 'MS_TIPO_VISTA_LG_ID', 'MS_PADRE_ID', 'MS_NOMBRE', 'MS_FECHA', 'MS_LOGO', 'MS_DESCRIPCION', 'MS_DISPLAY_LG_ID', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K4_K6_K3_K1_K12_7_9850', 'MS_ID', 'MS_SUS_LG_ID', 'MS_MENU_LG_ID', 'MS_PADRE_ID', 'MS_NOMBRE', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K11_K3_K6_1_4_7_12_1771', 'MS_ID', 'MS_SUS_LG_ID', 'MS_MENU_LG_ID', 'MS_PADRE_ID', 'MS_NOMBRE', 'MS_DISPLAY_LG_ID', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K4_K6_K3_K1_K12_7_9085', 'MS_ID', 'MS_SUS_LG_ID', 'MS_MENU_LG_ID', 'MS_PADRE_ID', 'MS_NOMBRE', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K1_K3_2_4_5_6_7_8_9_10_11_12_4364', 'MS_ID', 'MS_SUS_ID', 'MS_SUS_LG_ID', 'MS_MENU_LG_ID', 'MS_TIPO_VISTA_LG_ID', 'MS_PADRE_ID', 'MS_NOMBRE', 'MS_FECHA', 'MS_LOGO', 'MS_DESCRIPCION', 'MS_DISPLAY_LG_ID', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K4_K2_1_3_5_6_7_8_9_10_11_12', 'MS_ID', 'MS_SUS_ID', 'MS_SUS_LG_ID', 'MS_MENU_LG_ID', 'MS_TIPO_VISTA_LG_ID', 'MS_PADRE_ID', 'MS_NOMBRE', 'MS_FECHA', 'MS_LOGO', 'MS_DESCRIPCION', 'MS_DISPLAY_LG_ID', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K12_K1_K4_K6_K3_7_9085', 'MS_ID', 'MS_SUS_LG_ID', 'MS_MENU_LG_ID', 'MS_PADRE_ID', 'MS_NOMBRE', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K3_K6_K1_K11_4_7_12_1040', 'MS_ID', 'MS_SUS_LG_ID', 'MS_MENU_LG_ID', 'MS_PADRE_ID', 'MS_NOMBRE', 'MS_DISPLAY_LG_ID', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K3_K6_K1_2533', 'MS_ID', 'MS_SUS_LG_ID', 'MS_PADRE_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K12_K1_K4_K6_K3_7_6355', 'MS_ID', 'MS_SUS_LG_ID', 'MS_MENU_LG_ID', 'MS_PADRE_ID', 'MS_NOMBRE', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K1_K3_K6_4_1771', 'MS_ID', 'MS_SUS_LG_ID', 'MS_MENU_LG_ID', 'MS_PADRE_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K1_K3_4_6', 'MS_ID', 'MS_SUS_LG_ID', 'MS_MENU_LG_ID', 'MS_PADRE_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K3_K4_K6_K1_K12_7_8526', 'MS_ID', 'MS_SUS_LG_ID', 'MS_MENU_LG_ID', 'MS_PADRE_ID', 'MS_NOMBRE', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K3_K4_K6_K1_K12_7_8341', 'MS_ID', 'MS_SUS_LG_ID', 'MS_MENU_LG_ID', 'MS_PADRE_ID', 'MS_NOMBRE', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K11_K3_K6_1_4_7_12_2533', 'MS_ID', 'MS_SUS_LG_ID', 'MS_MENU_LG_ID', 'MS_PADRE_ID', 'MS_NOMBRE', 'MS_DISPLAY_LG_ID', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K12_K1_8341', 'MS_ID', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K2_K12_9987', 'MS_SUS_ID', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K12_K1_K3_2_4_5_6_7_8_9_10_11', 'MS_ID', 'MS_SUS_ID', 'MS_SUS_LG_ID', 'MS_MENU_LG_ID', 'MS_TIPO_VISTA_LG_ID', 'MS_PADRE_ID', 'MS_NOMBRE', 'MS_FECHA', 'MS_LOGO', 'MS_DESCRIPCION', 'MS_DISPLAY_LG_ID', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K12_K1_114', 'MS_ID', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K3_K6_K1_8258', 'MS_ID', 'MS_SUS_LG_ID', 'MS_PADRE_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K1_K3_K12_2_4_5_6_7_8_9_10_11', 'MS_ID', 'MS_SUS_ID', 'MS_SUS_LG_ID', 'MS_MENU_LG_ID', 'MS_TIPO_VISTA_LG_ID', 'MS_PADRE_ID', 'MS_NOMBRE', 'MS_FECHA', 'MS_LOGO', 'MS_DESCRIPCION', 'MS_DISPLAY_LG_ID', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K1_K12_7_6221', 'MS_ID', 'MS_NOMBRE', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K12_K2_4364', 'MS_SUS_ID', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K1_K12_7_4683', 'MS_ID', 'MS_NOMBRE', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K2_K12_9987_4364', 'MS_SUS_ID', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K3_K1_K12_2_4_5_6_7_8_9_10_11', 'MS_ID', 'MS_SUS_ID', 'MS_SUS_LG_ID', 'MS_MENU_LG_ID', 'MS_TIPO_VISTA_LG_ID', 'MS_PADRE_ID', 'MS_NOMBRE', 'MS_FECHA', 'MS_LOGO', 'MS_DESCRIPCION', 'MS_DISPLAY_LG_ID', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K2_K4_1_3_5_6_7_8_9_10_11_12_9987', 'MS_ID', 'MS_SUS_ID', 'MS_SUS_LG_ID', 'MS_MENU_LG_ID', 'MS_TIPO_VISTA_LG_ID', 'MS_PADRE_ID', 'MS_NOMBRE', 'MS_FECHA', 'MS_LOGO', 'MS_DESCRIPCION', 'MS_DISPLAY_LG_ID', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K12_K2_8066', 'MS_SUS_ID', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K3_K1', 'MS_ID', 'MS_SUS_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K4_K2_1_3_5_6_7_8_9_10_11_12_4364', 'MS_ID', 'MS_SUS_ID', 'MS_SUS_LG_ID', 'MS_MENU_LG_ID', 'MS_TIPO_VISTA_LG_ID', 'MS_PADRE_ID', 'MS_NOMBRE', 'MS_FECHA', 'MS_LOGO', 'MS_DESCRIPCION', 'MS_DISPLAY_LG_ID', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K1_K12_2_5_7_8_9_10_11', 'MS_ID', 'MS_SUS_ID', 'MS_TIPO_VISTA_LG_ID', 'MS_NOMBRE', 'MS_FECHA', 'MS_LOGO', 'MS_DESCRIPCION', 'MS_DISPLAY_LG_ID', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K3_1_4_6_3369', 'MS_ID', 'MS_SUS_LG_ID', 'MS_MENU_LG_ID', 'MS_PADRE_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K2_K4_1_3_5_6_7_8_9_10_11_12_9987_4364', 'MS_ID', 'MS_SUS_ID', 'MS_SUS_LG_ID', 'MS_MENU_LG_ID', 'MS_TIPO_VISTA_LG_ID', 'MS_PADRE_ID', 'MS_NOMBRE', 'MS_FECHA', 'MS_LOGO', 'MS_DESCRIPCION', 'MS_DISPLAY_LG_ID', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K1_K3_4_6_9987', 'MS_ID', 'MS_SUS_LG_ID', 'MS_MENU_LG_ID', 'MS_PADRE_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K3_1_4_6_5492', 'MS_ID', 'MS_SUS_LG_ID', 'MS_MENU_LG_ID', 'MS_PADRE_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K7_K12_8066', 'MS_NOMBRE', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K3_K1_4_6', 'MS_ID', 'MS_SUS_LG_ID', 'MS_MENU_LG_ID', 'MS_PADRE_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K4_K2_1_3_5_6_7_8_9_10_11_12_8066', 'MS_ID', 'MS_SUS_ID', 'MS_SUS_LG_ID', 'MS_MENU_LG_ID', 'MS_TIPO_VISTA_LG_ID', 'MS_PADRE_ID', 'MS_NOMBRE', 'MS_FECHA', 'MS_LOGO', 'MS_DESCRIPCION', 'MS_DISPLAY_LG_ID', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K12_K1_K3_2_4_5_6_7_8_9_10_11_4364', 'MS_ID', 'MS_SUS_ID', 'MS_SUS_LG_ID', 'MS_MENU_LG_ID', 'MS_TIPO_VISTA_LG_ID', 'MS_PADRE_ID', 'MS_NOMBRE', 'MS_FECHA', 'MS_LOGO', 'MS_DESCRIPCION', 'MS_DISPLAY_LG_ID', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K3_K6_K1_K4_K12_7_6478', 'MS_ID', 'MS_SUS_LG_ID', 'MS_MENU_LG_ID', 'MS_PADRE_ID', 'MS_NOMBRE', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K1_K3_4_6_9987_4364', 'MS_ID', 'MS_SUS_LG_ID', 'MS_MENU_LG_ID', 'MS_PADRE_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K12_K1_2_5_7_8_9_10_11', 'MS_ID', 'MS_SUS_ID', 'MS_TIPO_VISTA_LG_ID', 'MS_NOMBRE', 'MS_FECHA', 'MS_LOGO', 'MS_DESCRIPCION', 'MS_DISPLAY_LG_ID', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K1_K3_K12_2_4_5_6_7_8_9_10_11_8066', 'MS_ID', 'MS_SUS_ID', 'MS_SUS_LG_ID', 'MS_MENU_LG_ID', 'MS_TIPO_VISTA_LG_ID', 'MS_PADRE_ID', 'MS_NOMBRE', 'MS_FECHA', 'MS_LOGO', 'MS_DESCRIPCION', 'MS_DISPLAY_LG_ID', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K4_K6_K1_K3_K12_7_2166', 'MS_ID', 'MS_SUS_LG_ID', 'MS_MENU_LG_ID', 'MS_PADRE_ID', 'MS_NOMBRE', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K12_K1_K3_2_4_5_6_7_8_9_10_11_8066', 'MS_ID', 'MS_SUS_ID', 'MS_SUS_LG_ID', 'MS_MENU_LG_ID', 'MS_TIPO_VISTA_LG_ID', 'MS_PADRE_ID', 'MS_NOMBRE', 'MS_FECHA', 'MS_LOGO', 'MS_DESCRIPCION', 'MS_DISPLAY_LG_ID', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K3_K12_K1_2_4_5_6_7_8_9_10_11', 'MS_ID', 'MS_SUS_ID', 'MS_SUS_LG_ID', 'MS_MENU_LG_ID', 'MS_TIPO_VISTA_LG_ID', 'MS_PADRE_ID', 'MS_NOMBRE', 'MS_FECHA', 'MS_LOGO', 'MS_DESCRIPCION', 'MS_DISPLAY_LG_ID', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K3_K1_K12_2_4_5_6_7_8_9_10_11_1912', 'MS_ID', 'MS_SUS_ID', 'MS_SUS_LG_ID', 'MS_MENU_LG_ID', 'MS_TIPO_VISTA_LG_ID', 'MS_PADRE_ID', 'MS_NOMBRE', 'MS_FECHA', 'MS_LOGO', 'MS_DESCRIPCION', 'MS_DISPLAY_LG_ID', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K1_K3_K12_2_4_5_6_7_8_9_10_11_1912', 'MS_ID', 'MS_SUS_ID', 'MS_SUS_LG_ID', 'MS_MENU_LG_ID', 'MS_TIPO_VISTA_LG_ID', 'MS_PADRE_ID', 'MS_NOMBRE', 'MS_FECHA', 'MS_LOGO', 'MS_DESCRIPCION', 'MS_DISPLAY_LG_ID', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K3_K1_4149', 'MS_ID', 'MS_SUS_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K4_K6_K1_K3_K12_7_4801', 'MS_ID', 'MS_SUS_LG_ID', 'MS_MENU_LG_ID', 'MS_PADRE_ID', 'MS_NOMBRE', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K3_K1_K12_2_4_5_6_7_8_9_10_11_4149', 'MS_ID', 'MS_SUS_ID', 'MS_SUS_LG_ID', 'MS_MENU_LG_ID', 'MS_TIPO_VISTA_LG_ID', 'MS_PADRE_ID', 'MS_NOMBRE', 'MS_FECHA', 'MS_LOGO', 'MS_DESCRIPCION', 'MS_DISPLAY_LG_ID', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K1_4', 'MS_ID', 'MS_MENU_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K6_K4_K3_K1_K12_7_1240', 'MS_ID', 'MS_SUS_LG_ID', 'MS_MENU_LG_ID', 'MS_PADRE_ID', 'MS_NOMBRE', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K1_K12_2_5_7_8_9_10_11_5201', 'MS_ID', 'MS_SUS_ID', 'MS_TIPO_VISTA_LG_ID', 'MS_NOMBRE', 'MS_FECHA', 'MS_LOGO', 'MS_DESCRIPCION', 'MS_DISPLAY_LG_ID', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K3_K1_5201', 'MS_ID', 'MS_SUS_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K12_K2_7', 'MS_SUS_ID', 'MS_NOMBRE', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K3_K1_4_6_6497', 'MS_ID', 'MS_SUS_LG_ID', 'MS_MENU_LG_ID', 'MS_PADRE_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K3_K6_K1_K4_1240', 'MS_ID', 'MS_SUS_LG_ID', 'MS_MENU_LG_ID', 'MS_PADRE_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K1_K12_2_5_7_8_9_10_11_6497', 'MS_ID', 'MS_SUS_ID', 'MS_TIPO_VISTA_LG_ID', 'MS_NOMBRE', 'MS_FECHA', 'MS_LOGO', 'MS_DESCRIPCION', 'MS_DISPLAY_LG_ID', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K2_K12_7', 'MS_SUS_ID', 'MS_NOMBRE', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K12_1_7_3', 'MS_ID', 'MS_NOMBRE', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K12_K1_2_5_7_8_9_10_11_1040', 'MS_ID', 'MS_SUS_ID', 'MS_TIPO_VISTA_LG_ID', 'MS_NOMBRE', 'MS_FECHA', 'MS_LOGO', 'MS_DESCRIPCION', 'MS_DISPLAY_LG_ID', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K6_K4_K3_K1_K12_7_742', 'MS_ID', 'MS_SUS_LG_ID', 'MS_MENU_LG_ID', 'MS_PADRE_ID', 'MS_NOMBRE', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K3_K1_4_6_1040', 'MS_ID', 'MS_SUS_LG_ID', 'MS_MENU_LG_ID', 'MS_PADRE_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K3_K12_K1_2_4_5_6_7_8_9_10_11_1771', 'MS_ID', 'MS_SUS_ID', 'MS_SUS_LG_ID', 'MS_MENU_LG_ID', 'MS_TIPO_VISTA_LG_ID', 'MS_PADRE_ID', 'MS_NOMBRE', 'MS_FECHA', 'MS_LOGO', 'MS_DESCRIPCION', 'MS_DISPLAY_LG_ID', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K1_2_3_4_5_6_7_8_9_10_11_12', 'MS_ID', 'MS_SUS_ID', 'MS_SUS_LG_ID', 'MS_MENU_LG_ID', 'MS_TIPO_VISTA_LG_ID', 'MS_PADRE_ID', 'MS_NOMBRE', 'MS_FECHA', 'MS_LOGO', 'MS_DESCRIPCION', 'MS_DISPLAY_LG_ID', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K3_K12_K4_K6_K1_7_3885', 'MS_ID', 'MS_SUS_LG_ID', 'MS_MENU_LG_ID', 'MS_PADRE_ID', 'MS_NOMBRE', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K12_K1_2_5_7_8_9_10_11_1771', 'MS_ID', 'MS_SUS_ID', 'MS_TIPO_VISTA_LG_ID', 'MS_NOMBRE', 'MS_FECHA', 'MS_LOGO', 'MS_DESCRIPCION', 'MS_DISPLAY_LG_ID', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K1_4_9987', 'MS_ID', 'MS_MENU_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K1_7_11', 'MS_ID', 'MS_NOMBRE', 'MS_DISPLAY_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K4_K6_K1_K3_9762', 'MS_ID', 'MS_SUS_LG_ID', 'MS_MENU_LG_ID', 'MS_PADRE_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K12_1_7_7337', 'MS_ID', 'MS_NOMBRE', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K3_K12_K1_2_4_5_6_7_8_9_10_11_2533', 'MS_ID', 'MS_SUS_ID', 'MS_SUS_LG_ID', 'MS_MENU_LG_ID', 'MS_TIPO_VISTA_LG_ID', 'MS_PADRE_ID', 'MS_NOMBRE', 'MS_FECHA', 'MS_LOGO', 'MS_DESCRIPCION', 'MS_DISPLAY_LG_ID', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K3_K12_1_4_6_7_6241', 'MS_ID', 'MS_SUS_LG_ID', 'MS_MENU_LG_ID', 'MS_PADRE_ID', 'MS_NOMBRE', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K1_4_9987_4364', 'MS_ID', 'MS_MENU_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K12_K7', 'MS_NOMBRE', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K3_K12_K4_K6_K1_7_7027', 'MS_ID', 'MS_SUS_LG_ID', 'MS_MENU_LG_ID', 'MS_PADRE_ID', 'MS_NOMBRE', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K12_K2_7_9987', 'MS_SUS_ID', 'MS_NOMBRE', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K4_K6_K1_K3_3227', 'MS_ID', 'MS_SUS_LG_ID', 'MS_MENU_LG_ID', 'MS_PADRE_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K7_K12', 'MS_NOMBRE', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K12_K1_7_9912', 'MS_ID', 'MS_NOMBRE', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K3_K12_1_4_6_7_9437', 'MS_ID', 'MS_SUS_LG_ID', 'MS_MENU_LG_ID', 'MS_PADRE_ID', 'MS_NOMBRE', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K12_K2_7_9987_4364', 'MS_SUS_ID', 'MS_NOMBRE', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K2_K12_7_4364', 'MS_SUS_ID', 'MS_NOMBRE', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K1_11', 'MS_ID', 'MS_DISPLAY_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K2_K12_7_8066', 'MS_SUS_ID', 'MS_NOMBRE', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K3_K4_K6_K1_812', 'MS_ID', 'MS_SUS_LG_ID', 'MS_MENU_LG_ID', 'MS_PADRE_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K1_7_12', 'MS_ID', 'MS_NOMBRE', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K1_2_3_4_5_6_7_8_9_10_11_12_9987', 'MS_ID', 'MS_SUS_ID', 'MS_SUS_LG_ID', 'MS_MENU_LG_ID', 'MS_TIPO_VISTA_LG_ID', 'MS_PADRE_ID', 'MS_NOMBRE', 'MS_FECHA', 'MS_LOGO', 'MS_DESCRIPCION', 'MS_DISPLAY_LG_ID', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K12_7_11_9987', 'MS_NOMBRE', 'MS_DISPLAY_LG_ID', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K12_K1_7_7271', 'MS_ID', 'MS_NOMBRE', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K1_2_3_4_5_6_7_8_9_10_11_12_9987_4364', 'MS_ID', 'MS_SUS_ID', 'MS_SUS_LG_ID', 'MS_MENU_LG_ID', 'MS_TIPO_VISTA_LG_ID', 'MS_PADRE_ID', 'MS_NOMBRE', 'MS_FECHA', 'MS_LOGO', 'MS_DESCRIPCION', 'MS_DISPLAY_LG_ID', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K1_7_11_9987', 'MS_ID', 'MS_NOMBRE', 'MS_DISPLAY_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K1_2_5_7_8_9_10_11_12', 'MS_ID', 'MS_SUS_ID', 'MS_TIPO_VISTA_LG_ID', 'MS_NOMBRE', 'MS_FECHA', 'MS_LOGO', 'MS_DESCRIPCION', 'MS_DISPLAY_LG_ID', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K1_7_11_9987_4364', 'MS_ID', 'MS_NOMBRE', 'MS_DISPLAY_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K12_11_4364', 'MS_DISPLAY_LG_ID', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K3_K4_K6_K1_4120', 'MS_ID', 'MS_SUS_LG_ID', 'MS_MENU_LG_ID', 'MS_PADRE_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K1_K3_2_4_5_6_7_8_9_10_11_12', 'MS_ID', 'MS_SUS_ID', 'MS_SUS_LG_ID', 'MS_MENU_LG_ID', 'MS_TIPO_VISTA_LG_ID', 'MS_PADRE_ID', 'MS_NOMBRE', 'MS_FECHA', 'MS_LOGO', 'MS_DESCRIPCION', 'MS_DISPLAY_LG_ID', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K12_K7_9987', 'MS_NOMBRE', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K1_2_5_7_8_9_10_11_12_9987_4364', 'MS_ID', 'MS_SUS_ID', 'MS_TIPO_VISTA_LG_ID', 'MS_NOMBRE', 'MS_FECHA', 'MS_LOGO', 'MS_DESCRIPCION', 'MS_DISPLAY_LG_ID', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K12_7_11_9987_4364', 'MS_NOMBRE', 'MS_DISPLAY_LG_ID', 'MS_TEMA_LG_ID'),
        Index('_dta_stat_475148738_3_4', 'MS_SUS_LG_ID', 'MS_MENU_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K3_K1_2_4_5_6_7_8_9_10_11_12', 'MS_ID', 'MS_SUS_ID', 'MS_SUS_LG_ID', 'MS_MENU_LG_ID', 'MS_TIPO_VISTA_LG_ID', 'MS_PADRE_ID', 'MS_NOMBRE', 'MS_FECHA', 'MS_LOGO', 'MS_DESCRIPCION', 'MS_DISPLAY_LG_ID', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K12_7_8066', 'MS_NOMBRE', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K1_K3_2_4_5_6_7_8_9_10_11_12_8066', 'MS_ID', 'MS_SUS_ID', 'MS_SUS_LG_ID', 'MS_MENU_LG_ID', 'MS_TIPO_VISTA_LG_ID', 'MS_PADRE_ID', 'MS_NOMBRE', 'MS_FECHA', 'MS_LOGO', 'MS_DESCRIPCION', 'MS_DISPLAY_LG_ID', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K7_K12_4364', 'MS_NOMBRE', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K12_11_8066', 'MS_DISPLAY_LG_ID', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K1_7', 'MS_ID', 'MS_NOMBRE'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K3_K1_2_4_5_6_7_8_9_10_11_12_1912', 'MS_ID', 'MS_SUS_ID', 'MS_SUS_LG_ID', 'MS_MENU_LG_ID', 'MS_TIPO_VISTA_LG_ID', 'MS_PADRE_ID', 'MS_NOMBRE', 'MS_FECHA', 'MS_LOGO', 'MS_DESCRIPCION', 'MS_DISPLAY_LG_ID', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K11_1_7_12_9987', 'MS_ID', 'MS_NOMBRE', 'MS_DISPLAY_LG_ID', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K1_12', 'MS_ID', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K1_2_5_7_8_9_10_11_12_9987', 'MS_ID', 'MS_SUS_ID', 'MS_TIPO_VISTA_LG_ID', 'MS_NOMBRE', 'MS_FECHA', 'MS_LOGO', 'MS_DESCRIPCION', 'MS_DISPLAY_LG_ID', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K12_7_1912', 'MS_NOMBRE', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K12_K7_9987_4364', 'MS_NOMBRE', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K3_K6_1_4_4364', 'MS_ID', 'MS_SUS_LG_ID', 'MS_MENU_LG_ID', 'MS_PADRE_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K1_K2_3_4_5_6_7_8_9_10_11_12', 'MS_ID', 'MS_SUS_ID', 'MS_SUS_LG_ID', 'MS_MENU_LG_ID', 'MS_TIPO_VISTA_LG_ID', 'MS_PADRE_ID', 'MS_NOMBRE', 'MS_FECHA', 'MS_LOGO', 'MS_DESCRIPCION', 'MS_DISPLAY_LG_ID', 'MS_TEMA_LG_ID'),
        Index('_dta_index_K_MENU_SUSCRIPTOR_5_475148738__K3_K6_K1_4_8066', 'MS_ID', 'MS_SUS_LG_ID', 'MS_MENU_LG_ID', 'MS_PADRE_ID')
    )

    MS_ID = Column(Integer, primary_key=True, index=True)
    MS_SUS_ID = Column(ForeignKey('C_SUSCRIPTOR.SUS_ID'), nullable=False, index=True)
    MS_SUS_LG_ID = Column(Integer, nullable=False, index=True)
    MS_MENU_LG_ID = Column(Integer, nullable=False, index=True)
    MS_TIPO_VISTA_LG_ID = Column(Integer, nullable=False)
    MS_PADRE_ID = Column(Integer, nullable=False, index=True)
    MS_NOMBRE = Column(String(100, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    MS_FECHA = Column(SMALLDATETIME, nullable=False)
    MS_LOGO = Column(Unicode(150), nullable=False)
    MS_DESCRIPCION = Column(Unicode(100), nullable=False)
    MS_DISPLAY_LG_ID = Column(Integer, nullable=False)
    MS_TEMA_LG_ID = Column(BigInteger, index=True)

    C_SUSCRIPTOR = relationship('CSUSCRIPTOR')


class KNEWSLETTERCONFIGURACION(Base):
    __tablename__ = 'K_NEWSLETTER_CONFIGURACION'

    NC_ID = Column(Integer, primary_key=True)
    NC_SUS_ID = Column(ForeignKey('C_SUSCRIPTOR.SUS_ID'), nullable=False)
    NC_NL_ID = Column(ForeignKey('C_NLLAYOUT.NL_ID'), nullable=False)
    NC_PR_CABEZAL = Column(BIT, nullable=False)
    NC_PR_CONTEO_NEWS = Column(BIT, nullable=False)
    NC_PR_COSTO = Column(BIT, nullable=False)
    NC_PR_ESQUEMA_COLOR = Column(String(100, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    NC_PR_DIVISAS = Column(BIT, nullable=False)
    NC_PR_PORTADAS = Column(BIT, nullable=False)
    NC_PR_ACUMULAR_TEMAS = Column(BIT, nullable=False)
    NC_PR_ORDEN = Column(String(200, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    NC_PR_OCHOCOLUMNAS = Column(BIT, nullable=False)
    NC_PR_URLMEDIOS = Column(BIT, nullable=False)
    NC_PR_CLASIFICACION_PREVIA = Column(BIT, nullable=False)
    NC_PR_COMPARTIR_FACEBOOK = Column(BIT, nullable=False)
    NC_PR_COMPARTIR_TWITTER = Column(BIT, nullable=False)
    NC_PR_COMPARTIR_LINKEDIN = Column(BIT, nullable=False)
    NC_PR_COMPARTIR_CORREO = Column(BIT, nullable=False)
    NC_PR_INCLUYETEMAS_BLANCO = Column(BIT, nullable=False)
    NC_PR_CUENTA_MENCIONES = Column(BIT, nullable=False)
    NC_PR_IMAGEN = Column(String(collation='SQL_Latin1_General_CP1_CI_AS'))

    C_NLLAYOUT = relationship('CNLLAYOUT')
    C_SUSCRIPTOR = relationship('CSUSCRIPTOR')


class KPROCESOCOLA(Base):
    __tablename__ = 'K_PROCESO_COLA'

    PCO_ID = Column(Integer, primary_key=True)
    PCO_NUM = Column(Integer, nullable=False)
    PCO_SUS_ID = Column(ForeignKey('C_SUSCRIPTOR.SUS_ID'))
    PCO_T_ID = Column(ForeignKey('K_TEMA.T_ID'))
    PCO_FECHA_SOLICITADO = Column(DateTime)
    PCO_FECHA_INICIO = Column(DateTime)
    PCO_FECHA_FIN = Column(DateTime)
    PCO_STATUS = Column(Integer)
    PCO_USU_ID = Column(BigInteger, nullable=False)
    PCO_RESULTADO = Column(String(500, 'SQL_Latin1_General_CP1_CI_AS'))

    C_SUSCRIPTOR = relationship('CSUSCRIPTOR')
    K_TEMA = relationship('KTEMA')


class KSUSCRIPTORALERTA(Base):
    __tablename__ = 'K_SUSCRIPTOR_ALERTA'

    SA_ID = Column(Integer, primary_key=True)
    SA_TIPO = Column(String(300, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    SA_SUS_ID = Column(ForeignKey('C_SUSCRIPTOR.SUS_ID'), nullable=False)
    SA_ESTATUS = Column(String(300, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    SA_FECHA_CREACION = Column(DateTime, nullable=False)
    SA_DESCRIPCION = Column(String(5000, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    SA_FORMATO = Column(Integer)

    C_SUSCRIPTOR = relationship('CSUSCRIPTOR')


class KSUSCRIPTORPRODUCTO(Base):
    __tablename__ = 'K_SUSCRIPTOR_PRODUCTO'

    SP_ID = Column(Integer, primary_key=True)
    SP_SUS_ID = Column(ForeignKey('C_SUSCRIPTOR.SUS_ID'), nullable=False)
    SP_PR_ID = Column(ForeignKey('C_PRODUCTOS.PR_ID'), nullable=False)

    C_PRODUCTO = relationship('CPRODUCTO')
    C_SUSCRIPTOR = relationship('CSUSCRIPTOR')


class CMEDIOCOSTO(Base):
    __tablename__ = 'C_MEDIO_COSTOS'
    __table_args__ = (
        Index('_dta_index_C_MEDIO_COSTOS_5_2055678371__K2_1_5', 'CT_ID', 'CT_ME_ID', 'CT_COSTO'),
        Index('_dta_index_C_MEDIO_COSTOS_5_2055678371__K5_1', 'CT_ID', 'CT_COSTO'),
        Index('_dta_index_C_MEDIO_COSTOS_5_2055678371__K2_K5_1_3_4', 'CT_ID', 'CT_ME_ID', 'CT_DESCRIPCION', 'CT_MEDIDA', 'CT_COSTO'),
        Index('_dta_index_C_MEDIO_COSTOS_5_2055678371__K2_1_3_4_5', 'CT_ID', 'CT_ME_ID', 'CT_DESCRIPCION', 'CT_MEDIDA', 'CT_COSTO'),
        Index('_dta_index_C_MEDIO_COSTOS_5_2055678371__K5_1_2_3_4', 'CT_ID', 'CT_ME_ID', 'CT_DESCRIPCION', 'CT_MEDIDA', 'CT_COSTO'),
        Index('_dta_index_C_MEDIO_COSTOS_5_2055678371__K1_2_3_4_5', 'CT_ID', 'CT_ME_ID', 'CT_DESCRIPCION', 'CT_MEDIDA', 'CT_COSTO'),
        Index('_dta_stat_2055678371_2_5', 'CT_ME_ID', 'CT_COSTO')
    )

    CT_ID = Column(Integer, primary_key=True)
    CT_ME_ID = Column(ForeignKey('C_MEDIO.ME_ID'), nullable=False)
    CT_DESCRIPCION = Column(String(100, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    CT_MEDIDA = Column(String(100, 'SQL_Latin1_General_CP1_CI_AS'))
    CT_COSTO = Column(DECIMAL(18, 2), nullable=False)

    C_MEDIO = relationship('CMEDIO')


class CSECCION(Base):
    __tablename__ = 'C_SECCION'
    __table_args__ = (
        Index('_dta_index_C_SECCION_5_670625432_51856808_K1_K3_K4', 'SEC_ID', 'SEC_ME_ID', 'SEC_LG_ID'),
        Index('_dta_index_C_SECCION_5_670625432__K1_2_3_4_9987', 'SEC_ID', 'SEC_NOMBRE', 'SEC_ME_ID', 'SEC_LG_ID'),
        Index('_dta_index_C_SECCION_5_670625432__K3_K1_2_4_1040_1771', 'SEC_ID', 'SEC_NOMBRE', 'SEC_ME_ID', 'SEC_LG_ID'),
        Index('_dta_index_C_SECCION_5_670625432__K1_2', 'SEC_ID', 'SEC_NOMBRE'),
        Index('_dta_index_C_SECCION_5_670625432__K1_2_3_4_9085', 'SEC_ID', 'SEC_NOMBRE', 'SEC_ME_ID', 'SEC_LG_ID'),
        Index('_dta_index_C_SECCION_5_670625432__K3_K1_2_4_5201', 'SEC_ID', 'SEC_NOMBRE', 'SEC_ME_ID', 'SEC_LG_ID'),
        Index('_dta_index_C_SECCION_5_670625432__K1_K2_1912', 'SEC_ID', 'SEC_NOMBRE'),
        Index('_dta_index_C_SECCION_5_670625432_70953536_K1_2_3_4', 'SEC_ID', 'SEC_NOMBRE', 'SEC_ME_ID', 'SEC_LG_ID'),
        Index('_dta_index_C_SECCION_5_670625432_49239816_K1_2_3_4', 'SEC_ID', 'SEC_NOMBRE', 'SEC_ME_ID', 'SEC_LG_ID'),
        Index('_dta_index_C_SECCION_5_670625432__K1_2_3_4_9987_4364_8066', 'SEC_ID', 'SEC_NOMBRE', 'SEC_ME_ID', 'SEC_LG_ID'),
        Index('_dta_index_C_SECCION_5_670625432__K2_1_5201', 'SEC_ID', 'SEC_NOMBRE'),
        Index('_dta_index_C_SECCION_5_670625432__K1_K3_4_6497', 'SEC_ID', 'SEC_ME_ID', 'SEC_LG_ID'),
        Index('_dta_index_C_SECCION_5_670625432__K1_K2_9987', 'SEC_ID', 'SEC_NOMBRE'),
        Index('_dta_index_C_SECCION_5_670625432__K1_2_3_4_9850', 'SEC_ID', 'SEC_NOMBRE', 'SEC_ME_ID', 'SEC_LG_ID'),
        Index('_dta_index_C_SECCION_5_670625432__K1_K3_2_4_9987_4364', 'SEC_ID', 'SEC_NOMBRE', 'SEC_ME_ID', 'SEC_LG_ID'),
        Index('_dta_index_C_SECCION_5_670625432__K2_1', 'SEC_ID', 'SEC_NOMBRE'),
        Index('_dta_index_C_SECCION_5_670625432__K2_1_4364', 'SEC_ID', 'SEC_NOMBRE'),
        Index('_dta_index_C_SECCION_5_670625432_51857368_K1_2_3_4', 'SEC_ID', 'SEC_NOMBRE', 'SEC_ME_ID', 'SEC_LG_ID'),
        Index('_dta_index_C_SECCION_5_670625432__K1_2_3_4', 'SEC_ID', 'SEC_NOMBRE', 'SEC_ME_ID', 'SEC_LG_ID'),
        Index('_dta_index_C_SECCION_5_670625432__K3_K1_4_8066', 'SEC_ID', 'SEC_ME_ID', 'SEC_LG_ID'),
        Index('_dta_index_C_SECCION_5_670625432__K1_K3_2_4_9987_4364_8066_1912', 'SEC_ID', 'SEC_NOMBRE', 'SEC_ME_ID', 'SEC_LG_ID'),
        Index('_dta_index_C_SECCION_5_670625432__K1_K3_2_4_9987', 'SEC_ID', 'SEC_NOMBRE', 'SEC_ME_ID', 'SEC_LG_ID'),
        Index('_dta_index_C_SECCION_5_670625432_104889936_K1_2_3_4', 'SEC_ID', 'SEC_NOMBRE', 'SEC_ME_ID', 'SEC_LG_ID'),
        Index('_dta_index_C_SECCION_5_670625432__K1_K3_4_1912', 'SEC_ID', 'SEC_ME_ID', 'SEC_LG_ID'),
        Index('_dta_index_C_SECCION_5_670625432__K3_K1_4_4149', 'SEC_ID', 'SEC_ME_ID', 'SEC_LG_ID'),
        Index('_dta_index_C_SECCION_5_670625432__K3_K1_2_4_4149', 'SEC_ID', 'SEC_NOMBRE', 'SEC_ME_ID', 'SEC_LG_ID'),
        Index('_dta_index_C_SECCION_5_670625432__K3_K1_4_4364', 'SEC_ID', 'SEC_ME_ID', 'SEC_LG_ID'),
        Index('_dta_index_C_SECCION_5_670625432__K1_K3_4_5201', 'SEC_ID', 'SEC_ME_ID', 'SEC_LG_ID'),
        Index('_dta_index_C_SECCION_5_670625432__K1_K3_2_4', 'SEC_ID', 'SEC_NOMBRE', 'SEC_ME_ID', 'SEC_LG_ID'),
        Index('NonClusteredIndex-20170124-135201', 'SEC_ID', 'SEC_ME_ID', 'SEC_LG_ID'),
        Index('_dta_index_C_SECCION_5_670625432__K1_K3_4_8066', 'SEC_ID', 'SEC_ME_ID', 'SEC_LG_ID'),
        Index('_dta_index_C_SECCION_5_670625432__K1_2_6497', 'SEC_ID', 'SEC_NOMBRE'),
        Index('_dta_index_C_SECCION_5_670625432__K3_K1_4', 'SEC_ID', 'SEC_ME_ID', 'SEC_LG_ID'),
        Index('_dta_index_C_SECCION_5_670625432__K3_K1_2_4_1912', 'SEC_ID', 'SEC_NOMBRE', 'SEC_ME_ID', 'SEC_LG_ID'),
        Index('_dta_index_C_SECCION_5_670625432__K3_K1_2_4_1040', 'SEC_ID', 'SEC_NOMBRE', 'SEC_ME_ID', 'SEC_LG_ID'),
        Index('_dta_index_C_SECCION_5_670625432__K1_K3_4', 'SEC_ID', 'SEC_ME_ID', 'SEC_LG_ID'),
        Index('_dta_index_C_SECCION_5_670625432__K2_1_3_4_4149', 'SEC_ID', 'SEC_NOMBRE', 'SEC_ME_ID', 'SEC_LG_ID'),
        Index('_dta_index_C_SECCION_5_670625432__K3_K1_2_4', 'SEC_ID', 'SEC_NOMBRE', 'SEC_ME_ID', 'SEC_LG_ID'),
        Index('_dta_index_C_SECCION_5_670625432__K1_2_3_4_9987_4364', 'SEC_ID', 'SEC_NOMBRE', 'SEC_ME_ID', 'SEC_LG_ID'),
        Index('_dta_index_C_SECCION_5_670625432_100452352_K1_2_3_4', 'SEC_ID', 'SEC_NOMBRE', 'SEC_ME_ID', 'SEC_LG_ID'),
        Index('_dta_index_C_SECCION_5_670625432__K2_1_3_4_8066', 'SEC_ID', 'SEC_NOMBRE', 'SEC_ME_ID', 'SEC_LG_ID'),
        Index('_dta_index_C_SECCION_5_670625432__K1_2_4364', 'SEC_ID', 'SEC_NOMBRE'),
        Index('_dta_index_C_SECCION_5_670625432_70952808_K1_K3_K4', 'SEC_ID', 'SEC_ME_ID', 'SEC_LG_ID'),
        Index('_dta_index_C_SECCION_5_670625432__K1_2_3369', 'SEC_ID', 'SEC_NOMBRE'),
        Index('_dta_index_C_SECCION_5_670625432__K1_K3_2_4_9987_4364_8066', 'SEC_ID', 'SEC_NOMBRE', 'SEC_ME_ID', 'SEC_LG_ID'),
        Index('_dta_index_C_SECCION_5_670625432_104889936_K1_K3_K4', 'SEC_ID', 'SEC_ME_ID', 'SEC_LG_ID'),
        Index('_dta_index_C_SECCION_5_670625432__K1_2_9987', 'SEC_ID', 'SEC_NOMBRE'),
        Index('_dta_index_C_SECCION_5_670625432__K1_K2_1912_4149', 'SEC_ID', 'SEC_NOMBRE'),
        Index('_dta_index_C_SECCION_5_670625432__K2_1_3_4', 'SEC_ID', 'SEC_NOMBRE', 'SEC_ME_ID', 'SEC_LG_ID'),
        Index('_dta_index_C_SECCION_5_670625432__K3_K1_4_1912', 'SEC_ID', 'SEC_ME_ID', 'SEC_LG_ID'),
        Index('_dta_index_C_SECCION_5_670625432__K1_K3_2_4_9987_4364_8066_1912_4149', 'SEC_ID', 'SEC_NOMBRE', 'SEC_ME_ID', 'SEC_LG_ID'),
        Index('_dta_index_C_SECCION_5_670625432__K1_K3_4_4149', 'SEC_ID', 'SEC_ME_ID', 'SEC_LG_ID'),
        Index('_dta_index_C_SECCION_5_670625432__K1_K2', 'SEC_ID', 'SEC_NOMBRE'),
        Index('_dta_index_C_SECCION_5_670625432__K2_1_6497', 'SEC_ID', 'SEC_NOMBRE'),
        Index('_dta_index_C_SECCION_5_670625432__K3_K1_4_5201', 'SEC_ID', 'SEC_ME_ID', 'SEC_LG_ID'),
        Index('_dta_index_C_SECCION_5_670625432__K1_2_8337', 'SEC_ID', 'SEC_NOMBRE'),
        Index('_dta_index_C_SECCION_5_670625432_49273456_K1_K3_K4', 'SEC_ID', 'SEC_ME_ID', 'SEC_LG_ID')
    )

    SEC_ID = Column(BigInteger, primary_key=True, index=True)
    SEC_NOMBRE = Column(String(100, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    SEC_ME_ID = Column(ForeignKey('C_MEDIO.ME_ID'), nullable=False, index=True)
    SEC_LG_ID = Column(BigInteger, nullable=False, index=True)

    C_MEDIO = relationship('CMEDIO')


class KCONTROLACCESO(Base):
    __tablename__ = 'K_CONTROL_ACCESO'

    CA_ID = Column(Integer, primary_key=True)
    CA_ASM_ID = Column(ForeignKey('C_ACCION_SUBMODULO.ASM_ID'), nullable=False)
    CA_ESTATUS = Column(BIT, nullable=False)
    CA_TU_ID = Column(ForeignKey('C_TIPO_USUARIO.TU_ID'), nullable=False)

    C_ACCION_SUBMODULO = relationship('CACCIONSUBMODULO')
    C_TIPO_USUARIO = relationship('CTIPOUSUARIO')


class KMENUSUSCRIPTORGRUPO(Base):
    __tablename__ = 'K_MENU_SUSCRIPTOR_GRUPO'

    MSG_ID = Column(Integer, primary_key=True)
    MSG_MS_ID = Column(ForeignKey('K_MENU_SUSCRIPTOR.MS_ID'), nullable=False)
    MSG_GR_ID = Column(ForeignKey('C_GRUPO.GR_ID'), nullable=False)
    MSG_ORDEN = Column(Integer, nullable=False)

    C_GRUPO = relationship('CGRUPO')
    K_MENU_SUSCRIPTOR = relationship('KMENUSUSCRIPTOR')


class KNEWSLETTER(Base):
    __tablename__ = 'K_NEWSLETTER'
    __table_args__ = (
        Index('NonClusteredIndex-20180122-210104', 'NW_ID', 'NW_FECHA'),
    )

    NW_ID = Column(Integer, primary_key=True)
    NW_NC_ID = Column(ForeignKey('K_NEWSLETTER_CONFIGURACION.NC_ID'), nullable=False)
    NW_SUS_ID = Column(ForeignKey('C_SUSCRIPTOR.SUS_ID'), nullable=False)
    NW_FECHA = Column(DateTime, nullable=False)
    NW_TITULO = Column(String(2000, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    NW_GUID = Column(UNIQUEIDENTIFIER, nullable=False)

    K_NEWSLETTER_CONFIGURACION = relationship('KNEWSLETTERCONFIGURACION')
    C_SUSCRIPTOR = relationship('CSUSCRIPTOR')


class KSUSCRIPTORALERTADETALLE(Base):
    __tablename__ = 'K_SUSCRIPTOR_ALERTA_DETALLE'

    SAD_ID = Column(Integer, primary_key=True)
    SAD_TIPO = Column(String(400, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    SAD_T_ID = Column(ForeignKey('K_TEMA.T_ID'))
    SAD_MED_ID = Column(ForeignKey('C_MEDIO.ME_ID'))
    SAD_SA_ID = Column(ForeignKey('K_SUSCRIPTOR_ALERTA.SA_ID'), nullable=False)

    C_MEDIO = relationship('CMEDIO')
    K_SUSCRIPTOR_ALERTA = relationship('KSUSCRIPTORALERTA')
    K_TEMA = relationship('KTEMA')


class KSUSCRIPTORALERTADISTRIBUCION(Base):
    __tablename__ = 'K_SUSCRIPTOR_ALERTA_DISTRIBUCION'

    SADI_ID = Column(Integer, primary_key=True)
    SADI_SA_ID = Column(ForeignKey('K_SUSCRIPTOR_ALERTA.SA_ID'), nullable=False)
    SADI_NUM_CEL = Column(String(20, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    SADI_NOMBRE = Column(String(2000, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    SADI_HORA_INICIO = Column(DateTime, nullable=False)
    SADI_HORA_FIN = Column(DateTime, nullable=False)
    SADI_DIAS_SEMANA = Column(String(200, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    SADI_TIPO_HORARIO = Column(String(200, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)

    K_SUSCRIPTOR_ALERTA = relationship('KSUSCRIPTORALERTA')


class KSUSCRIPTORUSUARIOPRODUCTO(Base):
    __tablename__ = 'K_SUSCRIPTOR_USUARIO_PRODUCTO'

    SUP_ID = Column(Integer, primary_key=True)
    SUP_SUSU_ID = Column(Integer, nullable=False)
    SUP_SP_ID = Column(ForeignKey('K_SUSCRIPTOR_PRODUCTO.SP_ID'), nullable=False)

    K_SUSCRIPTOR_PRODUCTO = relationship('KSUSCRIPTORPRODUCTO')


class KTEMAMEDIO(Base):
    __tablename__ = 'K_TEMA_MEDIO'
    __table_args__ = (
        Index('_dta_index_K_TEMA_MEDIO_5_843150049__K3_K2_1_9987_4364_8066_1912', 'TM_ID', 'TM_T_ID', 'TM_ME_ID'),
        Index('_dta_index_K_TEMA_MEDIO_5_843150049__K3_1_2_9987_4364', 'TM_ID', 'TM_T_ID', 'TM_ME_ID'),
        Index('_dta_index_K_TEMA_MEDIO_5_843150049__K3_K2_8066', 'TM_T_ID', 'TM_ME_ID'),
        Index('_dta_index_K_TEMA_MEDIO_5_843150049__K2_K3', 'TM_T_ID', 'TM_ME_ID'),
        Index('_dta_index_K_TEMA_MEDIO_5_843150049__K3_K2_1_9987_4364', 'TM_ID', 'TM_T_ID', 'TM_ME_ID'),
        Index('_dta_index_K_TEMA_MEDIO_5_843150049__K3_1_2_9987_4364_8066', 'TM_ID', 'TM_T_ID', 'TM_ME_ID'),
        Index('_dta_index_K_TEMA_MEDIO_5_843150049__K2_K3_9987_4364', 'TM_T_ID', 'TM_ME_ID'),
        Index('_dta_index_K_TEMA_MEDIO_5_843150049__K3_K2_9987', 'TM_T_ID', 'TM_ME_ID'),
        Index('_dta_index_K_TEMA_MEDIO_5_843150049__K3_K2_1_9987', 'TM_ID', 'TM_T_ID', 'TM_ME_ID'),
        Index('_dta_index_K_TEMA_MEDIO_5_843150049__K3_K2_1', 'TM_ID', 'TM_T_ID', 'TM_ME_ID'),
        Index('_dta_index_K_TEMA_MEDIO_5_843150049__K3_K2_4364', 'TM_T_ID', 'TM_ME_ID'),
        Index('_dta_index_K_TEMA_MEDIO_5_843150049__K2_K3_9987_4364_8066', 'TM_T_ID', 'TM_ME_ID'),
        Index('_dta_index_K_TEMA_MEDIO_5_843150049__K2_1_3', 'TM_ID', 'TM_T_ID', 'TM_ME_ID'),
        Index('_dta_index_K_TEMA_MEDIO_5_843150049__K1_2_3', 'TM_ID', 'TM_T_ID', 'TM_ME_ID'),
        Index('_dta_index_K_TEMA_MEDIO_5_843150049__K3_1_2', 'TM_ID', 'TM_T_ID', 'TM_ME_ID'),
        Index('_dta_index_K_TEMA_MEDIO_5_843150049__K3_K2_1_9987_4364_8066', 'TM_ID', 'TM_T_ID', 'TM_ME_ID'),
        Index('_dta_index_K_TEMA_MEDIO_5_843150049__K3_1_2_9987', 'TM_ID', 'TM_T_ID', 'TM_ME_ID'),
        Index('_dta_index_K_TEMA_MEDIO_5_843150049__K3_1_2_9987_4364_8066_1912', 'TM_ID', 'TM_T_ID', 'TM_ME_ID'),
        Index('_dta_index_K_TEMA_MEDIO_5_843150049__K2_K3_9987', 'TM_T_ID', 'TM_ME_ID'),
        Index('_dta_index_K_TEMA_MEDIO_5_843150049__K3_K2_9987_4364', 'TM_T_ID', 'TM_ME_ID'),
        Index('_dta_index_K_TEMA_MEDIO_5_843150049__K3_K2', 'TM_T_ID', 'TM_ME_ID'),
        Index('_dta_index_K_TEMA_MEDIO_5_843150049__K2_K3_9987_4364_8066_1912', 'TM_T_ID', 'TM_ME_ID'),
        Index('_dta_index_K_TEMA_MEDIO_5_843150049__K1_2_3_9987', 'TM_ID', 'TM_T_ID', 'TM_ME_ID')
    )

    TM_ID = Column(BigInteger, primary_key=True, index=True)
    TM_T_ID = Column(ForeignKey('K_TEMA.T_ID'), nullable=False, index=True)
    TM_ME_ID = Column(ForeignKey('C_MEDIO.ME_ID'), nullable=False)

    C_MEDIO = relationship('CMEDIO')
    K_TEMA = relationship('KTEMA')


class CPROGRAMA(Base):
    __tablename__ = 'C_PROGRAMA'

    PRG_ID = Column(BigInteger, primary_key=True)
    PRG_NOMBRE = Column(String(500, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    PRG_SEC_ID = Column(ForeignKey('C_SECCION.SEC_ID'), nullable=False)
    PRG_LG_ID = Column(BigInteger, nullable=False)

    C_SECCION = relationship('CSECCION')


class KNEWSLETTERDETALLE(Base):
    __tablename__ = 'K_NEWSLETTER_DETALLE'
    __table_args__ = (
        Index('_dta_index_K_NEWSLETTER_DETALLE_5_1938105945__K1_2_3_5_6_7_8_9_10_11_12_13_14_15_16_17_18_19_20_21_22_23_24_25_26_9987', 'NWD_ID', 'NWD_NW_ID', 'NWD_NOTAID', 'NWD_NOMRE_MEDIO', 'NWD_TIPO_MEDIO', 'NWD_MENU_DISPLAY', 'NWD_MENU', 'NWD_TEMA', 'NWD_TEMA_DISPLAY', 'NWD_SECCION', 'NWD_PAGINA', 'NWD_COSTO', 'NWD_TITULO', 'NWD_TIPO_NOTA', 'NWD_CALIFICACION', 'NWD_AUTORES', 'NWD_FECHA_PUBLICACION', 'NWD_DURACION', 'NWD_URL', 'NWD_TESTIGOS', 'NWD_MENU_LG_ID', 'NWD_TEMAPADRE_LG_ID', 'NWD_TEMAHIJO_LG_ID', 'NWD_MEDIO_LG_ID', 'NWD_MEDIO_LOGO'),
        Index('_dta_index_K_NEWSLETTER_DETALLE_5_1938105945__K2_1_3_5_6_7_8_9_10_11_12_13_14_15_16_17_18_19_20_21_22_23_24_25_26_9987_4364', 'NWD_ID', 'NWD_NW_ID', 'NWD_NOTAID', 'NWD_NOMRE_MEDIO', 'NWD_TIPO_MEDIO', 'NWD_MENU_DISPLAY', 'NWD_MENU', 'NWD_TEMA', 'NWD_TEMA_DISPLAY', 'NWD_SECCION', 'NWD_PAGINA', 'NWD_COSTO', 'NWD_TITULO', 'NWD_TIPO_NOTA', 'NWD_CALIFICACION', 'NWD_AUTORES', 'NWD_FECHA_PUBLICACION', 'NWD_DURACION', 'NWD_URL', 'NWD_TESTIGOS', 'NWD_MENU_LG_ID', 'NWD_TEMAPADRE_LG_ID', 'NWD_TEMAHIJO_LG_ID', 'NWD_MEDIO_LG_ID', 'NWD_MEDIO_LOGO'),
        Index('_dta_index_K_NEWSLETTER_DETALLE_5_1938105945__K2_1_3_5_6_7_8_9_10_11_12_13_14_15_16_17_18_19_20_21_22_23_24_25_26', 'NWD_ID', 'NWD_NW_ID', 'NWD_NOTAID', 'NWD_NOMRE_MEDIO', 'NWD_TIPO_MEDIO', 'NWD_MENU_DISPLAY', 'NWD_MENU', 'NWD_TEMA', 'NWD_TEMA_DISPLAY', 'NWD_SECCION', 'NWD_PAGINA', 'NWD_COSTO', 'NWD_TITULO', 'NWD_TIPO_NOTA', 'NWD_CALIFICACION', 'NWD_AUTORES', 'NWD_FECHA_PUBLICACION', 'NWD_DURACION', 'NWD_URL', 'NWD_TESTIGOS', 'NWD_MENU_LG_ID', 'NWD_TEMAPADRE_LG_ID', 'NWD_TEMAHIJO_LG_ID', 'NWD_MEDIO_LG_ID', 'NWD_MEDIO_LOGO'),
        Index('_dta_index_K_NEWSLETTER_DETALLE_5_1938105945__K1_2_3_5_6_7_8_9_10_11_12_13_14_15_16_17_18_19_20_21_22_23_24_25_26_9987_4364', 'NWD_ID', 'NWD_NW_ID', 'NWD_NOTAID', 'NWD_NOMRE_MEDIO', 'NWD_TIPO_MEDIO', 'NWD_MENU_DISPLAY', 'NWD_MENU', 'NWD_TEMA', 'NWD_TEMA_DISPLAY', 'NWD_SECCION', 'NWD_PAGINA', 'NWD_COSTO', 'NWD_TITULO', 'NWD_TIPO_NOTA', 'NWD_CALIFICACION', 'NWD_AUTORES', 'NWD_FECHA_PUBLICACION', 'NWD_DURACION', 'NWD_URL', 'NWD_TESTIGOS', 'NWD_MENU_LG_ID', 'NWD_TEMAPADRE_LG_ID', 'NWD_TEMAHIJO_LG_ID', 'NWD_MEDIO_LG_ID', 'NWD_MEDIO_LOGO'),
        Index('_dta_index_K_NEWSLETTER_DETALLE_5_1938105945__K2_1_3_5_6_7_8_9_10_11_12_13_14_15_16_17_18_19_20_21_22_23_24_25_26_9987_4364_8066', 'NWD_ID', 'NWD_NW_ID', 'NWD_NOTAID', 'NWD_NOMRE_MEDIO', 'NWD_TIPO_MEDIO', 'NWD_MENU_DISPLAY', 'NWD_MENU', 'NWD_TEMA', 'NWD_TEMA_DISPLAY', 'NWD_SECCION', 'NWD_PAGINA', 'NWD_COSTO', 'NWD_TITULO', 'NWD_TIPO_NOTA', 'NWD_CALIFICACION', 'NWD_AUTORES', 'NWD_FECHA_PUBLICACION', 'NWD_DURACION', 'NWD_URL', 'NWD_TESTIGOS', 'NWD_MENU_LG_ID', 'NWD_TEMAPADRE_LG_ID', 'NWD_TEMAHIJO_LG_ID', 'NWD_MEDIO_LG_ID', 'NWD_MEDIO_LOGO'),
        Index('_dta_index_K_NEWSLETTER_DETALLE_5_1938105945__K1_2_3_5_6_7_8_9_10_11_12_13_14_15_16_17_18_19_20_21_22_23_24_25_26_9987_4364_8066', 'NWD_ID', 'NWD_NW_ID', 'NWD_NOTAID', 'NWD_NOMRE_MEDIO', 'NWD_TIPO_MEDIO', 'NWD_MENU_DISPLAY', 'NWD_MENU', 'NWD_TEMA', 'NWD_TEMA_DISPLAY', 'NWD_SECCION', 'NWD_PAGINA', 'NWD_COSTO', 'NWD_TITULO', 'NWD_TIPO_NOTA', 'NWD_CALIFICACION', 'NWD_AUTORES', 'NWD_FECHA_PUBLICACION', 'NWD_DURACION', 'NWD_URL', 'NWD_TESTIGOS', 'NWD_MENU_LG_ID', 'NWD_TEMAPADRE_LG_ID', 'NWD_TEMAHIJO_LG_ID', 'NWD_MEDIO_LG_ID', 'NWD_MEDIO_LOGO'),
        Index('_dta_index_K_NEWSLETTER_DETALLE_5_1938105945__K1_2_3_5_6_7_8_9_10_11_12_13_14_15_16_17_18_19_20_21_22_23_24_25_26', 'NWD_ID', 'NWD_NW_ID', 'NWD_NOTAID', 'NWD_NOMRE_MEDIO', 'NWD_TIPO_MEDIO', 'NWD_MENU_DISPLAY', 'NWD_MENU', 'NWD_TEMA', 'NWD_TEMA_DISPLAY', 'NWD_SECCION', 'NWD_PAGINA', 'NWD_COSTO', 'NWD_TITULO', 'NWD_TIPO_NOTA', 'NWD_CALIFICACION', 'NWD_AUTORES', 'NWD_FECHA_PUBLICACION', 'NWD_DURACION', 'NWD_URL', 'NWD_TESTIGOS', 'NWD_MENU_LG_ID', 'NWD_TEMAPADRE_LG_ID', 'NWD_TEMAHIJO_LG_ID', 'NWD_MEDIO_LG_ID', 'NWD_MEDIO_LOGO'),
        Index('_dta_index_K_NEWSLETTER_DETALLE_5_1938105945__K2_1_3_5_6_7_8_9_10_11_12_13_14_15_16_17_18_19_20_21_22_23_24_25_26_9987', 'NWD_ID', 'NWD_NW_ID', 'NWD_NOTAID', 'NWD_NOMRE_MEDIO', 'NWD_TIPO_MEDIO', 'NWD_MENU_DISPLAY', 'NWD_MENU', 'NWD_TEMA', 'NWD_TEMA_DISPLAY', 'NWD_SECCION', 'NWD_PAGINA', 'NWD_COSTO', 'NWD_TITULO', 'NWD_TIPO_NOTA', 'NWD_CALIFICACION', 'NWD_AUTORES', 'NWD_FECHA_PUBLICACION', 'NWD_DURACION', 'NWD_URL', 'NWD_TESTIGOS', 'NWD_MENU_LG_ID', 'NWD_TEMAPADRE_LG_ID', 'NWD_TEMAHIJO_LG_ID', 'NWD_MEDIO_LG_ID', 'NWD_MEDIO_LOGO')
    )

    NWD_ID = Column(Integer, primary_key=True, index=True)
    NWD_NW_ID = Column(ForeignKey('K_NEWSLETTER.NW_ID'), nullable=False, index=True)
    NWD_NOTAID = Column(BigInteger, nullable=False)
    NWD_NOTA = Column(TEXT(2147483647, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    NWD_NOMRE_MEDIO = Column(Unicode(2000), nullable=False)
    NWD_TIPO_MEDIO = Column(Unicode(2000), nullable=False)
    NWD_MENU_DISPLAY = Column(Integer)
    NWD_MENU = Column(Unicode(2000))
    NWD_TEMA = Column(Unicode(2000))
    NWD_TEMA_DISPLAY = Column(Integer)
    NWD_SECCION = Column(Unicode(2000))
    NWD_PAGINA = Column(Unicode(2000))
    NWD_COSTO = Column(Unicode(2000))
    NWD_TITULO = Column(Unicode(2000))
    NWD_TIPO_NOTA = Column(Unicode(2000))
    NWD_CALIFICACION = Column(Unicode(2000))
    NWD_AUTORES = Column(Unicode(2000))
    NWD_FECHA_PUBLICACION = Column(DateTime)
    NWD_DURACION = Column(Unicode(2000))
    NWD_URL = Column(Unicode(2000))
    NWD_TESTIGOS = Column(String(8000, 'SQL_Latin1_General_CP1_CI_AS'))
    NWD_MENU_LG_ID = Column(Integer)
    NWD_TEMAPADRE_LG_ID = Column(Integer)
    NWD_TEMAHIJO_LG_ID = Column(Integer)
    NWD_MEDIO_LG_ID = Column(Integer)
    NWD_MEDIO_LOGO = Column(Unicode(2000))
    NWD_ORDEN = Column(Integer, nullable=False)

    K_NEWSLETTER = relationship('KNEWSLETTER')


class KRADIOGRABACION(Base):
    __tablename__ = 'K_RADIO_GRABACION'

    RG_ID = Column(Integer, primary_key=True)
    RG_ME_ID = Column(ForeignKey('C_MEDIO.ME_ID'), nullable=False)
    RG_SEC_ID = Column(ForeignKey('C_SECCION.SEC_ID'), nullable=False)
    RG_URL_STREAM = Column(String(collation='SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    RG_HORA_INICIO = Column(DateTime, nullable=False)
    RG_HORA_FIN = Column(DateTime, nullable=False)
    RG_INTERVALO_MINUTOS = Column(Integer, nullable=False)
    RG_LUNES = Column(BIT, nullable=False)
    RG_MARTES = Column(BIT, nullable=False)
    RG_MIERCOLES = Column(BIT, nullable=False)
    RG_JUEVES = Column(BIT, nullable=False)
    RG_VIERNES = Column(BIT, nullable=False)
    RG_SABADO = Column(BIT, nullable=False)
    RG_DOMINGO = Column(BIT, nullable=False)
    RG_CREADO = Column(DateTime, nullable=False)
    RG_STATUS = Column(Integer, nullable=False)

    C_MEDIO = relationship('CMEDIO')
    C_SECCION = relationship('CSECCION')


class KTESTIGO(Base):
    __tablename__ = 'K_TESTIGO'
    __table_args__ = (
        Index('_dta_index_K_TESTIGO_5_219147826_51856528_K5_K1', 'S_ID', 'S_PAGINA'),
        Index('_dta_index_K_TESTIGO_5_219147826_70952808_K10_K1_2_3_4_5_6_7_8_9', 'S_ID', 'S_NOMBRE', 'S_ME_ID', 'S_SEC_ID', 'S_PAGINA', 'S_DURACION', 'S_FECHA_PUBLICACION', 'S_PUBLICIDAD', 'S_USU_ID', 'S_RECORTE'),
        Index('_dta_index_K_TESTIGO_5_219147826__K3_K10_1_2_4_5_6_7_8_9_9987_4364_8066_1912_4149', 'S_ID', 'S_NOMBRE', 'S_ME_ID', 'S_SEC_ID', 'S_PAGINA', 'S_DURACION', 'S_FECHA_PUBLICACION', 'S_PUBLICIDAD', 'S_USU_ID', 'S_RECORTE'),
        Index('_dta_index_K_TESTIGO_5_219147826__K1_2_3_4_5_6_7_8_9_10_9987', 'S_ID', 'S_NOMBRE', 'S_ME_ID', 'S_SEC_ID', 'S_PAGINA', 'S_DURACION', 'S_FECHA_PUBLICACION', 'S_PUBLICIDAD', 'S_USU_ID', 'S_RECORTE'),
        Index('_dta_index_K_TESTIGO_5_219147826_70952808_K1_K10_2_3_4_5_6_7_8_9', 'S_ID', 'S_NOMBRE', 'S_ME_ID', 'S_SEC_ID', 'S_PAGINA', 'S_DURACION', 'S_FECHA_PUBLICACION', 'S_PUBLICIDAD', 'S_USU_ID', 'S_RECORTE'),
        Index('_dta_index_K_TESTIGO_5_219147826__K3_1_2_4_5_6_7_8_9_10_9987', 'S_ID', 'S_NOMBRE', 'S_ME_ID', 'S_SEC_ID', 'S_PAGINA', 'S_DURACION', 'S_FECHA_PUBLICACION', 'S_PUBLICIDAD', 'S_USU_ID', 'S_RECORTE'),
        Index('_dta_index_K_TESTIGO_5_219147826_49273456_K10_K4_K1_2_3_5_6_7_8_9', 'S_ID', 'S_NOMBRE', 'S_ME_ID', 'S_SEC_ID', 'S_PAGINA', 'S_DURACION', 'S_FECHA_PUBLICACION', 'S_PUBLICIDAD', 'S_USU_ID', 'S_RECORTE'),
        Index('_dta_index_K_TESTIGO_5_219147826__K4_K3_K9_9987_4364_8066', 'S_ME_ID', 'S_SEC_ID', 'S_USU_ID'),
        Index('_dta_index_K_TESTIGO_5_219147826__K10_K4_K1_2_3_5_6_7_8_9_9987', 'S_ID', 'S_NOMBRE', 'S_ME_ID', 'S_SEC_ID', 'S_PAGINA', 'S_DURACION', 'S_FECHA_PUBLICACION', 'S_PUBLICIDAD', 'S_USU_ID', 'S_RECORTE'),
        Index('_dta_index_K_TESTIGO_5_219147826__K3_1_2_4_5_6_7_8_9_10_9987_4364', 'S_ID', 'S_NOMBRE', 'S_ME_ID', 'S_SEC_ID', 'S_PAGINA', 'S_DURACION', 'S_FECHA_PUBLICACION', 'S_PUBLICIDAD', 'S_USU_ID', 'S_RECORTE'),
        Index('_dta_index_K_TESTIGO_5_219147826__K10_K1_2_3_4_5_6_7_8_9_9987_4364_8066_1912_4149_5201', 'S_ID', 'S_NOMBRE', 'S_ME_ID', 'S_SEC_ID', 'S_PAGINA', 'S_DURACION', 'S_FECHA_PUBLICACION', 'S_PUBLICIDAD', 'S_USU_ID', 'S_RECORTE'),
        Index('_dta_index_K_TESTIGO_5_219147826__K1_K10_K4_2_3_5_6_7_8_9_4364', 'S_ID', 'S_NOMBRE', 'S_ME_ID', 'S_SEC_ID', 'S_PAGINA', 'S_DURACION', 'S_FECHA_PUBLICACION', 'S_PUBLICIDAD', 'S_USU_ID', 'S_RECORTE'),
        Index('_dta_index_K_TESTIGO_5_219147826__K10_K1_2_3_4_5_6_7_8_9_9987_4364', 'S_ID', 'S_NOMBRE', 'S_ME_ID', 'S_SEC_ID', 'S_PAGINA', 'S_DURACION', 'S_FECHA_PUBLICACION', 'S_PUBLICIDAD', 'S_USU_ID', 'S_RECORTE'),
        Index('_dta_index_K_TESTIGO_5_219147826__K1_K10_2_3_4_5_6_7_8_9_6497', 'S_ID', 'S_NOMBRE', 'S_ME_ID', 'S_SEC_ID', 'S_PAGINA', 'S_DURACION', 'S_FECHA_PUBLICACION', 'S_PUBLICIDAD', 'S_USU_ID', 'S_RECORTE'),
        Index('_dta_index_K_TESTIGO_5_219147826__K3_K10_1_2_4_5_6_7_8_9_9987_4364_8066', 'S_ID', 'S_NOMBRE', 'S_ME_ID', 'S_SEC_ID', 'S_PAGINA', 'S_DURACION', 'S_FECHA_PUBLICACION', 'S_PUBLICIDAD', 'S_USU_ID', 'S_RECORTE'),
        Index('_dta_index_K_TESTIGO_5_219147826_51856808_K1_K10_K4_2_3_5_6_7_8_9', 'S_ID', 'S_NOMBRE', 'S_ME_ID', 'S_SEC_ID', 'S_PAGINA', 'S_DURACION', 'S_FECHA_PUBLICACION', 'S_PUBLICIDAD', 'S_USU_ID', 'S_RECORTE'),
        Index('_dta_index_K_TESTIGO_5_219147826__K1_K10_2_3_4_5_6_7_8_9_8066', 'S_ID', 'S_NOMBRE', 'S_ME_ID', 'S_SEC_ID', 'S_PAGINA', 'S_DURACION', 'S_FECHA_PUBLICACION', 'S_PUBLICIDAD', 'S_USU_ID', 'S_RECORTE'),
        Index('_dta_index_K_TESTIGO_5_219147826__K4_K3_K9', 'S_ME_ID', 'S_SEC_ID', 'S_USU_ID'),
        Index('_dta_index_K_TESTIGO_5_219147826_70952808_K1_2_3_4_5_6_7_8_9_10', 'S_ID', 'S_NOMBRE', 'S_ME_ID', 'S_SEC_ID', 'S_PAGINA', 'S_DURACION', 'S_FECHA_PUBLICACION', 'S_PUBLICIDAD', 'S_USU_ID', 'S_RECORTE'),
        Index('_dta_index_K_TESTIGO_5_219147826_49273456_K10_K1_2_3_4_5_6_7_8_9', 'S_ID', 'S_NOMBRE', 'S_ME_ID', 'S_SEC_ID', 'S_PAGINA', 'S_DURACION', 'S_FECHA_PUBLICACION', 'S_PUBLICIDAD', 'S_USU_ID', 'S_RECORTE'),
        Index('_dta_index_K_TESTIGO_5_219147826_51856808_K10_K4_K1_2_3_5_6_7_8_9', 'S_ID', 'S_NOMBRE', 'S_ME_ID', 'S_SEC_ID', 'S_PAGINA', 'S_DURACION', 'S_FECHA_PUBLICACION', 'S_PUBLICIDAD', 'S_USU_ID', 'S_RECORTE'),
        Index('_dta_index_K_TESTIGO_5_219147826__K1_2_3_4_5_6_7_8_9_10_9987_4364_8066_1912', 'S_ID', 'S_NOMBRE', 'S_ME_ID', 'S_SEC_ID', 'S_PAGINA', 'S_DURACION', 'S_FECHA_PUBLICACION', 'S_PUBLICIDAD', 'S_USU_ID', 'S_RECORTE'),
        Index('_dta_index_K_TESTIGO_5_219147826__K1_K5_2_3_4_6_7_8_9_10_4149', 'S_ID', 'S_NOMBRE', 'S_ME_ID', 'S_SEC_ID', 'S_PAGINA', 'S_DURACION', 'S_FECHA_PUBLICACION', 'S_PUBLICIDAD', 'S_USU_ID', 'S_RECORTE'),
        Index('_dta_index_K_TESTIGO_5_219147826__K10_K1_2_3_4_5_6_7_8_9_9987', 'S_ID', 'S_NOMBRE', 'S_ME_ID', 'S_SEC_ID', 'S_PAGINA', 'S_DURACION', 'S_FECHA_PUBLICACION', 'S_PUBLICIDAD', 'S_USU_ID', 'S_RECORTE'),
        Index('_dta_index_K_TESTIGO_5_219147826_49273456_K1_K10_2_3_4_5_6_7_8_9', 'S_ID', 'S_NOMBRE', 'S_ME_ID', 'S_SEC_ID', 'S_PAGINA', 'S_DURACION', 'S_FECHA_PUBLICACION', 'S_PUBLICIDAD', 'S_USU_ID', 'S_RECORTE'),
        Index('_dta_index_K_TESTIGO_5_219147826__K1_K10_2_3_4_5_6_7_8_9', 'S_ID', 'S_NOMBRE', 'S_ME_ID', 'S_SEC_ID', 'S_PAGINA', 'S_DURACION', 'S_FECHA_PUBLICACION', 'S_PUBLICIDAD', 'S_USU_ID', 'S_RECORTE'),
        Index('_dta_index_K_TESTIGO_5_219147826__K3_1_2_4_5_6_7_8_9_10_9987_4364_8066_1912', 'S_ID', 'S_NOMBRE', 'S_ME_ID', 'S_SEC_ID', 'S_PAGINA', 'S_DURACION', 'S_FECHA_PUBLICACION', 'S_PUBLICIDAD', 'S_USU_ID', 'S_RECORTE'),
        Index('_dta_index_K_TESTIGO_5_219147826__K1_K10_2_3_4_5_6_7_8_9_4364', 'S_ID', 'S_NOMBRE', 'S_ME_ID', 'S_SEC_ID', 'S_PAGINA', 'S_DURACION', 'S_FECHA_PUBLICACION', 'S_PUBLICIDAD', 'S_USU_ID', 'S_RECORTE'),
        Index('_dta_index_K_TESTIGO_5_219147826__K4_K3_K9_9987_4364', 'S_ME_ID', 'S_SEC_ID', 'S_USU_ID'),
        Index('_dta_index_K_TESTIGO_5_219147826__K1_K5_2_8576', 'S_ID', 'S_NOMBRE', 'S_PAGINA'),
        Index('_dta_index_K_TESTIGO_5_219147826_51856808_K10_K1_2_3_4_5_6_7_8_9', 'S_ID', 'S_NOMBRE', 'S_ME_ID', 'S_SEC_ID', 'S_PAGINA', 'S_DURACION', 'S_FECHA_PUBLICACION', 'S_PUBLICIDAD', 'S_USU_ID', 'S_RECORTE'),
        Index('_dta_index_K_TESTIGO_5_219147826__K4_K3_K9_9987_4364_8066_1912', 'S_ME_ID', 'S_SEC_ID', 'S_USU_ID'),
        Index('_dta_index_K_TESTIGO_5_219147826_51856808_K1_K10_2_3_4_5_6_7_8_9', 'S_ID', 'S_NOMBRE', 'S_ME_ID', 'S_SEC_ID', 'S_PAGINA', 'S_DURACION', 'S_FECHA_PUBLICACION', 'S_PUBLICIDAD', 'S_USU_ID', 'S_RECORTE'),
        Index('_dta_index_K_TESTIGO_5_219147826__K3_K10_1_2_4_5_6_7_8_9_9987_4364', 'S_ID', 'S_NOMBRE', 'S_ME_ID', 'S_SEC_ID', 'S_PAGINA', 'S_DURACION', 'S_FECHA_PUBLICACION', 'S_PUBLICIDAD', 'S_USU_ID', 'S_RECORTE'),
        Index('_dta_index_K_TESTIGO_5_219147826__K10_K1_2_3_4_5_6_7_8_9_9987_4364_8066_1912', 'S_ID', 'S_NOMBRE', 'S_ME_ID', 'S_SEC_ID', 'S_PAGINA', 'S_DURACION', 'S_FECHA_PUBLICACION', 'S_PUBLICIDAD', 'S_USU_ID', 'S_RECORTE'),
        Index('_dta_index_K_TESTIGO_5_219147826__K5_K1', 'S_ID', 'S_PAGINA'),
        Index('_dta_index_K_TESTIGO_5_219147826__K4_K3_K9_9987', 'S_ME_ID', 'S_SEC_ID', 'S_USU_ID'),
        Index('_dta_index_K_TESTIGO_5_219147826_49273456_K1_2_3_4_5_6_7_8_9_10', 'S_ID', 'S_NOMBRE', 'S_ME_ID', 'S_SEC_ID', 'S_PAGINA', 'S_DURACION', 'S_FECHA_PUBLICACION', 'S_PUBLICIDAD', 'S_USU_ID', 'S_RECORTE'),
        Index('_dta_index_K_TESTIGO_5_219147826__K1_K10_2_3_4_5_6_7_8_9_4149', 'S_ID', 'S_NOMBRE', 'S_ME_ID', 'S_SEC_ID', 'S_PAGINA', 'S_DURACION', 'S_FECHA_PUBLICACION', 'S_PUBLICIDAD', 'S_USU_ID', 'S_RECORTE'),
        Index('_dta_index_K_TESTIGO_5_219147826__K1_K5', 'S_ID', 'S_PAGINA'),
        Index('_dta_index_K_TESTIGO_5_219147826__K3_K10_1_2_4_5_6_7_8_9_9987', 'S_ID', 'S_NOMBRE', 'S_ME_ID', 'S_SEC_ID', 'S_PAGINA', 'S_DURACION', 'S_FECHA_PUBLICACION', 'S_PUBLICIDAD', 'S_USU_ID', 'S_RECORTE'),
        Index('_dta_index_K_TESTIGO_5_219147826__K1_2_3_4_5_6_7_8_9_10_9987_4364_8066', 'S_ID', 'S_NOMBRE', 'S_ME_ID', 'S_SEC_ID', 'S_PAGINA', 'S_DURACION', 'S_FECHA_PUBLICACION', 'S_PUBLICIDAD', 'S_USU_ID', 'S_RECORTE'),
        Index('_dta_index_K_TESTIGO_5_219147826__K1_2_3_4_5_6_7_8_9_10_9987_4364_8066_1912_4149', 'S_ID', 'S_NOMBRE', 'S_ME_ID', 'S_SEC_ID', 'S_PAGINA', 'S_DURACION', 'S_FECHA_PUBLICACION', 'S_PUBLICIDAD', 'S_USU_ID', 'S_RECORTE'),
        Index('_dta_index_K_TESTIGO_5_219147826__K5_K1_2', 'S_ID', 'S_NOMBRE', 'S_PAGINA'),
        Index('_dta_index_K_TESTIGO_5_219147826__K3_1_2_4_5_6_7_8_9_10_9987_4364_8066', 'S_ID', 'S_NOMBRE', 'S_ME_ID', 'S_SEC_ID', 'S_PAGINA', 'S_DURACION', 'S_FECHA_PUBLICACION', 'S_PUBLICIDAD', 'S_USU_ID', 'S_RECORTE'),
        Index('_dta_index_K_TESTIGO_5_219147826__K5_K1_9987_4364', 'S_ID', 'S_PAGINA'),
        Index('_dta_index_K_TESTIGO_5_219147826__K1_K5_2', 'S_ID', 'S_NOMBRE', 'S_PAGINA'),
        Index('_dta_index_K_TESTIGO_5_219147826__K5_K1_5543', 'S_ID', 'S_PAGINA'),
        Index('_dta_index_K_TESTIGO_5_219147826__K5_K1_2_8066', 'S_ID', 'S_NOMBRE', 'S_PAGINA'),
        Index('_dta_index_K_TESTIGO_5_219147826_100452352_K5_K1', 'S_ID', 'S_PAGINA'),
        Index('_dta_index_K_TESTIGO_5_219147826__K5_K1_2_3982', 'S_ID', 'S_NOMBRE', 'S_PAGINA'),
        Index('_dta_index_K_TESTIGO_5_219147826__K10_K4_K1_2_3_5_6_7_8_9_8066', 'S_ID', 'S_NOMBRE', 'S_ME_ID', 'S_SEC_ID', 'S_PAGINA', 'S_DURACION', 'S_FECHA_PUBLICACION', 'S_PUBLICIDAD', 'S_USU_ID', 'S_RECORTE'),
        Index('_dta_index_K_TESTIGO_5_219147826__K1_K5_7646', 'S_ID', 'S_PAGINA'),
        Index('_dta_index_K_TESTIGO_5_219147826__K1_K5_1912', 'S_ID', 'S_PAGINA'),
        Index('_dta_index_K_TESTIGO_5_219147826__K5_K1_114', 'S_ID', 'S_PAGINA'),
        Index('_dta_index_K_TESTIGO_5_219147826__K1_K10_K4_2_3_5_6_7_8_9_5201', 'S_ID', 'S_NOMBRE', 'S_ME_ID', 'S_SEC_ID', 'S_PAGINA', 'S_DURACION', 'S_FECHA_PUBLICACION', 'S_PUBLICIDAD', 'S_USU_ID', 'S_RECORTE'),
        Index('_dta_index_K_TESTIGO_5_219147826_93621328_K1_K5_2', 'S_ID', 'S_NOMBRE', 'S_PAGINA'),
        Index('_dta_index_K_TESTIGO_5_219147826__K1_K5_2_1377', 'S_ID', 'S_NOMBRE', 'S_PAGINA'),
        Index('_dta_index_K_TESTIGO_5_219147826_70952808_K1_K10_K4_2_3_5_6_7_8_9', 'S_ID', 'S_NOMBRE', 'S_ME_ID', 'S_SEC_ID', 'S_PAGINA', 'S_DURACION', 'S_FECHA_PUBLICACION', 'S_PUBLICIDAD', 'S_USU_ID', 'S_RECORTE'),
        Index('_dta_index_K_TESTIGO_5_219147826__K1_K5_2_4149', 'S_ID', 'S_NOMBRE', 'S_PAGINA'),
        Index('_dta_index_K_TESTIGO_5_219147826__K1_K5_4606', 'S_ID', 'S_PAGINA'),
        Index('_dta_index_K_TESTIGO_5_219147826__K3_1_2_4_5_6_7_8_9_10_9987_4364_8066_1912_4149', 'S_ID', 'S_NOMBRE', 'S_ME_ID', 'S_SEC_ID', 'S_PAGINA', 'S_DURACION', 'S_FECHA_PUBLICACION', 'S_PUBLICIDAD', 'S_USU_ID', 'S_RECORTE'),
        Index('_dta_index_K_TESTIGO_5_219147826_100452352_K1_K5_2', 'S_ID', 'S_NOMBRE', 'S_PAGINA'),
        Index('_dta_index_K_TESTIGO_5_219147826__K5_K1_2_4288', 'S_ID', 'S_NOMBRE', 'S_PAGINA'),
        Index('_dta_index_K_TESTIGO_5_219147826_49239816_K5_K1', 'S_ID', 'S_PAGINA'),
        Index('_dta_index_K_TESTIGO_5_219147826_104889936_K10_K1_2_3_4_5_6_7_8_9', 'S_ID', 'S_NOMBRE', 'S_ME_ID', 'S_SEC_ID', 'S_PAGINA', 'S_DURACION', 'S_FECHA_PUBLICACION', 'S_PUBLICIDAD', 'S_USU_ID', 'S_RECORTE'),
        Index('_dta_index_K_TESTIGO_5_219147826_70952808_K10_K4_K1_2_3_5_6_7_8_9', 'S_ID', 'S_NOMBRE', 'S_ME_ID', 'S_SEC_ID', 'S_PAGINA', 'S_DURACION', 'S_FECHA_PUBLICACION', 'S_PUBLICIDAD', 'S_USU_ID', 'S_RECORTE'),
        Index('_dta_index_K_TESTIGO_5_219147826__K10_K4_K1_2_3_5_6_7_8_9_9987_4364_8066', 'S_ID', 'S_NOMBRE', 'S_ME_ID', 'S_SEC_ID', 'S_PAGINA', 'S_DURACION', 'S_FECHA_PUBLICACION', 'S_PUBLICIDAD', 'S_USU_ID', 'S_RECORTE'),
        Index('_dta_index_K_TESTIGO_5_219147826_93621328_K5_K1_2', 'S_ID', 'S_NOMBRE', 'S_PAGINA'),
        Index('_dta_index_K_TESTIGO_5_219147826__K1_K10_K4_2_3_5_6_7_8_9_1912', 'S_ID', 'S_NOMBRE', 'S_ME_ID', 'S_SEC_ID', 'S_PAGINA', 'S_DURACION', 'S_FECHA_PUBLICACION', 'S_PUBLICIDAD', 'S_USU_ID', 'S_RECORTE'),
        Index('_dta_index_K_TESTIGO_5_219147826_104889936_K1_2_3_4_5_6_7_8_9_10', 'S_ID', 'S_NOMBRE', 'S_ME_ID', 'S_SEC_ID', 'S_PAGINA', 'S_DURACION', 'S_FECHA_PUBLICACION', 'S_PUBLICIDAD', 'S_USU_ID', 'S_RECORTE'),
        Index('_dta_index_K_TESTIGO_5_219147826_49239816_K1_K5_2', 'S_ID', 'S_NOMBRE', 'S_PAGINA'),
        Index('_dta_index_K_TESTIGO_5_219147826__K5_K1_9987', 'S_ID', 'S_PAGINA'),
        Index('_dta_index_K_TESTIGO_5_219147826__K4_K3_K9_9987_4364_8066_1912_4149', 'S_ME_ID', 'S_SEC_ID', 'S_USU_ID'),
        Index('_dta_index_K_TESTIGO_5_219147826_93621328_K1_K5', 'S_ID', 'S_PAGINA'),
        Index('_dta_index_K_TESTIGO_5_219147826__K3_K10_1_2_4_5_6_7_8_9', 'S_ID', 'S_NOMBRE', 'S_ME_ID', 'S_SEC_ID', 'S_PAGINA', 'S_DURACION', 'S_FECHA_PUBLICACION', 'S_PUBLICIDAD', 'S_USU_ID', 'S_RECORTE'),
        Index('_dta_index_K_TESTIGO_5_219147826__K5_K1_2_4364', 'S_ID', 'S_NOMBRE', 'S_PAGINA'),
        Index('_dta_index_K_TESTIGO_5_219147826_49240208_K5_K1_2', 'S_ID', 'S_NOMBRE', 'S_PAGINA'),
        Index('_dta_index_K_TESTIGO_5_219147826__K3_K10_1_2_4_5_6_7_8_9_9987_4364_8066_1912', 'S_ID', 'S_NOMBRE', 'S_ME_ID', 'S_SEC_ID', 'S_PAGINA', 'S_DURACION', 'S_FECHA_PUBLICACION', 'S_PUBLICIDAD', 'S_USU_ID', 'S_RECORTE'),
        Index('_dta_index_K_TESTIGO_5_219147826_100452352_K5_K1_2', 'S_ID', 'S_NOMBRE', 'S_PAGINA'),
        Index('_dta_index_K_TESTIGO_5_219147826__K10_K1_2_3_4_5_6_7_8_9', 'S_ID', 'S_NOMBRE', 'S_ME_ID', 'S_SEC_ID', 'S_PAGINA', 'S_DURACION', 'S_FECHA_PUBLICACION', 'S_PUBLICIDAD', 'S_USU_ID', 'S_RECORTE'),
        Index('_dta_index_K_TESTIGO_5_219147826__K1_K5_8066', 'S_ID', 'S_PAGINA'),
        Index('_dta_index_K_TESTIGO_5_219147826_49240208_K1_K5', 'S_ID', 'S_PAGINA'),
        Index('_dta_index_K_TESTIGO_5_219147826_104889936_K1_K10_2_3_4_5_6_7_8_9', 'S_ID', 'S_NOMBRE', 'S_ME_ID', 'S_SEC_ID', 'S_PAGINA', 'S_DURACION', 'S_FECHA_PUBLICACION', 'S_PUBLICIDAD', 'S_USU_ID', 'S_RECORTE'),
        Index('_dta_index_K_TESTIGO_5_219147826__K1_K5_2_1912', 'S_ID', 'S_NOMBRE', 'S_PAGINA'),
        Index('_dta_index_K_TESTIGO_5_219147826_100452352_K1_K5', 'S_ID', 'S_PAGINA'),
        Index('_dta_index_K_TESTIGO_5_219147826_49239816_K5_K1_2', 'S_ID', 'S_NOMBRE', 'S_PAGINA'),
        Index('_dta_index_K_TESTIGO_5_219147826__K10_K1_2_3_4_5_6_7_8_9_9987_4364_8066_1912_4149', 'S_ID', 'S_NOMBRE', 'S_ME_ID', 'S_SEC_ID', 'S_PAGINA', 'S_DURACION', 'S_FECHA_PUBLICACION', 'S_PUBLICIDAD', 'S_USU_ID', 'S_RECORTE'),
        Index('_dta_index_K_TESTIGO_5_219147826__K1_K10_2_3_4_5_6_7_8_9_5201', 'S_ID', 'S_NOMBRE', 'S_ME_ID', 'S_SEC_ID', 'S_PAGINA', 'S_DURACION', 'S_FECHA_PUBLICACION', 'S_PUBLICIDAD', 'S_USU_ID', 'S_RECORTE'),
        Index('_dta_index_K_TESTIGO_5_219147826_93621328_K5_K1', 'S_ID', 'S_PAGINA'),
        Index('_dta_index_K_TESTIGO_5_219147826__K1_2_3_4_5_6_7_8_9_10_9987_4364', 'S_ID', 'S_NOMBRE', 'S_ME_ID', 'S_SEC_ID', 'S_PAGINA', 'S_DURACION', 'S_FECHA_PUBLICACION', 'S_PUBLICIDAD', 'S_USU_ID', 'S_RECORTE'),
        Index('_dta_index_K_TESTIGO_5_219147826_70953536_K5_K1', 'S_ID', 'S_PAGINA'),
        Index('_dta_index_K_TESTIGO_5_219147826__K1_2_3_4_5_6_7_8_9_10', 'S_ID', 'S_NOMBRE', 'S_ME_ID', 'S_SEC_ID', 'S_PAGINA', 'S_DURACION', 'S_FECHA_PUBLICACION', 'S_PUBLICIDAD', 'S_USU_ID', 'S_RECORTE'),
        Index('_dta_index_K_TESTIGO_5_219147826_70952192_K1_K5_2', 'S_ID', 'S_NOMBRE', 'S_PAGINA'),
        Index('_dta_index_K_TESTIGO_5_219147826_51857368_K1_K5', 'S_ID', 'S_PAGINA'),
        Index('_dta_index_K_TESTIGO_5_219147826__K1_K5_2_3_4_6_7_8_9_10', 'S_ID', 'S_NOMBRE', 'S_ME_ID', 'S_SEC_ID', 'S_PAGINA', 'S_DURACION', 'S_FECHA_PUBLICACION', 'S_PUBLICIDAD', 'S_USU_ID', 'S_RECORTE'),
        Index('_dta_index_K_TESTIGO_5_219147826_70953536_K1_K5_2', 'S_ID', 'S_NOMBRE', 'S_PAGINA'),
        Index('_dta_index_K_TESTIGO_5_219147826__K1_2_3_4_5_6_7_8_9_10_9987_4364_8066_1912_4149_5201', 'S_ID', 'S_NOMBRE', 'S_ME_ID', 'S_SEC_ID', 'S_PAGINA', 'S_DURACION', 'S_FECHA_PUBLICACION', 'S_PUBLICIDAD', 'S_USU_ID', 'S_RECORTE'),
        Index('_dta_index_K_TESTIGO_5_219147826__K3_1_2_4_5_6_7_8_9_10', 'S_ID', 'S_NOMBRE', 'S_ME_ID', 'S_SEC_ID', 'S_PAGINA', 'S_DURACION', 'S_FECHA_PUBLICACION', 'S_PUBLICIDAD', 'S_USU_ID', 'S_RECORTE'),
        Index('_dta_index_K_TESTIGO_5_219147826__K3_1_2_4_5_6_7_8_9_10_9987_4364_8066_1912_4149_5201', 'S_ID', 'S_NOMBRE', 'S_ME_ID', 'S_SEC_ID', 'S_PAGINA', 'S_DURACION', 'S_FECHA_PUBLICACION', 'S_PUBLICIDAD', 'S_USU_ID', 'S_RECORTE'),
        Index('_dta_index_K_TESTIGO_5_219147826_70952192_K5_K1_2', 'S_ID', 'S_NOMBRE', 'S_PAGINA'),
        Index('_dta_index_K_TESTIGO_5_219147826_51857368_K5_K1', 'S_ID', 'S_PAGINA'),
        Index('_dta_index_K_TESTIGO_5_219147826_51856808_K1_2_3_4_5_6_7_8_9_10', 'S_ID', 'S_NOMBRE', 'S_ME_ID', 'S_SEC_ID', 'S_PAGINA', 'S_DURACION', 'S_FECHA_PUBLICACION', 'S_PUBLICIDAD', 'S_USU_ID', 'S_RECORTE'),
        Index('_dta_index_K_TESTIGO_5_219147826__K5_K1_9987_4364_8066', 'S_ID', 'S_PAGINA'),
        Index('_dta_index_K_TESTIGO_5_219147826_51856528_K1_K5_2', 'S_ID', 'S_NOMBRE', 'S_PAGINA'),
        Index('_dta_index_K_TESTIGO_5_219147826_70952192_K1_K5', 'S_ID', 'S_PAGINA'),
        Index('_dta_index_K_TESTIGO_5_219147826_49240208_K1_K5_2', 'S_ID', 'S_NOMBRE', 'S_PAGINA'),
        Index('_dta_index_K_TESTIGO_5_219147826__K5_K1_2_1912', 'S_ID', 'S_NOMBRE', 'S_PAGINA'),
        Index('_dta_index_K_TESTIGO_5_219147826_70953536_K5_K1_2', 'S_ID', 'S_NOMBRE', 'S_PAGINA'),
        Index('_dta_index_K_TESTIGO_5_219147826_51857368_K1_K5_2', 'S_ID', 'S_NOMBRE', 'S_PAGINA'),
        Index('_dta_index_K_TESTIGO_5_219147826__K1_K5_4149', 'S_ID', 'S_PAGINA'),
        Index('_dta_index_K_TESTIGO_5_219147826_49239816_K1_K5', 'S_ID', 'S_PAGINA'),
        Index('_dta_index_K_TESTIGO_5_219147826_70953536_K1_K5', 'S_ID', 'S_PAGINA'),
        Index('_dta_index_K_TESTIGO_5_219147826__K1_K5_2_5201', 'S_ID', 'S_NOMBRE', 'S_PAGINA'),
        Index('_dta_index_K_TESTIGO_5_219147826_51856528_K5_K1_2', 'S_ID', 'S_NOMBRE', 'S_PAGINA'),
        Index('_dta_index_K_TESTIGO_5_219147826_49240208_K5_K1', 'S_ID', 'S_PAGINA'),
        Index('_dta_index_K_TESTIGO_5_219147826_70952192_K5_K1', 'S_ID', 'S_PAGINA'),
        Index('_dta_index_K_TESTIGO_5_219147826__K10_K4_K1_2_3_5_6_7_8_9_9987_4364_8066_1912', 'S_ID', 'S_NOMBRE', 'S_ME_ID', 'S_SEC_ID', 'S_PAGINA', 'S_DURACION', 'S_FECHA_PUBLICACION', 'S_PUBLICIDAD', 'S_USU_ID', 'S_RECORTE'),
        Index('_dta_index_K_TESTIGO_5_219147826_51856528_K1_K5', 'S_ID', 'S_PAGINA'),
        Index('_dta_index_K_TESTIGO_5_219147826__K10_K4_K1_2_3_5_6_7_8_9_9987_4364', 'S_ID', 'S_NOMBRE', 'S_ME_ID', 'S_SEC_ID', 'S_PAGINA', 'S_DURACION', 'S_FECHA_PUBLICACION', 'S_PUBLICIDAD', 'S_USU_ID', 'S_RECORTE'),
        Index('_dta_index_K_TESTIGO_5_219147826__K10_K1_2_3_4_5_6_7_8_9_9987_4364_8066', 'S_ID', 'S_NOMBRE', 'S_ME_ID', 'S_SEC_ID', 'S_PAGINA', 'S_DURACION', 'S_FECHA_PUBLICACION', 'S_PUBLICIDAD', 'S_USU_ID', 'S_RECORTE'),
        Index('_dta_index_K_TESTIGO_5_219147826__K1_K10_K4_2_3_5_6_7_8_9_4149', 'S_ID', 'S_NOMBRE', 'S_ME_ID', 'S_SEC_ID', 'S_PAGINA', 'S_DURACION', 'S_FECHA_PUBLICACION', 'S_PUBLICIDAD', 'S_USU_ID', 'S_RECORTE'),
        Index('_dta_index_K_TESTIGO_5_219147826__K1_K10_K4_2_3_5_6_7_8_9_8066', 'S_ID', 'S_NOMBRE', 'S_ME_ID', 'S_SEC_ID', 'S_PAGINA', 'S_DURACION', 'S_FECHA_PUBLICACION', 'S_PUBLICIDAD', 'S_USU_ID', 'S_RECORTE'),
        Index('_dta_index_K_TESTIGO_5_219147826_51857368_K5_K1_2', 'S_ID', 'S_NOMBRE', 'S_PAGINA'),
        Index('_dta_index_K_TESTIGO_5_219147826__K1_K10_2_3_4_5_6_7_8_9_1912', 'S_ID', 'S_NOMBRE', 'S_ME_ID', 'S_SEC_ID', 'S_PAGINA', 'S_DURACION', 'S_FECHA_PUBLICACION', 'S_PUBLICIDAD', 'S_USU_ID', 'S_RECORTE'),
        Index('_dta_index_K_TESTIGO_5_219147826__K4_K3_K9_9987_4364_8066_1912_4149_5201', 'S_ME_ID', 'S_SEC_ID', 'S_USU_ID'),
        Index('_dta_index_K_TESTIGO_5_219147826_49273456_K1_K10_K4_2_3_5_6_7_8_9', 'S_ID', 'S_NOMBRE', 'S_ME_ID', 'S_SEC_ID', 'S_PAGINA', 'S_DURACION', 'S_FECHA_PUBLICACION', 'S_PUBLICIDAD', 'S_USU_ID', 'S_RECORTE'),
        Index('_dta_index_K_TESTIGO_5_219147826__K1_K10_K4_2_3_5_6_7_8_9', 'S_ID', 'S_NOMBRE', 'S_ME_ID', 'S_SEC_ID', 'S_PAGINA', 'S_DURACION', 'S_FECHA_PUBLICACION', 'S_PUBLICIDAD', 'S_USU_ID', 'S_RECORTE'),
        Index('_dta_index_K_TESTIGO_5_219147826__K10_K4_K1_2_3_5_6_7_8_9', 'S_ID', 'S_NOMBRE', 'S_ME_ID', 'S_SEC_ID', 'S_PAGINA', 'S_DURACION', 'S_FECHA_PUBLICACION', 'S_PUBLICIDAD', 'S_USU_ID', 'S_RECORTE'),
        Index('_dta_index_K_TESTIGO_5_219147826_104889936_K1_K10_K4_2_3_5_6_7_8_9', 'S_ID', 'S_NOMBRE', 'S_ME_ID', 'S_SEC_ID', 'S_PAGINA', 'S_DURACION', 'S_FECHA_PUBLICACION', 'S_PUBLICIDAD', 'S_USU_ID', 'S_RECORTE'),
        Index('_dta_index_K_TESTIGO_5_219147826_104889936_K10_K4_K1_2_3_5_6_7_8_9', 'S_ID', 'S_NOMBRE', 'S_ME_ID', 'S_SEC_ID', 'S_PAGINA', 'S_DURACION', 'S_FECHA_PUBLICACION', 'S_PUBLICIDAD', 'S_USU_ID', 'S_RECORTE')
    )

    S_ID = Column(BigInteger, primary_key=True, index=True)
    S_NOMBRE = Column(String(5000, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    S_ME_ID = Column(ForeignKey('C_MEDIO.ME_ID'))
    S_SEC_ID = Column(ForeignKey('C_SECCION.SEC_ID'))
    S_PAGINA = Column(String(100, 'SQL_Latin1_General_CP1_CI_AS'))
    S_DURACION = Column(String(100, 'SQL_Latin1_General_CP1_CI_AS'))
    S_FECHA_PUBLICACION = Column(DateTime, nullable=False)
    S_PUBLICIDAD = Column(Integer)
    S_USU_ID = Column(BigInteger)
    S_RECORTE = Column(BIT, nullable=False, index=True)
    S_IA_ST = Column(Integer)
    S_IA_TEXT = Column(TEXT(2147483647, 'SQL_Latin1_General_CP1_CI_AS'))

    C_MEDIO = relationship('CMEDIO')
    C_SECCION = relationship('CSECCION')


class KTVGRABACION(Base):
    __tablename__ = 'K_TV_GRABACION'

    RG_ID = Column(Integer, primary_key=True)
    RG_ME_ID = Column(ForeignKey('C_MEDIO.ME_ID'), nullable=False)
    RG_SEC_ID = Column(ForeignKey('C_SECCION.SEC_ID'), nullable=False)
    RG_URL_STREAM = Column(String(collation='SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    RG_HORA_INICIO = Column(DateTime, nullable=False)
    RG_HORA_FIN = Column(DateTime, nullable=False)
    RG_INTERVALO_MINUTOS = Column(Integer, nullable=False)
    RG_LUNES = Column(BIT, nullable=False)
    RG_MARTES = Column(BIT, nullable=False)
    RG_MIERCOLES = Column(BIT, nullable=False)
    RG_JUEVES = Column(BIT, nullable=False)
    RG_VIERNES = Column(BIT, nullable=False)
    RG_SABADO = Column(BIT, nullable=False)
    RG_DOMINGO = Column(BIT, nullable=False)
    RG_CREADO = Column(DateTime, nullable=False)
    RG_STATUS = Column(Integer, nullable=False)

    C_MEDIO = relationship('CMEDIO')
    C_SECCION = relationship('CSECCION')


class KNOTA(Base):
    __tablename__ = 'K_NOTA'
    __table_args__ = (
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K20_K25_K4_K6_1_3_5_14_21_28_29', 'N_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_AUTOR1', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_VISIBLE', 'N_URL', 'N_COSTO'),
        Index('_dta_index_K_NOTA_5_2030630277_82397080_K1_K4_K25_K5_2_3_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K5_K4_K25_K1_K2_K3_K6_K7_K14_15_16_17_20_21_22_23_24_26_27_28_29_30_4467', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K4_K6_K20_K25_1_3_5_14_21_28_29_6321', 'N_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_AUTOR1', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_VISIBLE', 'N_URL', 'N_COSTO'),
        Index('_dta_index_K_NOTA_5_2030630277_51856808_K4_K1', 'N_ID', 'N_ME_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_93620880_K20_K25_K5_K6_K4_K1_3_14_21_28_29', 'N_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_AUTOR1', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_VISIBLE', 'N_URL', 'N_COSTO'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K4_K25_K5_K1_2_3_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_93620880_K20_K25_K6', 'N_SEC_ID', 'N_FECHA_CAPTURA', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277__K4_K1_9987', 'N_ID', 'N_ME_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_93620880_K4_K20_K25_K6_K5_K1_3_14_21_28_29', 'N_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_AUTOR1', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_VISIBLE', 'N_URL', 'N_COSTO'),
        Index('_dta_index_K_NOTA_5_2030630277__K1_K4_K25_K5', 'N_ID', 'N_ME_ID', 'N_TN_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277__K1_K4_1912', 'N_ID', 'N_ME_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_93614016_K6_K20_K25', 'N_SEC_ID', 'N_FECHA_CAPTURA', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_93614016_K20_K25_K5_K6_K4_K1_3_14_21_28_29', 'N_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_AUTOR1', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_VISIBLE', 'N_URL', 'N_COSTO'),
        Index('_dta_index_K_NOTA_5_2030630277__K4_K25_K5_K1', 'N_ID', 'N_ME_ID', 'N_TN_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_106796256_K1_K2_K3_K4_K5_K6_K7_K14_15_16_17_20_21_22_23_24_25_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K25_K1_K5_K4_K2_K3_K6_K7_K14_15_16_17_20_21_22_23_24_26_27_28_29_30_1473', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K1_2533', 'N_ID', 'N_TN_ID'),
        Index('_dta_index_K_NOTA_5_2030630277__K4_K25_K1_1912', 'N_ID', 'N_ME_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_93614016_K4_K20_K25_K6_K5_K1_3_14_21_28_29', 'N_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_AUTOR1', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_VISIBLE', 'N_URL', 'N_COSTO'),
        Index('_dta_index_K_NOTA_5_2030630277_82397080_K1_K4_K25_K5', 'N_ID', 'N_ME_ID', 'N_TN_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_93614016_K4_K6_K20_K25_1_3_5_14_21_28_29', 'N_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_AUTOR1', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_VISIBLE', 'N_URL', 'N_COSTO'),
        Index('_dta_index_K_NOTA_5_2030630277_106796312_K5_K4_K25_K1_K2_K3_K6_K7_K14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_51856808_K1_K25_K4_2_3_5_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K20_K25_K6_1653', 'N_ID', 'N_SEC_ID', 'N_FECHA_CAPTURA', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K20_K25_K5_K6_K4_K1_3_14_21_28_29', 'N_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_AUTOR1', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_VISIBLE', 'N_URL', 'N_COSTO'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K4_K25_K5_K1', 'N_ID', 'N_ME_ID', 'N_TN_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_51856808_K2_K1_K20_3_4_5_6_7_14_15_16_17_21_22_23_24_25_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K4_K6_K20_K25_9649', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_FECHA_CAPTURA', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K1_K20_K25', 'N_ID', 'N_SEC_ID', 'N_FECHA_CAPTURA', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_51856808_K5_K1', 'N_ID', 'N_TN_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K20_K25_K6_K4_K5_K1_3_14_21_28_29_4829', 'N_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_AUTOR1', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_VISIBLE', 'N_URL', 'N_COSTO'),
        Index('_dta_index_K_NOTA_5_2030630277_82397080_K4_K25_K5_K1', 'N_ID', 'N_ME_ID', 'N_TN_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K1_1771', 'N_ID', 'N_SEC_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_51856808_K5_K4_K25_K1_2_3_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K20_K25_K1_K6_K4_K5_3_14_21_28_29_6241', 'N_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_AUTOR1', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_VISIBLE', 'N_URL', 'N_COSTO'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K4_K6_K20_K25_1_3_5_14_21_28_29_3370', 'N_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_AUTOR1', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_VISIBLE', 'N_URL', 'N_COSTO'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K1_K4_K25_K5', 'N_ID', 'N_ME_ID', 'N_TN_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_51856808_K5_K4_K25_K1_2_3_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30_8066', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K20_K25_K5_9073', 'N_TN_ID', 'N_FECHA_CAPTURA', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_93620880_K20_K25_K4', 'N_ME_ID', 'N_FECHA_CAPTURA', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K4_K1_K5_K7_K6_K3_2_14_15_16_17_20_21_22_23_24_25_26_27_28_29_30_5201', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_51856808_K2_K1_K20_3_4_5_6_7_14_15_16_17_21_22_23_24_25_26_27_28_29_30_1912', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K25_K6_K4_K5_K1_K20_3_14_21_28_29_3227', 'N_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_AUTOR1', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_VISIBLE', 'N_URL', 'N_COSTO'),
        Index('_dta_index_K_NOTA_5_2030630277__K5_K1_K25_K4_2_3_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_93620880_K4_K6_K20_K25_K5_K1_3_14_21_28_29', 'N_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_AUTOR1', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_VISIBLE', 'N_URL', 'N_COSTO'),
        Index('_dta_index_K_NOTA_5_2030630277__K1_K25_2_3_5_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30_9987', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K4_K6_K20_K25_K5_K1_3_14_21_28_29_9437', 'N_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_AUTOR1', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_VISIBLE', 'N_URL', 'N_COSTO'),
        Index('_dta_index_K_NOTA_5_2030630277_82397080_K5_K1_K25_K4_2_3_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_106796536_K1_K5_K4_K25_K2_K3_K6_K7_K14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_93620880_K20_K25_K6_K4_K5_K1_3_14_21_28_29', 'N_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_AUTOR1', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_VISIBLE', 'N_URL', 'N_COSTO'),
        Index('_dta_index_K_NOTA_5_2030630277_51856808_K25', 'N_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K20_K25_9912', 'N_TN_ID', 'N_FECHA_CAPTURA', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K5_K1_K25_K4_2_3_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_93614016_K1_K20_K25', 'N_ID', 'N_FECHA_CAPTURA', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_51856808_K25_K1_K4_2_3_5_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277__K5_K25', 'N_TN_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K20_812', 'N_TN_ID', 'N_FECHA_CAPTURA'),
        Index('_dta_index_K_NOTA_5_2030630277_97758080_K5_K4_K25_K1_K2', 'N_ID', 'N_USU_ID', 'N_ME_ID', 'N_TN_ID', 'N_AUTOR4', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_51856808_K4_K1_K25_2_3_5_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K4_K6_K20_K25_5737', 'N_ME_ID', 'N_SEC_ID', 'N_FECHA_CAPTURA', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K5_K25', 'N_ID', 'N_TN_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K6_K20_K25_7241', 'N_TN_ID', 'N_SEC_ID', 'N_FECHA_CAPTURA', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K20_K25_K6_K4_K5_K1_3_14_21_28_29_8953', 'N_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_AUTOR1', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_VISIBLE', 'N_URL', 'N_COSTO'),
        Index('_dta_index_K_NOTA_5_2030630277_82397080_K5_K25', 'N_TN_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K1_K2_K3_K4_K5_K6_K7_K14_15_16_17_20_21_22_23_24_25_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K20_K25_K4_K6_1_3_5_14_21_28_29_7271', 'N_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_AUTOR1', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_VISIBLE', 'N_URL', 'N_COSTO'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K4_K6_K20_K25_1_3_5_14_21_28_29_506', 'N_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_AUTOR1', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_VISIBLE', 'N_URL', 'N_COSTO'),
        Index('_dta_index_K_NOTA_5_2030630277__K2_K4_20', 'N_USU_ID', 'N_ME_ID', 'N_FECHA_CAPTURA'),
        Index('_dta_index_K_NOTA_5_2030630277_82397080_K1_K2_K3_K4_K5_K6_K7_K14_15_16_17_20_21_22_23_24_25_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_93614016_K20_K25', 'N_FECHA_CAPTURA', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K5_K20_K25_786', 'N_ID', 'N_TN_ID', 'N_FECHA_CAPTURA', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277__K4_K2_20', 'N_USU_ID', 'N_ME_ID', 'N_FECHA_CAPTURA'),
        Index('_dta_index_K_NOTA_5_2030630277_93614016_K20_K25_K4_K6_1_3_5_14_21_28_29', 'N_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_AUTOR1', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_VISIBLE', 'N_URL', 'N_COSTO'),
        Index('_dta_index_K_NOTA_5_2030630277__K2_4_20', 'N_USU_ID', 'N_ME_ID', 'N_FECHA_CAPTURA'),
        Index('_dta_index_K_NOTA_5_2030630277_93620880_K20_K25_K4_K6_K5_K1_3_14_21_28_29', 'N_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_AUTOR1', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_VISIBLE', 'N_URL', 'N_COSTO'),
        Index('_dta_index_K_NOTA_5_2030630277_93620880_K1_K20_K25', 'N_ID', 'N_FECHA_CAPTURA', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K2', 'N_USU_ID', 'N_ME_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_93614016_K5_K20_K25_K6_K4_K1_3_14_21_28_29', 'N_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_AUTOR1', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_VISIBLE', 'N_URL', 'N_COSTO'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K1_K2_K5_K4_K25_K3_K6_K7_K14_15_16_17_20_21_22_23_24_26_27_28_29_30_7894', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K20_K25_K1_K6_K4_K5_3_14_21_28_29_4120', 'N_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_AUTOR1', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_VISIBLE', 'N_URL', 'N_COSTO'),
        Index('_dta_index_K_NOTA_5_2030630277_93614016_K6_K20_K25_K4_K5_K1_3_14_21_28_29', 'N_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_AUTOR1', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_VISIBLE', 'N_URL', 'N_COSTO'),
        Index('_dta_index_K_NOTA_5_2030630277_105562056_K5_K4_K25_K1_K2', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K20_K25_K5_3088', 'N_ME_ID', 'N_TN_ID', 'N_FECHA_CAPTURA', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_93614016_K20_K25_K4_K6', 'N_ME_ID', 'N_SEC_ID', 'N_FECHA_CAPTURA', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K2_K4_20', 'N_USU_ID', 'N_ME_ID', 'N_FECHA_CAPTURA'),
        Index('_dta_index_K_NOTA_5_2030630277_105562056_K4', 'N_AG_ID', 'N_ME_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K25_K6_K4_K5_K1_K20_3_14_21_28_29_1623', 'N_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_AUTOR1', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_VISIBLE', 'N_URL', 'N_COSTO'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K1_2_3_4_5_6_7_14_15_16_17_20_21_22_23_24_25_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K2_K4_20_4364', 'N_USU_ID', 'N_ME_ID', 'N_FECHA_CAPTURA'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K4_K6_K20_K25_K5_K1_3_14_21_28_29_2735', 'N_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_AUTOR1', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_VISIBLE', 'N_URL', 'N_COSTO'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K20_K25_5150', 'N_ME_ID', 'N_FECHA_CAPTURA', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K4_K2_20', 'N_USU_ID', 'N_ME_ID', 'N_FECHA_CAPTURA'),
        Index('_dta_index_K_NOTA_5_2030630277__K25_1_2_3_4_5_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K4_K1_K5_K7_K6_K3_2_14_15_16_17_20_21_22_23_24_25_26_27_28_29_30_6497', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K1_K2_K5_K4_K25_K3_K6_K7_K14_15_16_17_20_21_22_23_24_26_27_28_29_30_2527', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K20_7946', 'N_ME_ID', 'N_FECHA_CAPTURA'),
        Index('_dta_index_K_NOTA_5_2030630277_82397080_K25_1_2_3_4_5_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K4_8066', 'N_USU_ID', 'N_ME_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_106795752_K4_K1_K5_K25_K2_K3_K6_K7_K14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277__K5_K1', 'N_ID', 'N_TN_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K6_K20_K25_2562', 'N_ME_ID', 'N_SEC_ID', 'N_FECHA_CAPTURA', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K4_K2_20_1912', 'N_USU_ID', 'N_ME_ID', 'N_FECHA_CAPTURA'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K25_K1_K5_K4_K2_K3_K6_K7_K14_15_16_17_20_21_22_23_24_26_27_28_29_30_3997', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277__K1_K5', 'N_ID', 'N_TN_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K1_K2_K5_K4_K25_K3_K6_K7_K14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_106795752_K1_K2_K3_K4_K5_K6_K7_K14_15_16_17_20_21_22_23_24_25_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K20_K25_K4_K6_1_3_5_14_21_28_29_5315', 'N_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_AUTOR1', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_VISIBLE', 'N_URL', 'N_COSTO'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K5', 'N_ID', 'N_TN_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K2_4_20', 'N_USU_ID', 'N_ME_ID', 'N_FECHA_CAPTURA'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K4_K6_K20_K25', 'N_ID', 'N_ME_ID', 'N_SEC_ID', 'N_FECHA_CAPTURA', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K1_K5', 'N_ID', 'N_TN_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K5_K4_K25_K1_K2_K3_K6_K7_K14_15_16_17_20_21_22_23_24_26_27_28_29_30_1653', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K2_4_20_4149', 'N_USU_ID', 'N_ME_ID', 'N_FECHA_CAPTURA'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K1_K5_K4_K25_2920', 'N_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K20_K25_K6_K4_K5_K1_3_14_21_28_29', 'N_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_AUTOR1', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_VISIBLE', 'N_URL', 'N_COSTO'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K5_K1', 'N_ID', 'N_TN_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K1_K2_K3_K4_K5_K6_K7_K14_15_16_17_20_21_22_23_24_25_26_27_28_29_30_8843', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K4_K1_1040', 'N_ID', 'N_ME_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K4_K6_K20_K25_1_3_5_14_21_28_29', 'N_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_AUTOR1', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_VISIBLE', 'N_URL', 'N_COSTO'),
        Index('_dta_index_K_NOTA_5_2030630277__K6_1', 'N_ID', 'N_SEC_ID'),
        Index('_dta_index_K_NOTA_5_2030630277__K4_K2_K6_20', 'N_USU_ID', 'N_ME_ID', 'N_SEC_ID', 'N_FECHA_CAPTURA'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K25', 'N_SEC_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277__K2_4_6_20', 'N_USU_ID', 'N_ME_ID', 'N_SEC_ID', 'N_FECHA_CAPTURA'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K1_K2_K3_K4_K5_K6_K7_K14_15_16_17_20_21_22_23_24_25_26_27_28_29_30_2669', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_106796312_K1_K2_K3_K4_K5_K6_K7_K14_15_16_17_20_21_22_23_24_25_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K20_K25_K5_K6_K4_K1_3_14_21_28_29_5420', 'N_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_AUTOR1', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_VISIBLE', 'N_URL', 'N_COSTO'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K6_1', 'N_ID', 'N_SEC_ID'),
        Index('_dta_index_K_NOTA_5_2030630277__K2_K6_K4_20', 'N_USU_ID', 'N_ME_ID', 'N_SEC_ID', 'N_FECHA_CAPTURA'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K4_K1_K5_K25_K2_K3_K6_K7_K14_15_16_17_20_21_22_23_24_26_27_28_29_30_8597', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K1_K20_K25_508', 'N_ID', 'N_TN_ID', 'N_FECHA_CAPTURA', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277__K6_K2_K4_20', 'N_USU_ID', 'N_ME_ID', 'N_SEC_ID', 'N_FECHA_CAPTURA'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K25_K1_K5_K4_K2_K3_K6_K7_K14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K4_9987_4364', 'N_ME_ID', 'N_SEC_ID'),
        Index('_dta_index_K_NOTA_5_2030630277__K5_K4_K1_2_3_6_7_14_15_16_17_20_21_22_23_24_25_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K5_K25_K4_K1_2_3_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K2_K4_K6_K7_K3_K5_1', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K5_K6_8809', 'N_TN_ID', 'N_SEC_ID'),
        Index('_dta_index_K_NOTA_5_2030630277__K4_K1_K5_2_3_6_7_14_15_16_17_20_21_22_23_24_25_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K5_K4_K25_K1', 'N_ID', 'N_ME_ID', 'N_TN_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K2_4_6_20', 'N_USU_ID', 'N_ME_ID', 'N_SEC_ID', 'N_FECHA_CAPTURA'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K6_K4_K2_K7_K3_K5_1_5201', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K1_K5_K4_2_3_6_7_14_15_16_17_20_21_22_23_24_25_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K5_K4_K1_K6_2_3_7_14_15_16_17_20_21_22_23_24_25_26_27_28_29_30_9953', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K2_K4_K6_K7_K3_K5_1_6497', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K4_K1_K5_K25_2_3_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K4_K2_K6_20', 'N_USU_ID', 'N_ME_ID', 'N_SEC_ID', 'N_FECHA_CAPTURA'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K4_K1_K5_2_3_6_7_14_15_16_17_20_21_22_23_24_25_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K5_K6_9910', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K4_1040', 'N_ME_ID', 'N_TN_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_82397080_K4_K1_K5_K25_2_3_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K4_K5_K1', 'N_ID', 'N_ME_ID', 'N_TN_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K6_8066', 'N_ME_ID', 'N_SEC_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K25_K1_K5_K4_2_3_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K5_K4_K1_K6_2_3_7_14_15_16_17_20_21_22_23_24_25_26_27_28_29_30_6221', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K2_K4_K6_K7_K3_K5_1_1771', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K4_K5_K1_2_3_6_7_14_15_16_17_20_21_22_23_24_25_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_82397080_K1_K5_K25_K4_2_3_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K2_4_6_20_1912', 'N_USU_ID', 'N_ME_ID', 'N_SEC_ID', 'N_FECHA_CAPTURA'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K4_K5', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K5_K4_K2_K6_K7_K3_1', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K5_K4_K1_2_3_6_7_14_15_16_17_20_21_22_23_24_25_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_82397080_K5_K4_K25_K1_2_3_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K1_K5_K6_K4_2_3_7_14_15_16_17_20_21_22_23_24_25_26_27_28_29_30_4683', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K5_K4_K2_K6_K7_K3_1_2533', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K4_K2_K6_20_4149', 'N_USU_ID', 'N_ME_ID', 'N_SEC_ID', 'N_FECHA_CAPTURA'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K5_K4_K1', 'N_ID', 'N_ME_ID', 'N_TN_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_82397080_K1_K5_K4_K25', 'N_ID', 'N_ME_ID', 'N_TN_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K4_K5_4288', 'N_ME_ID', 'N_TN_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K2_K4_K6_K7_K3_K5_1_8258', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K6_5201', 'N_USU_ID', 'N_SEC_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K5_K4_K2_K6_K7_K3_1_1410', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID'),
        Index('_dta_index_K_NOTA_5_2030630277__K1_K2_K5_K4_K25_K3_K6_K7_K14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K5_K4_K25_K1_2_3_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K4_K5_3982', 'N_ME_ID', 'N_TN_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K2_4_6_20_6497', 'N_USU_ID', 'N_ME_ID', 'N_SEC_ID', 'N_FECHA_CAPTURA'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K4_K2_K6_K7_K3_K5_1', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID'),
        Index('_dta_index_K_NOTA_5_2030630277__K25_K1_K5_K4_K2_K3_K6_K7_K14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_82397080_K5_K4_K25', 'N_ME_ID', 'N_TN_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K5_K6_3928', 'N_ID', 'N_TN_ID', 'N_SEC_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K4_K2_K6_K7_K3_K5_1_2894', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID'),
        Index('_dta_index_K_NOTA_5_2030630277__K1_K2_K5_K4_K25', 'N_ID', 'N_USU_ID', 'N_ME_ID', 'N_TN_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K6_K2_K4_20', 'N_USU_ID', 'N_ME_ID', 'N_SEC_ID', 'N_FECHA_CAPTURA'),
        Index('_dta_index_K_NOTA_5_2030630277_97758080_K5_K4_K25_K1', 'N_ID', 'N_ME_ID', 'N_TN_ID', 'N_AUTOR4', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K5_K4_K25', 'N_ID', 'N_ME_ID', 'N_TN_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K5_K4_K2_K6_K7_K3_1_4864', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID'),
        Index('_dta_index_K_NOTA_5_2030630277__K1_K5_K4_K25_K2_K3_K6_K7_K14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K5_K4_K1_K6_2_3_7_14_15_16_17_20_21_22_23_24_25_26_27_28_29_30_8337', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K2_K6_K4_20', 'N_USU_ID', 'N_ME_ID', 'N_SEC_ID', 'N_FECHA_CAPTURA'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K4_K2_K6_K7_K3_K5_1_6960', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID'),
        Index('_dta_index_K_NOTA_5_2030630277__K5_K4_K25_K1_K2', 'N_ID', 'N_USU_ID', 'N_ME_ID', 'N_TN_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277__K25_K1_2_3_5_6_7_14_15_16_17_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K4_K5_3369', 'N_ID', 'N_ME_ID', 'N_TN_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K6_9850', 'N_TN_ID', 'N_SEC_ID'),
        Index('_dta_index_K_NOTA_5_2030630277__K5_K4_K25_K1_K2_K3_K6_K7_K14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277__K1_K25_2_3_5_6_7_14_15_16_17_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K4_K2_K6_20_1040', 'N_USU_ID', 'N_ME_ID', 'N_SEC_ID', 'N_FECHA_CAPTURA'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K5_5492', 'N_TN_ID', 'N_SEC_ID'),
        Index('_dta_index_K_NOTA_5_2030630277__K1_K2_K3_K4_K5_K6_K7_K14_15_16_17_20_21_22_23_24_25_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277__K4_K1_K25_2_3_5_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K6_K2_K4_20_1771', 'N_USU_ID', 'N_ME_ID', 'N_SEC_ID', 'N_FECHA_CAPTURA'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K4_K2_K6_K7_K3_K5_1_9085', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID'),
        Index('_dta_index_K_NOTA_5_2030630277__K4_K1_K5_K25_K2_K3_K6_K7_K14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277__K1_K25_K4_2_3_5_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K2_K6_K4_20_2533', 'N_USU_ID', 'N_ME_ID', 'N_SEC_ID', 'N_FECHA_CAPTURA'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K5_6355', 'N_TN_ID', 'N_SEC_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_97757800_K5', 'N_TN_ID', 'N_AUTOR1'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K25_K1', 'N_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K6_K2_K4_20_8258', 'N_USU_ID', 'N_ME_ID', 'N_SEC_ID', 'N_FECHA_CAPTURA'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K1_K5_9429', 'N_ID', 'N_TN_ID', 'N_SEC_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_106795752_K5_K4_K25_K1_K2_K3_K6_K7_K14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K1_K5_K4_K25_1937', 'N_ID', 'N_ME_ID', 'N_TN_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K1_20', 'N_ID', 'N_FECHA_CAPTURA'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K2_K6_K4_20_1410', 'N_USU_ID', 'N_ME_ID', 'N_SEC_ID', 'N_FECHA_CAPTURA'),
        Index('_dta_index_K_NOTA_5_2030630277_97758080_K5', 'N_TN_ID', 'N_AUTOR4'),
        Index('_dta_index_K_NOTA_5_2030630277_106796256_K5_K4_K25_K1_K2_K3_K6_K7_K14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K25_K1_2_3_5_6_7_14_15_16_17_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K2_2894', 'N_USU_ID', 'N_SEC_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K5_K6_K1_K4_2_3_7_14_15_16_17_20_21_22_23_24_25_26_27_28_29_30_3923', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K5_8341', 'N_ME_ID', 'N_TN_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K1_K5_K4_K25_5282', 'N_ID', 'N_USU_ID', 'N_ME_ID', 'N_TN_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K4_K25_K1_2_3_5_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K5_2166', 'N_ME_ID', 'N_TN_ID'),
        Index('_dta_index_K_NOTA_5_2030630277__K20_K2_K1', 'N_ID', 'N_USU_ID', 'N_FECHA_CAPTURA'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K2_K1_K20_3_4_5_6_7_14_15_16_17_21_22_23_24_25_26_27_28_29_30_114', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K5_K4_K25_K1_6250', 'N_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_82397080_K1_20', 'N_ID', 'N_FECHA_CAPTURA', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_106796256_K1_K2_K5_K4_K25_K3_K6_K7_K14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277__K1_K2_K20_3_4_5_6_7_14_15_16_17_21_22_23_24_25_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K1_K5_1973', 'N_ID', 'N_TN_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K5_K4_K25_K1_2_3_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30_5543', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K5_K4_K25_K1_K2_K3_K6_K7_K14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_82397080_K25_K1_2_3_5_6_7_14_15_16_17_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277__K2_K20_K1_3_4_5_6_7_14_15_16_17_21_22_23_24_25_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K5_K4_K25_K1_2_3_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30_8809', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K5_K4_K25_K1_K2_K3_K6_K7_K14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K4_K1_9987', 'N_ID', 'N_ME_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K5_K6_K1_K4_2_3_7_14_15_16_17_20_21_22_23_24_25_26_27_28_29_30_4801', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_106796256_K25_K1_K5_K4_K2_K3_K6_K7_K14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277__K20_K2_K1_3_4_5_6_7_14_15_16_17_21_22_23_24_25_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K2_K1_K20_3_4_5_6_7_14_15_16_17_21_22_23_24_25_26_27_28_29_30_9953', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_106796032_K1_K5_K4_K25', 'N_ID', 'N_ME_ID', 'N_TN_ID', 'N_VISIBLE', 'N_URL'),
        Index('_dta_index_K_NOTA_5_2030630277__K5_K4_K2_K6_K7_K3_1', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K1_K25_K4_2_3_5_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277__K5_K4_K1_K6_2_3_7_14_15_16_17_20_21_22_23_24_25_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277__K5_K4_K1', 'N_ID', 'N_ME_ID', 'N_TN_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K5_K4_K25_K1_1530', 'N_ID', 'N_ME_ID', 'N_TN_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_82397080_K4_K1_K25_2_3_5_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277__K5_K6', 'N_TN_ID', 'N_SEC_ID'),
        Index('_dta_index_K_NOTA_5_2030630277__K2_K4_K6_K7_K3_K5_1', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID'),
        Index('_dta_index_K_NOTA_5_2030630277__K1_K5_K4', 'N_ID', 'N_ME_ID', 'N_TN_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_106796032_K1_K2_K5_K4_K25', 'N_ID', 'N_USU_ID', 'N_ME_ID', 'N_TN_ID', 'N_VISIBLE', 'N_URL'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K25_K1_K4_2_3_5_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277__K6_K5_K1_K4_2_3_7_14_15_16_17_20_21_22_23_24_25_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277__K4_K5_K1', 'N_ID', 'N_ME_ID', 'N_TN_ID'),
        Index('_dta_index_K_NOTA_5_2030630277__K4_K1_K23_2_3_5_6_7_14_15_16_17_20_21_22_24_25_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277__K4_K2_K6_K7_K3_K5_1', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_97758080_K25_K1_K5_K4_K2_K3_K6_K7_K14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_97757800_K4_1', 'N_ID', 'N_ME_ID', 'N_AUTOR1'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K1_K4_4364', 'N_ID', 'N_ME_ID'),
        Index('_dta_index_K_NOTA_5_2030630277__K5_K4', 'N_ME_ID', 'N_TN_ID'),
        Index('_dta_index_K_NOTA_5_2030630277__K4_K1_K5', 'N_ID', 'N_ME_ID', 'N_TN_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K5_K4_K25_K1_K2_K3_K6_K7_K14_15_16_17_20_21_22_23_24_26_27_28_29_30_6831', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277__K1_K5_K6_K4_2_3_7_14_15_16_17_20_21_22_23_24_25_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277__K6_K4_K2_K7_K3_K5_1', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID'),
        Index('_dta_index_K_NOTA_5_2030630277__K5_K1_K4', 'N_ID', 'N_ME_ID', 'N_TN_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K4_K1_K25_2_3_5_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_97758080_K1_K5_K4_K25_K2_K3_K6_K7_K14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K1_K2_K3_K4_K5_K6_K7_K14_15_16_17_20_21_22_23_24_25_26_27_28_29_30_9983', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277__K4_K5_K1_K6_2_3_7_14_15_16_17_20_21_22_23_24_25_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K1_K5_9987', 'N_ID', 'N_ME_ID', 'N_TN_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K1_K25_2_3_5_6_7_14_15_16_17_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K6_K4_K2_K7_K3_K5_1', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K1_K5_K4_K25_K2_K3_K6_K7_K14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277__K6_K5', 'N_TN_ID', 'N_SEC_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K5_K4_K25_K1_K2_K3_K6_K7_K14_15_16_17_20_21_22_23_24_26_27_28_29_30_7472', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K1_K25', 'N_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K2_9987_4364', 'N_USU_ID', 'N_TN_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K1_K5_K4', 'N_ID', 'N_ME_ID', 'N_TN_ID'),
        Index('_dta_index_K_NOTA_5_2030630277__K5_K6_K1_K4_2_3_7_14_15_16_17_20_21_22_23_24_25_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K5_K4_K25_K1_5439', 'N_ID', 'N_ME_ID', 'N_TN_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_82397080_K1_K25_2_3_5_6_7_14_15_16_17_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_106796984_K4', 'N_ME_ID', 'N_EN_ID'),
        Index('_dta_index_K_NOTA_5_2030630277__K5_K1_K6_K4_2_3_7_14_15_16_17_20_21_22_23_24_25_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K5_8066', 'N_USU_ID', 'N_TN_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K5_K1_K4', 'N_ID', 'N_ME_ID', 'N_TN_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_82397080_K5_K4_K25_K1_K2_K3_K6_K7_K14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_82397080_K4_K1', 'N_ID', 'N_ME_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K4_7281', 'N_ME_ID', 'N_PRG_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K1_K4_4149', 'N_ID', 'N_ME_ID', 'N_TN_ID'),
        Index('_dta_index_K_NOTA_5_2030630277__K4_K5', 'N_ME_ID', 'N_TN_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K1_K5_K4_K25_8555', 'N_ID', 'N_ME_ID', 'N_TN_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277__K1_K4_K23_2_3_5_6_7_14_15_16_17_20_21_22_24_25_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_82397080_K1_K4', 'N_ID', 'N_ME_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K6_K4_K2_K7_K3_K5_1_1912', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K4_K1_K5', 'N_ID', 'N_ME_ID', 'N_TN_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K1_K5', 'N_ID', 'N_ME_ID', 'N_TN_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_82397080_K5_K4_K25_K1_K2', 'N_ID', 'N_USU_ID', 'N_ME_ID', 'N_TN_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_97757800_K1_K4', 'N_ID', 'N_ME_ID', 'N_AUTOR1'),
        Index('_dta_index_K_NOTA_5_2030630277_82397080_K1_K25_K4_2_3_5_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K6_K4_K2_K7_K3_K5_1_4149', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K5_K4_K25_K1_K2_K3_K6_K7_K14_15_16_17_20_21_22_23_24_26_27_28_29_30_9389', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277__K1_K4_K25', 'N_ID', 'N_ME_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_93620880_K6_K20_K25_K4_K5_K1_3_14_21_28_29', 'N_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_AUTOR1', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_VISIBLE', 'N_URL', 'N_COSTO'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K4_K20_K25_8310', 'N_ME_ID', 'N_TN_ID', 'N_FECHA_CAPTURA', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277__K4_K25', 'N_ME_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K1_K2_K5_K4_K25_9725', 'N_ID', 'N_USU_ID', 'N_ME_ID', 'N_TN_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K20_K25_K5_K6_K4_K1_3_14_21_28_29_2555', 'N_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_AUTOR1', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_VISIBLE', 'N_URL', 'N_COSTO'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K6_K20_K25_K4_K5_K1_3_14_21_28_29_3426', 'N_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_AUTOR1', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_VISIBLE', 'N_URL', 'N_COSTO'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K4_K1_K5_K25_K2_K3_K6_K7_K14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277__K1_K4_K25_2_3_5_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_106795752_K1_K2_K5_K4_K25_K3_K6_K7_K14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K1_K20_K25_8917', 'N_ID', 'N_ME_ID', 'N_FECHA_CAPTURA', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K1_K20_K25_K6_K4_K5_3_14_21_28_29_5081', 'N_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_AUTOR1', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_VISIBLE', 'N_URL', 'N_COSTO'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K1_K6', 'N_ID', 'N_SEC_ID'),
        Index('_dta_index_K_NOTA_5_2030630277__K4_K25_K1', 'N_ID', 'N_ME_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_97758080_K4_K1_K5_K25_K2_K3_K6_K7_K14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K20_K25_K4_K6_K5_K1_3_14_21_28_29', 'N_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_AUTOR1', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_VISIBLE', 'N_URL', 'N_COSTO'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K4_K20_K25_9364', 'N_ME_ID', 'N_FECHA_CAPTURA', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277__K4_K25_K1_2_3_5_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K4_K1_K5_K25_K2_K3_K6_K7_K14_15_16_17_20_21_22_23_24_26_27_28_29_30_53', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K5_K1_K7_K4_K6_K3_2_14_15_16_17_20_21_22_23_24_25_26_27_28_29_30_8258', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K25_4009', 'N_TN_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K20_K25_K5_K6_K4_K1_3_14_21_28_29_3002', 'N_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_AUTOR1', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_VISIBLE', 'N_URL', 'N_COSTO'),
        Index('_dta_index_K_NOTA_5_2030630277__K25_K1_K4_2_3_5_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_106796536_K5_K4_K25_K1_K2_K3_K6_K7_K14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K1_K20_K25_4951', 'N_ID', 'N_FECHA_CAPTURA', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K4_K1_K5_K7_K6_K3_2_14_15_16_17_20_21_22_23_24_25_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_93614016_K20_K25_K5', 'N_TN_ID', 'N_FECHA_CAPTURA', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K4_K25_K1', 'N_ID', 'N_ME_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K5_K4_K25_K1_K2_4274', 'N_ID', 'N_USU_ID', 'N_ME_ID', 'N_TN_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K20_K25_K4', 'N_ME_ID', 'N_SEC_ID', 'N_FECHA_CAPTURA', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_105562056_K5_K4_K25_K1', 'N_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_93620880_K5_K20_K25_K6_K4_K1_3_14_21_28_29', 'N_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_AUTOR1', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_VISIBLE', 'N_URL', 'N_COSTO'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K4_K25_K1_2_3_5_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_93620880_K20_K25_K5', 'N_TN_ID', 'N_FECHA_CAPTURA', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_93620880_K20_K25_K4_K6', 'N_ME_ID', 'N_SEC_ID', 'N_FECHA_CAPTURA', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_82397080_K4_K25', 'N_ME_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_97758080_K1_K2_K5_K4_K25', 'N_ID', 'N_USU_ID', 'N_ME_ID', 'N_TN_ID', 'N_AUTOR4', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_93614016_K4_K6_K20_K25', 'N_ME_ID', 'N_SEC_ID', 'N_FECHA_CAPTURA', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_82397080_K4_K25_K1', 'N_ID', 'N_ME_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_93620880_K6_K20_K25', 'N_SEC_ID', 'N_FECHA_CAPTURA', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K1_K2_K5_K4_K25_9494', 'N_ID', 'N_USU_ID', 'N_ME_ID', 'N_TN_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K5_K1_K7_K4_K6_K3_2_14_15_16_17_20_21_22_23_24_25_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_93620880_K5_K20_K25', 'N_TN_ID', 'N_FECHA_CAPTURA', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_82397080_K1_K4_K25_2_3_5_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_106796984_K5', 'N_TN_ID', 'N_EN_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_93614016_K5_K20_K25', 'N_TN_ID', 'N_FECHA_CAPTURA', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_82397080_K1_K4_K25', 'N_ID', 'N_ME_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K4_K1_K5_K25_K2_K3_K6_K7_K14_15_16_17_20_21_22_23_24_26_27_28_29_30_4686', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_93614016_K4_K20_K25', 'N_ME_ID', 'N_FECHA_CAPTURA', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K1_K2_K5_K4_K25_K3_K6_K7_K14_15_16_17_20_21_22_23_24_26_27_28_29_30_7139', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K25_6147', 'N_ME_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_97758080_K1_K2_K3_K4_K5_K6_K7_K14_15_16_17_20_21_22_23_24_25_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K25_K1_K4_2_3_5_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K25_8525', 'N_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K1_K2_K3_K4_K5_K6_K7_K14_15_16_17_20_21_22_23_24_25_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K6_K20_K25_K4_K5_K1_3_14_21_28_29', 'N_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_AUTOR1', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_VISIBLE', 'N_URL', 'N_COSTO'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K4', 'N_ID', 'N_ME_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_97757800_K5_K4_K25_K1_K2', 'N_ID', 'N_USU_ID', 'N_ME_ID', 'N_TN_ID', 'N_AUTOR1', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K1_K20_K25_K6_K4_K5_3_14_21_28_29', 'N_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_AUTOR1', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_VISIBLE', 'N_URL', 'N_COSTO'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K6_K4_K5_K1_K20_K25_3_14_21_28_29', 'N_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_AUTOR1', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_VISIBLE', 'N_URL', 'N_COSTO'),
        Index('_dta_index_K_NOTA_5_2030630277_82397080_K25_K1_K4_2_3_5_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K4_K20_K25', 'N_ME_ID', 'N_SEC_ID', 'N_FECHA_CAPTURA', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K5_K20_K25_K6_K4_K1_3_14_21_28_29', 'N_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_AUTOR1', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_VISIBLE', 'N_URL', 'N_COSTO'),
        Index('_dta_index_K_NOTA_5_2030630277_82397080_K4_K25_K1_2_3_5_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_97757800_K1_K2_K5_K4_K25', 'N_ID', 'N_USU_ID', 'N_ME_ID', 'N_TN_ID', 'N_AUTOR1', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K20_K25_K4_504', 'N_ME_ID', 'N_TN_ID', 'N_FECHA_CAPTURA', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_82397080_K4', 'N_ME_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K20_K25_K4_K6_K5_K1_3_14_21_28_29_2649', 'N_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_AUTOR1', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_VISIBLE', 'N_URL', 'N_COSTO'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K25_K1_K5_K4_K2_K3_K6_K7_K14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K4_K25', 'N_ID', 'N_ME_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_93620880_K20_K25', 'N_FECHA_CAPTURA', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_93614016_K20_K25_K1_K6_K4_K5_3_14_21_28_29', 'N_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_AUTOR1', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_VISIBLE', 'N_URL', 'N_COSTO'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K1_K2_K5_K4_K25_K3_K6_K7_K14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K1_K4_K25_2_3_5_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_93614016_K1_K20_K25_K6_K4_K5_3_14_21_28_29', 'N_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_AUTOR1', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_VISIBLE', 'N_URL', 'N_COSTO'),
        Index('_dta_index_K_NOTA_5_2030630277_93620880_K20_K25_K1', 'N_ID', 'N_FECHA_CAPTURA', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_106796312_K4_K1_K5_K25_K2_K3_K6_K7_K14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K1_K4_K25', 'N_ID', 'N_ME_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_93620880_K4_K6_K20_K25_1_3_5_14_21_28_29', 'N_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_AUTOR1', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_VISIBLE', 'N_URL', 'N_COSTO'),
        Index('_dta_index_K_NOTA_5_2030630277_106796256_K4_K1_K5_K25_K2_K3_K6_K7_K14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K20_K25_K4_8584', 'N_ME_ID', 'N_FECHA_CAPTURA', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_93620880_K20_K25_K4_K6_1_3_5_14_21_28_29', 'N_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_AUTOR1', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_VISIBLE', 'N_URL', 'N_COSTO'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K2_K1_K20_3_4_5_6_7_14_15_16_17_21_22_23_24_25_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K1_K2_K3_K4_K5_K6_K7_K14_15_16_17_20_21_22_23_24_25_26_27_28_29_30_8059', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K20_K25_K4_K6_K5_K1_3_14_21_28_29_948', 'N_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_AUTOR1', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_VISIBLE', 'N_URL', 'N_COSTO'),
        Index('_dta_index_K_NOTA_5_2030630277_93614016_K20_K25_K1', 'N_ID', 'N_FECHA_CAPTURA', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K5_K1', 'N_ID', 'N_TN_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_97758080_K5_K4_K25_K1_K2_K3_K6_K7_K14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K4_K20_K25_K6_K5_K1_3_14_21_28_29', 'N_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_AUTOR1', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_VISIBLE', 'N_URL', 'N_COSTO'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K5_K4_K25_K1_2_3_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_106796984_K5_K4_K25_K1_K2', 'N_ID', 'N_USU_ID', 'N_ME_ID', 'N_TN_ID', 'N_VISIBLE', 'N_EN_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K20_K25_K4_K6_K5_K1_3_14_21_28_29_3910', 'N_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_AUTOR1', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_VISIBLE', 'N_URL', 'N_COSTO'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K20_K25_K4_K6', 'N_ME_ID', 'N_SEC_ID', 'N_FECHA_CAPTURA', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K5_K4_K25_K1_2_3_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30_9987', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K5_K4_K25_K1_K2_1569', 'N_ID', 'N_USU_ID', 'N_ME_ID', 'N_TN_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K20_K25_K1_K6_K4_K5_3_14_21_28_29_4275', 'N_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_AUTOR1', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_VISIBLE', 'N_URL', 'N_COSTO'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K6_K4_K5_K1_K20_K25_3_14_21_28_29_3071', 'N_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_AUTOR1', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_VISIBLE', 'N_URL', 'N_COSTO'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K2_K1_K20_3_4_5_6_7_14_15_16_17_21_22_23_24_25_26_27_28_29_30_4364', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_106796984_K5_K4_K25_K1', 'N_ID', 'N_ME_ID', 'N_TN_ID', 'N_VISIBLE', 'N_EN_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K20_K25_K5_6386', 'N_ID', 'N_TN_ID', 'N_FECHA_CAPTURA', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K5_K20_K25_K6_K4_K1_3_14_21_28_29_6969', 'N_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_AUTOR1', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_VISIBLE', 'N_URL', 'N_COSTO'),
        Index('_dta_index_K_NOTA_5_2030630277__K4_K1', 'N_ID', 'N_ME_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K25_K6_K4_K5_K1_K20_3_14_21_28_29_8484', 'N_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_AUTOR1', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_VISIBLE', 'N_URL', 'N_COSTO'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K1_K2_K5_K4_K25_3732', 'N_ID', 'N_USU_ID', 'N_ME_ID', 'N_TN_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_93614016_K25_K6_K4_K5_K1_K20_3_14_21_28_29', 'N_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_AUTOR1', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_VISIBLE', 'N_URL', 'N_COSTO'),
        Index('_dta_index_K_NOTA_5_2030630277__K1_K4', 'N_ID', 'N_ME_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K4_K6_K20_K25_K5_K1_3_14_21_28_29_7748', 'N_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_AUTOR1', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_VISIBLE', 'N_URL', 'N_COSTO'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K25_K1_K5_K4_K2_K3_K6_K7_K14_15_16_17_20_21_22_23_24_26_27_28_29_30_3423', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_93614016_K6_K4_K5_K1_K20_K25_3_14_21_28_29', 'N_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_AUTOR1', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_VISIBLE', 'N_URL', 'N_COSTO'),
        Index('_dta_index_K_NOTA_5_2030630277__K4_1', 'N_ID', 'N_ME_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K20_K25_5748', 'N_ID', 'N_FECHA_CAPTURA', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K1_K2_K5_K4_K25_K3_K6_K7_K14_15_16_17_20_21_22_23_24_26_27_28_29_30_8021', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_93620880_K1_K20_K25_K6_K4_K5_3_14_21_28_29', 'N_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_AUTOR1', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_VISIBLE', 'N_URL', 'N_COSTO'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K4_K1', 'N_ID', 'N_ME_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K4_K1_K5_K25_K2_K3_K6_K7_K14_15_16_17_20_21_22_23_24_26_27_28_29_30_1578', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K20_1971', 'N_ID', 'N_FECHA_CAPTURA'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K6_K4_K5_K1_K20_K25_3_14_21_28_29_5734', 'N_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_AUTOR1', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_VISIBLE', 'N_URL', 'N_COSTO'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K1_K2_K3_K4_K5_K6_K7_K14_15_16_17_20_21_22_23_24_25_26_27_28_29_30_8766', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K5_K20_K25_K6_K4_K1_3_14_21_28_29_9296', 'N_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_AUTOR1', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_VISIBLE', 'N_URL', 'N_COSTO'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K6_K20_K25_4828', 'N_ID', 'N_SEC_ID', 'N_FECHA_CAPTURA', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K1_K4', 'N_ID', 'N_ME_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K5_K4_K25_K1_K2_8900', 'N_ID', 'N_USU_ID', 'N_ME_ID', 'N_TN_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K6_K20_K25_K4_K5_K1_3_14_21_28_29_333', 'N_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_AUTOR1', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_VISIBLE', 'N_URL', 'N_COSTO'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K20_K25_K4_K6_1_3_5_14_21_28_29_100', 'N_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_AUTOR1', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_VISIBLE', 'N_URL', 'N_COSTO'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K1', 'N_ID', 'N_ME_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K1_K5_K4_K25_2568', 'N_ID', 'N_ME_ID', 'N_TN_ID', 'N_PRG_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K1_K20_K25_K6_K4_K5_3_14_21_28_29_3168', 'N_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_AUTOR1', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_VISIBLE', 'N_URL', 'N_COSTO'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K6_K20_K25_K4_K5_K1_3_14_21_28_29_2484', 'N_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_AUTOR1', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_VISIBLE', 'N_URL', 'N_COSTO'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K4_1', 'N_ID', 'N_ME_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_82397080_K1_K2_K5_K4_K25', 'N_ID', 'N_USU_ID', 'N_ME_ID', 'N_TN_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K4_K20_K25_8467', 'N_ID', 'N_ME_ID', 'N_FECHA_CAPTURA', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K1_K20_K25_K6_K4_K5_3_14_21_28_29_6544', 'N_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_AUTOR1', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_VISIBLE', 'N_URL', 'N_COSTO'),
        Index('_dta_index_K_NOTA_5_2030630277__K4_K1_2_3_5_6_7_14_15_16_17_20_21_22_23_24_25_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K4_K1_9987_4364', 'N_ID', 'N_ME_ID', 'N_SEC_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K1_K5_K4_K25_K2_K3_K6_K7_K14_15_16_17_20_21_22_23_24_26_27_28_29_30_170', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K1_K20_2_3_4_5_6_7_14_15_16_17_21_22_23_24_25_26_27_28_29_30_1771', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277__K1_K4_K14', 'N_ID', 'N_ME_ID', 'N_AUTOR1'),
        Index('_dta_index_K_NOTA_5_2030630277_97757800_K5_K4_K25_K1', 'N_ID', 'N_ME_ID', 'N_TN_ID', 'N_AUTOR1', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K20D_K1_K4_K6_K7_2_3_5_14_15_16_17_21_22_23_24_25_26_27_28_29_30_2533', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K1_K20D_K4_K6_K7_2_3_5_14_15_16_17_21_22_23_24_25_26_27_28_29_30_8258', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_106796312_K25_K1_K5_K4_K2_K3_K6_K7_K14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277__K1_14_21_28', 'N_ID', 'N_AUTOR1', 'N_FECHA_PUBLICACION', 'N_URL'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K5_K4_K25_K1_2608', 'N_ID', 'N_USU_ID', 'N_ME_ID', 'N_TN_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277__K1_K14', 'N_ID', 'N_AUTOR1'),
        Index('_dta_index_K_NOTA_5_2030630277__K1_21_28_29', 'N_ID', 'N_FECHA_PUBLICACION', 'N_URL', 'N_COSTO'),
        Index('_dta_index_K_NOTA_5_2030630277_106796984_K1_K2_K5_K4_K25', 'N_ID', 'N_USU_ID', 'N_ME_ID', 'N_TN_ID', 'N_VISIBLE', 'N_EN_ID'),
        Index('_dta_index_K_NOTA_5_2030630277__K1_21', 'N_ID', 'N_FECHA_PUBLICACION'),
        Index('_dta_index_K_NOTA_5_2030630277_82397080_K1_K5_K4_K25_K2_K3_K6_K7_K14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277__K1_21_28_30', 'N_ID', 'N_FECHA_PUBLICACION', 'N_URL', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K1_K5_K4_K25_K2_K3_K6_K7_K14_15_16_17_20_21_22_23_24_26_27_28_29_30_4327', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277__K5_K1_K7_K4_K6_K3_2_14_15_16_17_20_21_22_23_24_25_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277__K4_K6_K1_7', 'N_ID', 'N_ME_ID', 'N_SEC_ID', 'N_PRG_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_105562056_K1_K5_K4_K25', 'N_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K4_K1_K5_K7_K6_K3_2_14_15_16_17_20_21_22_23_24_25_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K6_K1_9850', 'N_ID', 'N_TN_ID', 'N_SEC_ID'),
        Index('_dta_index_K_NOTA_5_2030630277__K6_K1_K4_7', 'N_ID', 'N_ME_ID', 'N_SEC_ID', 'N_PRG_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K6_K1_K5_K7_K4_K3_2_14_15_16_17_20_21_22_23_24_25_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K1_K4_K5_K7_K6_K3_2_14_15_16_17_20_21_22_23_24_25_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277__K1_K6_K4_7', 'N_ID', 'N_ME_ID', 'N_SEC_ID', 'N_PRG_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_82397080_K25_K1_K5_K4_K2_K3_K6_K7_K14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K1_K6_4864', 'N_ID', 'N_TN_ID', 'N_SEC_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K1_K4_2894', 'N_ID', 'N_ME_ID'),
        Index('_dta_index_K_NOTA_5_2030630277__K4_K1_K6_7', 'N_ID', 'N_ME_ID', 'N_SEC_ID', 'N_PRG_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_106796312_K1_K2_K5_K4_K25_K3_K6_K7_K14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K6_K1', 'N_ID', 'N_SEC_ID'),
        Index('_dta_index_K_NOTA_5_2030630277__K1_K4_K6_7', 'N_ID', 'N_ME_ID', 'N_SEC_ID', 'N_PRG_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_105562056_K5', 'N_AG_ID', 'N_TN_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K1_K4_1912', 'N_ID', 'N_ME_ID', 'N_SEC_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K6_K1_K4_7', 'N_ID', 'N_ME_ID', 'N_SEC_ID', 'N_PRG_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K5_K4_K25_K1_K2', 'N_ID', 'N_USU_ID', 'N_ME_ID', 'N_TN_ID', 'N_PRG_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K1_K2_K5_K4_K25', 'N_ID', 'N_USU_ID', 'N_ME_ID', 'N_TN_ID', 'N_PRG_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K1_K6_6960', 'N_ID', 'N_ME_ID', 'N_SEC_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K4_K1_9987', 'N_ID', 'N_ME_ID', 'N_SEC_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K1_K6_K5_K7_K4_K3_2_14_15_16_17_20_21_22_23_24_25_26_27_28_29_30_9910', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_106795752_K25_K1_K5_K4_K2_K3_K6_K7_K14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K6_K1_K4_7_4364', 'N_ID', 'N_ME_ID', 'N_SEC_ID', 'N_PRG_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_106796536_K25_K1_K5_K4_K2_K3_K6_K7_K14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277__K2_K1_K20_3_4_5_6_7_14_15_16_17_21_22_23_24_25_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K4_K6_K1_7', 'N_ID', 'N_ME_ID', 'N_SEC_ID', 'N_PRG_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K20_K25_K5', 'N_TN_ID', 'N_SEC_ID', 'N_FECHA_CAPTURA', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_82397080_K1_K2_K5_K4_K25_K3_K6_K7_K14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277__K20_K25_K4', 'N_ME_ID', 'N_FECHA_CAPTURA', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_97758080_K4', 'N_ME_ID', 'N_AUTOR4'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K1_K4_8066', 'N_ID', 'N_ME_ID', 'N_SEC_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K20_K25_K1_K6_K4_K5_3_14_21_28_29', 'N_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_AUTOR1', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_VISIBLE', 'N_URL', 'N_COSTO'),
        Index('_dta_index_K_NOTA_5_2030630277_97757800_K4', 'N_ME_ID', 'N_AUTOR1'),
        Index('_dta_index_K_NOTA_5_2030630277__K1_20', 'N_ID', 'N_FECHA_CAPTURA'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K4_K6_K1_7_1912', 'N_ID', 'N_ME_ID', 'N_SEC_ID', 'N_PRG_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_106796032_K5', 'N_TN_ID', 'N_URL'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K4_K1_K6_7', 'N_ID', 'N_ME_ID', 'N_SEC_ID', 'N_PRG_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K4_K1_K5_K25_K2_K3_K6_K7_K14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277__K4_K1_K5_K2_3_6_7_14_15_16_17_20_21_22_23_24_25_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_106796536_K1_K2_K3_K4_K5_K6_K7_K14_15_16_17_20_21_22_23_24_25_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K1_4149', 'N_ID', 'N_SEC_ID'),
        Index('_dta_index_K_NOTA_5_2030630277__K1_K5_K2_K4_3_6_7_14_15_16_17_20_21_22_23_24_25_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K5_K4_K25_K1_K2_8040', 'N_ID', 'N_USU_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277__K1_K4_K5_K7_K6_K3_2_14_15_16_17_20_21_22_23_24_25_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277__K5_K2_K4_K1_3_6_7_14_15_16_17_20_21_22_23_24_25_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K4_K1_K6_7_5201', 'N_ID', 'N_ME_ID', 'N_SEC_ID', 'N_PRG_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_106795752_K1_K5_K4_K25_K2_K3_K6_K7_K14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277__K2_K5_K4_K1', 'N_ID', 'N_USU_ID', 'N_ME_ID', 'N_TN_ID'),
        Index('_dta_index_K_NOTA_5_2030630277__K6_K1', 'N_ID', 'N_SEC_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K1_K6_6497', 'N_ID', 'N_SEC_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_106796256_K1_K5_K4_K25_K2_K3_K6_K7_K14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277__K1_K5_K2_K4_3_6_7_14_15_16_17_21_22_23_24_25_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K1_K5_K4_K25_K2_K3_K6_K7_K14_15_16_17_20_21_22_23_24_26_27_28_29_30_2386', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K6_K1_1040', 'N_ID', 'N_SEC_ID'),
        Index('_dta_index_K_NOTA_5_2030630277__K5_K2_K4_K1_3_6_7_14_15_16_17_21_22_23_24_25_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K1_K2_K5_K4_K25_1605', 'N_ID', 'N_USU_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277__K2_K5_K4_K1_3_6_7_14_15_16_17_20_21_22_23_24_25_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K1_K6_1771', 'N_ID', 'N_ME_ID', 'N_SEC_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_106796536_K1_K2_K5_K4_K25_K3_K6_K7_K14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K1_K5_K4_K25_K2_K3_K6_K7_K14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K1_K4_K6_7', 'N_ID', 'N_ME_ID', 'N_SEC_ID', 'N_PRG_ID'),
        Index('_dta_index_K_NOTA_5_2030630277__K1_2_3_4_5_6_7_14_15_16_17_20_21_22_23_24_25_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K4_K1_K5_K25_K2_K3_K6_K7_K14_15_16_17_20_21_22_23_24_26_27_28_29_30_6023', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K5_K1_K7_K4_K6_K3_2_14_15_16_17_20_21_22_23_24_25_26_27_28_29_30_1410', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277__K1_K25', 'N_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K1_K6_K5_K7_K4_K3_2_14_15_16_17_20_21_22_23_24_25_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K6_K1_2533', 'N_ID', 'N_ME_ID', 'N_SEC_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_106796032_K5_K4_K25_K1_K2', 'N_ID', 'N_USU_ID', 'N_ME_ID', 'N_TN_ID', 'N_VISIBLE', 'N_URL'),
        Index('_dta_index_K_NOTA_5_2030630277__K26_K1', 'N_ID', 'N_EN_ID'),
        Index('_dta_index_K_NOTA_5_2030630277__K1_K25_2_3_4_5_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K5_K4_K25_K1_K2_4990', 'N_ID', 'N_USU_ID', 'N_ME_ID', 'N_TN_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K1_K4_K6_7_8258', 'N_ID', 'N_ME_ID', 'N_SEC_ID', 'N_PRG_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K4_K1_8066', 'N_ID', 'N_ME_ID', 'N_TN_ID'),
        Index('_dta_index_K_NOTA_5_2030630277__K1_29', 'N_ID', 'N_COSTO'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K1_K5_K4_K25_K2_K3_K6_K7_K14_15_16_17_20_21_22_23_24_26_27_28_29_30_1098', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K1_K6_K4_7', 'N_ID', 'N_ME_ID', 'N_SEC_ID', 'N_PRG_ID'),
        Index('_dta_index_K_NOTA_5_2030630277__K25_K1_2_3_4_5_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_97758080_K1_K5_K4_K25', 'N_ID', 'N_ME_ID', 'N_TN_ID', 'N_AUTOR4', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K1_K5_K7_K4_K6_K3_2_14_15_16_17_20_21_22_23_24_25_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277__K25_K1', 'N_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K1_K6_K4_7_1410', 'N_ID', 'N_ME_ID', 'N_SEC_ID', 'N_PRG_ID'),
        Index('_dta_index_K_NOTA_5_2030630277__K4_K1_K5_K7_K6_K3_2_14_15_16_17_20_21_22_23_24_25_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277__K1_21_29', 'N_ID', 'N_FECHA_PUBLICACION', 'N_COSTO'),
        Index('_dta_index_K_NOTA_5_2030630277_82397080_K1_K25', 'N_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_106796032_K5_K4_K25_K1', 'N_ID', 'N_ME_ID', 'N_TN_ID', 'N_VISIBLE', 'N_URL'),
        Index('_dta_index_K_NOTA_5_2030630277__K6_K1_K4_K7', 'N_ID', 'N_ME_ID', 'N_SEC_ID', 'N_PRG_ID'),
        Index('_dta_index_K_NOTA_5_2030630277__K1_K2_3_4_5_6_7_14_15_16_17_20_21_22_23_24_25_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K5_K6_K1_K4_2_3_7_14_15_16_17_20_21_22_23_24_25_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_82397080_K25_K1', 'N_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K1_K6_K5_K7_K4_K3_2_14_15_16_17_20_21_22_23_24_25_26_27_28_29_30_8809', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277__K1_K6_K4_K7', 'N_ID', 'N_ME_ID', 'N_SEC_ID', 'N_PRG_ID'),
        Index('_dta_index_K_NOTA_5_2030630277__K2_K1', 'N_ID', 'N_USU_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K6_K5', 'N_TN_ID', 'N_SEC_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K6_K1', 'N_ID', 'N_SEC_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K1_K25_2_3_4_5_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277__K4_K1_K6_K7', 'N_ID', 'N_ME_ID', 'N_SEC_ID', 'N_PRG_ID'),
        Index('_dta_index_K_NOTA_5_2030630277__K2_K1_3_4_5_6_7_14_15_16_17_20_21_22_23_24_25_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K6_K5_9987', 'N_TN_ID', 'N_SEC_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K25', 'N_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277__K4_K6_K7_K1', 'N_ID', 'N_ME_ID', 'N_SEC_ID', 'N_PRG_ID'),
        Index('_dta_index_K_NOTA_5_2030630277__K5_K25_K1_2_3_4_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_82397080_K25_K1_2_3_4_5_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K6_K5_K1_K4_2_3_7_14_15_16_17_20_21_22_23_24_25_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277__K1_K4_K6_K7', 'N_ID', 'N_ME_ID', 'N_SEC_ID', 'N_PRG_ID'),
        Index('_dta_index_K_NOTA_5_2030630277__K5_K25_K1', 'N_ID', 'N_TN_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K25_K1_2_3_4_5_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K6_K5_4364', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K4_K1_K6_K7', 'N_ID', 'N_ME_ID', 'N_SEC_ID', 'N_PRG_ID'),
        Index('_dta_index_K_NOTA_5_2030630277__K1_K5_K25_2_3_4_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K1_K6', 'N_ID', 'N_SEC_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K1_K25', 'N_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277__K25_K1_K5_2_3_4_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K5', 'N_ID', 'N_TN_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K1_K4_K6_K7', 'N_ID', 'N_ME_ID', 'N_SEC_ID', 'N_PRG_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_82397080_K1_K25_2_3_4_5_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277__K1_K5_K25', 'N_ID', 'N_TN_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K6_K5_K1_K4_2_3_7_14_15_16_17_20_21_22_23_24_25_26_27_28_29_30_8066', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K25_K1', 'N_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K1_K4_K6_K7_9987', 'N_ID', 'N_ME_ID', 'N_SEC_ID', 'N_PRG_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K5_K25_K1', 'N_ID', 'N_TN_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K5_K1_K6_K4_2_3_7_14_15_16_17_20_21_22_23_24_25_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277__K1_K20_K25', 'N_ID', 'N_FECHA_CAPTURA', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K1_K6_K4_K7', 'N_ID', 'N_ME_ID', 'N_SEC_ID', 'N_PRG_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K6_K5_K1_K4_2_3_7_14_15_16_17_20_21_22_23_24_25_26_27_28_29_30_1912', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K6_K1_K5_K7_K4_K3_2_14_15_16_17_20_21_22_23_24_25_26_27_28_29_30_9953', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277__K20_K25_K1', 'N_ID', 'N_FECHA_CAPTURA', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_82397080_K5_K25_K1_2_3_4_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K1_K5_4149', 'N_ID', 'N_TN_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K4_K6_K7_K1', 'N_ID', 'N_ME_ID', 'N_SEC_ID', 'N_PRG_ID'),
        Index('_dta_index_K_NOTA_5_2030630277__K20_K25_K4_K6_1_3_5_14_21_28_29', 'N_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_AUTOR1', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_VISIBLE', 'N_URL', 'N_COSTO'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K5_K25_K1_2_3_4_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277__K4_K20_K25', 'N_ME_ID', 'N_FECHA_CAPTURA', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_82397080_K1_K5_K25_2_3_4_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K5_K6_K1_K4_2_3_7_14_15_16_17_20_21_22_23_24_25_26_27_28_29_30_5201', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K1_K6_K4_K7_4364', 'N_ID', 'N_ME_ID', 'N_SEC_ID', 'N_PRG_ID'),
        Index('_dta_index_K_NOTA_5_2030630277__K5_K20_K25', 'N_TN_ID', 'N_FECHA_CAPTURA', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K1_K5_K25', 'N_ID', 'N_TN_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K5_K1_K6_K4_2_3_7_14_15_16_17_20_21_22_23_24_25_26_27_28_29_30_6497', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K4_K6_K7_K1_8066', 'N_ID', 'N_ME_ID', 'N_SEC_ID', 'N_PRG_ID'),
        Index('_dta_index_K_NOTA_5_2030630277__K4_K6_K20_K25_1_3_5_14_21_28_29', 'N_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_AUTOR1', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_VISIBLE', 'N_URL', 'N_COSTO'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K4_K5_K1_K6_2_3_7_14_15_16_17_20_21_22_23_24_25_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K5_K1_K7_K4_K6_K3_2_14_15_16_17_20_21_22_23_24_25_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K25_K1_K5_2_3_4_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K6_K1_K4_K7', 'N_ID', 'N_ME_ID', 'N_SEC_ID', 'N_PRG_ID'),
        Index('_dta_index_K_NOTA_5_2030630277__K1_K20_K25_K6_K4_K5_3_14_21_28_29', 'N_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_AUTOR1', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_VISIBLE', 'N_URL', 'N_COSTO'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K5_K4', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_82397080_K25_K1_K5_2_3_4_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K6_K1_K4_K7_1912', 'N_ID', 'N_ME_ID', 'N_SEC_ID', 'N_PRG_ID'),
        Index('_dta_index_K_NOTA_5_2030630277__K6_K20_K25', 'N_SEC_ID', 'N_FECHA_CAPTURA', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K5_K1_K6_K4_2_3_7_14_15_16_17_20_21_22_23_24_25_26_27_28_29_30_1040', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_82397080_K5_K25_K1', 'N_ID', 'N_TN_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K4_K1_K6_K7_4149', 'N_ID', 'N_ME_ID', 'N_SEC_ID', 'N_PRG_ID'),
        Index('_dta_index_K_NOTA_5_2030630277__K20_K25_K4_K6', 'N_ME_ID', 'N_SEC_ID', 'N_FECHA_CAPTURA', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K4_K5_K1_K6_2_3_7_14_15_16_17_20_21_22_23_24_25_26_27_28_29_30_1771', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277__K1_K5_21', 'N_ID', 'N_TN_ID', 'N_FECHA_PUBLICACION'),
        Index('_dta_index_K_NOTA_5_2030630277__K6_K20_K25_K4_K5_K1_3_14_21_28_29', 'N_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_AUTOR1', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_VISIBLE', 'N_URL', 'N_COSTO'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K1_K5_K25_2_3_4_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K5_K4_2533', 'N_ME_ID', 'N_TN_ID'),
        Index('_dta_index_K_NOTA_5_2030630277__K5_K1_21', 'N_ID', 'N_TN_ID', 'N_FECHA_PUBLICACION'),
        Index('_dta_index_K_NOTA_5_2030630277__K4_K20_K25_K6_K5_K1_3_14_21_28_29', 'N_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_AUTOR1', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_VISIBLE', 'N_URL', 'N_COSTO'),
        Index('_dta_index_K_NOTA_5_2030630277_82397080_K1_K5_K25', 'N_ID', 'N_TN_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K4_K5_K1_K6_2_3_7_14_15_16_17_20_21_22_23_24_25_26_27_28_29_30_8258', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K1_K5_21', 'N_ID', 'N_TN_ID', 'N_FECHA_PUBLICACION'),
        Index('_dta_index_K_NOTA_5_2030630277__K20_K25_K6_K4_K5_K1_3_14_21_28_29', 'N_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_AUTOR1', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_VISIBLE', 'N_URL', 'N_COSTO'),
        Index('_dta_index_K_NOTA_5_2030630277__K1_K25_K5_K4_2_3_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K5_K4_1410', 'N_ME_ID', 'N_TN_ID'),
        Index('_dta_index_K_NOTA_5_2030630277__K5_K20_K25_K6_K4_K1_3_14_21_28_29', 'N_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_AUTOR1', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_VISIBLE', 'N_URL', 'N_COSTO'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K5_K1_21', 'N_ID', 'N_TN_ID', 'N_FECHA_PUBLICACION'),
        Index('_dta_index_K_NOTA_5_2030630277__K25_K5_K4_K1_2_3_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277__K4_K6_K20_K25', 'N_ME_ID', 'N_SEC_ID', 'N_FECHA_CAPTURA', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K6_K5_2894', 'N_ID', 'N_TN_ID', 'N_SEC_ID'),
        Index('_dta_index_K_NOTA_5_2030630277__K4_K1_K25_K5_2_3_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277__K25_K1_K4', 'N_ID', 'N_ME_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277__K20_K25_K4_K6_K5_K1_3_14_21_28_29', 'N_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_AUTOR1', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_VISIBLE', 'N_URL', 'N_COSTO'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K4_K1_K25_K5_2_3_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K5_K1_4864', 'N_ID', 'N_TN_ID', 'N_SEC_ID'),
        Index('_dta_index_K_NOTA_5_2030630277__K1_K25_K4', 'N_ID', 'N_ME_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277__K20_K25', 'N_FECHA_CAPTURA', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_82397080_K25_K5_K4_K1_2_3_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277__K25_K4_K1', 'N_ID', 'N_ME_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277__K20_K25_K5_K6_K4_K1_3_14_21_28_29', 'N_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_AUTOR1', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_VISIBLE', 'N_URL', 'N_COSTO'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K1_K5_K6_K4_2_3_7_14_15_16_17_20_21_22_23_24_25_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_82397080_K1_K25_K5_K4_2_3_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277__K25_K4', 'N_ME_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277__K20_K25_K6', 'N_SEC_ID', 'N_FECHA_CAPTURA', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K6_K5_K1_K4_2_3_7_14_15_16_17_20_21_22_23_24_25_26_27_28_29_30_6960', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K6_K1_K5_K7_K4_K3_2_14_15_16_17_20_21_22_23_24_25_26_27_28_29_30_5543', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K1_K25_K5_K4_2_3_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K4_K25_K1', 'N_ID', 'N_ME_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277__K6_K4_K5_K1_K20_K25_3_14_21_28_29', 'N_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_AUTOR1', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_VISIBLE', 'N_URL', 'N_COSTO'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K5_K1_9850', 'N_ID', 'N_TN_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K25_K5_K4_K1_2_3_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277__K4_K6_K20_K25_K5_K1_3_14_21_28_29', 'N_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_AUTOR1', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_VISIBLE', 'N_URL', 'N_COSTO'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K25_9987', 'N_ME_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_82397080_K4_K1_K25_K5_2_3_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K1_K5_K6_K4_2_3_7_14_15_16_17_20_21_22_23_24_25_26_27_28_29_30_9085', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277__K25_K6_K4_K5_K1_K20_3_14_21_28_29', 'N_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_AUTOR1', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_VISIBLE', 'N_URL', 'N_COSTO'),
        Index('_dta_index_K_NOTA_5_2030630277__K1_K4_K25_K5_2_3_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K5_K1_6355', 'N_ID', 'N_ME_ID', 'N_TN_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K1_K6_K5_K7_K4_K3_2_14_15_16_17_20_21_22_23_24_25_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K1_K25_4364', 'N_ID', 'N_ME_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277__K20_K25_K5', 'N_TN_ID', 'N_FECHA_CAPTURA', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277__K4_K25_K5_K1_2_3_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K1_K5_K6_K4_2_3_7_14_15_16_17_20_21_22_23_24_25_26_27_28_29_30_8526', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K6_K1_K5_K7_K4_K3_2_14_15_16_17_20_21_22_23_24_25_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_82397080_K25_K4_K1', 'N_ID', 'N_ME_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K4_K6_K20_K25_K5_K1_3_14_21_28_29', 'N_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_AUTOR1', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_VISIBLE', 'N_URL', 'N_COSTO'),
        Index('_dta_index_K_NOTA_5_2030630277__K25_K1_K4_K5_2_3_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K4_K1_K23_2_3_5_6_7_14_15_16_17_20_21_22_24_25_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K5_K1_K6_K4_2_3_7_14_15_16_17_20_21_22_23_24_25_26_27_28_29_30_8341', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K20_K25', 'N_SEC_ID', 'N_FECHA_CAPTURA', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K25_K1_K4_K5_2_3_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_82397080_K25_K4', 'N_ME_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K5_K6', 'N_TN_ID', 'N_SEC_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_82397080_K25_K1_K4_K5_2_3_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K25_K4_K1', 'N_ID', 'N_ME_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K20', 'N_SEC_ID', 'N_FECHA_CAPTURA'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K5_K4_K1_K6_2_3_7_14_15_16_17_20_21_22_23_24_25_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K1_K4_K25_K5_2_3_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K23D_1_2_3_4_5_6_7_14_15_16_17_20_21_22_24_25_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K6_K20_K25', 'N_SEC_ID', 'N_FECHA_CAPTURA', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K4_K5_K1_K6_2_3_7_14_15_16_17_20_21_22_23_24_25_26_27_28_29_30_114', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K4_K25_8066', 'N_ME_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_82397080_K4_K25_K5_K1_2_3_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K5_K4_5543', 'N_ID', 'N_ME_ID', 'N_TN_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K4_K1_K23_2_3_5_6_7_14_15_16_17_20_21_22_24_25_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_82397080_K1_K25_K4', 'N_ID', 'N_ME_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277__K1_14_21', 'N_ID', 'N_AUTOR1', 'N_FECHA_PUBLICACION'),
        Index('_dta_index_K_NOTA_5_2030630277__K1_K4_2_3_5_6_7_14_15_16_17_20_21_22_23_24_25_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K1_K5_K7_K4_K6_K3_2_14_15_16_17_20_21_22_23_24_25_26_27_28_29_30_114', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277__K1_K6_K7', 'N_ID', 'N_SEC_ID', 'N_PRG_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K1_2_3_4_5_6_7_14_15_16_17_20_21_22_23_24_25_26_27_28_29_30_9987', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K25_K4', 'N_ME_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277__K6_K7_K1', 'N_ID', 'N_SEC_ID', 'N_PRG_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K4_K1_2_3_5_6_7_14_15_16_17_20_21_22_23_24_25_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_82397080_K25_K1_K4', 'N_ID', 'N_ME_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277__K6_K1_K7', 'N_ID', 'N_SEC_ID', 'N_PRG_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K25_K1_1912', 'N_ID', 'N_ME_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K6_K7_K1', 'N_ID', 'N_SEC_ID', 'N_PRG_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K1_4364', 'N_ID', 'N_ME_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K1_K25_K4', 'N_ID', 'N_ME_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K6_K1_K7', 'N_ID', 'N_SEC_ID', 'N_PRG_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K4_K1_2_3_5_6_7_14_15_16_17_20_21_22_23_24_25_26_27_28_29_30_8066', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K4_1912', 'N_ID', 'N_ME_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K25_K1_K4', 'N_ID', 'N_ME_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K1_K6_K7', 'N_ID', 'N_SEC_ID', 'N_PRG_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K1_K4_2_3_5_6_7_14_15_16_17_20_21_22_23_24_25_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_82397080_K4_K1_K5_K25_K2_K3_K6_K7_K14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K1_K4_K25_4149', 'N_ID', 'N_ME_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277__K3_K1_21_29', 'N_ID', 'N_AG_ID', 'N_FECHA_PUBLICACION', 'N_COSTO'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K1_K4_2_3_5_6_7_14_15_16_17_20_21_22_23_24_25_26_27_28_29_30_4149', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277__K1_K3_21_29', 'N_ID', 'N_AG_ID', 'N_FECHA_PUBLICACION', 'N_COSTO'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K25_K4_K1', 'N_ID', 'N_ME_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K4_K1', 'N_ID', 'N_ME_ID'),
        Index('_dta_stat_2030630277_1_3', 'N_ID', 'N_AG_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K1_K4', 'N_ID', 'N_ME_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K25_K4', 'N_ID', 'N_ME_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277__K5_K1_16_21_28_30', 'N_ID', 'N_TN_ID', 'N_AUTOR3', 'N_FECHA_PUBLICACION', 'N_URL', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277__K20_K1', 'N_ID', 'N_FECHA_CAPTURA'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K4_K25', 'N_ID', 'N_ME_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277__K1_K5_16_21_28_30', 'N_ID', 'N_TN_ID', 'N_AUTOR3', 'N_FECHA_PUBLICACION', 'N_URL', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277__K1_K20', 'N_ID', 'N_FECHA_CAPTURA'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K4_K25_K1_5201', 'N_ID', 'N_ME_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_93620880_K20_K1', 'N_ID', 'N_FECHA_CAPTURA'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K1_K5_16_21_28_30', 'N_ID', 'N_TN_ID', 'N_AUTOR3', 'N_FECHA_PUBLICACION', 'N_URL', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K1_K25_K4', 'N_ID', 'N_ME_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K20', 'N_ID', 'N_FECHA_CAPTURA'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K5_K1_16_21_28_30', 'N_ID', 'N_TN_ID', 'N_AUTOR3', 'N_FECHA_PUBLICACION', 'N_URL', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K1_K20', 'N_ID', 'N_FECHA_CAPTURA'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K25_K1_K4', 'N_ID', 'N_ME_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277__K1_3_21_28_30', 'N_ID', 'N_AG_ID', 'N_FECHA_PUBLICACION', 'N_URL', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_93620880_K1_K20', 'N_ID', 'N_FECHA_CAPTURA'),
        Index('_dta_index_K_NOTA_5_2030630277__K1_14_21_28_30', 'N_ID', 'N_AUTOR1', 'N_FECHA_PUBLICACION', 'N_URL', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K1_K4_K25', 'N_ID', 'N_ME_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K20_K1', 'N_ID', 'N_FECHA_CAPTURA'),
        Index('_dta_index_K_NOTA_5_2030630277__K1_14_16_21_28_30', 'N_ID', 'N_AUTOR1', 'N_AUTOR3', 'N_FECHA_PUBLICACION', 'N_URL', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277__K4_K1_K5_K25_2_3_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K1_K25_K4_6497', 'N_ID', 'N_ME_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277__K1_21_28_29_30', 'N_ID', 'N_FECHA_PUBLICACION', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277__K5_K25_K4_K1_2_3_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277__K1_K5_21_28_30', 'N_ID', 'N_TN_ID', 'N_FECHA_PUBLICACION', 'N_URL', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277__K1_15_21_28', 'N_ID', 'N_AUTOR2', 'N_FECHA_PUBLICACION', 'N_URL'),
        Index('_dta_index_K_NOTA_5_2030630277__K25_K1_K5_K4_2_3_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277__K5_K1_21_28_30', 'N_ID', 'N_TN_ID', 'N_FECHA_PUBLICACION', 'N_URL', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277__K1_16_21_22_28_30', 'N_ID', 'N_AUTOR3', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_URL', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277__K5_K4_K25_K1', 'N_ID', 'N_ME_ID', 'N_TN_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K1_K5_21_28_30', 'N_ID', 'N_TN_ID', 'N_FECHA_PUBLICACION', 'N_URL', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277__K1_K5_K4_K25', 'N_ID', 'N_ME_ID', 'N_TN_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277__K1_14_21_22_28', 'N_ID', 'N_AUTOR1', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_URL'),
        Index('_dta_index_K_NOTA_5_2030630277__K5_K4_K25', 'N_ME_ID', 'N_TN_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K5_K1_21_28_30', 'N_ID', 'N_TN_ID', 'N_FECHA_PUBLICACION', 'N_URL', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277__K1_29_30', 'N_ID', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277__K1_K5_K25_K4_2_3_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277__K1_K6_7', 'N_ID', 'N_SEC_ID', 'N_PRG_ID'),
        Index('_dta_index_K_NOTA_5_2030630277__K1_14_15_21_28', 'N_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_FECHA_PUBLICACION', 'N_URL'),
        Index('_dta_index_K_NOTA_5_2030630277__K1_K5_K4_K25_2_3_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277__K6_K1_7', 'N_ID', 'N_SEC_ID', 'N_PRG_ID'),
        Index('_dta_index_K_NOTA_5_2030630277__K1_K5_14_21_28', 'N_ID', 'N_TN_ID', 'N_AUTOR1', 'N_FECHA_PUBLICACION', 'N_URL'),
        Index('_dta_index_K_NOTA_5_2030630277_82397080_K25_K1_K5_K4_2_3_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K6_K1_7', 'N_ID', 'N_SEC_ID', 'N_PRG_ID'),
        Index('_dta_index_K_NOTA_5_2030630277__K5_K1_14_21_28', 'N_ID', 'N_TN_ID', 'N_AUTOR1', 'N_FECHA_PUBLICACION', 'N_URL'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K1_K5_K25_K4_2_3_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K1_K5_14_21_28', 'N_ID', 'N_TN_ID', 'N_AUTOR1', 'N_FECHA_PUBLICACION', 'N_URL'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K1_K6_7', 'N_ID', 'N_SEC_ID', 'N_PRG_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K1_K5_K4_K25', 'N_ID', 'N_ME_ID', 'N_TN_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K5_K1_14_21_28', 'N_ID', 'N_TN_ID', 'N_AUTOR1', 'N_FECHA_PUBLICACION', 'N_URL'),
        Index('_dta_index_K_NOTA_5_2030630277__K1_K5_3', 'N_ID', 'N_AG_ID', 'N_TN_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_82397080_K1_K5_K4_K25_2_3_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277__K5_K1_3', 'N_ID', 'N_AG_ID', 'N_TN_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_82397080_K5', 'N_TN_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277__K1_16_21_28_30', 'N_ID', 'N_AUTOR3', 'N_FECHA_PUBLICACION', 'N_URL', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K1_K5_3', 'N_ID', 'N_AG_ID', 'N_TN_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_82397080_K5_K4_K25_K1', 'N_ID', 'N_ME_ID', 'N_TN_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277__K1_22', 'N_ID', 'N_FEHCA_VENCIMIENTO'),
        Index('_dta_index_K_NOTA_5_2030630277__K1_14', 'N_ID', 'N_AUTOR1'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K5_K1_3', 'N_ID', 'N_AG_ID', 'N_TN_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K1_K5_K4_K25_2_3_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277__K1_21_22', 'N_ID', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO'),
        Index('_dta_index_K_NOTA_5_2030630277_82397080_K5_K25_K4_K1_2_3_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277__K1_7', 'N_ID', 'N_PRG_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K20_K25_K1', 'N_ID', 'N_SEC_ID', 'N_FECHA_CAPTURA', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K5_K4_K1', 'N_ID', 'N_ME_ID', 'N_TN_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K1_K4_K25_2_3_5_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K1_4', 'N_ID', 'N_ME_ID'),
        Index('_dta_index_K_NOTA_5_2030630277__K1_22_28', 'N_ID', 'N_FEHCA_VENCIMIENTO', 'N_URL'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K4_K20_K25_K6_K5_K1_3_14_21_28_29_1227', 'N_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_AUTOR1', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_VISIBLE', 'N_URL', 'N_COSTO'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K20_K1', 'N_ID', 'N_FECHA_CAPTURA'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K5_K1_K4_4364', 'N_ID', 'N_ME_ID', 'N_TN_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K1_K4_K5_K7_K6_K3_2_14_15_16_17_20_21_22_23_24_25_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K1_K5_K7_K4_K6_K3_2_14_15_16_17_20_21_22_23_24_25_26_27_28_29_30_8526', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277__K26_K4', 'N_ME_ID', 'N_EN_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K20_K25_K4_K6_1783', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_FECHA_CAPTURA', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277__K4_K2_6_20', 'N_USU_ID', 'N_ME_ID', 'N_SEC_ID', 'N_FECHA_CAPTURA'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K4_K5_K1', 'N_ID', 'N_ME_ID', 'N_TN_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K1_K4_K23_2_3_5_6_7_14_15_16_17_20_21_22_24_25_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_93620880_K4_K6_K20_K25', 'N_ME_ID', 'N_SEC_ID', 'N_FECHA_CAPTURA', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277__K26_K2', 'N_USU_ID', 'N_EN_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K1_K4_K23_2_3_5_6_7_14_15_16_17_20_21_22_24_25_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277__K1_21_28', 'N_ID', 'N_FECHA_PUBLICACION', 'N_URL'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K5_K1_4', 'N_ID', 'N_ME_ID', 'N_TN_ID'),
        Index('_dta_index_K_NOTA_5_2030630277__K1_K4_K5_K25_2_3_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K5_K1_8066', 'N_ID', 'N_ME_ID', 'N_TN_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_93620880_K4_K20_K25', 'N_ME_ID', 'N_FECHA_CAPTURA', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K23D_1_2_3_4_5_6_7_14_15_16_17_20_21_22_24_25_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277__K20_K25_K1_K6_K4_K5_3_14_21_28_29', 'N_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_AUTOR1', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_VISIBLE', 'N_URL', 'N_COSTO'),
        Index('_dta_index_K_NOTA_5_2030630277__K5_K1_K4_K25_2_3_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K4_K5_K1_1912', 'N_ID', 'N_ME_ID', 'N_TN_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K4_K20_K25_K6_K5_K1_3_14_21_28_29_4179', 'N_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_AUTOR1', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_VISIBLE', 'N_URL', 'N_COSTO'),
        Index('_dta_index_K_NOTA_5_2030630277__K4_K5_K25_K1_2_3_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_51857256_K4_K25_K1_2_3_5_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K20_K25_K4_K6_8086', 'N_ME_ID', 'N_SEC_ID', 'N_FECHA_CAPTURA', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277__K1_K4_K5_K25', 'N_ID', 'N_ME_ID', 'N_TN_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K1_K5_K4_4149', 'N_ID', 'N_ME_ID', 'N_TN_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K20_K25_K6', 'N_SEC_ID', 'N_FECHA_CAPTURA', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277__K4_K5_K25_K1', 'N_ID', 'N_ME_ID', 'N_TN_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K4_K1_K5_5201', 'N_ID', 'N_ME_ID', 'N_TN_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_82397080_K1_K4_K5_K25_2_3_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_106796536_K4_K1_K5_K25_K2_K3_K6_K7_K14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K1_K4_K5_K7_K6_K3_2_14_15_16_17_20_21_22_23_24_25_26_27_28_29_30_8341', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K25_K6_K4_K5_K1_K20_3_14_21_28_29', 'N_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_AUTOR1', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_VISIBLE', 'N_URL', 'N_COSTO'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K20_K25_K1_8221', 'N_ID', 'N_TN_ID', 'N_FECHA_CAPTURA', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_93568736_K2_K1_K20_3_4_5_6_7_14_15_16_17_21_22_23_24_25_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K1_K4_K5_K25', 'N_ID', 'N_ME_ID', 'N_TN_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K5_K4_K1_6497', 'N_ID', 'N_ME_ID', 'N_TN_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_93620880_K20_K25_K1_K6_K4_K5_3_14_21_28_29', 'N_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_AUTOR1', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_VISIBLE', 'N_URL', 'N_COSTO'),
        Index('_dta_index_K_NOTA_5_2030630277_93568736_K4_K1', 'N_ID', 'N_ME_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_93614016_K20', 'N_FECHA_CAPTURA', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K4_K5_K25_K1_2_3_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K1_2_3_4_5_6_7_14_15_16_17_20_21_22_23_24_25_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_93568736_K5_K4_K25_K1_2_3_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_106796312_K1_K5_K4_K25_K2_K3_K6_K7_K14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K20_K25_K1_1828', 'N_ID', 'N_ME_ID', 'N_FECHA_CAPTURA', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_82397080_K4_K5_K25_K1', 'N_ID', 'N_ME_ID', 'N_TN_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277__K1_25', 'N_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_51857256_K4_K25', 'N_ME_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K20_K25_K4_5247', 'N_ID', 'N_ME_ID', 'N_FECHA_CAPTURA', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277__K2_K20', 'N_USU_ID', 'N_FECHA_CAPTURA'),
        Index('_dta_index_K_NOTA_5_2030630277_51857368_K5_K1', 'N_ID', 'N_TN_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K1_4', 'N_ID', 'N_ME_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K5_K20_K25', 'N_TN_ID', 'N_SEC_ID', 'N_FECHA_CAPTURA', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277__K20_K2', 'N_USU_ID', 'N_FECHA_CAPTURA'),
        Index('_dta_index_K_NOTA_5_2030630277_82397080_K1_K4_K5_K25', 'N_ID', 'N_ME_ID', 'N_TN_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277__K26_K2_K20', 'N_USU_ID', 'N_FECHA_CAPTURA', 'N_EN_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_51857368_K4_K25_K1', 'N_ID', 'N_ME_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K20_K25_K6_8444', 'N_TN_ID', 'N_SEC_ID', 'N_FECHA_CAPTURA', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277__K25_K5_K1_2_3_4_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_93614016_K20_K25_K4', 'N_ME_ID', 'N_FECHA_CAPTURA', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K4_K5_K25_K1', 'N_ID', 'N_ME_ID', 'N_TN_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_51857256_K4_K25_K1', 'N_ID', 'N_ME_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277__K1_K25_K5_2_3_4_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277__K5_K4_K25_K1_2_3_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_93620880_K25_K6_K4_K5_K1_K20_3_14_21_28_29', 'N_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_AUTOR1', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_VISIBLE', 'N_URL', 'N_COSTO'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K1_K4_K5_K25_2_3_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_82397080_K25_K5_K1_2_3_4_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277__K4_K25_K1_2_3_5_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30_4149', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_93620880_K6_K4_K5_K1_K20_K25_3_14_21_28_29', 'N_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_AUTOR1', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_VISIBLE', 'N_URL', 'N_COSTO'),
        Index('_dta_index_K_NOTA_5_2030630277_82397080_K5_K1_K4_K25_2_3_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K1_K25_K5_2_3_4_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_51857256_K1_K4_K25_2_3_5_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_93614016_K20_K25_K6', 'N_SEC_ID', 'N_FECHA_CAPTURA', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K5_K1_K4_K25_2_3_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K25_K5_K1_2_3_4_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277__K4_K25_K5_K1_2_3_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30_4364', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277__K5_K1_K2_K4_3_6_7_14_15_16_17_20_21_22_23_24_25_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_82397080_K4_K5_K25_K1_2_3_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_82397080_K1_K25_K5_2_3_4_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277__K1_K25_9987', 'N_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K20_K25_K6_4960', 'N_ME_ID', 'N_SEC_ID', 'N_FECHA_CAPTURA', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277__K23D_1_2_3_4_5_6_7_14_15_16_17_20_21_22_24_25_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K2_K1_K20_3_4_5_6_7_14_15_16_17_21_22_23_24_25_26_27_28_29_30_4364_8066', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277__K1_K25_K5', 'N_ID', 'N_TN_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K1_K5_K7_K4_K6_K3_2_14_15_16_17_20_21_22_23_24_25_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_51857256_K1_K4_K25', 'N_ID', 'N_ME_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K6_K4_K5_K1_K20_K25_3_14_21_28_29_2679', 'N_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_AUTOR1', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_VISIBLE', 'N_URL', 'N_COSTO'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K5_K4_K25_K1_2_3_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30_1912', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277__K5_K1_K25_2_3_4_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K5_K20_K25_K6_K4_K1_3_14_21_28_29_5944', 'N_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_AUTOR1', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_VISIBLE', 'N_URL', 'N_COSTO'),
        Index('_dta_index_K_NOTA_5_2030630277__K4_K2_20_8066', 'N_USU_ID', 'N_ME_ID', 'N_FECHA_CAPTURA'),
        Index('_dta_index_K_NOTA_5_2030630277__K25_K4_K1_2_3_5_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277__K25_K5_K1', 'N_ID', 'N_TN_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_106796984_K1_K5_K4_K25', 'N_ID', 'N_ME_ID', 'N_TN_ID', 'N_VISIBLE', 'N_EN_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K5_K20_K25_7204', 'N_TN_ID', 'N_FECHA_CAPTURA', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277__K4_K1_K25_2_3_5_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30_8066', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K25_K4_K1_2_3_5_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_82397080_K5_K1_K25_2_3_4_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K1_K5_K4_K25_K2_K3_K6_K7_K14_15_16_17_20_21_22_23_24_26_27_28_29_30_7022', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_93614016_K4_K6_K20_K25_K5_K1_3_14_21_28_29', 'N_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_AUTOR1', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_VISIBLE', 'N_URL', 'N_COSTO'),
        Index('_dta_index_K_NOTA_5_2030630277_51856808_K25_K1_2_3_5_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K1_K25_K4_2_3_5_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_82397080_K1_K25_K5', 'N_ID', 'N_TN_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_93614016_K20_K25_K4_K6_K5_K1_3_14_21_28_29', 'N_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_AUTOR1', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_VISIBLE', 'N_URL', 'N_COSTO'),
        Index('_dta_index_K_NOTA_5_2030630277__K1_K4_K25_9987', 'N_ID', 'N_ME_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_82397080_K25_K4_K1_2_3_5_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K6_K1_9085', 'N_ID', 'N_ME_ID', 'N_SEC_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_93614016_K20_K25_K6_K4_K5_K1_3_14_21_28_29', 'N_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_AUTOR1', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_VISIBLE', 'N_URL', 'N_COSTO'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K5_K1_K25_2_3_4_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_97758080_K1_K2_K5_K4_K25_K3_K6_K7_K14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277__K1_2_3_5_6_7_14_15_16_17_20_21_22_23_24_25_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_51856808_K25_K1', 'N_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K5_K20_K25_4312', 'N_ME_ID', 'N_TN_ID', 'N_FECHA_CAPTURA', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K1_K25_K5', 'N_ID', 'N_TN_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_51856808_K2_K1_K20_3_4_5_6_7_14_15_16_17_21_22_23_24_25_26_27_28_29_30_5201', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277__K1_K25_2_3_5_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K4_K20_K25_K6_K5_K1_3_14_21_28_29_3177', 'N_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_AUTOR1', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_VISIBLE', 'N_URL', 'N_COSTO'),
        Index('_dta_index_K_NOTA_5_2030630277__K1_4', 'N_ID', 'N_ME_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_51856808_K1_K25_2_3_5_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277__K25_K1_2_3_5_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_82397080_K25_K5_K1', 'N_ID', 'N_TN_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K20_K25_K4_K6_2441', 'N_ID', 'N_ME_ID', 'N_SEC_ID', 'N_FECHA_CAPTURA', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_51857368_K4_K25_K1_2_3_5_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K25_K1_2_3_5_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K25_K5_K1', 'N_ID', 'N_TN_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_51856808_K4_K25_K1_2_3_5_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K1_K25_2_3_5_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K20_K25_K1_2780', 'N_ID', 'N_FECHA_CAPTURA', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277__K4_K25_4364', 'N_ME_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_82397080_K1_K25_2_3_5_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277__K4_K5_K1_2_3_6_7_14_15_16_17_20_21_22_23_24_25_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K4_K6_K20_K25_5247', 'N_ME_ID', 'N_SEC_ID', 'N_FECHA_CAPTURA', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_51856808_K1_K4', 'N_ID', 'N_ME_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_82397080_K25_K1_2_3_5_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277__K1_K5_K4_2_3_6_7_14_15_16_17_20_21_22_23_24_25_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K20_K25_K6_K4_K5_K1_3_14_21_28_29_8769', 'N_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_AUTOR1', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_VISIBLE', 'N_URL', 'N_COSTO'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K1_K4_K5_K7_K6_K3_2_14_15_16_17_20_21_22_23_24_25_26_27_28_29_30_6355', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277__K1_K4_K25_2_3_5_6_7_14_15_16_17_20_21_22_23_24_26_27_28_29_30_8066', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K1_K2_K5_K4_K25_6859', 'N_ID', 'N_USU_ID', 'N_ME_ID', 'N_TN_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277__K1_K5_K7_K4_K6_K3_2_14_15_16_17_20_21_22_23_24_25_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K25_K1_K5_K4_K2_K3_K6_K7_K14_15_16_17_20_21_22_23_24_26_27_28_29_30_589', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277__K6_K1_K5_K7_K4_K3_2_14_15_16_17_20_21_22_23_24_25_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K1_K5_21_28', 'N_ID', 'N_TN_ID', 'N_FECHA_PUBLICACION', 'N_URL'),
        Index('_dta_index_K_NOTA_5_2030630277_105562056_K1_K2_K5_K4_K25', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K1_K5_8066', 'N_ID', 'N_TN_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K1_K5_K7_K4_K6_K3_2_14_15_16_17_20_21_22_23_24_25_26_27_28_29_30_1040', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277__K1_K6_K4_K7_K20_2_3_5_14_15_16_17_21_22_23_24_25_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K4_K1_K5_K7_K6_K3_2_14_15_16_17_20_21_22_23_24_25_26_27_28_29_30_8066', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K5_K1_21_28', 'N_ID', 'N_TN_ID', 'N_FECHA_PUBLICACION', 'N_URL'),
        Index('_dta_index_K_NOTA_5_2030630277__K20D_K1_K4_K6_K7_2_3_5_14_15_16_17_21_22_23_24_25_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277__K20D_K1', 'N_ID', 'N_FECHA_CAPTURA'),
        Index('_dta_index_K_NOTA_5_2030630277__K1_K5_21_28', 'N_ID', 'N_TN_ID', 'N_FECHA_PUBLICACION', 'N_URL'),
        Index('_dta_index_K_NOTA_5_2030630277__K6_K1_K4_K7_K20_2_3_5_14_15_16_17_21_22_23_24_25_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277__K14_1', 'N_ID', 'N_AUTOR1'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K6_K1_K5_K7_K4_K3_2_14_15_16_17_20_21_22_23_24_25_26_27_28_29_30_9987', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277__K1_K20D', 'N_ID', 'N_FECHA_CAPTURA'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K1_K2_K5_K4_K25_K3_K6_K7_K14_15_16_17_20_21_22_23_24_26_27_28_29_30_5454', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K1_4364', 'N_ID', 'N_TN_ID'),
        Index('_dta_index_K_NOTA_5_2030630277__K1_K20_2_3_4_5_6_7_14_15_16_17_21_22_23_24_25_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K1_K4_K5_K7_K6_K3_2_14_15_16_17_20_21_22_23_24_25_26_27_28_29_30_6497', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277__K20D_K1_2_3_4_5_6_7_14_15_16_17_21_22_23_24_25_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K5_K1_9987', 'N_ID', 'N_TN_ID'),
        Index('_dta_index_K_NOTA_5_2030630277__K1_K20D_K4_K6_K7_2_3_5_14_15_16_17_21_22_23_24_25_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277__K5_K1_21_28', 'N_ID', 'N_TN_ID', 'N_FECHA_PUBLICACION', 'N_URL'),
        Index('_dta_index_K_NOTA_5_2030630277__K4_K6_K7_K1_K20_2_3_5_14_15_16_17_21_22_23_24_25_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277__K4_K1_K6_K7_K20_2_3_5_14_15_16_17_21_22_23_24_25_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277__K1_K6', 'N_ID', 'N_SEC_ID'),
        Index('_dta_index_K_NOTA_5_2030630277__K14_K4_1', 'N_ID', 'N_ME_ID', 'N_AUTOR1'),
        Index('_dta_index_K_NOTA_5_2030630277__K1_K6_K5_K7_K4_K3_2_14_15_16_17_20_21_22_23_24_25_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277__K1_K4_K6_K7_K20_2_3_5_14_15_16_17_21_22_23_24_25_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K25_K1_K5_K4_K2_K3_K6_K7_K14_15_16_17_20_21_22_23_24_26_27_28_29_30_8862', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K20D_K1_K4_K6_K7_2_3_5_14_15_16_17_21_22_23_24_25_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_97757800_K1_K5_K4_K25', 'N_ID', 'N_ME_ID', 'N_TN_ID', 'N_AUTOR1', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K4_K1_K6_K7_K20_2_3_5_14_15_16_17_21_22_23_24_25_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K4_K6_K7_K1_K20_2_3_5_14_15_16_17_21_22_23_24_25_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_106796032_K4', 'N_ME_ID', 'N_URL'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K1_K20D_K4_K6_K7_2_3_5_14_15_16_17_21_22_23_24_25_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K5_K1_K7_K4_K6_K3_2_14_15_16_17_20_21_22_23_24_25_26_27_28_29_30_1912', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K1_K6_K4_K7_K20_2_3_5_14_15_16_17_21_22_23_24_25_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K4_K1_K6_K7_K20_2_3_5_14_15_16_17_21_22_23_24_25_26_27_28_29_30_9987', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K4_K6_K7_K1_K20_2_3_5_14_15_16_17_21_22_23_24_25_26_27_28_29_30_4364', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K6_K1_K4_K7_K20_2_3_5_14_15_16_17_21_22_23_24_25_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277__K4_K1_K14', 'N_ID', 'N_ME_ID', 'N_AUTOR1'),
        Index('_dta_index_K_NOTA_5_2030630277_97757800_K4_K1', 'N_ID', 'N_ME_ID', 'N_AUTOR1'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K1_K6_K4_K7_K20_2_3_5_14_15_16_17_21_22_23_24_25_26_27_28_29_30_8066', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K1_K20D', 'N_ID', 'N_SEC_ID', 'N_FECHA_CAPTURA'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K5_K4_K25_K1_9857', 'N_ID', 'N_ME_ID', 'N_TN_ID', 'N_PRG_ID', 'N_VISIBLE'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K6_K1_K4_K7_K20_2_3_5_14_15_16_17_21_22_23_24_25_26_27_28_29_30_1912', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K1_K20D_4149', 'N_ID', 'N_ME_ID', 'N_FECHA_CAPTURA'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K1_K4_K6_K7_K20_2_3_5_14_15_16_17_21_22_23_24_25_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K20D_K1_2_3_4_5_6_7_14_15_16_17_21_22_23_24_25_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K1_K6_4149', 'N_ID', 'N_SEC_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K20D_K1', 'N_ID', 'N_SEC_ID', 'N_FECHA_CAPTURA'),
        Index('_dta_stat_2030630277_1_2_3_4_5_6_7_14', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K6_K1_5201', 'N_ID', 'N_SEC_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K1_K4_K6_K7_K20_2_3_5_14_15_16_17_21_22_23_24_25_26_27_28_29_30_5201', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K1_K6_K5_K7_K4_K3_2_14_15_16_17_20_21_22_23_24_25_26_27_28_29_30_4364', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K20D_K1_2_3_4_5_6_7_14_15_16_17_21_22_23_24_25_26_27_28_29_30_6497', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K20D_K1_1040', 'N_ID', 'N_ME_ID', 'N_FECHA_CAPTURA'),
        Index('_dta_index_K_NOTA_5_2030630277_100452352_K5_6636', 'N_TN_ID', 'N_PRG_ID'),
        Index('_dta_index_K_NOTA_5_2030630277_104889936_K1_K20_2_3_4_5_6_7_14_15_16_17_21_22_23_24_25_26_27_28_29_30', 'N_ID', 'N_USU_ID', 'N_AG_ID', 'N_ME_ID', 'N_TN_ID', 'N_SEC_ID', 'N_PRG_ID', 'N_AUTOR1', 'N_AUTOR2', 'N_AUTOR3', 'N_AUTOR4', 'N_FECHA_CAPTURA', 'N_FECHA_PUBLICACION', 'N_FEHCA_VENCIMIENTO', 'N_FECHA_NOTA', 'N_FECHA_INSERT', 'N_VISIBLE', 'N_EN_ID', 'N_TCN_ID', 'N_URL', 'N_COSTO', 'N_COSTO_DES')
    )

    N_ID = Column(BigInteger, primary_key=True, index=True)
    N_USU_ID = Column(BigInteger, nullable=False, index=True)
    N_AG_ID = Column(ForeignKey('C_AGENCIA.AG_ID'))
    N_ME_ID = Column(ForeignKey('C_MEDIO.ME_ID'), index=True)
    N_TN_ID = Column(ForeignKey('C_TIPO_NOTA.TN_ID'), nullable=False, index=True)
    N_SEC_ID = Column(ForeignKey('C_SECCION.SEC_ID'), index=True)
    N_PRG_ID = Column(ForeignKey('C_PROGRAMA.PRG_ID'))
    N_TITULO = Column(TEXT(2147483647, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    N_NOTA = Column(TEXT(2147483647, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    N_BALAZO1 = Column(TEXT(2147483647, 'SQL_Latin1_General_CP1_CI_AS'))
    N_BALAZO2 = Column(TEXT(2147483647, 'SQL_Latin1_General_CP1_CI_AS'))
    N_BALAZO3 = Column(TEXT(2147483647, 'SQL_Latin1_General_CP1_CI_AS'))
    N_BALAZO4 = Column(TEXT(2147483647, 'SQL_Latin1_General_CP1_CI_AS'))
    N_AUTOR1 = Column(String(500, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    N_AUTOR2 = Column(String(500, 'SQL_Latin1_General_CP1_CI_AS'))
    N_AUTOR3 = Column(String(500, 'SQL_Latin1_General_CP1_CI_AS'))
    N_AUTOR4 = Column(String(500, 'SQL_Latin1_General_CP1_CI_AS'))
    N_KIKER = Column(TEXT(2147483647, 'SQL_Latin1_General_CP1_CI_AS'))
    N_OPCIONALES = Column(TEXT(2147483647, 'SQL_Latin1_General_CP1_CI_AS'))
    N_FECHA_CAPTURA = Column(DateTime, nullable=False, index=True)
    N_FECHA_PUBLICACION = Column(DateTime, nullable=False)
    N_FEHCA_VENCIMIENTO = Column(DateTime, nullable=False)
    N_FECHA_NOTA = Column(DateTime, nullable=False)
    N_FECHA_INSERT = Column(DateTime, nullable=False)
    N_VISIBLE = Column(Integer, nullable=False, index=True)
    N_EN_ID = Column(Integer, nullable=False, index=True)
    N_TCN_ID = Column(Integer, nullable=False)
    N_URL = Column(String(5000, 'SQL_Latin1_General_CP1_CI_AS'))
    N_COSTO = Column(String(5000, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    N_COSTO_DES = Column(String(5000, 'SQL_Latin1_General_CP1_CI_AS'))

    C_AGENCIA = relationship('CAGENCIA')
    C_MEDIO = relationship('CMEDIO')
    C_PROGRAMA = relationship('CPROGRAMA')
    C_SECCION = relationship('CSECCION')
    C_TIPO_NOTA = relationship('CTIPONOTA')


class KALERTA(Base):
    __tablename__ = 'K_ALERTA'

    AL_ID = Column(Integer, primary_key=True)
    AL_SA_ID = Column(ForeignKey('K_SUSCRIPTOR_ALERTA.SA_ID'))
    AL_SAD_ID = Column(ForeignKey('K_SUSCRIPTOR_ALERTA_DETALLE.SAD_ID'))
    AL_N_ID = Column(ForeignKey('K_NOTA.N_ID'))
    AL_TW_ID = Column(BigInteger)
    AL_ESTATUS = Column(String(300, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    AL_ACEPTADA_RECAZADA = Column(String(300, 'SQL_Latin1_General_CP1_CI_AS'))
    AL_FECHA_ENVIO = Column(DateTime)
    AL_FECHA_CREADA = Column(DateTime, nullable=False)
    AL_USU_ENVIA = Column(String(2000, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    AL_LOG = Column(String(collation='SQL_Latin1_General_CP1_CI_AS'), nullable=False)

    K_NOTA = relationship('KNOTA')
    K_SUSCRIPTOR_ALERTA_DETALLE = relationship('KSUSCRIPTORALERTADETALLE')
    K_SUSCRIPTOR_ALERTA = relationship('KSUSCRIPTORALERTA')


class KNOTACLASIFICACION(Base):
    __tablename__ = 'K_NOTA_CLASIFICACION'

    NCL_ID = Column(Integer, primary_key=True)
    NCL_CL_ID = Column(ForeignKey('C_CLASIFICACION.CL_ID'), nullable=False)
    NCL_N_ID = Column(ForeignKey('K_NOTA.N_ID'), nullable=False)

    C_CLASIFICACION = relationship('CCLASIFICACION')
    K_NOTA = relationship('KNOTA')


class KNOTAGRUPO(Base):
    __tablename__ = 'K_NOTA_GRUPO'
    __table_args__ = (
        Index('_dta_index_K_NOTA_GRUPO_5_932198371__K2_1_3_4', 'NG_ID', 'NG_N_ID', 'NG_MSG_ID', 'NG_VALOR'),
    )

    NG_ID = Column(Integer, primary_key=True)
    NG_N_ID = Column(ForeignKey('K_NOTA.N_ID'), nullable=False)
    NG_MSG_ID = Column(ForeignKey('K_MENU_SUSCRIPTOR_GRUPO.MSG_ID'), nullable=False)
    NG_VALOR = Column(String(2000, 'SQL_Latin1_General_CP1_CI_AS'))

    K_MENU_SUSCRIPTOR_GRUPO = relationship('KMENUSUSCRIPTORGRUPO')
    K_NOTA = relationship('KNOTA')


class KNOTATEMA(Base):
    __tablename__ = 'K_NOTA_TEMA'
    __table_args__ = (
        Index('_dta_index_K_NOTA_TEMA_5_43147199_93906392_K9_2_4', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51856808_K2_K9_K7', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70951968_K9_K1_K7', 'NT_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51875920_K9_K1_K7_2_4_5_6_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49273568_K1_K9', 'NT_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K6_K7_K2_K1_6355', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_104889936_K2_K9_K7_4', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51855688_K9_K7', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51857480_K1_K9', 'NT_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49273568_K1_K9_K7_2_4_5_6_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70952584_K9_K1_K7_2_4_5_6_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51856808_K9_K6_K7_K2_K1', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70952136_K1_K9', 'NT_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_104889936_K7_K2_K9_4', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51855688_K9_K7_2', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51857480_K1_K9_K7_2_4_5_6_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49273568_K1_K7_2_4_5_6_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51856808_K9_K7_K2_K6_K1', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51857480_K1_K7_2_4_5_6_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49275192_K7_K9_K1_2_4_5_6_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70952136_K1_K9_K7_2_4_5_6_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_93906392_K2_K9', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51856808_K9_K7_K2_K1_K6', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51875920_K7_K9_K1_2_4_5_6_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49274968_K1_K9', 'NT_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70952136_K1_K7_2_4_5_6_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51856808_K9_K7', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51856808_K7_K9_K6_K2_K1', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_93906392_K9_K2', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51857424_K1_K9', 'NT_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70952584_K7_K9_K1_2_4_5_6_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51875920_K9_K7', 'NT_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49273680_K7', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51856808_K9_K7_2', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70951968_K1_K9', 'NT_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51875528_K7', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49275192_K9_K7_K1_2_4_5_6_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51857424_K7', 'NT_ID', 'NT_VISIBLE'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_93906392_K2', 'NT_N_ID', 'NT_VISIBLE'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51856808_K7', 'NT_N_ID', 'NT_VISIBLE'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51875920_K9_K7_K1_2_4_5_6_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51856808_K6_K9_K7_K2_K1', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49273568_K7_K1_2_4_5_6_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70953368_K7', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_104889936_K9_K7_K2_4', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51855688_K9', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51857480_K7_K1_2_4_5_6_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51856808_K9_K6_K7', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49273680_K9_K1', 'NT_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70952584_K9_K7_K1_2_4_5_6_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51855688_K7_K9_K2', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51875528_K9_K1', 'NT_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70952136_K7_K1_2_4_5_6_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_104889936_K9_K2_4', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49273680_K9_K1_K7', 'NT_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51857480_K9', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70953368_K9_K1', 'NT_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K7_K2_K1_9987', 'NT_ID', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51875528_K9_K1_K7', 'NT_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_93906392_K9_K2_4', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51857368_K9_K6_K7', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49275136_K9_K1_K7_2_4_5_6_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70953368_K9_K1_K7', 'NT_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K7_K9_K6_K2_K1_4364', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51874520_K9_K1_K7_2_4_5_6_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49275192_K1_K9_K7_2_4_5_6_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_100452352_K8', 'NT_N_ID', 'NT_USU_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51856808_K9_K7_K6_K2_K1', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51875920_K1_K9_K7_2_4_5_6_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49275192_K1_K7_2_4_5_6_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70953032_K9_K1_K7_2_4_5_6_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_100452352_K8_K2_K9', 'NT_N_ID', 'NT_USU_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K2_K9_K6_K7_8066', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51875808_K9_K7', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51875920_K1_K7_2_4_5_6_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49275136_K7_K9_K1_2_4_5_6_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70952584_K1_K9_K7_2_4_5_6_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K2_4149', 'NT_N_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K7_K2_K1_K6_1912', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51857480_K9_K6_K7', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51874520_K7_K9_K1_2_4_5_6_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49273568_K1_K9_K7', 'NT_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70952584_K1_K7_2_4_5_6_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51857368_K9', 'NT_N_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51857480_K1_K9_K7', 'NT_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70953032_K7_K9_K1_2_4_5_6_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51856808_K6', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49273680_K1_K9', 'NT_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51857368_K2_K9', 'NT_N_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70952136_K1_K9_K7', 'NT_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K7_K2_K6_K1_5201', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51856808_K1_K2_K9_K7_K6', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51875528_K1_K9', 'NT_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49275136_K9_K7_K1_2_4_5_6_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51857368_K9_K2', 'NT_N_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51857424_K9', 'NT_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70953368_K1_K9', 'NT_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K2_K9_K7_K1_K6_6497', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51874520_K9_K7_K1_2_4_5_6_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49273568_K9_K7_K1', 'NT_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51857368_K9_K7_K2', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51857480_K9_K7_K1', 'NT_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70953032_K9_K7_K1_2_4_5_6_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K1_K2_K9_K6_K7_1040', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49275192_K7_K1_2_4_5_6_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K7_2_1912', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51857480_K6', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70952136_K9_K7_K1', 'NT_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51875920_K7_K1_2_4_5_6_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49274968_K1_K9_K7', 'NT_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K7_K2_1040', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K2_K9_K7_K6_K1_1771', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51856808_K2_K9_K7_K6_K1', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51857424_K1_K9_K7', 'NT_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70952584_K7_K1_2_4_5_6_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51856808_K2_K9_K7_K1_K6', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49275136_K1_K9_K7_2_4_5_6_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K7_K9_K2_8809', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K2_K9_K6_K7_K1_2533', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70951968_K1_K9_K7', 'NT_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51857480_K2_K9_K7', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49275136_K1_K7_2_4_5_6_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K7_4801', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K6_K7_K2_8258', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K2_K9_K7_4_5201', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51857368_K2_K9_K7', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49274968_K9_K7_K1', 'NT_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70953032_K1_K9_K7_2_4_5_6_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K2_K9_K7_2733', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70953032_K1_K7_2_4_5_6_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K6_K7_1410', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K7_2_4_1771', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49273568_K9_K1_K7_2_4_5_6_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51857424_K9_K6_K7', 'NT_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70951968_K9_K7_K1', 'NT_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51855688_K9_K7_K2', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49273568_K7_K9_K1_2_4_5_6_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K6_K9_K7_K2_K1_2894', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K2_K9_4_2533', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51857480_K9_K7_K2', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_1_2_4_5_6_7_8_10_9987_4364', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70952136_K9_K1_K7_2_4_5_6_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51856808_K9', 'NT_N_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K7_K2_4_8258', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K1_K2_K9_K7_K6_4864', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K2_1_4_5_6_7_8_9_10_9987_4364', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70952136_K7_K9_K1_2_4_5_6_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51855688_K2_K9_K7', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51875808_K7', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51856808_K2_K9_4', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K1_7_9987_4364', 'NT_ID', 'NT_VISIBLE'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K2_K9_K7_1_4_5_6_8_2533_8258_1410', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K2_K9_K7_K1_6960', 'NT_ID', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51856808_K2_K9_K6_K7', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51856808_K7_K9_K2', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K7_K2_1_4_5_6_8_4864', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51857480_K2_K9_4', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49273568_K9_K7_2', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K7_K6_K2_K1_9850', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51856808_K9_K6_K7_K2', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K7_K9_K2_1_4_5_6_8_9850', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51856808_K9_K7_K2', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51856808_K9_K7_2_4', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49273680_K9_2', 'NT_N_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70952808_K2_K9_K7_1_4_5_6_8', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K1_K2_K9_K7_9085', 'NT_ID', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51857424_K9_K7_K2', 'NT_ID', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_104889936_K9_K2', 'NT_N_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K2_1_4_5_6_7_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_104889936_K2_K1_4_5_6_7_8_9_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K8_K9', 'NT_USU_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_104889936_K9_K2_K1_4_5_6_7_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_2', 'NT_N_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_100452352_K9_2', 'NT_N_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_104889936_K9_K2_1_4_5_6_7_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_104889936_K2_K9_1_4_5_6_7_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K7_K2_K9', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K2_K9_K7_1_4_5_6_8', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_100452352_K9_K7', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K7_K2_1_4_5_6_8', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_93614016_K7_K2_K9', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K7_K9_K2_1_4_5_6_8', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_100452352_K7_K2_K9', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_104889936_K2_K9_K7_1_4_5_6_8', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_104889936_K9_2', 'NT_N_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_93906392_K2_K9_K7_1_4_5_6_8', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_96766016_K9_K7_K2_1_4_5_6_8', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_102839032_K9_K2', 'NT_N_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_104889936_K7_K9_K2_1_4_5_6_8', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_93906392_K7_K9_K2_1_4_5_6_8', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_102839032_K2', 'NT_N_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_104889936_K9_K7_K2_1_4_5_6_8', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_93906392_K9_K7_K2_1_4_5_6_8', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_96766016_K2_K9_K7_1_4_5_6_8', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_102839032_K2_K9', 'NT_N_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_96766016_K7_K9_K2_1_4_5_6_8', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_96766016_K2_K9', 'NT_N_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_96766016_K2_K9_K7', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_96766016_K2_K1_4_5_6_7_8_9_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_96766016_K9_K7_K2', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_96766016_K9_K2_K1_4_5_6_7_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_100452352_K7_K9_K2', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K4D_K9_K7_2', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K7_K4_2', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_93906392_K7_K9_K2', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K7_K9_K4_2', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K8_K2_K9', 'NT_N_ID', 'NT_USU_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_96766016_K7_K9_K4_2', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_104889936_K8', 'NT_N_ID', 'NT_USU_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_96766016_K9_K7', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_104889936_K8_K2_K9', 'NT_N_ID', 'NT_USU_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_96766016_K7', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K7_K9_K1_2_4_5_6_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_96766016_K9_K7_K4_2', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K7_K1_2_4_5_6_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K7_K1', 'NT_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_96766016_K4D_K9_K7_2', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K1_K9_K7', 'NT_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K7_K1_2_4_5_6_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K2_K9_1_4_5_6_7_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49239816_K2_K9_K7', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49274968_K9_K7_K2', 'NT_ID', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49273680_K2', 'NT_N_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K6_K7_K2_K1_8526', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49609384_K9_K7_K2', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_93906392_K6', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51856808_K1_K2_K9_K7', 'NT_ID', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49240096_K9_K7', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49273456_K1_K2_K9_K7', 'NT_ID', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_104889936_K2_K9_K7_K6_K1', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49273456_K9_K6_K7_K2_K1', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K2_K9_1_4_5_6_7_8_10_9987_4364_8066_1912', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51856808_K9_K7_K2_K1', 'NT_ID', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_104889936_K2_K9_K7_K1_K6', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49240096_K9_K7_2', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49273456_K9_K7_K2_K6_K1', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49273456_K9_K7_K2_K1', 'NT_ID', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49273680_K2_K9', 'NT_N_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K2_1_4_5_6_7_8_10_4149', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_93906392_K2_K9_K7', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51857424_K2_K9_K7', 'NT_ID', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49273456_K9_K7_K2_K1_K6', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49274968_K2_K9_K7', 'NT_ID', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49275136_K2_K9', 'NT_N_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49273456_K7_K9_K6_K2_K1', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K7_K9_K2_9987', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_100452352_K2_K9_K7', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51875808_K9', 'NT_FECHA_VENCIMIENTO', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49239816_K9_K7', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49275192_K9_K7', 'NT_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49273512_K9', 'NT_FECHA_VENCIMIENTO', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49275136_K2_K1_4_5_6_7_8_9_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51875920_K6', 'NT_ID', 'NT_FECHA_VENCIMIENTO'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49580264_K7_K9_K2', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_93906336_K9_K6_K7', 'NT_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49239816_K9_K7_2', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49275192_K6', 'NT_ID', 'NT_FECHA_VENCIMIENTO'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49275136_K9_K2_K1_4_5_6_7_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51856808_K1_K2_K9_K6_K7', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49274968_K7', 'NT_ID', 'NT_VISIBLE'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49273456_K1_K2_K9_K6_K7', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K4D_K9_K7_2_9987_4364', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49609272_K7_K9_K2', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_93906392_K9_K7_K2', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51875808_K9_K6_K7', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49239816_K7', 'NT_N_ID', 'NT_VISIBLE'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49273456_K9', 'NT_N_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49273512_K9_K6_K7', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K7_K4_2_8066', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49240096_K9', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49273456_K6_K9_K7_K2_K1', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49580264_K9_K7', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_93906448_K7', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49240096_K7_K9_K2', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49273456_K9_K6_K7', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_104889936_K2_K9_K6_K7', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51856808_K2_K9_K6_K7_K1', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K7_K9_K4_2_1912', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_1_2_4_5_6_7_8_10_9987_4364_8066_1912', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49273456_K2_K9_K6_K7_K1', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51857480_K9_K7', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K7_K2_K1_9987_4364', 'NT_ID', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49273568_K9', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49275136_K7_K9_K4_2', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_104889936_K9_K6_K7_K2', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49273568_K9_K7', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K2_1_4_5_6_7_8_9_10_9987_4364_8066_1912', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K7_K9_K6_K2_K1_8066', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49239816_K9_K6_K7', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K8_K9_9987_4364_8066_1912', 'NT_USU_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51875808_K9_K7_K2', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49275136_K9_K7', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_93906336_K9_K7_K2', 'NT_ID', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49273456_K9_K7', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_55412640_K9', 'NT_N_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K2_K9_K6_K7_1912', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49273456_K9_K7_K6_K2_K1', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51875808_K2_K9_K7', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49275136_K7', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_55428928_K2', 'NT_N_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_104889936_K1_K2_K9_K7', 'NT_ID', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49273512_K9_K7', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49273512_K9_K7_K2', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K7_K2_K1_K6_4149', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49275136_K9_K7_K4_2', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51856808_K2_K9_K7_K1', 'NT_ID', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_104889936_K9_K7_K2_K1', 'NT_ID', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49273568_K9_K6_K7', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49273512_K2_K9_K7', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_55428928_K2_K9', 'NT_N_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_93906336_K2_K9_K7', 'NT_ID', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K7_K2_K6_K1_6497', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49273456_K6', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51857368_K7', 'NT_N_ID', 'NT_VISIBLE'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49273456_K2_K9_K7_K1', 'NT_ID', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49275136_K4D_K9_K7_2', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49273456_K1_K2_K9_K7_K6', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_55428592_K9_2', 'NT_N_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_93906448_K9', 'NT_FECHA_VENCIMIENTO', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51856808_K2_K1_4_5_6_7_8_9_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K2_K9_K7_K1_K6_1040', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49273456_K7', 'NT_N_ID', 'NT_VISIBLE'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49273456_K9_K7_K2', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K2_K9_1_4_5_6_7_8_10_9987_4364', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_55428984_K7_K9_K2_1_4_5_6_8', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_93907544_K6', 'NT_ID', 'NT_FECHA_VENCIMIENTO'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51856808_K9_K2_K1_4_5_6_7_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K2_1_4_5_6_7_8_10_8066', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K1_K2_K9_K6_K7_1771', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_55412640_K9_2', 'NT_N_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_104889936_K1_K2_K9_K6_K7', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51856808_K2_K9', 'NT_N_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49274968_K9', 'NT_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49273456_K2_K9', 'NT_N_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K8_K9_9987_4364', 'NT_USU_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_55428592_K9', 'NT_N_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_93906448_K9_K6_K7', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K2_K9_K7_K6_K1_2533', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49273568_K6', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51856808_K9_K2', 'NT_N_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49273456_K9_K2', 'NT_N_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49273456_K2_K9_K7', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_55428984_K2_K9', 'NT_N_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K2_K9_K6_K7_K1_8258', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_2_5201', 'NT_N_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49273456_K2_K1_4_5_6_7_8_9_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_104889936_K2_K9_K6_K7_K1', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49273456_K2_K9_K7_K6_K1', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49273456_K9_K2_1_4_5_6_7_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51857368_K9_2', 'NT_N_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K6_K7_K2_1410', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49273456_K9_K2_K1_4_5_6_7_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K2_5201_6497_1040', 'NT_N_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_93906392_K9_K7', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49273456_K2_K9_K7_K1_K6', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49273456_K2_K9_1_4_5_6_7_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K7_K2_K9_8066', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_2_9987', 'NT_N_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K6_K7_2894', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49273568_K2_K9_K7', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K2_K9_K7_1_4_5_6_8_2533_8258', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_93906448_K9_K7_K2', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49239816_K9_2', 'NT_N_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_58921568_K2_K1_4_5_6_7_8_9_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51857368_K9_K7', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K7_K2_1_4_5_6_8_2894', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_58921568_K9_K2_K1_4_5_6_7_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K6_K9_K7_K2_K1_4864', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49274968_K9_K6_K7', 'NT_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K7_K2_K9_8066_1912', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_93906448_K2_K9_K7', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K7_K9_K2_1_4_5_6_8_6960', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_110169208_K9_K7_K2', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51855688_K7_K2_K9', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K1_K2_K9_K7_K6_6960', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49273568_K9_K7_K2', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49240096_K7_K2_K9', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_104889936_K2_K9_K7_K1', 'NT_ID', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49273456_K2_K9_K7_1_4_5_6_8', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K8_K2_K9_9987_4364_8066_1912', 'NT_N_ID', 'NT_USU_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51857368_K7_K2_K9', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49273568_K2_K9_K7_1_4_5_6_8', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K2_K9_K7_K1_9850', 'NT_ID', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49273512_K7', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49239816_K7_K2_K9', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_58921568_K9_K7_K2', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49275136_K9_K7_K2_1_4_5_6_8', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49273456_K2_K9_K6_K7', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_100452352_K7', 'NT_N_ID', 'NT_VISIBLE'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K7_K6_K2_K1_9085', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51875528_K9_K2', 'NT_N_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49273456_K7_K9_K2_1_4_5_6_8', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID'),
        Index('_dta_stat_43147199_2_9_6', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49273456_K9_K6_K7_K2', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49273680_K9_K2', 'NT_N_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K1_K2_K9_K7_6355', 'NT_ID', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49273568_K7_K9_K2_1_4_5_6_8', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_58921568_K9', 'NT_N_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_104889936_K2_K9', 'NT_N_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51875528_K2', 'NT_N_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49273456_K9_K7_K2_1_4_5_6_8', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_2_9987_4364', 'NT_N_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70952136_K2_K9_K7_1_4_5_6_8', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K7_K9_K6_K2_K1_1912', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K2_K9_K6_K7', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70952808_K9_K6_K7_K2_K1', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70953032_K9_K7_K2_1_4_5_6_8', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K7_K2_K1_K6', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K2_K9_K6_K7_4149', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70952808_K9_K7_K2_K6_K1', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70952808_K7_K9_K2_1_4_5_6_8', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70952808_K9_K7_K2_K1_K6', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70952136_K7_K9_K2_1_4_5_6_8', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70952808_K7_K9_K6_K2_K1', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70952808_K9_K7_K2_1_4_5_6_8', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K7_K2_K6_K1', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K7_K2_K1_K6_6497', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70952584_K9_K7', 'NT_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70952136_K9_K7_K2_1_4_5_6_8', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_100452352_K9', 'NT_N_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K2_K9_K7_K1_K6', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70953032_K2_K9_K7_1_4_5_6_8', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_100452352_K2_K9', 'NT_N_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70951968_K7', 'NT_ID', 'NT_VISIBLE'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K7_K2_K6_K1_1771', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70953032_K7_K9_K2_1_4_5_6_8', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K1_K2_K9_K6_K7', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70952808_K9', 'NT_N_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_100452352_K9_K2', 'NT_N_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70953032_K2_K9_K7', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K7_K2_2533', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70952808_K6_K9_K7_K2_K1', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K2_K9_K7_K6_K1', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70952808_K9_K6_K7', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70953032_K9_K7_K2', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K2_K9_K7_K1_K6_8258', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K7_2', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K2_K9_K6_K7_K1', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70952136_K9', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_1_2_4_5_6_7_8_10_9987_4364_8066', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K7_K2', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K1_K2_K9_K6_K7_1410', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K6_K7_K2', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70953536_K9_K6_K7', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K2_1_4_5_6_7_8_9_10_9987_4364_8066', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K7_K9_K2', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K6_K7', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K2_K9_K7_K6_K1_2894', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K1_7_9987_4364_8066', 'NT_ID', 'NT_VISIBLE'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K7', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70952808_K9_K7_K6_K2_K1', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K6_K9_K7_K2_K1', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K2_K9_K7', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K2_K9_K6_K7_K1_4864', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70952528_K9_K7', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70952136_K9_K7_2', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_93614016_K9_K7_K2', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K1_K2_K9_K7_K6', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51874520_K1_K9_K7_2_4_5_6_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K6_K7_K2_6960', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70952136_K9_K6_K7', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K7_K2_K1_9987_4364_8066_1912', 'NT_ID', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K2_K9_K7_K1', 'NT_ID', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_104889936_K9', 'NT_N_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K7_K9_K6_K2_K1_4149', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K6_K7_9850', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70952808_K6', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_93614016_K2_K9_K7', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K7_K6_K2_K1', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70952808_K1_K2_K9_K7_K6', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K2_K9_K6_K7_5201', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K6_K9_K7_K2_K1_9085', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_104889936_K7_K9_K2', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K1_K2_K9_K7', 'NT_ID', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70952808_K9_K7_K2', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K6_K7_K2_K1', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K7_6355', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_104889936_K9_K7_K2', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70951968_K9', 'NT_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K7_K2_K1_K6_1040', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K2_K9_K7_8526', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_104889936_K9_K6_K7_K2_K1', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70953536_K9_K7_K2', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_104889936_K2_K9_K7', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_104889936_K9_K7_K2_K6_K1', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K1_K2_K9_K7_K6_8341', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70952136_K6', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K7_K2_K6_K1_2533', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_93614016_K9_K7', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_104889936_K9_K7_K2_K1_K6', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K2_K9_K7_K1_114', 'NT_ID', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70952808_K2_K9_K7', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_104889936_K7_K9_K6_K2_K1', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K7_K2_8258', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_93614016_K9_K7_2', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_93907544_K9_K7', 'NT_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K7_K6_K2_K1_5543', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70952808_K2_K9_K7_K6_K1', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K2_K9_K7_K1_K6_1410', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70952808_K2_K9_K7_K1_K6', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_93906336_K7', 'NT_ID', 'NT_VISIBLE'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K1_K2_K9_K7_8809', 'NT_ID', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_104889936_K9_K7', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70952136_K2_K9_K7', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K1_K2_K9_K6_K7_2894', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_104889936_K9_K7_K6_K2_K1', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K6_K7_K2_K1_9953', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_104889936_K9_K7_2', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_93906448_K9_K7', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70953536_K2_K9_K7', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K2_K9_K7_K6_K1_4864', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K7_2_4364', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_104889936_K7', 'NT_N_ID', 'NT_VISIBLE'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_93906392_K9_K6_K7', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70951968_K9_K6_K7', 'NT_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K2_K9_K6_K7_K1_6960', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K7_K9_K2_1410', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_93614016_K9', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_104889936_K6', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70952136_K9_K7_K2', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K6_K7_K2_9850', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_93614016_K7_K9_K2', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70953536_K9', 'NT_N_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_104889936_K1_K2_K9_K7_K6', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70953536_K2_K9', 'NT_N_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70952528_K7', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K6_K7_9085', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K7_K2_K1', 'NT_ID', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_93906336_K9', 'NT_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70952808_K2_K9_K6_K7', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K7_K9_K6_K2_K1', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_100452352_K9_K7_K2', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70953536_K9_K2', 'NT_N_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K6_K9_K7_K2_K1_6355', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_2_4_9987_4364', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51856808_K9_K2_K7_4', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70952808_K9_K6_K7_K2', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70952920_K9', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K2_K7_4_8066', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70952920_K7_K9_K2', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51856808_K9_2_4', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70951968_K9_K7_K2', 'NT_ID', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51875528_K2_K9', 'NT_N_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K2_4_1912', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70952808_K2_K9', 'NT_N_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51857480_K9_2_4', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70952808_K1_K2_K9_K7', 'NT_ID', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51874520_K2_K9', 'NT_N_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K7_K2_K9_4_5201', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70952808_K9_K2', 'NT_N_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51856808_K2_K9_K7_4', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70952808_K9_K7_K2_K1', 'NT_ID', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51874520_K2_K1_4_5_6_7_8_9_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K2_K9_K7_4_6497', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70952808_K2_K1_4_5_6_7_8_9_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51874520_K9_K2_K1_4_5_6_7_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51856808_K7_K2_K9_4', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70951968_K2_K9_K7', 'NT_ID', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K7_2_4_2533', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70952808_K9_K2_K1_4_5_6_7_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K4D_K9_K7_2_9987', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51857480_K2_K9', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70952528_K9', 'NT_FECHA_VENCIMIENTO', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_2_6497', 'NT_N_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K2_K9_4_8258', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K7_K4_2_4364', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70952584_K6', 'NT_ID', 'NT_FECHA_VENCIMIENTO'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70953536_K9_2', 'NT_N_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51857480_K9_K2', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K7_K2_4_1410', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70952808_K1_K2_K9_K6_K7', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K4D_K9_K7_2_9987_4364_8066', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K7_K9_K4_2_8066', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49273456_K2_K9_4', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70952528_K9_K6_K7', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K7_K4_2_1912', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51874520_K7_K9_K4_2', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51857480_K2', 'NT_N_ID', 'NT_VISIBLE'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49273568_K2_K9_4', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K7_K9_K4_2_4149', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51856808_K9_K7_K2_4', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51874520_K9_K7', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70952808_K2_K9_K6_K7_K1', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49273456_K9_K7_2_4', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70953032_K7_K9_K4_2', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51856808_K9_K2_4', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70952136_K9_K7', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51874520_K7', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49273456_K9_K2_K7_4', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70953032_K9_K7', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51874520_K9_K7_K4_2', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51857480_K9_K2_4', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70952808_K9_K7', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49273456_K9_2_4', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70953032_K7', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K2_5201', 'NT_N_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70952528_K9_K7_K2', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70953032_K9_K7_K4_2', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51874520_K4D_K9_K7_2', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49239816_K9', 'NT_N_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49273568_K9_2_4', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70952528_K2_K9_K7', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49239816_K2_K9', 'NT_N_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K2_K9_1_4_5_6_7_8_10_9987', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49273456_K2_K9_K7_4', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70952808_K2_K9_K7_K1', 'NT_ID', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70953032_K4D_K9_K7_2', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K2_1_4_5_6_7_8_10_4364', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49239816_K9_K2', 'NT_N_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49273456_K7_K2_K9_4', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K8_K9_9987', 'NT_USU_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70952808_K7', 'NT_N_ID', 'NT_VISIBLE'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49273568_K2_K9', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K7_2_4149', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70953368_K9_K2', 'NT_N_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70953536_K7', 'NT_N_ID', 'NT_VISIBLE'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K7_K2_1771', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49273568_K9_K2', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51856808_K9_K2_1_4_5_6_7_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70952920_K9_K7_K2', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70953368_K2', 'NT_N_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51856808_K2_K9_1_4_5_6_7_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K7_K9_K2_9953', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70952920_K2_K9_K7', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K2_K9_K7_1_4_5_6_8_2533', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49273456_K9_K7_2', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K7_2733', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K7_K2_1_4_5_6_8_1410', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70953536_K7_K9_K2', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70953368_K2_K9', 'NT_N_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K2_K9_K7_4606', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49273568_K2', 'NT_N_ID', 'NT_VISIBLE'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K7_K9_K2_1_4_5_6_8_4864', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49273456_K9_K7_K2_4', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70952920_K9_K7', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70953032_K2_K1_4_5_6_7_8_9_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51856808_K2_K9_K7_1_4_5_6_8', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49240096_K9_K7_K2', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70953032_K9_K2_K1_4_5_6_7_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51857480_K2_K9_K7_1_4_5_6_8', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49273456_K9_K2_4', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70952920_K9_K7_2', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49240096_K2_K9_K7', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70953032_K2_K9', 'NT_N_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51874520_K9_K7_K2_1_4_5_6_8', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49273568_K9_K2_4', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51856808_K7_K9_K2_1_4_5_6_8', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49239816_K7_K9_K2', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K7_K2_K9_8066_1912_4149', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70953536_K9_K7', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51857480_K7_K9_K2_1_4_5_6_8', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K2_5201_6497', 'NT_N_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70952920_K7_K2_K9', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49239816_K9_K7_K2', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51856808_K9_K7_K2_1_4_5_6_8', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70953536_K9_K7_2', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K7_K2_K1_9987_4364_8066', 'NT_ID', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70953536_K7_K2_K9', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51857480_K9_K7_K2_1_4_5_6_8', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51857368_K9_K7_2', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51874520_K2_K9_K7_1_4_5_6_8', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_1_2_4_5_6_7_8_10_9987', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K7_8526', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_55428592_K2_K9', 'NT_N_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51856808_K8', 'NT_N_ID', 'NT_USU_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51874520_K7_K9_K2_1_4_5_6_8', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K1_7_9987', 'NT_ID', 'NT_VISIBLE'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K2_K9_K7_8341', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K2_1_4_5_6_7_8_9_10_9987', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_55428592_K2_K1_4_5_6_7_8_9_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51874520_K2_K9_K7', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K1_K2_K9_K7_K6_114', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_55428592_K9_K2_K1_4_5_6_7_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51856808_K8_K2_K9', 'NT_N_ID', 'NT_USU_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51874520_K9_K7_K2', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_58921568_K2_K9', 'NT_N_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K2_K9_K7_K1_5543', 'NT_ID', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51857368_K7_K9_K2', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_55412640_K2_K9', 'NT_N_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K7_K6_K2_K1_8809', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51857480_K7_K9_K2', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_55412640_K9_K2', 'NT_N_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K1_K2_K9_K7_9953', 'NT_ID', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_100452352_K9_K6_K7', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K8_K2_K9_9987', 'NT_N_ID', 'NT_USU_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K8_K9_9987_4364_8066_1912_4149', 'NT_USU_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K6_K7_K2_K1_9910', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51857368_K8', 'NT_N_ID', 'NT_USU_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49580600_K9_K6_K7_K2_K1', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_55428984_K2_K1_4_5_6_7_8_9_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51857368_K8_K2_K9', 'NT_N_ID', 'NT_USU_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49580600_K9_K7_K2_K6_K1', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_55428984_K9_K2_K1_4_5_6_7_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K7_K9_K1_2_4_5_6_8_10_9987', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49580600_K9_K7_K2_K1_K6', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_1_2_4_5_6_7_8_10_9987_4364_8066_1912_4149', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K7_K1_2_4_5_6_8_10_4364', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49580600_K7_K9_K6_K2_K1', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K2_1_4_5_6_7_8_9_10_9987_4364_8066_1912_4149', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51857480_K9_K1_K7_2_4_5_6_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K7_K1_8066', 'NT_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49609440_K9_K7', 'NT_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51856808_K9_2', 'NT_N_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K2_9987', 'NT_N_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K1_K9_K7_1912', 'NT_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49581104_K7', 'NT_ID', 'NT_VISIBLE'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_55428928_K9_K2', 'NT_N_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49580600_K9', 'NT_N_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K7_K1_2_4_5_6_8_10_4149', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49580600_K6_K9_K7_K2_K1', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_110169208_K2_K1_4_5_6_7_8_9_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K1_K7_2_4_5_6_8_10_5201', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49580264_K9', 'NT_N_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K7_2_9987', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K1_K9_K7_2_4_5_6_8_10_6497', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49580600_K9_K6_K7', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K7_K2_1410', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K1_K9_1040', 'NT_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K1_K7_2_4_5_6_8_10_1771', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49609272_K9', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_58921568_K8', 'NT_N_ID', 'NT_USU_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K1_K7_2533', 'NT_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49580264_K9_K6_K7', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_58921568_K9_K2', 'NT_N_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K1_8258', 'NT_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51857424_K9_K7_K1', 'NT_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49580600_K9_K7_K6_K2_K1', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51857480_K7_K9_K1_2_4_5_6_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_58921568_K8_K2_K9', 'NT_N_ID', 'NT_USU_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51875528_K1_K9_K7', 'NT_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49610112_K9_K7', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51874520_K1_K7_2_4_5_6_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K2_5201_6497_1040_1771', 'NT_N_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51874520_K7_K1_2_4_5_6_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49609272_K9_K6_K7', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_61974320_K7_K9_K6_K2_K1', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51857480_K9_K1', 'NT_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_61974320_K2_K1_4_5_6_7_8_9_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49580600_K6', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_2_4_9987_4364_8066', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51857480_K9_K1_K7', 'NT_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49580600_K1_K2_K9_K7_K6', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_110169208_K9_K2_K1_4_5_6_7_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49580600_K9_K7_K2', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51857480_K9_K7_K1_2_4_5_6_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_61974320_K9_K2_K1_4_5_6_7_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51875528_K9_K7_K1', 'NT_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49581104_K9', 'NT_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K4D_K9_K7_2_9987_4364_8066_1912', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49580264_K9_K7_K2', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_62027624_K2_K1_4_5_6_7_8_9_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51857424_K9_K1', 'NT_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_93906392_K9', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K2_1_4_5_6_7_8_9_10_9987_4364_8066_1912_4149_5201', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49609272_K6', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51857424_K9_K1_K7', 'NT_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_61974320_K9_K7_2', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49580600_K2_K9_K7', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K1_K7_2_4_5_6_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_110169208_K2_K9', 'NT_N_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K2_K9_1_4_5_6_7_8_10_9987_4364_8066', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49580600_K2_K9_K7_K6_K1', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K1_K9_K7_2_4_5_6_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K2_1_4_5_6_7_8_10_1912', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49580600_K2_K9_K7_K1_K6', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_62027624_K9_K2_K1_4_5_6_7_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K1_K9', 'NT_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K8_K9_9987_4364_8066', 'NT_USU_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49609272_K2_K9_K7', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_58922352_K9', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K1_K7_2_4_5_6_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K1_K7', 'NT_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49580264_K2_K9_K7', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K1', 'NT_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70952808_K9_K2_1_4_5_6_7_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49581104_K9_K6_K7', 'NT_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_102839032_K1_K9_K7', 'NT_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70952808_K2_K9_1_4_5_6_7_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49609272_K9_K7_K2', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_96766016_K7_K1_2_4_5_6_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_93906392_K9_K1', 'NT_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70952136_K7_K9_K2', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49610112_K7', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49580600_K2_K9_K6_K7', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_93906392_K9_K1_K7', 'NT_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K8_K2_K9_9987_4364_8066', 'NT_N_ID', 'NT_USU_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70953536_K8', 'NT_N_ID', 'NT_USU_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49580600_K9_K6_K7_K2', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_93906392_K9_K7_K1_2_4_5_6_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70953536_K8_K2_K9', 'NT_N_ID', 'NT_USU_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_102839032_K9_K7_K1', 'NT_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49581104_K9_K7_K2', 'NT_ID', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K7_K9_K1_2_4_5_6_8_10_9987_4364_8066', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_93906336_K9_K1', 'NT_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49580600_K1_K2_K9_K7', 'NT_ID', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K7_K1_2_4_5_6_8_10_1912', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_93906336_K9_K1_K7', 'NT_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K7_K1_4149', 'NT_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49580600_K9_K7_K2_K1', 'NT_ID', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_93907544_K9_K1_K7_2_4_5_6_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K1_K9_K7_5201', 'NT_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49581104_K2_K9_K7', 'NT_ID', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_93906392_K1_K9', 'NT_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K7_K1_2_4_5_6_8_10_6497', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49610112_K9', 'NT_FECHA_VENCIMIENTO', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_93906392_K1_K9_K7_2_4_5_6_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K1_K7_2_4_5_6_8_10_1040', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49609440_K6', 'NT_ID', 'NT_FECHA_VENCIMIENTO'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_93906392_K1_K7_2_4_5_6_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K1_K9_K7_2_4_5_6_8_10_1771', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49580600_K1_K2_K9_K6_K7', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_93907544_K7_K9_K1_2_4_5_6_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K1_K9_2533', 'NT_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49610112_K9_K6_K7', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_93906336_K1_K9', 'NT_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K1_K7_2_4_5_6_8_10_8258', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K1_K7_1410', 'NT_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_102839032_K7', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49580600_K2_K9_K6_K7_K1', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_93907544_K9_K7_K1_2_4_5_6_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K1_2894', 'NT_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49609272_K9_K7', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_93906392_K7_K1_2_4_5_6_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70953368_K1_K9_K7', 'NT_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49580600_K9_K7', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_102839032_K9_K1', 'NT_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70953032_K7_K1_2_4_5_6_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49610112_K9_K7_K2', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_102839032_K9_K1_K7', 'NT_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70952136_K9_K1', 'NT_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49610112_K2_K9_K7', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_96766016_K9_K1_K7_2_4_5_6_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70952136_K9_K1_K7', 'NT_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_93907544_K1_K9_K7_2_4_5_6_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49580600_K2_K9_K7_K1', 'NT_ID', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70952136_K9_K7_K1_2_4_5_6_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_93907544_K1_K7_2_4_5_6_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70953368_K9_K7_K1', 'NT_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49580600_K7', 'NT_N_ID', 'NT_VISIBLE'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_96766016_K7_K9_K1_2_4_5_6_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_93906392_K1_K9_K7', 'NT_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_70951968_K9_K1', 'NT_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49580264_K7', 'NT_N_ID', 'NT_VISIBLE'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_102839032_K1_K9', 'NT_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K2_4149_5201', 'NT_N_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49273568_K9_K7_K2_1_4_5_6_8', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_96766016_K9_K7_K1_2_4_5_6_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49275136_K2_K9_K7_1_4_5_6_8', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49580264_K2_K9', 'NT_N_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_93906392_K9_K7_K1', 'NT_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49275136_K7_K9_K2_1_4_5_6_8', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49580264_K9_K2', 'NT_N_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49275136_K2_K9_K7', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_93907544_K7_K1_2_4_5_6_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K2_K1_4_5_6_7_8_9_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_93906336_K1_K9_K7', 'NT_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49275136_K9_K7_K2', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49610168_K9_K2', 'NT_N_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_96766016_K1_K9_K7_2_4_5_6_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49273568_K7_K9_K2', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49610168_K2', 'NT_N_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_104889936_K6_K9_K7_K2_K1', 'NT_ID', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_96766016_K1_K7_2_4_5_6_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K8_K2_K9_9987_4364', 'NT_N_ID', 'NT_USU_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_93906336_K9_K7_K1', 'NT_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K2_K7_4_4364', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49239816_K8', 'NT_N_ID', 'NT_USU_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_93906392_K9_K1_K7_2_4_5_6_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49610168_K2_K9', 'NT_N_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49239816_K8_K2_K9', 'NT_N_ID', 'NT_USU_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K2', 'NT_N_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_93906392_K7_K9_K1_2_4_5_6_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_104889936_K9_K6_K7', 'NT_N_ID', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49580600_K2_K9', 'NT_N_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_1_2_4_5_6_7_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K7_K9_K1_2_4_5_6_8_10_9987_4364', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K7_K2_K9_4_4149', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K7_K1_2_4_5_6_8_10_8066', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49580600_K2_K1_4_5_6_7_8_9_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K2_1_4_5_6_7_8_9_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K7_K1_1912', 'NT_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49580600_K9_K2_K1_4_5_6_7_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K2_4_8066', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K1_7', 'NT_ID', 'NT_VISIBLE'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49609384_K2_K9', 'NT_N_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K1_K9_K7_4149', 'NT_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_100452352_K9_K7_2', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49609384_K2_K1_4_5_6_7_8_9_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K7_K1_2_4_5_6_8_10_5201', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_93906392_K9_K7_2', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49609384_K9_K2_K1_4_5_6_7_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K1_K7_2_4_5_6_8_10_6497', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_102839032_K9_2', 'NT_N_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K1_K9_K7_2_4_5_6_8_10_1040', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K2_K9_K7_1_4_5_6_8_5201', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K1_K9_1771', 'NT_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_2_4', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K7_K2_1_4_5_6_8_6497', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K1_K7_2_4_5_6_8_10_2533', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K2_K7_4', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K7_K9_K2_1_4_5_6_8_1040', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K1_K7_8258', 'NT_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K2_4', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49580600_K2_K9_K7_1_4_5_6_8', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K7_K2_K9_4', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K1_1410', 'NT_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49609272_K2_K9_K7_1_4_5_6_8', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K2_K9_K7_4', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49273680_K1_K9_K7', 'NT_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49609384_K9_K7_K2_1_4_5_6_8', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K7_2_4', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49580600_K7_K9_K2_1_4_5_6_8', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49275136_K7_K1_2_4_5_6_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K2_K9_4', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49609272_K7_K9_K2_1_4_5_6_8', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49273568_K9_K1', 'NT_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K7_K2_4', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49609384_K9_K7', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51875528_K9_2', 'NT_N_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_104889936_K2_K9_4', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49273568_K9_K1_K7', 'NT_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49580600_K9_K7_K2_1_4_5_6_8', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_51857480_K9_K7_2', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_93906392_K2_K9_4', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49273568_K9_K7_K1_2_4_5_6_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49609272_K9_K7_K2_1_4_5_6_8', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49273680_K9_K7_K1', 'NT_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49609384_K7', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_104889936_K9_K7_2_4', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49609384_K2_K9_K7_1_4_5_6_8', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID'),
        Index('NonClusteredIndex-20160927-090533', 'NT_N_ID', 'NT_T_ID', unique=True),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_2_4_9987', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49274968_K9_K1', 'NT_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_104889936_K9_K2_K7_4', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199__K9_K2_K1_4_5_6_7_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49274968_K9_K1_K7', 'NT_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49609384_K7_K9_K2_1_4_5_6_8', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_104889936_K9_2_4', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49609384_K2_K9_K7', 'NT_N_ID', 'NT_VISIBLE', 'NT_T_ID'),
        Index('_dta_index_K_NOTA_TEMA_5_43147199_49275192_K9_K1_K7_2_4_5_6_8_10', 'NT_ID', 'NT_N_ID', 'NT_FECHA_PUBLICACION', 'NT_FECHA_CAPTURA', 'NT_FECHA_VENCIMIENTO', 'NT_VISIBLE', 'NT_USU_ID', 'NT_T_ID', 'NT_FECHA_INGRESADA_TEMA')
    )

    NT_ID = Column(BigInteger, primary_key=True, index=True)
    NT_N_ID = Column(ForeignKey('K_NOTA.N_ID'), nullable=False, index=True)
    NT_FECHA_PUBLICACION = Column(DateTime, nullable=False)
    NT_FECHA_CAPTURA = Column(DateTime, nullable=False)
    NT_FECHA_VENCIMIENTO = Column(DateTime, nullable=False, index=True)
    NT_VISIBLE = Column(Integer, nullable=False, index=True)
    NT_USU_ID = Column(Integer, nullable=False, index=True)
    NT_T_ID = Column(ForeignKey('K_TEMA.T_ID'), index=True)
    NT_FECHA_INGRESADA_TEMA = Column(DateTime)

    K_NOTA = relationship('KNOTA')
    K_TEMA = relationship('KTEMA')


class KNOTATESTIGO(Base):
    __tablename__ = 'K_NOTA_TESTIGO'
    __table_args__ = (
        Index('_dta_index_K_NOTA_TESTIGO_5_2069582411__K1_K2_K3_8066', 'NTS_ID', 'NTS_N_ID', 'NT_S_ID'),
        Index('_dta_index_K_NOTA_TESTIGO_5_2069582411__K3_K2_1_9987', 'NTS_ID', 'NTS_N_ID', 'NT_S_ID'),
        Index('_dta_index_K_NOTA_TESTIGO_5_2069582411_100452352_K2', 'NTS_N_ID', 'NT_S_ID'),
        Index('_dta_index_K_NOTA_TESTIGO_5_2069582411_100452352_K2_K3_6497', 'NTS_N_ID', 'NT_S_ID'),
        Index('_dta_index_K_NOTA_TESTIGO_5_2069582411__K1_2_3_9987', 'NTS_ID', 'NTS_N_ID', 'NT_S_ID'),
        Index('_dta_index_K_NOTA_TESTIGO_5_2069582411__K2_K3_9987', 'NTS_N_ID', 'NT_S_ID'),
        Index('_dta_index_K_NOTA_TESTIGO_5_2069582411__K3_K2_1_4364', 'NTS_ID', 'NTS_N_ID', 'NT_S_ID'),
        Index('_dta_index_K_NOTA_TESTIGO_5_2069582411__K3_K2_8066', 'NTS_N_ID', 'NT_S_ID'),
        Index('_dta_index_K_NOTA_TESTIGO_5_2069582411_104889936_K2_K3', 'NTS_N_ID', 'NT_S_ID'),
        Index('_dta_index_K_NOTA_TESTIGO_5_2069582411__K2_K3_9910', 'NTS_N_ID', 'NT_S_ID'),
        Index('_dta_index_K_NOTA_TESTIGO_5_2069582411__K2_1_3_9987_4364_8066_1912', 'NTS_ID', 'NTS_N_ID', 'NT_S_ID'),
        Index('_dta_index_K_NOTA_TESTIGO_5_2069582411__K3_1_2_9987_4364_8066_1912', 'NTS_ID', 'NTS_N_ID', 'NT_S_ID'),
        Index('_dta_index_K_NOTA_TESTIGO_5_2069582411_100452352_K2_K3', 'NTS_N_ID', 'NT_S_ID'),
        Index('_dta_index_K_NOTA_TESTIGO_5_2069582411__K3_K2_32', 'NTS_N_ID', 'NT_S_ID'),
        Index('_dta_index_K_NOTA_TESTIGO_5_2069582411_49239816_K3_K2', 'NTS_N_ID', 'NT_S_ID'),
        Index('_dta_index_K_NOTA_TESTIGO_5_2069582411__K3_K2_4149', 'NTS_N_ID', 'NT_S_ID'),
        Index('_dta_index_K_NOTA_TESTIGO_5_2069582411_100452352_K3_K2_4364', 'NTS_N_ID', 'NT_S_ID'),
        Index('_dta_index_K_NOTA_TESTIGO_5_2069582411_104889936_K2_5201', 'NTS_N_ID', 'NT_S_ID'),
        Index('_dta_index_K_NOTA_TESTIGO_5_2069582411_49239816_K3_K2_3370', 'NTS_N_ID', 'NT_S_ID'),
        Index('_dta_index_K_NOTA_TESTIGO_5_2069582411_104889936_K2_K3_4149', 'NTS_N_ID', 'NT_S_ID'),
        Index('_dta_index_K_NOTA_TESTIGO_5_2069582411_70952808_K3_K2', 'NTS_N_ID', 'NT_S_ID'),
        Index('_dta_index_K_NOTA_TESTIGO_5_2069582411_100452352_K3_1912', 'NTS_N_ID', 'NT_S_ID'),
        Index('_dta_index_K_NOTA_TESTIGO_5_2069582411_70953536_K3_K2', 'NTS_N_ID', 'NT_S_ID'),
        Index('_dta_index_K_NOTA_TESTIGO_5_2069582411_49239816_K3_5737', 'NTS_N_ID', 'NT_S_ID'),
        Index('_dta_index_K_NOTA_TESTIGO_5_2069582411_49239816_K2_K3', 'NTS_N_ID', 'NT_S_ID'),
        Index('_dta_index_K_NOTA_TESTIGO_5_2069582411_70953536_K3', 'NTS_N_ID', 'NT_S_ID'),
        Index('_dta_index_K_NOTA_TESTIGO_5_2069582411_49239816_K2_K3_8953', 'NTS_N_ID', 'NT_S_ID'),
        Index('_dta_index_K_NOTA_TESTIGO_5_2069582411_70952808_K2_K3', 'NTS_N_ID', 'NT_S_ID'),
        Index('_dta_index_K_NOTA_TESTIGO_5_2069582411_49239816_K2', 'NTS_N_ID', 'NT_S_ID'),
        Index('_dta_index_K_NOTA_TESTIGO_5_2069582411_70953536_K2_K3', 'NTS_N_ID', 'NT_S_ID'),
        Index('_dta_index_K_NOTA_TESTIGO_5_2069582411_49273456_K3_K2', 'NTS_N_ID', 'NT_S_ID'),
        Index('_dta_index_K_NOTA_TESTIGO_5_2069582411_70952808_K2', 'NTS_N_ID', 'NT_S_ID'),
        Index('_dta_index_K_NOTA_TESTIGO_5_2069582411_49273456_K2_K3', 'NTS_N_ID', 'NT_S_ID'),
        Index('_dta_index_K_NOTA_TESTIGO_5_2069582411_70953536_K3_K2_4149', 'NTS_N_ID', 'NT_S_ID'),
        Index('_dta_index_K_NOTA_TESTIGO_5_2069582411_104889936_K3_K2_9987', 'NTS_N_ID', 'NT_S_ID'),
        Index('_dta_index_K_NOTA_TESTIGO_5_2069582411_49273456_K2', 'NTS_N_ID', 'NT_S_ID'),
        Index('_dta_index_K_NOTA_TESTIGO_5_2069582411_70953536_K2_K3_6497', 'NTS_N_ID', 'NT_S_ID'),
        Index('_dta_index_K_NOTA_TESTIGO_5_2069582411_49273456_K2_K3_786', 'NTS_N_ID', 'NT_S_ID'),
        Index('_dta_index_K_NOTA_TESTIGO_5_2069582411__K2_K3', 'NTS_N_ID', 'NT_S_ID'),
        Index('_dta_index_K_NOTA_TESTIGO_5_2069582411_70953536_K2_1040', 'NTS_N_ID', 'NT_S_ID'),
        Index('_dta_index_K_NOTA_TESTIGO_5_2069582411__K3_1_2_9987_4364', 'NTS_ID', 'NTS_N_ID', 'NT_S_ID'),
        Index('_dta_index_K_NOTA_TESTIGO_5_2069582411__K2_1_3_9987_4364', 'NTS_ID', 'NTS_N_ID', 'NT_S_ID'),
        Index('_dta_index_K_NOTA_TESTIGO_5_2069582411__K3_1_2_9987_4364_8066', 'NTS_ID', 'NTS_N_ID', 'NT_S_ID'),
        Index('_dta_index_K_NOTA_TESTIGO_5_2069582411__K3_K2_K1_9987_4364', 'NTS_ID', 'NTS_N_ID', 'NT_S_ID'),
        Index('_dta_index_K_NOTA_TESTIGO_5_2069582411__K2_1_3_9987_4364_8066', 'NTS_ID', 'NTS_N_ID', 'NT_S_ID'),
        Index('_dta_index_K_NOTA_TESTIGO_5_2069582411__K2_K1_K3_8066', 'NTS_ID', 'NTS_N_ID', 'NT_S_ID'),
        Index('_dta_index_K_NOTA_TESTIGO_5_2069582411__K3_K2_K1_9987_4364_8066', 'NTS_ID', 'NTS_N_ID', 'NT_S_ID'),
        Index('_dta_index_K_NOTA_TESTIGO_5_2069582411__K2_K1_K3_1912', 'NTS_ID', 'NTS_N_ID', 'NT_S_ID'),
        Index('_dta_index_K_NOTA_TESTIGO_5_2069582411__K1_K2_K3_1912', 'NTS_ID', 'NTS_N_ID', 'NT_S_ID'),
        Index('_dta_index_K_NOTA_TESTIGO_5_2069582411__K1_K2_K3_4149', 'NTS_ID', 'NTS_N_ID', 'NT_S_ID'),
        Index('_dta_index_K_NOTA_TESTIGO_5_2069582411__K1_2_3_9987_4364', 'NTS_ID', 'NTS_N_ID', 'NT_S_ID'),
        Index('_dta_index_K_NOTA_TESTIGO_5_2069582411__K3_K2_1_8066', 'NTS_ID', 'NTS_N_ID', 'NT_S_ID'),
        Index('_dta_index_K_NOTA_TESTIGO_5_2069582411__K1_2_3_9987_4364_8066', 'NTS_ID', 'NTS_N_ID', 'NT_S_ID'),
        Index('_dta_index_K_NOTA_TESTIGO_5_2069582411__K2_K1_3_9987', 'NTS_ID', 'NTS_N_ID', 'NT_S_ID'),
        Index('_dta_index_K_NOTA_TESTIGO_5_2069582411__K2_K3_4364', 'NTS_N_ID', 'NT_S_ID'),
        Index('_dta_index_K_NOTA_TESTIGO_5_2069582411_104889936_K3_K2', 'NTS_N_ID', 'NT_S_ID'),
        Index('_dta_index_K_NOTA_TESTIGO_5_2069582411__K3_1_2', 'NTS_ID', 'NTS_N_ID', 'NT_S_ID'),
        Index('_dta_index_K_NOTA_TESTIGO_5_2069582411__K1_2_3', 'NTS_ID', 'NTS_N_ID', 'NT_S_ID'),
        Index('_dta_index_K_NOTA_TESTIGO_5_2069582411__K2_1_3', 'NTS_ID', 'NTS_N_ID', 'NT_S_ID'),
        Index('_dta_index_K_NOTA_TESTIGO_5_2069582411__K3_K2_K1', 'NTS_ID', 'NTS_N_ID', 'NT_S_ID'),
        Index('_dta_index_K_NOTA_TESTIGO_5_2069582411__K2_K1_3', 'NTS_ID', 'NTS_N_ID', 'NT_S_ID'),
        Index('_dta_index_K_NOTA_TESTIGO_5_2069582411__K1_K2_K3', 'NTS_ID', 'NTS_N_ID', 'NT_S_ID'),
        Index('_dta_index_K_NOTA_TESTIGO_5_2069582411__K3_K2_1', 'NTS_ID', 'NTS_N_ID', 'NT_S_ID'),
        Index('_dta_index_K_NOTA_TESTIGO_5_2069582411__K2_K3_9953', 'NTS_N_ID', 'NT_S_ID'),
        Index('_dta_index_K_NOTA_TESTIGO_5_2069582411__K3_K2_7903', 'NTS_N_ID', 'NT_S_ID'),
        Index('_dta_index_K_NOTA_TESTIGO_5_2069582411_51857368_K3_K2', 'NTS_N_ID', 'NT_S_ID'),
        Index('_dta_index_K_NOTA_TESTIGO_5_2069582411_51856808_K3_K2', 'NTS_N_ID', 'NT_S_ID'),
        Index('_dta_index_K_NOTA_TESTIGO_5_2069582411__K1_K2_K3_9987', 'NTS_ID', 'NTS_N_ID', 'NT_S_ID'),
        Index('_dta_index_K_NOTA_TESTIGO_5_2069582411__K1_2_3_9987_4364_8066_1912', 'NTS_ID', 'NTS_N_ID', 'NT_S_ID'),
        Index('_dta_index_K_NOTA_TESTIGO_5_2069582411_51856808_K3', 'NTS_N_ID', 'NT_S_ID'),
        Index('_dta_index_K_NOTA_TESTIGO_5_2069582411__K2_K1_3_9987_4364', 'NTS_ID', 'NTS_N_ID', 'NT_S_ID'),
        Index('_dta_index_K_NOTA_TESTIGO_5_2069582411__K2_K3_1', 'NTS_ID', 'NTS_N_ID', 'NT_S_ID'),
        Index('_dta_index_K_NOTA_TESTIGO_5_2069582411_51857368_K2_K3', 'NTS_N_ID', 'NT_S_ID'),
        Index('_dta_index_K_NOTA_TESTIGO_5_2069582411__K2_K3_9987_4364', 'NTS_N_ID', 'NT_S_ID'),
        Index('_dta_index_K_NOTA_TESTIGO_5_2069582411_51857368_K2', 'NTS_N_ID', 'NT_S_ID'),
        Index('_dta_index_K_NOTA_TESTIGO_5_2069582411_51856808_K2_K3', 'NTS_N_ID', 'NT_S_ID'),
        Index('_dta_index_K_NOTA_TESTIGO_5_2069582411__K3_K2_1912', 'NTS_N_ID', 'NT_S_ID'),
        Index('_dta_index_K_NOTA_TESTIGO_5_2069582411__K2_1_3_9987_4364_8066_1912_4149', 'NTS_ID', 'NTS_N_ID', 'NT_S_ID'),
        Index('_dta_index_K_NOTA_TESTIGO_5_2069582411__K3_1_2_9987_4364_8066_1912_4149', 'NTS_ID', 'NTS_N_ID', 'NT_S_ID'),
        Index('_dta_index_K_NOTA_TESTIGO_5_2069582411_51856808_K3_K2_8066', 'NTS_N_ID', 'NT_S_ID'),
        Index('_dta_index_K_NOTA_TESTIGO_5_2069582411__K1_K2_K3_9987_4364', 'NTS_ID', 'NTS_N_ID', 'NT_S_ID'),
        Index('_dta_index_K_NOTA_TESTIGO_5_2069582411__K2_K1_K3', 'NTS_ID', 'NTS_N_ID', 'NT_S_ID'),
        Index('_dta_index_K_NOTA_TESTIGO_5_2069582411_51857368_K3_K2_1912', 'NTS_N_ID', 'NT_S_ID'),
        Index('_dta_index_K_NOTA_TESTIGO_5_2069582411__K1_2_3_9987_4364_8066_1912_4149', 'NTS_ID', 'NTS_N_ID', 'NT_S_ID'),
        Index('_dta_index_K_NOTA_TESTIGO_5_2069582411__K2_K1_3_9987_4364_8066', 'NTS_ID', 'NTS_N_ID', 'NT_S_ID'),
        Index('_dta_index_K_NOTA_TESTIGO_5_2069582411_51857368_K3_5201', 'NTS_N_ID', 'NT_S_ID'),
        Index('_dta_index_K_NOTA_TESTIGO_5_2069582411__K2_K3_1_5201', 'NTS_ID', 'NTS_N_ID', 'NT_S_ID'),
        Index('_dta_index_K_NOTA_TESTIGO_5_2069582411__K3_K2', 'NTS_N_ID', 'NT_S_ID'),
        Index('_dta_index_K_NOTA_TESTIGO_5_2069582411_51856808_K2_K3_6497', 'NTS_N_ID', 'NT_S_ID'),
        Index('_dta_index_K_NOTA_TESTIGO_5_2069582411_51857368_K2_K3_1040', 'NTS_N_ID', 'NT_S_ID'),
        Index('_dta_index_K_NOTA_TESTIGO_5_2069582411_51856808_K2_1771', 'NTS_N_ID', 'NT_S_ID'),
        Index('_dta_index_K_NOTA_TESTIGO_5_2069582411__K3_1_2_9987', 'NTS_ID', 'NTS_N_ID', 'NT_S_ID'),
        Index('_dta_index_K_NOTA_TESTIGO_5_2069582411_104889936_K3', 'NTS_N_ID', 'NT_S_ID'),
        Index('_dta_index_K_NOTA_TESTIGO_5_2069582411__K2_1_3_9987', 'NTS_ID', 'NTS_N_ID', 'NT_S_ID'),
        Index('_dta_index_K_NOTA_TESTIGO_5_2069582411__K3_K2_K1_9987', 'NTS_ID', 'NTS_N_ID', 'NT_S_ID'),
        Index('_dta_index_K_NOTA_TESTIGO_5_2069582411_100452352_K3_K2', 'NTS_N_ID', 'NT_S_ID'),
        Index('_dta_index_K_NOTA_TESTIGO_5_2069582411__K2_K1_K3_4364', 'NTS_ID', 'NTS_N_ID', 'NT_S_ID')
    )

    NTS_ID = Column(BigInteger, primary_key=True, nullable=False)
    NTS_N_ID = Column(ForeignKey('K_NOTA.N_ID'), primary_key=True, nullable=False, index=True)
    NT_S_ID = Column(ForeignKey('K_TESTIGO.S_ID'), primary_key=True, nullable=False, index=True)

    K_NOTA = relationship('KNOTA')
    K_TESTIGO = relationship('KTESTIGO')


class KUSUARIOSUSCRIPTORFAV(Base):
    __tablename__ = 'K_USUARIO_SUSCRIPTOR_FAV'

    FAV_ID = Column(BigInteger, primary_key=True)
    FAV_SUSU_ID = Column(Integer, nullable=False)
    FAV_N_ID = Column(ForeignKey('K_NOTA.N_ID'), nullable=False)
    FAV_T_ID = Column(ForeignKey('K_TEMA.T_ID'), nullable=False)
    FAV_VISIBLE = Column(BIT, nullable=False)
    FAV_FECHA_AGREGADA = Column(DateTime, nullable=False)

    K_NOTA = relationship('KNOTA')
    K_TEMA = relationship('KTEMA')


class KALERTAENVIO(Base):
    __tablename__ = 'K_ALERTA_ENVIO'

    AV_ID = Column(Integer, primary_key=True)
    AV_SADI_ID = Column(ForeignKey('K_SUSCRIPTOR_ALERTA_DISTRIBUCION.SADI_ID'))
    AV_AL_ID = Column(ForeignKey('K_ALERTA.AL_ID'), nullable=False)
    AV_FECHA_ENVIO = Column(DateTime)
    AV_ACK = Column(String(collation='SQL_Latin1_General_CP1_CI_AS'))
    AV_NUMERO = Column(String(200, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    AV_DEST = Column(String(200, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)

    K_ALERTA = relationship('KALERTA')
    K_SUSCRIPTOR_ALERTA_DISTRIBUCION = relationship('KSUSCRIPTORALERTADISTRIBUCION')
