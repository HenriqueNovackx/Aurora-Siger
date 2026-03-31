import random


def simulate_sensor_readings():
    
    temperature = random.uniform(-100, 150)  
    integrity = random.choice([0, 1])  
    energy = random.uniform(0, 100)  
    pressure = random.uniform(100, 400)  
    
    return temperature, integrity, energy, pressure


def check_sensors(temp, integ, ener, pres):
    checks = []
    all_good = True
    
    
    if -50 <= temp <= 100:
        checks.append(f"Temperatura: {temp:.2f}°C - OK")
    else:
        checks.append(f"Temperatura: {temp:.2f}°C - FAIL")
        all_good = False
    
    
    if integ == 1:
        checks.append(f"Integridade: {integ} - OK")
    else:
        checks.append(f"Integridade: {integ} - FAIL")
        all_good = False
    
    
    if ener > 80:
        checks.append(f"Energia: {ener:.2f}% - OK")
    else:
        checks.append(f"Energia: {ener:.2f}% - FAIL")
        all_good = False
    
    
    if 200 <= pres <= 300:
        checks.append(f"Pressão: {pres:.2f} bar - OK")
    else:
        checks.append(f"Pressão: {pres:.2f} bar - FAIL")
        all_good = False
    
    return checks, all_good


if __name__ == "__main__":
    temp, integ, ener, pres = simulate_sensor_readings()
    checks, all_good = check_sensors(temp, integ, ener, pres)
    
   
    for check in checks:
        print(check)
 
    if all_good:
        print("PRONTO PARA DECOLAR")
    else:
        print("DECOLAGEM ABORTADA")
