#  Home Appliance Energy Consumption Calculator
name = input("Device Name: ")
P = float(input("Power(W) "))
t = float(input("Daily usage time (h): "))

E_day = (P * t) / 1000
E_month = E_day * 30

print(f"Device: {name}")
print(f"Daily usage {E_day:.2f} kWh")
print(f"Monthly usage: {E_month:.2f} kWh")
