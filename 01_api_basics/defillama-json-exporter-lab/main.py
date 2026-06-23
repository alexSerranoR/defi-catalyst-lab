import json
import requests

PROTOCOLS_URL = "https://api.llama.fi/protocols"
PROTOCOL_URL = "https://api.llama.fi/protocol/"

response = requests.get(PROTOCOLS_URL, timeout=20)
response.raise_for_status()

protocols = response.json()
protocols_data = []

for protocol in protocols:

    # Skip centralised exchanges before making another API request
    if protocol.get("category") == "CEX":
        continue

    slug = protocol.get("slug")

    if not slug:
        continue

    print("Checking:", protocol.get("name"))

    response = requests.get(PROTOCOL_URL + slug, timeout=20)
    response.raise_for_status()

    data = response.json()
    github = data.get("github")
    category = data.get("category")

    # Skip protocols without GitHub or centralised exchanges
    if not github or category == "CEX":
        continue

    selected_data = {
        "name": data.get("name"),
        "slug": slug,
        "category": category,
        "description": data.get("description"),
        "chains": data.get("chains"),
        "currentChainTvls": data.get("currentChainTvls"),
        "github": github
    }

    protocols_data.append(selected_data)

    print("Added:", data.get("name"))

    if len(protocols_data) == 5:
        break

with open("protocols_data.json", "w", encoding="utf-8") as file:
    json.dump(
        protocols_data,
        file,
        indent=4,
        ensure_ascii=False
    )

print("\nData saved in protocols_data.json")