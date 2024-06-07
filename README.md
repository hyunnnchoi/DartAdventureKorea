# DartAdventureKorea

Welcome to **DartAdventureKorea**! 🎯✨

DartAdventureKorea is a fun and interactive project that generates random coordinates within South Korea and displays them on an interactive map. Perfect for those spontaneous travel enthusiasts looking for their next adventure spot!

## Features

- Generates random coordinates within South Korea.
- Displays the coordinates on an interactive map using Folium.
- Opens the map automatically in your default web browser.

## Installation

To get started with DartAdventureKorea, you need to have Python installed on your system. Then follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/DartAdventureKorea.git
    cd DartAdventureKorea
    ```

2. Install the required packages:

    ```bash
    pip install folium
    ```

## Usage

Run the following script to generate a random coordinate and display it on the map:

```python
import random
import folium
import webbrowser

def generate_random_coordinate():
    # South Korea's latitude and longitude range
    min_latitude = 33.1000
    max_latitude = 38.6137
    min_longitude = 124.6231
    max_longitude = 131.8722

    # Generate random latitude and longitude
    random_latitude = random.uniform(min_latitude, max_latitude)
    random_longitude = random.uniform(min_longitude, max_longitude)

    return random_latitude, random_longitude

# Center the map around South Korea
map_center = [36.5, 127.5]

# Create a map
m = folium.Map(location=map_center, zoom_start=7)

# Generate a random coordinate and add it to the map
for _ in range(1):
    lat, lon = generate_random_coordinate()
    folium.Marker([lat, lon], popup=f"Latitude: {lat:.6f}, Longitude: {lon:.6f}").add_to(m)

# Save the map as an HTML file
map_file = "random_coordinates_map.html"
m.save(map_file)

# Open the map in the web browser
webbrowser.open(map_file)
