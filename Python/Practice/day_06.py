cpu_usage = input("Enter CPU usage: ")

int_cpu_usage = int(cpu_usage)

try:
    if int_cpu_usage > 80:
        print("High CPU ", int_cpu_usage)
    else:
        print("Normal CPU ", int_cpu_usage)
except ValueError:
    print("Invalid Input")
finally:
    print("Monitoring Completed")