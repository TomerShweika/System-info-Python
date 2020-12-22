import platform
import psutil


print("="*40, "System Information", "="*40)

#check battery level

battery = psutil.sensors_battery()
#check if plugged in

plugged = battery.power_plugged
percent = str(battery.percent)
plugged = "Plugged In" if plugged else "Not Plugged In"
print("Battery-Level: " +percent+'% | '+plugged)

#other information

uname = platform.uname()
print(f"System: {uname.system}")
print(f"Node Name: {uname.node}")
print(f"Release: {uname.release}")
print(f"Version: {uname.version}")
print(f"Machine: {uname.machine}")
print(f"Processor: {uname.processor}")