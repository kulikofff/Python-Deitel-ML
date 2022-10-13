import folium
map = folium.Map(location=[-39.8283, 98.5795],
                   tiles='Stamen Terrain',
                   zoom_start=5, detect_retina=True)

map.save('tweet_map.html')