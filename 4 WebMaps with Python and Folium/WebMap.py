#Not Completed
import folium

map = folium.Map([38.58,-99.09], zoom_start=6)
fg = folium.FeatureGroup(name='My Map')
fg.add_child(folium.Marker(location=[38.2,-99.0],popup="Hi Mark"))
map.add_child(fg)
map.save("map.html")
