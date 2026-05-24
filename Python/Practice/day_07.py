servers = [
    {"name": "app1", "cpu": 85},
    {"name": "app2", "cpu": 60}
]

with open("report.txt", "w") as file:
    for server in servers:
        if server["cpu"] > 80:
            file.write(f"{server['name']} - High CPU\n")