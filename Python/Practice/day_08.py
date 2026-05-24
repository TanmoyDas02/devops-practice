servers = [
  {"name": "app1", "cpu": 85},
  {"name": "app2", "cpu": 65},
  {"name": "app3", "cpu": 95}
]

with open("server_report.txt", "w") as file:
    for server in servers:
        if server["cpu"] > 80:
            file.write(f"{server['name']} - High CPU\n")
        else:
            file.write(f"{server['name']} - Normal CPU\n")