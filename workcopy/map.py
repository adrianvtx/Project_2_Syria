import folium

# create map object
m = folium.Map(location=[36, 36], zoom_start=6)

# global tooltip
tooltip = 'Click For More Info'

#  custom icon
logoIcon = folium.features.CustomIcon('tank.png', icon_size=(50, 50))

folium.Marker([36, 37],
                popup='<strong>Location One<strong>', 
                tooltip=tooltip).add_to(m),              
folium.Marker([36.5, 37.5],
                popup='<strong>Location Two<strong>',
                tooltip=tooltip,
                icon=folium.Icon(color='green', icon='hospital')).add_to(m)
folium.Marker([36.5, 38.5],
                popup='<strong>Location Three<strong>',
                tooltip=tooltip,
                icon=folium.Icon(color='red', icon='leaf')).add_to(m),
folium.Marker([35.5, 38.5],
                popup='<strong>Location Four<strong>',
                tooltip=tooltip,
                icon=logoIcon).add_to(m),
#  generate map
m.save('map.html')