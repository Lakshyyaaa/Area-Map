import folium
import pandas as pd

crime_data = {
    "State": [
        "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh",
        "Delhi", "Goa", "Gujarat", "Haryana", "Himachal Pradesh",
        "Jammu and Kashmir", "Jharkhand", "Karnataka", "Kerala",
        "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya",
        "Mizoram", "Nagaland", "Odisha", "Punjab",
        "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana",
        "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal"
    ],
    "Crimes": [
        129389, 2700, 107014, 189696, 84192,
        216920, 3706, 435422, 143111, 17249,
        26624, 47817, 179479, 27078,
        365154, 430866, 4098, 3582,
        2800, 1908, 103565, 57739,
        251147, 1020, 467369, 120273,
        4081, 494025, 16074, 204400
    ]
}

data = pd.DataFrame(crime_data)

state_coordinates = {
    "Andhra Pradesh": [15.9129, 79.7400],
    "Arunachal Pradesh": [28.2180, 94.7278],
    "Assam": [26.2006, 92.9376],
    "Bihar": [25.0961, 85.3131],
    "Chhattisgarh": [21.2787, 81.8661],
    "Delhi": [28.6139, 77.2090],
    "Goa": [15.2993, 74.1240],
    "Gujarat": [22.2587, 71.1924],
    "Haryana": [29.0588, 76.0856],
    "Himachal Pradesh": [31.1048, 77.1734],
    "Jammu and Kashmir": [34.0836, 74.7973],
    "Jharkhand": [23.6102, 85.2799],
    "Karnataka": [15.3173, 75.7139],
    "Kerala": [10.8505, 76.2711],
    "Madhya Pradesh": [22.9734, 78.6569],
    "Maharashtra": [19.6010, 75.3333],
    "Manipur": [24.6637, 93.9063],
    "Meghalaya": [25.4670, 91.3662],
    "Mizoram": [23.1645, 92.9376],
    "Nagaland": [26.1584, 94.5624],
    "Odisha": [20.9517, 85.0985],
    "Punjab": [30.7333, 76.7794],
    "Rajasthan": [27.0238, 74.2176],
    "Sikkim": [27.5330, 88.5122],
    "Tamil Nadu": [13.0658, 80.1682],
    "Telangana": [17.1232, 78.6572],
    "Tripura": [23.9400, 91.9882],
    "Uttar Pradesh": [26.8467, 80.9462],
    "Uttarakhand": [30.3165, 78.0322],
    "West Bengal": [22.9868, 87.8550]
}

india = folium.Map(location=[20.5937, 78.9629], zoom_start=5)

for index, row in data.iterrows():
    state = row['State']
    crime_rate = row['Crimes']

    if crime_rate < 50000:
        color = 'green'
    elif crime_rate < 100000:
        color = 'orange'
    else:
        color = 'red'

    folium.CircleMarker(
        location=state_coordinates[state],
        radius=min(crime_rate / 10000, 30),
        color=color,
        fill=True,
        fill_color=color,
        fill_opacity=0.6,
        popup=f'{state}: {crime_rate} crimes'
    ).add_to(india)

india.save("india_crime_map.html")
