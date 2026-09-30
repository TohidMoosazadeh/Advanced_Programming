# ============================================================
#  1. Assignment - Assigning values to variables
# ============================================================
# Like setting circuit parameters in a simulation software (e.g., SPICE)

voltage_source = 12.0        # Source voltage (Volts)
resistance_1 = 4.0           # First resistor (Ohms)
resistance_2 = 6.0           # Second resistor (Ohms)
current = 0.0                # Initial current (Amperes)
power = 0.0                  # Initial power (Watts)

# Compound assignment
resistance_total = 0
resistance_total += resistance_1   # Series resistance: R_total = R1 + R2
resistance_total += resistance_2

print(f"Total series resistance: {resistance_total} Ohms")
# Output: Total series resistance: 10.0 Ohms


# ============================================================
#  2. Arithmetic - Basic mathematical operations
# ============================================================
# Like Ohm's Law and power calculations in a circuit

# Ohm's Law: I = V / R
current = voltage_source / resistance_total
print(f"Circuit current: {current} Amperes")          # 1.2 A

# Power: P = V × I
power = voltage_source * current
print(f"Consumed power: {power} Watts")               # 14.4 W

# Voltage drop across each resistor (V = I × R)
voltage_drop_1 = current * resistance_1
voltage_drop_2 = current * resistance_2
print(f"Voltage drop R1: {voltage_drop_1} Volts")     # 4.8 V
print(f"Voltage drop R2: {voltage_drop_2} Volts")     # 7.2 V

# Modulo - Like remaining phase in AC systems
phase_angle = 370 % 360   # 370 degrees phase is equivalent to 10 degrees
print(f"Equivalent phase: {phase_angle} degrees")     # 10 degrees

# Exponent - Calculating I²R for power
power_r1 = current ** 2 * resistance_1
print(f"Power R1 (I²R): {power_r1} Watts")            # 5.76 W

# Floor division - Number of batteries required
battery_capacity = 12.0
total_energy_needed = 50.0
batteries_needed = total_energy_needed // battery_capacity
print(f"Number of batteries needed: {batteries_needed}")  # 4 batteries


# ============================================================
#  3. Comparison - Comparing two values
# ============================================================
# Like checking circuit safety conditions (Protection Relay)

print("\n--- Circuit Safety Check ---")

# Is the current above the safe limit? (Overcurrent Protection)
max_current = 2.0
is_overcurrent = current > max_current
print(f"Overcurrent? {is_overcurrent}")               # False (1.2 < 2.0)

# Is the voltage within the acceptable range? (Undervoltage/Overvoltage)
min_voltage = 10.0
max_voltage = 15.0
voltage_ok = (voltage_source >= min_voltage) and (voltage_source <= max_voltage)
print(f"Voltage within range? {voltage_ok}")          # True

# Are two resistors equal? (Balanced Bridge)
r3 = 4.0
is_balanced = (resistance_1 == r3)
print(f"Wheatstone bridge balanced? {is_balanced}")   # True

# Is power non-zero? (Fault Detection)
no_fault = power != 0
print(f"Circuit fault? {not no_fault}")               # False


# ============================================================
#  4. Logical - Combining conditions
# ============================================================
# Like protection relay logic (Protection Logic)

temperature = 75.0       # Transformer temperature (°C)
humidity = 60.0          # Ambient humidity (%)

# Protection relay: if temperature is high AND humidity is high → Alarm
temp_high = temperature > 70
humidity_high = humidity > 50
alarm = temp_high and humidity_high
print(f"\nThermal-Humidity Alarm: {alarm}")           # True

# If temperature is high OR current is over limit → Trip the circuit
trip = temp_high or is_overcurrent
print(f"Circuit Trip: {trip}")                        # True

# Negating a condition (Not)
circuit_safe = not trip
print(f"Circuit is safe? {circuit_safe}")             # False


# ============================================================
#  5. Bitwise - Operations on bits
# ============================================================
# Like working with microcontroller registers and communication protocols

# Status register of a microcontroller (8-bit)
# Bits: [Fault][OverTemp][OverCurrent][OverVoltage][Reserved][Running][Enabled][Powered]
status_register = 0b10110011  # = 179

# Masks
FAULT_MASK       = 0b10000000  # Bit 7
OVERTEMP_MASK    = 0b01000000  # Bit 6
OVERCURRENT_MASK = 0b00100000  # Bit 5
RUNNING_MASK     = 0b00000010  # Bit 1
ENABLED_MASK     = 0b00000001  # Bit 0

# Bitwise AND: Check the state of a specific bit
has_fault = bool(status_register & FAULT_MASK)
print(f"\nSystem fault? {has_fault}")                 # True

is_running = bool(status_register & RUNNING_MASK)
print(f"System running? {is_running}")                # True

# Bitwise OR: Set a bit (Set Bit) - Enable the system
status_register = status_register | ENABLED_MASK
print(f"Register after enabling: {bin(status_register)}")

# Bitwise XOR: Toggle a bit - Toggle Running state
status_register = status_register ^ RUNNING_MASK
print(f"Register after toggling Running: {bin(status_register)}")

# Bitwise NOT (Complement): Invert all bits
inverted = ~status_register & 0xFF  # 8-bit mask
print(f"Inverted register: {bin(inverted)}")

# Shift Left: Like frequency division in a PLL
base_frequency = 50  # Hz
doubled_freq = base_frequency << 1   # Multiply by 2
halved_freq = base_frequency >> 1    # Divide by 2
print(f"Frequency ×2: {doubled_freq} Hz")             # 100 Hz
print(f"Frequency ÷2: {halved_freq} Hz")              # 25 Hz


# ============================================================
#  6. Special Operators
# ============================================================

# --- is : Identity check ---
# Like checking whether two wires are connected to the same node

node_a = [12.0, 1.2, 14.4]   # [Voltage, Current, Power]
node_b = node_a               # Same node (Reference)
node_c = [12.0, 1.2, 14.4]   # Different node with same values

print(f"\nnode_a is node_b: {node_a is node_b}")       # True (same node)
print(f"node_a is node_c: {node_a is node_c}")         # False (different nodes)
print(f"node_a == node_c: {node_a == node_c}")         # True (same values)

# None check - Like checking for an open circuit
sensor_reading = None
if sensor_reading is None:
    print("Sensor not connected (Open Circuit)!")

# --- in : Membership check ---
# Like checking if a component exists in a BOM (Bill of Materials)

components = ["resistor", "capacitor", "inductor", "diode", "transistor"]

print(f"\n'capacitor' in parts list? {'capacitor' in components}")     # True
print(f"'relay' in parts list? {'relay' in components}")              # False

# Check within a string (Like searching in an error code)
error_code = "ERR_OVERCURRENT_042"
if "OVERCURRENT" in error_code:
    print("Overcurrent error detected!")

# Check within a dictionary (Like a transformer lookup table)
transformer_specs = {
    "primary_voltage": 220,
    "secondary_voltage": 12,
    "power_rating": 50
}
print(f"'power_rating' in specs? {'power_rating' in transformer_specs}")  # True