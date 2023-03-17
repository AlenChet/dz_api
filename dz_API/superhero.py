import requests

response = requests.get("https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json")
data = response.json()
superheroes = ["Hulk", "Captain America", "Thanos"]

max_intellect = 0
most_intelligent = ""

for hero in data:
    if hero["name"] in superheroes:
        if hero["powerstats"]["intelligence"] != "null":
            intellect = int(hero["powerstats"]["intelligence"])
            if intellect > max_intellect:
                max_intellect = intellect
                most_intelligent = hero["name"]

print(f"Супергерой с самым высоким интеллектом в {max_intellect}:", most_intelligent)












