import json
aws_response = '''
{
  "servers": [
    {"name": "app1", "status": "running"},
    {"name": "app2", "status": "stopped"},
    {"name": "app3", "status": "running"}
  ]
}
'''

data = json.loads(aws_response)

for i in data["servers"]:
    if i["status"] == "stopped":
        print(i["name"], "is stopped")