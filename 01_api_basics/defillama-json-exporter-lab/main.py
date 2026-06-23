import json
import requests

protocols_url = "https://api.llama.fi/protocols"

response = requests.get(protocols_url)
protocols = response.json()

protocols_data = []

for protocol in protocols[:5]:
    slug = protocol["slug"]

    protocol_url = "https://api.llama.fi/protocol/" + slug
    response = requests.get(protocol_url)
    data = response.json()

    selected_data = {
        "name": data.get("name"),
        "slug": slug,
        "description": data.get("description"),
        "chains": data.get("chains"),
        "currentChainTvls": data.get("currentChainTvls"),
        "github": data.get("github")
    }

    protocols_data.append(selected_data)

with open("protocols_data.json", "w", encoding="utf-8") as file:
    json.dump(protocols_data, file, indent=4, ensure_ascii=False)

print("Data saved in protocols_data.json")

