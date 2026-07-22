
kilo = int(input("Enter the distance in kilometers: "))
petrol_price_per_litre = float(input("Enter the petrol price per litre: "))
liters_needed = kilo/10
total_cost = liters_needed * petrol_price_per_litre
print("\n==============================")
print("      FUEL COST CALCULATOR")
print("==============================")
print(f"Distance: {kilo} km")
print(f"Petrol Price: R{petrol_price_per_litre} per litre")
print(f"Liters Needed: {liters_needed:.2f} litres")
print(f"Total Cost: R{total_cost:.2f}")