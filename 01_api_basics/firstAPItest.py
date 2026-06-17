import requests

urlProtocols = "https://api.llama.fi/protocols"
reply = requests.get(urlProtocols)
protocols = reply.json()
for protocol in protocols[:10]:
    #print(protocol["name"])
    slug = protocol["slug"] #slug = id
    url = "https://api.llama.fi/protocol/" + slug

    response = requests.get(url)
    data = response.json()

    print("---------------")
    print("Name:", data.get("name"))
    print("Description:", data.get("description"))
    print("Chains:", data.get("chains"))
    print("Github:", data.get("github"))
    print("Governance:", data.get("governanceID"))

""" not auto
project = input("Project name: ")
url = "https://api.llama.fi/protocol/" + project.lower()

response = requests.get(url)
data = response.json()

# print(data.keys()) useful to see data options

print("-----------------------------------------------------")
print("Name:", data.get("name"))
print("Description:", data.get("description"))
print("Chains:", data.get("chains"))
print("Current chain TVLs:", data.get("currentChainTvls"))
print("Treasury:", data.get("treasury"))
print("Github:", data.get("github"))
print("Governance:", data.get("governanceID"))
"""
