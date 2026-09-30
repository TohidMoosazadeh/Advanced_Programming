# input function to get voltage and resistance values from the user
V = float(input("Voltage (V): "))
R = float(input("Resistance (Ω): "))
I = V / R
print(f"Current = {I:.2f} A")
