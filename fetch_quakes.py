import requests

url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson"

response = requests.get(url)
data = response.json()

quakes = data["features"]
print(f"Earthquakes in the last 24 hours: {len(quakes)}")

for quake in quakes[:5]:
    props = quake["properties"]
    print(props["mag"], "-", props["place"])