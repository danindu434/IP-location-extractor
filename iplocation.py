# importing modules...

import json
import webbrowser
import requests
import folium
from time import sleep

# -----------------------------


def main():
    with open("ip_file.txt", "r") as f:
        for line in f:
            ip = line.strip()
            print(ip)
            request_url = 'https://geolocation-db.com/jsonp/' + ip
            response = requests.get(request_url)
            result = response.content.decode()
            result = result.split("(")[1].strip(")")
            result = json.loads(result)
            lat = result.get('latitude')
            long = result.get('longitude')
            print(result, "\n")
            print(lat, long)
            map_ = folium.Map(location=[lat, long], zoom_start=13)

            tooltip = [lat, long]
            folium.Marker(
                [lat, long], tooltip=tooltip
            ).add_to(map_)

            map_.save("loc.html")

            webbrowser.open("loc.html", new=0)


file_or_not = input("file or enter ip: (file/ip)").lower()
if file_or_not == "file":
    main()

elif file_or_not == "ip":
    ip = input("Enter your ip address: ")
    request_url = 'https://geolocation-db.com/jsonp/' + ip
    response = requests.get(request_url)
    result = response.content.decode()
    result = result.split("(")[1].strip(")")
    result = json.loads(result)
    lat = result.get('latitude')
    long = result.get('longitude')
    print(result, "\n")
    print(lat, long)
    map_ = folium.Map(location=[lat, long], zoom_start=13)

    tooltip = [lat, long]
    folium.Marker(
        [lat, long], tooltip=tooltip
    ).add_to(map_)

    map_.save("loc.html")
    sleep(3.0)

    webbrowser.open("loc.html", new=0)

