import streamlit as st
import pandas as pd
from app import collect_smhi_data

st.set_page_config(page_title="SMHI Weather Forecast", page_icon="🌦️", layout="wide")
st.title("🌦️ SMHI Weather Forecast Dashboard")

st.write("View 48-hour weather forecast from **SMHI** API.")

st.sidebar.header("Plats")

cities = [
    ("Stockholm",   59.3293, 18.0686),
    ("Göteborg",    57.7089, 11.9746),
    ("Malmö",       55.6050, 13.0038),
    ("Uppsala",     59.8586, 17.6389),
    ("Västerås",    59.6099, 16.5448),
    ("Örebro",      59.2741, 15.2066),
    ("Linköping",   58.4109, 15.6216),
    ("Helsingborg", 56.0465, 12.6945),
    ("Jönköping",   57.7826, 14.1618),
    ("Norrköping",  58.5877, 16.1924),
]

city_names = [c[0] for c in cities]
selected_city = st.sidebar.selectbox("Välj stad (topp 10)", city_names, index=0)

city_lat, city_lon = next((lat, lon) for name, lat, lon in cities if name == selected_city)

latitude = city_lat
longitude = city_lon

with st.spinner("Hämtar prognos från SMHI..."):
    df_smhi, msg = collect_smhi_data(lat=latitude, lon=longitude)

if df_smhi is not None:
    st.success(f"✅ Prognos hämtad för {selected_city} ({latitude:.4f}, {longitude:.4f})")
    st.dataframe(df_smhi, width="stretch")
else:
    st.error(msg)