import requests
import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()
engine = create_engine(os.getenv("DATABASE_URL"))

def fetch_earthquake_data():
    # Mengambil data gempa 7 hari terakhir, magnitudo > 2.0
    # pakai parameter 'endtime' dan 'starttime' yang lebih masuk akal
    url = "https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&minmagnitude=2.5&orderby=time"
    
    print(f"📡 Menghubungi API: {url}")
    response = requests.get(url)
    
    # Cek apakah request berhasil (status 200)
    if response.status_code != 200:
        print(f"❌ API Error: Status {response.status_code}")
        return pd.DataFrame() # Kembalikan tabel kosong jika gagal

    try:
        data = response.json()
    except Exception as e:
        print(f"❌ Gagal mengubah ke JSON. Response teks: {response.text[:100]}")
        raise e
    
    features = data['features']
    quakelist = []
    
    for quake in features:
        quakelist.append({
            'place': quake['properties']['place'],
            'mag': quake['properties']['mag'],
            'time': pd.to_datetime(quake['properties']['time'], unit='ms'),
            'latitude': quake['geometry']['coordinates'][1],
            'longitude': quake['geometry']['coordinates'][0],
            'depth': quake['geometry']['coordinates'][2]
        })
    
    df = pd.DataFrame(quakelist)
    return df

# Jalankan ETL
df_quake = fetch_earthquake_data()
df_quake.to_sql('earthquake_data', engine, if_exists='replace', index=False)
print(f"✅ Berhasil menyimpan {len(df_quake)} data gempa ke Neon!")