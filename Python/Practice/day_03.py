cpu_usage = [45, 67, 82, 91, 55]

for i in cpu_usage:
    if i > 90:
        print("Critical ", i)
    elif i > 80:
        print("Warning ", i)
    else:
        print ("Normal ", i)