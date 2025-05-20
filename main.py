import pandas as pd
import folium
import os


CSV_PATH = os.path.join("data", "metro-bike-share-stations-2025-04-01.csv")

# CSV laden (latin1 wegen Sonderzeichen in Spalte 'status2')
df = pd.read_csv(CSV_PATH, encoding='latin1')

# Ungültige Koordinaten (z. B. 0.0) filtern
df = df[(df['Latitude'] != 0.0) & (df['Longitude'] != 0.0)]

# Karte auf Mittelwert zentrieren. Grund: user freundlichkeit
center_lat = df['Latitude'].mean()
center_lon = df['Longitude'].mean()
m = folium.Map(location=[center_lat, center_lon], zoom_start=14)

# Marker setzen
for _, row in df.iterrows():
    folium.Marker(
        location=[row['Latitude'], row['Longitude']],
        tooltip=row['Kiosk Name']
    ).add_to(m)

# Karte speichern
m.save("map.html")
print("✅ Karte gespeichert als map.html")
