a = int(input("CPU usage: "))
b = int(input("Memory usage: "))

if a > 80 and b > 80:
    print("Scale Up Required")
elif a > 80:
    print("CPU High")
elif b > 80:
    print("Memory High")
else:
    print("System Stable")