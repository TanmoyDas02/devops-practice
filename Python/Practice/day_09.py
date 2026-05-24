import requests

response = requests.get("https://api.github.com/users/octocat")

data = response.json()

print(f"Login: {data['login']}")
print(f"ID: {data['id']}")
print(f"Type: {data['type']}")