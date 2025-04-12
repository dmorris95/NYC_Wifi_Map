import folium
import folium.map
import pandas as pd

borough = input("Please enter the name of the borough: ".title())
outfile = borough.lower() + "wifihotspots.html"

data = pd.read_csv("NYC_Wi-Fi_Hotspot_Locations_20250412.csv")

map = folium.Map(location=[40.768731, -73.964915])

for index, row in data.iterrows():
    if row["Borough Name"] == borough:
        lat = row["Latitude"]
        long = row["Longitude"]
        name = row["Name"]
        provider = row["Provider"]
        ssid = row["SSID"]
        location = row["Location"]
        remarks = row["Remarks"]

        newMarker = folium.Marker(
            location=[lat, long],
            popup=f'''
            <html>
                <p>Name: {name}</p>
                <p>Provider: {provider}</p>
                <p>SSID: {ssid}</p>
                <p>Location: {location}</p>
                <p>Remarks: {remarks}</p>
            </html>
            '''
        )

        newMarker.add_to(map)

map.save(outfile)