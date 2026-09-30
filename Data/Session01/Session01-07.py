# Example: power, period, and energy calculations
V = float(input("Voltage (V): "))
I = float(input("Current (A): "))
f = float(input("Frequency (Hz): "))
t = float(input("Time (s): "))
P = V * I
T = 1 / f
E = P * t
print(f"Power: {P:.2f} W")
print(f"Period: {T:.4f} s")
print(f"Energy: {E:.2f} J")