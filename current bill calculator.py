watt = float(input("Enter the watt of the device: "))
time = float(input("Enter the time of usage by hours : "))
unit_cost = float(input("Enter the unit cost from your current bill: "))

def watt_per_hour():
    wh = watt * time
    return wh

def killo_watt_hour():
    kwh = watt_per_hour() / 1000
    return kwh

def cost_per_kwh():
    cost = killo_watt_hour() * unit_cost
    return cost

print("your power consumption in unit: ",killo_watt_hour(),"kWh")
print("your current bill is: ", cost_per_kwh())

