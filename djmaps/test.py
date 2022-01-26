a = [
    {
        "id": 7,
        "lat": 43.4145823683576,
        "lng": 39.94917028602126,
        "DeBe": 10.0
    },
    {
        "id": 8,
        "lat": 43.41441560542985,
        "lng": 39.949514647423264,
        "DeBe": 47.0
    },
    {
        "id": 9,
        "lat": 43.41420533847507,
        "lng": 39.94962943455727,
        "DeBe": 89.0
    },
    {
        "id": 10,
        "lat": 43.4139588176673,
        "lng": 39.949579527107694,
        "DeBe": 120.0
    }
]
map_di=dict
maps = []
for i in a:
    d = {'lat': i['lat'], 'lng': i['lng']}
    d1 = {'center': d, 'DeBe': i['DeBe']}
    map_di = {i['id']: d1}
    maps.append(map_di)
print(maps)
for i in maps:
    print(i)