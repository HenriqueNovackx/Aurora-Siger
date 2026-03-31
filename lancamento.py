import random

# Simulate sensor readings
def simulate_sensor_readings():
    
    temperature = random.uniform(-100, 150)  # Wider range for simulation
    integrity = random.choice([0, 1])  # 0 or 1
    energy = random.uniform(0, 100)  # 0 to 100
    pressure = random.uniform(100, 400)  # Wider range for simulation
    
    return temperature, integrity, energy, pressure

# Check each sensor
def check_sensors(temp, integ, ener, pres):
    checks = []
    all_good = True
    
    # Temperature check
    if -50 <= temp <= 100:
        checks.append(f"Temperatura: {temp:.2f}°C - OK")
    else:
        checks.append(f"Temperatura: {temp:.2f}°C - FAIL")
        all_good = False
    
    # Integrity check
    if integ == 1:
        checks.append(f"Integridade: {integ} - OK")
    else:
        checks.append(f"Integridade: {integ} - FAIL")
        all_good = False
    
    # Energy check
    if ener > 80:
        checks.append(f"Energia: {ener:.2f}% - OK")
    else:
        checks.append(f"Energia: {ener:.2f}% - FAIL")
        all_good = False
    
    # Pressure check
    if 200 <= pres <= 300:
        checks.append(f"Pressão: {pres:.2f} bar - OK")
    else:
        checks.append(f"Pressão: {pres:.2f} bar - FAIL")
        all_good = False
    
    return checks, all_good

# Main script
if __name__ == "__main__":
    temp, integ, ener, pres = simulate_sensor_readings()
    checks, all_good = check_sensors(temp, integ, ener, pres)
    
    # Print each check
    for check in checks:
        print(check)
    
    # Final decision
    if all_good:
        print("PRONTO PARA DECOLAR")
    else:
        print("DECOLAGEM ABORTADA")