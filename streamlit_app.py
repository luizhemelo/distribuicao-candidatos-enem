#import locale
import pandas as pd
import streamlit as st
import plotly.express as px

# set page config
st.set_page_config(layout="wide")
#locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
px.set_mapbox_access_token("pk.eyJ1IjoibHVpemhlbWVsbyIsImEiOiJjbG9hZGkzdDQwaG94Mm1udmg4Mmx0ZG45In0.etjGdsIyRFv-oaU74-8DTg")

# load ENEM preprocessed data
df = pd.read_pickle('./data/enem_data.pickle')

# build map visualization
fig = px.scatter_mapbox(
    data_frame=df,
    lat="Latitude",
    lon="Longitude",
    size="Num_Candidatos",
    animation_frame="Ano",
    text="Cidade",
    #color="room_type",
    color_continuous_scale=px.colors.cyclical.IceFire,
    size_max=60,
    zoom=4,
    mapbox_style="outdoors",
    title="Distribuição do Número de Candidatos do ENEM por Cidade / Anos 2013-2022",
    width=2000
)

# build webpage
st.plotly_chart(fig, use_container_width=True)
