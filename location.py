import requests
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import geocoder
import folium
import io
import sys
import PyQt5
from PyQt5 import QtWidgets, QtWebEngineWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView
import sys
from PyQt5.QtCore import QUrl


# Set your home address
home_address = "1900 Fox Sterling Drive, Raleigh , NC - 27606"

# Use Nominatim Geocoder for address to lat/long conversion
geolocator = Nominatim(user_agent="myapp/01")



def get_current_gps_coordinates():
    print("hi")
    g = geocoder.ip('me')#this function is used to find the current information using our IP Add
    print(g.latlng)
    if g.latlng is not None: #g.latlng tells if the coordiates are found or not
        return g.latlng
    else:
        return None

# # if __name__ == "__main__":
# #     coordinates = get_current_gps_coordinates()
# #     if coordinates is not None:
# #         latitude, longitude = coordinates
# #         print(f"Your current GPS coordinates are:")
# #         print(f"Latitude: {latitude}")
# #         print(f"Longitude: {longitude}")
#     else:
#         print("Unable to retrieve your GPS coordinates.")

# Function to get your current location based on your IP address
def get_current_location():
    print("hi")
    response = requests.get("https://ipinfo.io/")
    data = response.json()
    location = data["loc"].split(",")
    print(location)
    return location[0], location[1]  # Return as tuple (latitude, longitude)

# Function to calculate distance and provide basic direction to home
def get_home_distance_directions(current_loc, home):
    # Convert home address to lat/long
    home_location = geolocator.geocode(home)
    
    home_latlong = (home_location.latitude, home_location.longitude)
    print("Location:", home_latlong)

    # Calculate the distance
    distance = geodesic(current_loc, home_latlong).kilometers

    print(f"Distance to home: {distance:.2f} kilometers.")

    return home_location.latitude, home_location.longitude

    # For actual turn-by-turn directions, use a dedicated API like Google Maps Directions API

# Get current location
current_lat, current_log = get_current_gps_coordinates()
home_lat , home_long = get_home_distance_directions([current_lat,current_log], home_address)

# Print distance and directions




# Coordinates
location_curr = (current_lat, current_log)
location_home = (home_lat, home_long)

# Create a map centered around the average of the two locations
map_center = [(location_curr[0] + location_home[0]) / 2, 
              (location_curr[1] + location_home[1]) / 2]

m = folium.Map(location=map_center, zoom_start=14)

# Add points for the two locations
folium.Marker(location_curr, tooltip='Current Address').add_to(m)
folium.Marker(location_home, tooltip='Home Address').add_to(m)

# Draw a line between them
folium.PolyLine(locations=[location_curr, location_home], color='red').add_to(m)

# Display the map
m.save("footprint.html")





# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     m = folium.Map(
#         location=[45.5236, -122.6750], tiles="Stamen Toner", zoom_start=13
#     )

#     data = io.BytesIO()
#     m.save(data, close_file=False)

#     w = QtWebEngineWidgets.QWebEngineView()
#     w.setHtml(data.getvalue().decode())
#     w.resize(640, 480)
#     w.show()

#     sys.exit(app.exec_())


class MapViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Folium Map Viewer")
        self.browser = QWebEngineView()

        # Load the HTML file
        self.browser.load(QUrl.fromLocalFile("footprint.html"))  # Update the path

        self.setCentralWidget(self.browser)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MapViewer()
    window.resize(700, 520)
    window.show()
    sys.exit(app.exec_())