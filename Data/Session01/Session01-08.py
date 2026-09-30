# Parallel resistance calculator
print("Insert parallel resistor's value")
R1 = float(input("R1 (Ω): "))
R2 = float(input("R2 (Ω): "))

Req = (R1 * R2) / (R1 + R2)

print(f"R_eq = {Req:.2f} Ω")


#  Triangle to Star connection converter
print("Insert triangle connection resistor's value")
Ra = float(input("Ra (Ω): "))
Rb = float(input("Rb (Ω): "))
Rc = float(input("Rc (Ω): "))

sum_products = Ra*Rb + Rb*Rc + Rc*Ra

RAB = sum_products / Rc
RBC = sum_products / Ra
RCA = sum_products / Rb

print(f"RAB = {RAB:.2f} Ω")
print(f"RBC = {RBC:.2f} Ω")
print(f"RCA = {RCA:.2f} Ω")
