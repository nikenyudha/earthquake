import streamlit as st
import pandas as pd
import pydeck as pdk
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()
engine = create_engine(os.getenv("DATABASE_URL"))

st.set_page_config(page_title="Global Quake Tracker", layout="wide")

# Ambil data
df = pd.read_sql("SELECT * FROM earthquake_data", engine)

st.title("🌍 Global Earthquake Real-time Tracker")
st.markdown("Latest earthquake monitoring worldwide using USGS data.")

# --- Bagian Ringkasan (Metrics) ---
col1, col2, col3 = st.columns(3)
col1.metric("Strongest Earthquake", f"{df['mag'].max()} SR")
col2.metric("Total Events", len(df))
col3.metric("Average Depth", f"{round(df['depth'].mean(), 2)} km")

# --- Bagian Peta 3D (Pydeck) ---
st.subheader("📍 Distribution of Earthquake Points (3D)")

# Menentukan warna berdasarkan magnitudo (Kuning ke Merah)
df['color_r'] = df['mag'].apply(lambda x: 255 if x > 5 else 255)
df['color_g'] = df['mag'].apply(lambda x: 0 if x > 5 else 200)
df['color_b'] = 0

layer = pdk.Layer(
    "ScatterplotLayer",
    df,
    get_position=["longitude", "latitude"],
    get_color="[color_r, color_g, color_b, 160]",
    get_radius="mag * 50000", # Ukuran titik tergantung kekuatan gempa
    pickable=True,
)

view_state = pdk.ViewState(latitude=df['latitude'].mean(), longitude=df['longitude'].mean(), zoom=1, pitch=45)

r = pdk.Deck(layers=[layer], initial_view_state=view_state, tooltip={"text": "{place}\nMag: {mag}"})
st.pydeck_chart(r)

# --- Tabel Data ---
st.subheader("📋 Latest Data Details")
st.dataframe(df.sort_values(by='time', ascending=False), use_container_width=True)

st.markdown(
    "<hr style='margin-top:50px;'>"
    "<center style='color: gray;'>© 2026 Niken Larasati —  Global EarthQuake Tracker 💗</center>",
    unsafe_allow_html=True
)