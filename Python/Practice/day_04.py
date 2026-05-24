aws = {
    "name": "web-server",
    "cpu": 92,
    "memory": 75,
    "status": "running"
}

#If cpu > 90 → print "Critical CPU"
if aws["cpu"] > 90:
    print("Critical CPU ", aws["cpu"]) 

#If memory > 80 → print "High Memory"
if aws["memory"] > 80:
    print ("High Memory", aws["memory"])

#Print all key-value pairs using loop
for i,j in aws.items():
    print(i, ":", j)
    